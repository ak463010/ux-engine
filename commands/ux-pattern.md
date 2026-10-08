---
name: ux-pattern
description: Look up detailed rule, insights, do/don'ts, and CSS formulas for any of the 112 patterns.
arguments:
  - name: slug
    description: Pattern slug (e.g. accordion-disclosure, border-radius, doherty-threshold)
    required: true
---

# UX Pattern Command

Retrieve the complete pattern specification:

```bash
python3 scripts/ux_engine.py pattern "$SLUG"
```
