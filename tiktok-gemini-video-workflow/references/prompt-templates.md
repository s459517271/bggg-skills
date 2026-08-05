# English Prompt Templates

Write every storyboard-image prompt and video-generation prompt in English. Keep product names, source-video captions, logos, and spoken lines in their exact original language when fidelity requires it. Do not translate or rewrite a source caption unless the user asks.

## 1. Complete 9:16 3x3 Storyboard Prompt

Generate one intact portrait storyboard sheet. Do not split the grid into separate reference images.

```text
Inputs:
- Product Image 1...N: the single source of truth for product identity, geometry, color, material, proportions, packaging, label placement, logo placement, and scale.
- Reference Video: controls the hook, narrative function, shot order, action rhythm, camera path, transition logic, and ending state.
- Previous Segment Final Frame: [omit for Segment 1 / for Segment 2, this is the highest-priority continuity reference and the exact starting state].
- Previous Approved Storyboard: [omit for Segment 1 / for Segment 2, locks the same character, face, hair, wardrobe, hands, environment, lighting, lens language, and spatial direction].

Goal:
Create one complete VERTICAL PORTRAIT 9:16 storyboard sheet containing a clean 3x3 chronological grid for Segment [1/2] of a [duration]-second TikTok product video. This is a director's time-and-action plan for video generation, not a poster, mood board, infographic, or collection of unrelated stills.

Story:
[One precise sentence stating the hook, change, reveal, or narrative payoff.]

Reference Roles:
- The Reference Video controls [timeline / camera path / action rhythm / transition / text-led narrative].
- Product Image 1...N controls product identity only and must not replace or redesign the approved character or environment.
- [Segment 2 only] The Previous Segment Final Frame overrides all other references for the first-panel pose, framing, hand position, object state, lighting, and background.
- [Segment 2 only] The Previous Approved Storyboard controls identity and visual continuity after the exact first-panel state.

Character / Product Lock:
[Lock the same adult character, face, age range, skin tone, hair, makeup, clothing, accessories, hands, nail count, body proportions, and performance style.]
[Lock exact product geometry, material, color, label/logo placement, dimensions, parts, packaging, and realistic scale.]

Scene Lock:
[Lock location, background objects, time of day, light source and direction, color temperature, camera height, lens perspective, scene direction, and key props.]

Visual Style:
Photorealistic native-phone TikTok UGC with believable skin, hair, fabric, packaging, and product texture; realistic exposure, depth, contact shadows, reflections, motion cues, and casual camera imperfections matching the Reference Video.

Storyboard Layout:
- One VERTICAL PORTRAIT 9:16 canvas containing exactly nine equal cinematic panels in a clean 3x3 grid.
- Read left-to-right and top-to-bottom.
- Each panel is one sequential keyframe from the same continuous segment.
- The grid itself is a planning image only. Do not place captions, panel numbers, timecodes, arrows, UI, logos, or explanatory text inside the image.

Panel 1: [time range], [shot size and angle], [hook/setup/continuity function], [visible action and object state], camera movement: [start state or movement cue], emotion: [restrained physical performance cue].
Panel 2: [time range], [shot size and angle], [story function], [visible action and state change], camera movement: [movement], emotion: [cue].
Panel 3: [time range], [shot size and angle], [story function], [visible action and state change], camera movement: [movement], emotion: [cue].
Panel 4: [time range], [shot size and angle], [story function], [visible action and state change], camera movement: [movement], emotion: [cue].
Panel 5: [time range], [shot size and angle], [turn/escalation/transition function], [visible action and state change], camera movement: [movement], emotion: [cue].
Panel 6: [time range], [shot size and angle], [story function], [visible action and state change], camera movement: [movement], emotion: [cue].
Panel 7: [time range], [shot size and angle], [story function], [visible action and state change], camera movement: [movement], emotion: [cue].
Panel 8: [time range], [shot size and angle], [payoff/result function], [visible action and state change], camera movement: [movement], emotion: [cue].
Panel 9: [time range], [shot size and angle], [ending/continuation function], [final stable visible state], camera movement: [settle or hold], emotion: [cue].

Continuity Requirements:
- Keep the same character, face, hair, wardrobe, accessories, hands, product, environment, lighting direction, color temperature, lens perspective, and scene direction across all nine panels.
- Every panel must advance the same story; do not create nine beauty variations.
- Preserve cause and effect. Do not show the solved state before the product action that creates it.
- [Segment 2 only] Panel 1 must reproduce the Previous Segment Final Frame exactly. Change only the actions and product states in Panels 2-9.

Text / Logo Rules:
- Preserve only real physical product labels or logos that are visible in the supplied product references, with correct placement, perspective, occlusion, material, lighting, and blur.
- Do not render source-video captions, subtitles, hook text, timecodes, UI, or floating graphic overlays in the storyboard.
- Record required on-screen hook text separately for post-production, preserving exact spelling, capitalization, punctuation, line breaks, position, style, and time range.

Negative Rules:
No landscape 16:9 canvas, no separate images, no poster layout, no infographic, no unrelated backgrounds, no identity drift, no wardrobe drift, no product redesign, no product-color drift, no label gibberish, no premature result, no repeated action, no impossible state change, no extra or missing fingers, no fused hands, no malformed anatomy, no floating objects, no random characters, no captions, no panel labels, no watermark, no collage clutter.
```

