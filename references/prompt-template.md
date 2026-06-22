# Prompt template (English + Chinese)

This is the skeleton you fill after transcribing the video and choosing styles.
Replace every `[PLACEHOLDER]` with real values, using the exact word timestamps from
`transcript.json`. Output BOTH languages. The creator uploads only their video to Seedance.

## How to fill it
- **Beats:** from `transcript.json`, group words into beats on natural pauses and phrase ends. Aim for **1.4s or more per beat**. If the clip is too short for the number of beats, use fewer beats.
- **Styles:** one collage style per beat, each full-frame. With reference images, describe each faithfully. Without, pick distinct looks (cubist pop-art, black-and-white newspaper, constructivist with one accent color, shattered photo, graffiti street, halftone risograph, ransom-note cut-paper, etc).
- **Per beat choose:** the on-screen TEXT (short, the key word), its position (top or bottom, never over the face), and an illustrative motion graphic for the spoken word, made of the same collage material as the active style.
- **Stressed words** become beat hits and each gets its own SFX. No background music.

## Gotchas / pro-tips (hard-won, read before filling)
These are the failure modes Seedance falls into and the exact wording that fixes them. They matter more than the skeleton.

1. **NEVER write a meta-warning about captions vs speech.** Do not add any line like "the on-screen text is NOT the script" or "don't read the captions." It backfires: the model fixates on the captions and speaks ONLY those words, truncating the line. Instead, attribute the **exact spoken phrase per beat** in the `[SHOT TIMELINE]` (`lip-sync "anyone can now turn their own footage"`) and state the **full spoken line once**. Clean attribution makes it speak everything.
2. **Identity vs style is the hardest balance.** To restyle the face every beat WITHOUT losing the person, anchor each beat: "keeps the real traits (beard, beanie, face shape), clearly recognizable as the same person, BUT repainted in this beat's material." Push style too hard and the face turns generic; push identity too hard and the face stays in one style all reel.
3. **Force full-frame in EVERY beat, not just globally.** The model loves to stylize the face and leave the background normal. Repeat in the global rule AND in each beat: "the ENTIRE frame including the background is this style, edge to edge, no untouched/photographic area."
4. **Anti-newspaper lock.** The default collage drift is newsprint. For any non-newspaper style add "no newspaper, no newsprint, no columns of printed text" (already baked into `style-library.md`).
5. **Abstract styles (cubist, 8-bit pixel, glitch) lose the face.** Either anchor identity hard (rule 2), OR keep the face recognizable and push the abstraction to the ENVIRONMENT (e.g. a game world with a recognizable face, NOT a pixelated sprite of him).
6. **No engineering specs.** Use beat timestamps in seconds (the workflow needs them), but never percentages, degrees, pixel sizes or opacity numbers. Describe motion, background and face concretely but qualitatively (how they LOOK and MOVE), not as specs.
7. **Semantic mapping is per-STYLE, not just per-MG.** Pick each beat's style to echo the word, not only its motion graphic: "footage" -> film/VHS look, "motion graphics" -> Memphis/animated-TV, "easy/simple" -> a clean minimal style, "steps/levels" -> a game-world look, a loud hook -> cubist/op-art.
8. **Never embed the real video inside a motion graphic** (it glitches). Use the LOOK only: a film strip, an old camera, a VHS frame.
9. **Lip-sync from reference is fragile.** If the line still truncates even with clean attribution (rule 1), fall back to: keep the real talking video as the base layer, or marry the original audio in post.
10. **Captions are more reliable in post than baked in.** Baked text warps and can hijack the speech; the recommended route is to keep baked text short (or skip it) and add kinetic captions afterward (e.g. in an editor), since you already have word-level timestamps.

## Motion-graphic idea library (spoken word to collage element)
- "footage" / "video" / "clip" -> a torn-paper film strip or vintage camera (the LOOK only, never embed real video, it glitches).
- "turn" / "into" / "transform" -> a big cut-out arrow sweeping, or a morph.
- "motion graphics" / "animated" / "like this" -> cut-paper shapes, motion lines, a halftone waveform, paper gears, flying fragments coming alive.
- "easy" / "simple" / "fast" -> a cut-paper HARD-to-EASY meter, a tangle snapping into a clean line, or a CLICK button with a sparkle.
- numbers / "steps" / "1 2 3" -> cut-out numbers that pop or assemble in sequence (match them to the active style: shattered style = numbers built from shards).
- "comment" / "follow" / CTA -> a cut-paper banner with an arrow.
- "money" / "grow" / "blow up" -> cut-out charts, arrows up, confetti shards.
Keep every element in the collage material so it reinforces meaning AND stays cohesive.

