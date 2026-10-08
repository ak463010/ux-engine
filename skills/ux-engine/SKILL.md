---
name: ux-engine
description: Senior UI/UX Design and Engineering Engine by DesignMotionHQ. Features 112 tactical patterns across 7 categories, a 31-module routing engine, Hybrid Design System principles, token architecture, and the production-grade 15-point AppGuard reliability checklist.
---

# UX Engine — Senior UI/UX Intelligence

UX Engine provides senior design system architecture, cognitive ergonomics, and battle-tested component patterns adapted from [@designmotionhq](https://www.instagram.com/designmotionhq/) and the Hybrid Design System methodology.

## Core Philosophy: The Senior Designer's Mindset

1. **Intent-First Design**: Before writing any code, identify the real user and their highest-stakes mistake. Model actors explicitly; never rely on ephemeral viewer-relative state.
2. **Hierarchy Over Defaults**: Every view requires deliberate primary, secondary, and tertiary ranking. Nothing is weighted equally by accident.
3. **Pick the Best Few, Never All**: A settings page requires four or five precise patterns, not forty. Prioritize specific systems over generic one-liners.
4. **State Completeness**: Loading, empty, error, active, disabled, success, and offline states must be designed upfront.
5. **Audit Against Written Remit, Not Vibes**: Evaluate every control against the screen's core responsibilities. Defend decisions with cognitive principles (Fitts's Law, Doherty Threshold, Von Restorff effect, Zeigarnik effect).

---

## 31-Module Routing Table

When building or reviewing any product screen, route to the primary foundation first, then selectively add secondary patterns only if that element exists:

| Module Being Built | Primary Patterns (Mandatory) | Secondary Patterns (Conditional) |
|---|---|---|
| **Settings page** | `settings-system`, `toggle-anatomy`, `form-field-states`, `autosave-ux` | `destructive-actions`, `disabled-buttons`, `dark-mode-surfaces` |
| **Dashboard / admin home** | `de-ai-dashboard`, `number-formatting`, `charts-that-lie`, `loading-states-system`, `empty-states` | `skeleton-loading`, `notification-badge`, `avatar-system` |
| **Data table / records list** | `data-table-system`, `responsive-table`, `bulk-actions`, `pagination`, `empty-states` | `inline-editing`, `context-menu`, `filter-chips`, `search-experience-system`, `text-truncation` |
| **Form (any)** | `form-field-states`, `form-validation-timing`, `microcopy`, `double-submit-guard` | `input-masking`, `otp-input`, `password-field-ux`, `date-pickers`, `range-sliders`, `focus-states` |
| **Long form (7+ fields) / onboarding** | `stepper-wizard`, `form-field-states`, `zeigarnik-effect`, `peak-end-rule` | `autosave-ux`, `microcopy` |
| **Sign-up / login** | `password-field-ux`, `form-validation-timing`, `microcopy`, `otp-input` | `focus-states`, `error-states` |
| **Checkout / payment** | `input-masking`, `double-submit-guard`, `behind-the-button`, `error-states`, `peak-end-rule` | `stepper-wizard`, `loading-states-system` |
| **Pricing section** | `von-restorff`, `decoy-effect`, `pricing-psychology`, `perfect-card` | `serial-position`, `microcopy` |
| **Landing page** | `landing-page-skeleton`, `de-ai-landing-hero`, `visual-hierarchy`, `perfect-card`, `reverse-engineered-linear` | `scroll-driven-animations`, `gradient-design`, `typography-system` |
| **Modal / dialog / drawer** | `modal-hierarchy`, `modal-backdrop`, `animation-timing`, `focus-states` | `destructive-actions`, `bottom-sheets` |
| **Destructive actions** | `destructive-actions`, `undo-ux`, `disabled-buttons` | `modal-hierarchy`, `toast-notifications` |
| **Navigation / app shell** | `navigation-patterns`, `tabs-system`, `focus-states` | `bottom-sheets`, `command-palette`, `scroll-restoration`, `resizable-panels` |
| **Search / filters** | `search-experience-system`, `filter-chips`, `empty-states` | `command-palette`, `loading-states-system`, `pagination` |
| **Notifications / feedback** | `notification-system`, `toast-notifications`, `notification-badge`, `undo-ux` | `optimistic-ui`, `error-states` |
| **Buttons & primary CTAs** | `perfect-button`, `button-feedback`, `disabled-buttons`, `behind-the-button` | `buy-button-css`, `hover-trap`, `double-submit-guard`, `fitts-law` |
| **File upload** | `file-upload-ux`, `error-states`, `loading-states-system` | `undo-ux`, `drag-and-drop-tips` |
| **Drag and drop / Kanban** | `drag-and-drop`, `drag-and-drop-tips`, `optimistic-ui` | `live-cursors`, `scroll-restoration` |
| **Chat / messaging** | `chat-ui-system`, `avatar-system`, `notification-badge`, `text-truncation` | `live-cursors`, `empty-states` |
| **Calendar / scheduling** | `calendar-week-view`, `date-pickers`, `drag-and-drop` | `empty-states`, `tooltip-design` |
| **Cards & content grids** | `perfect-card`, `card-hover-anatomy`, `card-spacing-fixes`, `border-radius-system` | `depth-layers`, `shadow-elevation`, `hover-trap`, `proximity-rule` |
| **Loading / waiting states** | `loading-states-system`, `skeleton-loading`, `perceived-performance`, `doherty-threshold` | `optimistic-ui`, `behind-the-button` |
| **Empty / error states** | `empty-states`, `error-states`, `app-guard` | `microcopy`, `undo-ux` |
| **Mobile screen** | `bottom-sheets`, `swipe-actions`, `hover-trap`, `pull-to-refresh`, `fitts-law` | `responsive-table`, `navigation-patterns` |
| **Dark mode / theming** | `dark-mode-surfaces`, `color-accessibility`, `depth-layers` | `design-tokens`, `gradient-design`, `glassmorphism` |
| **Typography & hierarchy** | `typography-system`, `visual-hierarchy`, `pop-out-effect`, `serial-position` | `golden-ratio`, `proximity-rule`, `whitespace-types`, `gestalt-laws` |
| **Design system tokens** | `design-tokens`, `design-system-build`, `atomic-design`, `border-radius-system`, `typography-system` | `design-system-kit`, `whitespace-types`, `color-harmony`, `icon-design-rules` |
| **Motion pass** | `animation-timing`, `easing-curves`, `card-hover-anatomy` | `scroll-driven-animations`, `button-feedback` |
| **Rating / reviews** | `star-rating`, `microcopy` | `empty-states` |
| **Tooltips & dropdowns** | `tooltip-design`, `context-menu`, `dropdown-design` | `z-index-mastery`, `focus-states`, `css-has-selector` |
| **Colour / palette choice** | `color-harmony`, `color-accessibility`, `gradient-design` | `rounded-shapes`, `radius-spectrum`, `optical-corrections` |
| **"This looks AI-made"** | `de-ai-landing-hero`, `de-ai-dashboard`, `reverse-engineered-linear`, `visual-hierarchy`, `perfect-card` | `typography-system`, `whitespace-types` |

