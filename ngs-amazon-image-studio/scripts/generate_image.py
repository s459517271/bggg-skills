#!/usr/bin/env python3
"""Generate one ecommerce image through an OpenAI-compatible Images API."""

from __future__ import annotations

import argparse
import base64
import io
import os
import sys
import urllib.request
from contextlib import ExitStack
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate one image. Use this only when the current agent has no "
            "built-in image-generation capability."
        )
    )
    prompt_group = parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt", help="Confirmed image prompt text")
    prompt_group.add_argument(
        "--prompt-file", type=Path, help="UTF-8 file containing the confirmed prompt"
    )
    parser.add_argument(
        "--reference",
        action="append",
        default=[],
        type=Path,
        help="Product reference image; repeat for multiple images",
    )
    parser.add_argument("--output", required=True, type=Path, help="Final PNG/JPEG path")
    parser.add_argument(
        "--model",
        default=os.environ.get("IMAGE_MODEL", "gpt-image-1"),
        help="Image model; defaults to IMAGE_MODEL or gpt-image-1",
    )
    parser.add_argument(
        "--api-size",
        default="1024x1024",
        help="Size requested from the image API (default: 1024x1024)",
    )
    parser.add_argument(
        "--output-size",
        default="2000x2000",
        help="Saved pixel dimensions after resize (default: 2000x2000; use 'original' to skip)",
    )
    parser.add_argument(
        "--quality",
        default="high",
        choices=("auto", "low", "medium", "high"),
        help="API image quality (default: high)",
    )
    return parser.parse_args()


def read_prompt(args: argparse.Namespace) -> str:
    if args.prompt is not None:
        prompt = args.prompt.strip()
    else:
        if not args.prompt_file.is_file():
            raise SystemExit(f"Prompt file not found: {args.prompt_file}")
        prompt = args.prompt_file.read_text(encoding="utf-8").strip()
    if not prompt:
        raise SystemExit("Prompt is empty")
    return prompt


def validate_inputs(args: argparse.Namespace) -> None:
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("Missing environment variable: OPENAI_API_KEY")
    for reference in args.reference:
        if not reference.is_file():
            raise SystemExit(f"Reference image not found: {reference}")
    if args.output.exists():
        raise SystemExit(f"Refusing to overwrite existing output: {args.output}")
    if args.output.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
        raise SystemExit("Output extension must be .png, .jpg, or .jpeg")


def create_client():
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency 'openai'. Install scripts/requirements-image-api.txt"
        ) from exc

    kwargs = {"api_key": os.environ["OPENAI_API_KEY"]}
    base_url = os.environ.get("OPENAI_BASE_URL")
    if base_url:
        kwargs["base_url"] = base_url
    return OpenAI(**kwargs)


def generate_bytes(client, args: argparse.Namespace, prompt: str) -> bytes:
    if args.reference:
        with ExitStack() as stack:
            images = [stack.enter_context(path.open("rb")) for path in args.reference]
            image_arg = images[0] if len(images) == 1 else images
            response = client.images.edit(
                model=args.model,
                image=image_arg,
                prompt=prompt,
                size=args.api_size,
                quality=args.quality,
            )
    else:
        response = client.images.generate(
            model=args.model,
            prompt=prompt,
            size=args.api_size,
            quality=args.quality,
        )

    if not response.data:
        raise SystemExit("Image API returned no image data")
    item = response.data[0]
    encoded = getattr(item, "b64_json", None)
    if encoded:
        return base64.b64decode(encoded)
    url = getattr(item, "url", None)
    if url:
        with urllib.request.urlopen(url, timeout=120) as result:
            return result.read()
    raise SystemExit("Image API returned neither b64_json nor url")


def parse_pixel_size(value: str) -> tuple[int, int] | None:
    if value.lower() == "original":
        return None
    try:
        width_text, height_text = value.lower().split("x", 1)
        width, height = int(width_text), int(height_text)
    except (ValueError, TypeError) as exc:
        raise SystemExit("--output-size must be WIDTHxHEIGHT or original") from exc
    if width <= 0 or height <= 0:
        raise SystemExit("--output-size dimensions must be positive")
    return width, height


def prepare_output_bytes(image_bytes: bytes, output: Path, size: tuple[int, int] | None) -> bytes:
    if size is None:
        return image_bytes
    try:
        from PIL import Image
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency 'Pillow'. Install scripts/requirements-image-api.txt"
        ) from exc

    with Image.open(io.BytesIO(image_bytes)) as image:
        resized = image.resize(size, Image.Resampling.LANCZOS)
        buffer = io.BytesIO()
        if output.suffix.lower() in {".jpg", ".jpeg"}:
            resized.convert("RGB").save(buffer, format="JPEG", quality=95, optimize=True)
        else:
            resized.save(buffer, format="PNG", optimize=True)
        return buffer.getvalue()


def main() -> int:
    args = parse_args()
    prompt = read_prompt(args)
    validate_inputs(args)
    target_size = parse_pixel_size(args.output_size)
    client = create_client()
    image_bytes = generate_bytes(client, args, prompt)
    output_bytes = prepare_output_bytes(image_bytes, args.output, target_size)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with args.output.open("xb") as file:
            file.write(output_bytes)
    except FileExistsError as exc:
        raise SystemExit(f"Refusing to overwrite existing output: {args.output}") from exc
    print(args.output.resolve())
    return 0


if __name__ == "__main__":
    sys.exit(main())

