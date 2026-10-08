---
name: ux-audit
description: Audit UI code (HTML/CSS/JS/React) against DesignMotionHQ patterns and senior anti-patterns.
arguments:
  - name: path
    description: File path to audit
    required: true
---

# UX Audit Command

Run the automated UX Engine code auditor:

```bash
python3 scripts/ux_engine.py audit "$PATH"
```

Review results for:
- Outline elimination without replacement focus rings
- Layout-displacing hover transforms
- Emoji icons used in place of SVG
- Missing submit guards and pending states
- Flattened pure-black surfaces in dark mode
- Unchecked chart baseline truncations
- Incomplete view states (loading, empty, error)