---

## 112 Patterns Catalog Overview

The plugin contains 112 patterns cataloged in `data/catalog.json`:
- **Visual (38 patterns)**: `border-radius`, `charts-that-lie`, `color-accessibility`, `dark-mode-surfaces`, `depth-layers`, `gradient-design`, `optical-corrections`, `shadow-elevation`, `whitespace-types`, etc.
- **Interaction (30 patterns)**: `accordion-disclosure`, `behind-the-button`, `bottom-sheets`, `bulk-actions`, `context-menu`, `double-submit-guard`, `fitts-law`, `inline-editing`, `modal-hierarchy`, `otp-input`, `toggle-anatomy`, etc.
- **Forms (13 patterns)**: `autosave-ux`, `date-pickers`, `file-upload-ux`, `form-field-states`, `form-validation-timing`, `input-masking`, `password-field-ux`, `stepper-wizard`, etc.
- **Feedback (13 patterns)**: `doherty-threshold`, `error-states`, `loading-states-system`, `notification-system`, `optimistic-ui`, `skeleton-loading`, `toast-notifications`, `undo-ux`, etc.
- **Content (9 patterns)**: `empty-states`, `landing-page-skeleton`, `microcopy`, `serial-position`, `von-restorff`, `decoy-effect`, `pricing-psychology`, `zeigarnik-effect`, etc.
- **Navigation (5 patterns)**: `focus-states`, `navigation-patterns`, `pagination`, `tabs-system`, `command-palette`.
- **Motion (4 patterns)**: `animation-timing`, `card-hover-anatomy`, `easing-curves`, `scroll-driven-animations`.

---

## 15-Point AppGuard Production Checklist

Every production view must satisfy these 15 rules before shipping:

1. **Boot Guard**: Load `app-guard.js` first in `<head>`. Automatic reload on cached script failure.
2. **Error Screen**: Catch uncaught runtime errors and promise rejections with in-app recovery.
3. **Offline Banner**: Monitor network state and disable non-idempotent mutations when offline.
4. **State Completeness**: Provide explicit designs for loading, empty, partial, and error states.
5. **Submit Guard**: Guard form submissions against double-clicks with pending/done state feedback.
6. **Destructive Friction**: Isolate delete/cancel actions, use secondary styling, and offer undo toasts.
7. **Human Microcopy**: Describe errors and confirmations in user terms, never raw error messages.
8. **Concentric Radii**: Maintain geometric integrity: $R_{inner} = R_{outer} - Padding$.
9. **No Emoji Icons**: Use unified SVG icons with fixed viewBox (24x24 or 20x20). Never use emoji in UI controls.
10. **Calibrated Motion**: Keep entry transitions within 200–300ms ease-out; hover transitions within 150–200ms.
11. **WCAG AA Contrast**: Enforce 4.5:1 minimum contrast on all body text and 3:1 on large text.
12. **Touch Targets**: Minimum 44x44px bounding box for all tappable elements.
13. **Mobile 390px Check**: Ensure inputs are at least 16px to prevent iOS auto-zoom; zero horizontal scroll.
14. **Focus Rings**: Never remove outline without providing a 2px high-contrast offset focus ring.
15. **Doherty Threshold**: Return immediate visual feedback within 400ms for every interaction.

---

## Command Line Interface

Run commands directly via Python:

```bash
# Route a module to its optimal patterns
python3 scripts/ux_engine.py route "settings page"

# Inspect pattern details, do/don'ts, and implementation rules
python3 scripts/ux_engine.py pattern accordion-disclosure

# Search the 112 patterns catalog
python3 scripts/ux_engine.py search "table"

# Audit a file for UI/UX anti-patterns
python3 scripts/ux_engine.py audit src/components/Card.tsx

# Print 15-point checklist
python3 scripts/ux_engine.py checklist
```


---

## Universal Senior UI Polish Rules (Cross-Domain Standard)

These universal rules apply to any application across all domains (SaaS, Fintech, E-commerce, Healthcare, Developer Tools, Analytics, Consumer Web, and Mobile).

1. **Universal Dark Mode Badge & Select Pill Formula**:
   Never render solid white pills with light text in dark mode. Across all domains, status badges, filter chips, and dropdown select pills must follow a calibrated tint-and-border system:
   - **Neutral (Draft, Inactive, Default)**: 12-15% slate surface, 30% border, slate-300 text (`rgba(148, 163, 184, 0.15)`, border `rgba(148, 163, 184, 0.30)`, text `#CBD5E1`).
   - **Info (Active, Review, Processing)**: 12-15% blue surface, 30% border, blue-400 text (`rgba(59, 130, 246, 0.15)`, border `rgba(59, 130, 246, 0.30)`, text `#60A5FA`).
   - **Accent (Specialized, Premium, Beta)**: 12-15% purple surface, 30% border, purple-300 text (`rgba(168, 85, 247, 0.15)`, border `rgba(168, 85, 247, 0.30)`, text `#C084FC`).
   - **Warning (Pending, In Progress, Review)**: 12-15% amber surface, 30% border, amber-300 text (`rgba(245, 158, 11, 0.15)`, border `rgba(245, 158, 11, 0.30)`, text `#FBBF24`).
   - **Success (Completed, Live, Verified)**: 12-15% emerald surface, 30% border, emerald-400 text (`rgba(16, 185, 129, 0.15)`, border `rgba(16, 185, 129, 0.30)`, text `#34D399`).
   - **Danger (Failed, Blocked, Critical)**: 12-15% rose surface, 30% border, rose-400 text (`rgba(244, 63, 94, 0.15)`, border `rgba(244, 63, 94, 0.30)`, text `#FB7185`).

2. **Numeric Tabular Alignment**:
   In any table or list (financial balances, inventory counts, metric quotas, timestamps), right-align numeric columns and enforce `font-variant-numeric: tabular-nums` so decimal points and digit positions align for scanning.

3. **Chart-to-Legend Visual Parity**:
   Every entry in a chart legend must represent a visible mark on the canvas. Never include orphan metrics in a chart legend that do not have a corresponding visual series or axis.

4. **Interactive Affordance Distinction**:
   Filter chips, action triggers, and dropdown buttons must look clickable (distinct hover states, chevrons, cursor pointer), while static informational badges must have subdued non-interactive styling.

5. **Peer Metric Card Symmetry**:
   Peer tiles in a dashboard or overview grid must maintain visual balance. If one card features trend micro-charts or sparklines, all sibling cards must maintain equal graphic density.

6. **Bulk Action Surface**:
   Any table or grid that includes row-selection checkboxes must provide a dedicated bulk action bar (floating bar or header replacement) that activates upon selection.

7. **Accessible Identification**:
   User avatars, team badges, and status icons must always provide visible text labels, initials, or accessible tooltips rather than relying exclusively on bare images.