## 2. Frame-by-Frame Video Prompt Contract

The storyboard-image prompt and the video-generation prompt are two independent artifacts:

- The storyboard image is always one intact 9:16, 3x3 sheet containing exactly nine chronological key states.
- The video prompt is not limited to those nine panels. Re-analyze the Reference Video and write one `VIDEO FRAME` entry for every visible frame state identified in the source breakdown.
- If the source breakdown contains 16 frame states, the video prompt must contain `VIDEO FRAME 01` through `VIDEO FRAME 16`. Do not collapse them into six or nine generic shots.
- The nine-panel storyboard controls visual continuity and key-state direction only. It must not determine, reduce, rename, or replace the video frame list.
- The video frame list must account for the complete runtime with consecutive, non-overlapping timecodes and an explicit state handoff from every frame entry to the next.

### Duration Feasibility Gate

- The sum of all video-frame durations must equal the live generator duration exactly.
- Preserve every frame state found in the Reference Video analysis. Do not delete frame entries merely to reach an assumed “normal” count.
- Derive each frame entry's duration from the source timing and the target segment timing. Rapid inserts may be shorter than the average cadence when the reference uses them.
- If the reference duration requires two generated segments under the workflow's duration rule, assign every frame state to Segment 1 or Segment 2 without dropping any; Segment 2 starts from Segment 1's real final frame.
- Give a complex product state change enough time to show contact, force, resistance, and the resulting state. When one source frame state contains several simultaneous details, describe all of them in that frame entry.
- The video frame list must have no time gaps, overlaps, missing source states, duplicated actions, or unexplained jumps.

### Global Fixed Requirements

```text
GLOBAL FIXED REQUIREMENTS

Continuity and completion:
- Generate one complete, fluid, temporally continuous video.
- Every video frame entry must begin from the exact character, limb, prop, product, part-count, assembly, and spatial state left by the previous frame entry.
- Preserve cause and effect. No result may appear before the action that creates it.

Music and voice:
- Background music: [genre], [mood], [energy curve], [rhythm or beat], mixed below required dialogue and action sounds.
- Voiceover language: [one target language].
- If multiple languages are requested, create one separate prompt/output variant per language unless the user explicitly requests a bilingual video.
- Dialogue / voiceover wording, speaker, tone, and timing must be exact. Do not require lip sync when the speaking mouth is off-frame.

Visible-text policy:
- Choose exactly one policy before writing the video frame list:
  A. NO VISIBLE TEXT: no captions, subtitles, dialogue text, notes, shot numbers, titles, timecodes, brand names, logos, package text, account names, platform names, UI, or watermarks.
  B. PHYSICAL LABELS ONLY: preserve exact physical product labels/logos from the supplied references, but generate no captions, subtitles, UI, floating graphics, platform marks, or invented text.
- If Policy A is selected, use only the product's non-text visual design from the product references. This policy overrides label preservation.
- Required hook captions are recorded separately for post-production and are never delegated to the video model.

Character identity:
- The main character is controlled strictly by the designated Main Character Reference Image. Do not describe or reconstruct the main character's specific facial features in text.
- Other characters must not reuse the main character's face or one another's face. Unless twins or multiples are explicitly required, every secondary character must have a unique, stable face, age range, body type, wardrobe, and role across all video frames.
- Do not copy the number of people from the number of supplied reference images.

Product and part identity:
- Product Image 1...N jointly describe one physical product and its parts from different views. They do not authorize duplicate products or duplicate parts.
- Lock the product's non-text geometry, color, material, proportions, structure, interfaces, part shapes, assembly logic, and connection method.
- Preserve product count, part count, assembly state, orientation, and location from video frame to video frame.
- A detached functional part must remain that same part; do not replace it with a complete product.
- For every product/tool action, name the holding area, functional working end, contact target, and motion direction. Never use a handle, base, back, cap, or other non-working surface to perform the function.

Body mechanics and object conservation:
- Assign every action to the character's own left hand, right hand, left foot, or right foot.
- One limb cannot perform two incompatible actions at the same time.
- Paired objects and detachable parts keep stable counts and positions.
- No duplicated object, no single object in two places, no disappearing part, no teleportation, and no spontaneous assembly/disassembly.

Realism and camera:
- Use hyper-realistic live-action lifestyle footage with natural behavior, relaxed body language, unrehearsed observational energy, believable environment relationships, rich real-world detail, and anatomically plausible motion.
- Faces, hands, product geometry, part structure, and key contact actions must remain clear and readable.
- A video frame entry labeled LOCKED-OFF must have no handheld shake. Natural handheld motion is allowed only when the entry is explicitly labeled HANDHELD.
- Editing cadence: average frame-state duration [target], primary transition [hard cut / match cut / other], audio-picture synchronization [weak beat sync / strong beat sync / natural action sync].
```

