---
name: ux-route
description: Route any UI module to the exact primary & secondary DesignMotionHQ patterns.
arguments:
  - name: module
    description: Name of the UI module (e.g., settings, data-table, checkout, onboarding)
    required: true
---

# UX Route Command

Execute the UX Engine routing workflow for the specified module:

```bash
python3 scripts/ux_engine.py route "$MODULE"
```

1. Identify the module requirements and user stakes.
2. Select the mandatory Primary patterns.
3. Select Secondary patterns only if those controls exist on screen.
4. Enforce the required view states (loading, empty, error, active).
5. State what was intentionally excluded to maintain design clarity.
