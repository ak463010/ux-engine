# UX Engine — Claude Code Plugin

> **Senior UI/UX Intelligence by DesignMotionHQ**  
> 112 tactical patterns, 31-module routing engine, Hybrid Design System principles, token architecture, and the production-grade 15-point AppGuard checklist.

UX Engine empowers Claude Code to think, design, and architect user experiences like a senior UI/UX designer and design systems engineer. Based on the 112 tactical patterns from [@designmotionhq](https://www.instagram.com/designmotionhq/) and the house methodology of the Hybrid Design System.

---

## Features

- **112 Tactical UX Patterns**: Complete dataset across 7 categories (Visual, Interaction, Forms, Feedback, Content, Navigation, Motion) with hooks, deep insights, do/don'ts, and implementation rules.
- **31-Module Routing Engine**: Directs any UI module (settings, data tables, forms, pricing, onboarding, dashboards) to the exact primary foundation and secondary elements.
- **Automated UI/UX Auditor**: Scans HTML, CSS, React, and Vue code for layout shifts, missing focus rings, emoji icons, missing submit guards, and uncalibrated contrast.
- **Production AppGuard Runtime**: Drop-in script protecting users from boot timeouts, unhandled errors, offline states, and double-submits.
- **Semantic Token Architecture**: OKLCH color palettes, 4px numeric spacing grid, concentric radii formulas ($R_{inner} = R_{outer} - Padding$), and calibrated easing curves.
- **15-Point Pre-Delivery Checklist**: Mandatory verification suite before shipping any screen.

---

## Installation

### Method 1: Local Development / Skills Directory
To load UX Engine into your Claude Code session:

```bash
claude plugin validate /home/ubuntu/claude-plugin
```

Or pass via command line:
```bash
claude --plugin-dir /home/ubuntu/claude-plugin
```

### Method 2: Global Marketplace
Once published to your repository:
```text
/plugin install ux-engine
```

---

## Slash Commands

| Command | Description |
|---|---|
| `/ux-route <module>` | Route any UI module to the exact primary & secondary patterns |
| `/ux-audit <path>` | Audit UI code for senior design anti-patterns |
| `/ux-pattern <slug>` | Inspect deep rules and insights for any of the 112 patterns |
| `/ux-guard` | Inspect and configure the AppGuard runtime |
| `/ux-system` | Output complete semantic design tokens (OKLCH, radii, typography) |
| `/ux-checklist` | Display the 15-point pre-delivery verification checklist |

---

## CLI Usage

The engine can also be executed directly via Python CLI:

```bash
# Route a module
python3 scripts/ux_engine.py route "settings"

# Search patterns
python3 scripts/ux_engine.py search "table"

# Inspect pattern details
python3 scripts/ux_engine.py pattern accordion-disclosure

# Audit code
python3 scripts/ux_engine.py audit src/components/Form.tsx

# Print 15-point checklist
python3 scripts/ux_engine.py checklist

# Print design tokens
python3 scripts/ux_engine.py tokens
```

---

## 15-Point AppGuard Checklist

1. **Boot Guard**: `app-guard.js` loaded first; automatic reload on script failure.
2. **Error Screen**: Full-page recovery panel for uncaught runtime errors.
3. **Offline Banner**: Network state listener holding mutations when offline.
4. **State Completeness**: Explicit designs for loading, empty, partial, and error states.
5. **Submit Guard**: Double-click prevention with pending/done feedback.
6. **Destructive Friction**: Danger actions named, separated, with undo toast.
7. **Human Microcopy**: Error copy in user terms, never raw error messages.
8. **Concentric Radii**: Inner radius = Outer radius - Padding.
9. **No Emoji Icons**: 100% SVG icons with fixed viewBox (no emojis as UI controls).
10. **Calibrated Motion**: Entrances 200–300ms ease-out; hover 150–200ms.
11. **WCAG AA Contrast**: 4.5:1 minimum contrast on body text.
12. **Touch Targets**: Minimum 44x44px clickable target bounding box.
13. **Mobile 390px Check**: Input text >= 16px (no iOS auto-zoom); no horizontal scroll.
14. **Focus Rings**: 2px offset contrast ring visible on keyboard Tab traversal.
15. **Doherty Threshold**: Visual feedback within 400ms for every interaction.

---

## License

MIT © DesignMotionHQ & Senior UX Engineering Team.