### Mandatory Per-Video-Frame Schema

Every frame state identified in the Reference Video breakdown must receive its own complete block using all fields below. Do not compress multiple frame states into one paragraph, and do not restrict the count to the nine storyboard panels.

```text
[VIDEO FRAME 01]
Timecode and Duration:
[00.0-01.5s, 1.5 seconds. Timecodes must be consecutive.]

Reference Images:
[None / Main Character Image / Product Images 1-5 / Previous Segment Final Frame / other exact roles.]

Continuity In:
[Exact character pose, gaze, left/right limb positions, product state, part count, prop locations, camera position, lighting, and motion inherited from the previous shot.]

Shot Purpose:
[Hook / setup / preparation / product reveal / contact / state change / proof / payoff / ending.]

Framing and Camera:
[Shot size, camera angle, camera height, lens feel, subject position, LOCKED-OFF or HANDHELD, camera movement, focus target, and ending composition.]

Character and Limb Actions:
[Who acts; exact left hand, right hand, left foot, and right foot assignments; posture, balance, gaze, expression, and one primary visible action.]

Product and Part State:
[Product identity, count, assembly state, orientation, location, which hand supports it, and what changes during this shot.]

Functional Interaction:
[Holding area, working end, contact target, contact point, force/motion direction, visible resistance, and before -> action -> after state transition. Write “None” when no functional interaction occurs.]

Secondary Characters:
[Identity and continuity locks or “None”.]

Environment and Lighting:
[Only frame-specific changes; otherwise state “Continue the locked scene unchanged”.]

Audio:
- Voiceover / Dialogue: [exact line, language, speaker, tone, timing, or None].
- Required Sound Effect: [action-synchronized sound or None].
- Music / Ambience: [how the global track and ambience continue].

Transition In / Out:
[Hard cut / match cut / continuation; triggering movement or beat; no transition invented when the frame entry is locked-off.]

Continuity Out:
[Exact stable end state that the next video frame entry must inherit: pose, limbs, product/part count and locations, assembly state, camera, light, and motion direction.]
```

## 3. Single-Segment Video Prompt

