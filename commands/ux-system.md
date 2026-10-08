---
name: ux-system
description: Generate complete semantic design tokens (OKLCH, modular typography, concentric radii, shadows).
---

# UX System Command

Generate the full semantic token architecture:

```bash
python3 scripts/ux_engine.py tokens
```

Includes:
- OKLCH surface ladder with high-contrast text ratios
- 4px numeric spacing grid
- Concentric radii formula: $R_{inner} = R_{outer} - Padding$
- Calibrated cubic-bezier easing curves
