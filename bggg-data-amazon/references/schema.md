# Amazon collection contract

## Target TSV

Required column: `asin`.

Optional columns:

- `mode`: `basic`, `full`, or `max`; default `basic`
- `lang`: normalized row language; default `EN`
- `title`: product name stored in context

## Evidence directory

Keep:

- `ASIN_mode.attemptN.json`
- `ASIN_mode.attemptN.stdout.log`
- `ASIN_mode.attemptN.stderr.log`
- reconciled `ASIN_mode.json`
- `acquisition_manifest.json`
- `normalize_summary.json`

## Normalized JSONL

Rows contain `platform`, `lang`, `source_id`, nullable `native_id`, parsed `date`, `date_raw`, exact `text_raw`, engagement fields, source/ASIN/product context, `keyword_hit`, and `round`.