```text
Inputs:
- Storyboard Image 1: one intact 3x3 chronological storyboard, read left-to-right and top-to-bottom. It controls character and scene continuity, shot progression, action order, rhythm, transition, and target ending state. It must never appear as a grid in the output.
- Product Image 1...N: the single source of truth for product geometry, color, material, proportions, parts, packaging, label/logo placement, and scale.
- Reference Video Analysis: controls the hook, narrative function, camera logic, action rhythm, and editing cadence; do not copy unrelated products or people.

Goal:
Generate one [actual generator duration]-second, photorealistic TikTok product video in VERTICAL PORTRAIT, aspect ratio 9:16 (width:height), 1080x1920 orientation. Preserve the source hook and narrative logic while replacing only the product-specific solution.

Reference Roles:
[State exactly what each uploaded image controls and what it must not change.]

Output Format — Non-Negotiable:
- VERTICAL PORTRAIT, aspect ratio 9:16 (width:height), 1080x1920 orientation.
- This is the visual width-to-height ratio, not a duration or timestamp.
- One full-screen video only. Never show the storyboard grid, panel borders, panel numbers, split screen, collage, multi-window layout, black bars, rotation, square framing, or 16:9 landscape.
- The written duration must match the generator's live setting; the prompt cannot override the interface setting.

Must Follow:
- Preserve the Reference Video's [hook / scene order / camera path / action rhythm / transition / payoff].
- Keep one consistent character, product, environment, lighting logic, and spatial direction.
- Preserve cause and effect and the exact order of physical state changes.
- Use the storyboard only as a chronological director's plan, never as visible content.
- Apply the complete Global Fixed Requirements and Mandatory Per-Video-Frame Schema from Section 2.
- Account for the entire runtime frame by frame. Do not summarize several different video frame states in one sentence.
- Build the `VIDEO FRAME 01...N` list from a fresh breakdown of the Reference Video. Its count is independent of the nine storyboard panels.

Character / Product Lock:
[Assign a Main Character Reference Image. Lock identity through that image without describing or reconstructing specific facial features in text. Lock hair, wardrobe, accessories, hands, expression language, and performance.]
[Detailed product identity, geometry, material, color, labels, parts, packaging, scale, and state.]

Scene Lock:
[Location, background, props, time of day, light source, direction and falloff, color temperature, depth, lens perspective, camera height, and start/end framing.]

Camera Plan:
[Starting shot size and angle.] [Camera movement with speed and emotional purpose.] [Any cut or transition with exact timing.] [Ending framing and stable hold.] Keep exposure, white balance, focus logic, and scene direction consistent.

Complete Video Frame List — Mandatory:
[Write VIDEO FRAME 01...N using every field in the Mandatory Per-Video-Frame Schema. Include every visible frame state found in the Reference Video breakdown, even when N is greater than nine. Timecodes must start at 0.0s, remain consecutive and non-overlapping, and end exactly at the live generator duration.]

Realism Pass:
- Lighting: use believable directional light, falloff, contact shadows, and material-specific reflections matching the scene.
- Texture: preserve pores, fine lines, hair fibers, fabric weave, fingerprints, packaging grain, product edges, and surface imperfections where relevant; no beauty-filter plastic finish.
- Depth: maintain clear foreground, midground, and background separation without obscuring the face, hand action, or product.
- Performance: use restrained eye movement, breathing, posture, hand pressure, weight shift, and micro-expression rather than theatrical acting.
- Camera: preserve natural phone-camera micro-movement or fixed-camera logic from the reference.
- Physical response: hair, fabric, packaging, liquid, tools, product parts, and hands must react to gravity, pressure, friction, inertia, and contact.

Action Physics Pass:
- Initial state: [visible starting state of hands, product, packaging, surface, and environment].
- Preconditions: [what must already be open, aligned, held, dry, attached, or visible].
- Contact: [which hand/finger/tool touches which exact object or surface].
- Force direction: [press / pull / tap / twist / lift / sweep direction].
- Visible resistance: [flex, friction, tension, weight, liquid viscosity, packaging resistance].
- State transition: [before state -> action -> after state], with no teleportation or skipped intermediate state.
- Quantity and identity conservation: no duplicated, disappearing, fused, or spontaneously transformed objects.

Audio:
- Dialogue / Voiceover: [exact line, speaker, tone, and timing; if the mouth is off-frame, specify voiceover and do not require lip sync].
- Sound Effects: [action-synchronized sounds].
- Ambience: [room or environmental sound].
- Music: [style and level / none].

Text / Logo Rules:
- Physical product labels and logos must follow the product references exactly and remain integrated into the object with correct perspective, lighting, occlusion, and motion blur.
- Do not ask the model to render captions, subtitles, hook text, UI, or floating graphics.
- POST-PRODUCTION TEXT REQUIREMENT: [exact source caption or "None"]. If required, preserve exact spelling, capitalization, punctuation, line breaks, screen position, font family/weight, color, shadow/outline, start time, and end time. The task is incomplete until this text is verified after download.

Continuity Requirements:
[Identity, wardrobe, hand, product, environment, camera, light, and object-state rules that must remain unchanged from first frame to last.]

Negative Rules:
Never output 16:9 landscape, square, letterboxed, or rotated video. No visible storyboard grid, panels, borders, split screen, collage, panel numbers, captions generated by the model, subtitle gibberish, random text, watermark, identity drift, face swap, wardrobe drift, product redesign, color drift, label gibberish, anatomy errors, extra or missing fingers, fused hands, floating objects, object teleportation, skipped state changes, reversed action order, premature final result, repeated action, random scene change, flat artificial lighting, plastic skin, or over-polished studio style when the reference is casual UGC.
```

## 4. Segment 2 Continuation Video Prompt

Use only after Segment 1 has been generated, downloaded, post-processed, and its last stable real frame has been extracted.

