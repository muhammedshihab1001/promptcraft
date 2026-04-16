# Name: Image Generation Profile
# Works with: Midjourney, DALL-E 3, Flux, Ideogram, Leonardo AI, Stable Diffusion
# Best for: Generating high-quality prompts for image AI tools
# Extends: None
# Version: 0.1.0

---

## Prompt Structure

Every image prompt should follow this order:

```
[Subject] + [Style] + [Lighting] + [Composition] + [Quality modifiers]
```

Example:
```
A lone samurai standing in a bamboo forest, cinematic photography style,
golden hour side lighting, wide shot, 8k, highly detailed, sharp focus
```

---

## Rules

- Be specific. Vague prompts produce vague images.
- Name the style explicitly: "oil painting", "photorealistic", "anime", "watercolor".
- Name the lighting: golden hour, studio, overcast, neon, candlelight.
- Name the composition: close-up, wide shot, bird's eye view, Dutch angle.
- Add quality terms at the end: "highly detailed", "sharp focus", "8k".

---

## Negative Prompts (where supported)

Always include negatives for clean output:
```
blurry, low quality, watermark, text, extra limbs, distorted, oversaturated
```

---

## Per-tool Notes

| Tool | Max prompt length | Supports negatives | Notes |
|---|---|---|---|
| Midjourney | ~60 words ideal | Yes, with `--no` | Use `--ar` for aspect ratio |
| DALL-E 3 | ~4000 chars | No | Describe in natural language |
| Flux | No hard limit | Yes | Very prompt-sensitive |
| Ideogram | ~500 chars | No | Great for text in images |
| Leonardo AI | ~500 chars | Yes | Use preset styles |
| Stable Diffusion | No hard limit | Yes | Most flexible |