## English skeleton
```
[OVERALL] Vertical 9:16, about [DURATION]s. [Reels / Shorts] high-energy viral edit: fast, high-contrast, mobile-first. Animated transitions, kinetic text, animated background, motion graphics, SFX. No background music.
[MATERIAL: ONLY THE REFERENCE VIDEO] The video provides the person's face, identity, speech and lip movement. No style images; all collage styles are generated from the descriptions below.
[CHARACTER CONSISTENCY] Always the same person from the video, recognizable, mouth clearly able to move, same framing. Each shot only changes the style; the person never changes.
[FULL-FRAME RULE] Every style fills the ENTIRE frame edge to edge, background included; no untouched or photographic area. Never a centered patch with empty space.
[IDENTITY ANCHOR] In every style the face keeps the real traits (e.g. beard, beanie, face shape), clearly the same recognizable person, only repainted in that beat's material. The person never changes; abstract styles push the abstraction to the background, not the face.
[STYLES] Style 1 [TEXT] ([style name]): full-frame edge to edge incl. background, [vivid description], face recognizable as the same person but repainted in this material, mouth coherent. ... Style N ...
[FULL SPOKEN LINE] The person speaks the complete line: "[entire transcript line, verbatim]". Lip-sync every word; do not stop early.
[LIP-SYNC 1:1] Every shot lip-syncs, even abstract ones; mouth, jaw, eyes, head, rhythm copied frame for frame from the reference video, aligned to the seconds below.
[TEXT RULE] Text NEVER covers the face. Above the head or below the chin only. English ransom-note cut-out, clear, no warping, no watermark.
[TEXT ANIMATION] [TEXT 1] [position] enters on "[word]" ([t]s); ... ; never over the face.
[MOTION GRAPHICS] [t]s "[word]": [collage element illustrating the word]. (one line per beat)
[CONTINUOUS MOTION] Fragments float, shift, parallax; halftone flickers; every stressed word a beat hit; no static frame.
[BEAT HITS] [t] "[word]"; ... (the stressed words)
[ANIMATED TRANSITIONS, never hard cuts] [t] Style X to Style Y: [animated transition, e.g. morph / card-shuffle / spray wipe / paper tear].
[BACKGROUND ANIMATION] per style: [...].
[SFX, no background music, aligned] [t] [event]: [precise sound]. (one line per transition, MG and text pop)
[SHOT TIMELINE] [t1 to t2] [TEXT] (Style k): lip-sync "[exact spoken line]"; [MG at its word]; [text enters].
[QUALITY] Pro viral look, sharp, mobile-clear; face is always the person and never covered by text; text and numbers clear, no warping, no overflow; no watermark, no signature.
```

## Chinese skeleton (mirror; keep spoken lines and on-screen TEXT in the creator's language)
```
[整体设定] 竖屏 9:16,约 [DURATION] 秒。高能病毒式剪辑:快、强对比、手机优先。动画转场、动态文字、动态背景、动态图形、音效全开。无背景音乐。
[素材:只有参考视频] 视频提供本人的脸、身份、说话口型与表演。没有风格参考图,所有拼贴风格按下面文字生成。
[人物一致性] 全程同一个人,脸不变、清晰可辨、嘴部清晰可动,机位一致;每镜头只换风格。
[满屏规则] 每个风格填满整个画面,边到边,连背景一起,没有任何未处理或写实的区域,绝不只在中央留白。
[身份锚定] 每个风格里脸都保留本人的真实特征(如胡子、毛线帽、脸型),始终是同一个可辨认的人,只是用该镜头的材质重绘。人物绝不改变;抽象风格把抽象效果放到背景,而不是脸上。
[风格] 风格1 [TEXT]([名称]):满屏边到边连背景,[详细描述],脸仍是同一个可辨认的人、只是用该材质重绘,嘴连贯。... 风格N ...
[完整台词] 本人说完整句:"[逐字的完整原话]"。每个字都对口型,不要提前停。
[最重要:口型 1:1] 每镜头都 lip-sync,抽象风格也要;口型、下巴、眼神、头部、节奏逐帧复制参考视频,对齐下面秒数。
[文字规则] 文字绝不盖脸,只放头顶上方或下巴下方;英文剪报 cut-out,清晰不变形不水印。
[文字动画] [TEXT1] [位置] 在 "[word]"([t]秒)入场;...;绝不盖脸。
[动态图形 MG] [t]秒 "[word]":[剪纸材质、说明那个词的元素]。
[全程动效] 碎片浮动、错位、视差,半色调闪烁,每个重音词打点,无一帧静止。
[打点] [t] "[word]";...
[动画转场,绝不硬切] [t] 风格X→风格Y:[动画转场]。
[背景动画] 各风格:[...]。
[音效,无背景音乐,对齐] [t] [事件]:[精确的声音]。
[分镜时间轴] [t1 到 t2] [TEXT](风格k):lip-sync "[原话]";[MG 在它的词];[文字入场]。
[质量] 专业病毒质感,锐利、手机清晰;脸全程是本人且绝不被文字盖住;文字数字清晰不变形不溢出;不要水印不要签名。
```

## Worked example (generic, a 3-beat clip)
Spoken line (from the transcript): "This one trick blew up my account. Steal it before I delete this."
Transcript beats: "This one trick blew up my account" (0.0 to 2.1), pause, "Steal it" (2.5 to 3.2), "before I delete this" (3.2 to 4.4).

Filled English prompt (abridged):
```
[OVERALL] Vertical 9:16, about 4.4s. Shorts high-energy viral edit ... No background music.
[STYLES] Style 1 BLEW UP (cubist pop-art collage): full-frame ... Style 2 STEAL IT (black-and-white newspaper collage): full-frame ... Style 3 DELETE (shattered photo collage): full-frame ...
[MOTION GRAPHICS] 1.6s "blew up": cut-out arrows shooting up + confetti shards. 2.5s "steal": a cut-paper hand grabbing a tag. 3.6s "delete": a torn-paper trash/X that shreds the frame.
[ANIMATED TRANSITIONS] 2.1 Style 1 to Style 2: paper shuffle. 3.2 Style 2 to Style 3: paper tear.
[SFX] 1.6 rising whoosh + pop on the arrows; 2.1 paper riffle whoosh; 3.2 sharp paper RIP; ...
[SHOT TIMELINE] 0.0 to 2.1 BLEW UP (Style 1): lip-sync "This one trick blew up my account"; arrows-up MG at 1.6; text top. 2.5 to 3.2 STEAL IT (Style 2): lip-sync "Steal it"; grab-hand MG; text bottom. 3.2 to 4.4 DELETE (Style 3): lip-sync "before I delete this"; shred MG; text bottom.
```
Then mirror the whole thing in Chinese. Tell the creator to upload only their video.