```text
Inputs:
- Previous Segment Final Frame: highest-priority reference and exact frame-zero state for pose, hand position, object state, framing, environment, lighting, focus, and camera direction.
- Storyboard Image 2: one intact 3x3 chronological storyboard for Segment 2. It controls only the continuation action order, rhythm, camera progression, and target ending state. It must never appear as a grid in the output.
- Product Image 1...N: product-identity references only. They must not redesign the character, hands, environment, or exact starting state.
- Previous Approved Storyboard: continuity lock for the same character, face, hair, wardrobe, hands, environment, lighting, and visual language.

Goal:
Generate one [actual generator duration]-second seamless continuation in VERTICAL PORTRAIT, aspect ratio 9:16 (width:height), 1080x1920 orientation. Frame zero must visually match the Previous Segment Final Frame before any new action begins.

Reference Priority:
1. Previous Segment Final Frame = exact starting state; highest priority.
2. Previous Approved Storyboard = character, wardrobe, environment, light, lens, and spatial continuity.
3. Storyboard Image 2 = new action order and target ending state.
4. Product Image 1...N = product identity only.

Output Format — Non-Negotiable:
[Use the same complete Output Format block as the single-segment template.]

Must Follow:
- Hold or continue the exact final-frame state for the first 0.2-0.5 seconds before the next action becomes readable.
- Preserve motion direction, body mechanics, object state, camera position, focus, exposure, white balance, and scene geography across the join.
- Read Storyboard Image 2 chronologically; never render the grid.
- Apply the complete Global Fixed Requirements and Mandatory Per-Video-Frame Schema from Section 2.

Character / Product Lock:
[Detailed continuity locks.]

Scene Lock:
[Detailed continuity locks.]

Camera Plan:
0.0-[time]s keeps the exact previous framing and motion direction; then [continuation movement/cut plan]; end on [stable target state].

Complete Video Frame List — Mandatory:
- VIDEO FRAME 01 Continuity In must reproduce the Previous Segment Final Frame exactly.
- Hold or naturally continue that state for the first 0.2-0.5 seconds.
- Write every source frame state assigned to Segment 2 with the full Mandatory Per-Video-Frame Schema.
- End exactly at the live generator duration with a stable Continuity Out state.

Realism Pass:
[Use the same complete Realism Pass as the single-segment template, adapted to this segment.]

Action Physics Pass:
[Use the same state-machine fields as the single-segment template, starting from the real final-frame state.]

Audio:
[Continue ambience/music naturally; list dialogue/voiceover and synchronized effects.]

Text / Logo Rules:
[Use the same complete rules and post-production text requirement.]

Continuity Requirements:
No first-frame jump, no new character, no changed face, hair, wardrobe, hands, environment, light, lens, focus, product identity, product state, or camera direction unless the Scene Script explicitly changes it after the join.

Negative Rules:
Never output 16:9 landscape. No first-frame mismatch, jump cut at frame zero, visible storyboard grid, panel borders, collage, model-generated captions, random text, watermark, identity drift, product drift, object teleportation, repeated previous action, reversed action, malformed hands, extra fingers, random scene change, or sudden exposure/white-balance shift.
```

## 5. Prompt QA Gate

Reject and rewrite a prompt if any answer is missing:

1. Are all instructions in English, except exact source captions, physical labels, product names, or spoken lines that must remain unchanged?
2. Does every uploaded reference have one explicit role and a clear priority?
3. Does the prompt state `VERTICAL PORTRAIT, aspect ratio 9:16 (width:height)` in Goal, Output Format, and Negative Rules?
4. Does every storyboard panel include time, shot size, story function, visible action/state, camera movement, and emotion?
5. Does the video prompt cover the full runtime with consecutive, non-overlapping video-frame timecodes whose durations sum exactly to the live generator duration?
6. Are character, product, scene, lighting, lens, and continuity locks testable?
7. For hand-object actions, are initial state, precondition, contact, force, resistance, state transition, and quantity conservation explicit?
8. Is the 3x3 storyboard described only as a planning timeline, with grid leakage forbidden in the final video?
9. For Segment 2, is the real Previous Segment Final Frame the highest-priority exact starting state?
10. Is source hook text separated into a post-production requirement with exact wording, layout, style, and timing instead of relying on the video model?
11. Does every frame state identified in the Reference Video breakdown have its own `VIDEO FRAME` block containing every Mandatory Per-Video-Frame field, including Reference Images, Continuity In, limb assignments, Product and Part State, Functional Interaction, Audio, Transition, and Continuity Out?
12. Is the video frame count independent of the nine-panel storyboard, with no source frame state silently collapsed, omitted, or renamed merely to match nine panels or an assumed shot-count limit?
13. Is exactly one visible-text policy selected, with no contradiction between “no visible text” and physical-label preservation?
14. Is the main character controlled by the designated reference image without reconstructing specific facial features in text, and are all secondary identities unique and stable?
15. Are every product, detachable part, paired object, left/right limb, holding point, working end, contact target, and motion direction physically consistent from video frame to video frame?
