#!/usr/bin/env python3
"""
UX Engine CLI: Senior UI/UX Intelligence by DesignMotionHQ
Routes modules to curated patterns, audits UI code for anti-patterns,
retrieves tactical patterns, and enforces the 15-point AppGuard checklist.
"""

import sys
import os
import json
import argparse
import re

PLUGIN_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_PATH = os.path.join(PLUGIN_ROOT, 'data', 'catalog.json')
ROUTING_PATH = os.path.join(PLUGIN_ROOT, 'data', 'routing.json')
TOKENS_PATH = os.path.join(PLUGIN_ROOT, 'data', 'tokens.css')
GUARD_PATH = os.path.join(PLUGIN_ROOT, 'data', 'app-guard.js')

def load_json(path):
    if not os.path.exists(path):
        return [] if 'catalog' in path else {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def cmd_route(args):
    routing = load_json(ROUTING_PATH)
    catalog = {p['slug']: p for p in load_json(CATALOG_PATH)}
    query = ' '.join(args.module).lower() if args.module else ''

    best_match = None
    best_score = 0

    for key, data in routing.items():
        score = 0
        if query in key.lower() or query in data['name'].lower():
            score += 10
        for kw in data.get('keywords', []):
            if kw.lower() in query or query in kw.lower():
                score += 5
        for word in query.split():
            if word in key.lower() or word in data['name'].lower():
                score += 3
        if score > best_score:
            best_score = score
            best_match = (key, data)

    if not best_match:
        print(f"No exact module match found for '{query}'. Available modules:")
        for key, data in sorted(routing.items()):
            print(f"  • {key}: {data['name']}")
        return

    key, data = best_match
    print("=" * 72)
    print(f"UX ENGINE ROUTING: {data['name'].upper()}")
    print("=" * 72)
    print("\n[!] CORE PHILOSOPHY:")
    print("  Pick the best few patterns, never all of them. Specificity first.")
    
    print("\n[+] PRIMARY PATTERNS (Mandatory Foundation):")
    for slug in data.get('primary', []):
        p = catalog.get(slug, {})
        title = p.get('title', slug)
        hook = p.get('hook', 'Core pattern requirement')
        print(f"  * {slug} ({title})")
        print(f"    Hook: \"{hook}\"")
        if p.get('insights'):
            print(f"    Key Rule: {p['insights'][0]}")

    print("\n[*] SECONDARY PATTERNS (Include ONLY if element exists on screen):")
    for slug in data.get('secondary', []):
        p = catalog.get(slug, {})
        title = p.get('title', slug)
        hook = p.get('hook', '')
        print(f"  - {slug} ({title}): {hook}")

    print("\n[-] ANTI-PATTERNS TO ELIMINATE:")
    for ap in data.get('anti_patterns', []):
        print(f"  x {ap}")

    print("\n[✓] MANDATORY STATE COMPLETENESS:")
    states = ", ".join(data.get('required_states', ['default', 'loading', 'error', 'empty']))
    print(f"  Every view must implement: [{states}]")
    print("=" * 72)

def cmd_search(args):
    catalog = load_json(CATALOG_PATH)
    query = ' '.join(args.query).lower()
    results = []

    for p in catalog:
        text = f"{p['slug']} {p.get('title', '')} {p.get('category', '')} {p.get('hook', '')} {' '.join(p.get('insights', []))} {' '.join(p.get('dodont', []))}".lower()
        if query in text:
            results.append(p)

    print(f"Found {len(results)} patterns matching '{query}':")
    for p in results[:args.limit]:
        print(f"\n• [{p.get('category', 'general').upper()}] {p['slug']} - {p.get('title', p['slug'])}")
        print(f"  Hook: {p.get('hook', '')}")
        if p.get('insights'):
            print(f"  Insight: {p['insights'][0]}")

def cmd_pattern(args):
    catalog = {p['slug']: p for p in load_json(CATALOG_PATH)}
    slug = args.slug.lower()

    if slug not in catalog:
        matches = [k for k in catalog.keys() if slug in k]
        if matches:
            print(f"Pattern '{slug}' not found. Did you mean:")
            for m in matches[:5]:
                print(f"  • {m}")
        else:
            print(f"Pattern '{slug}' not found in the 112 catalog.")
        return

    p = catalog[slug]
    print("=" * 72)
    print(f"PATTERN: {p.get('title', p['slug']).upper()} ({p.get('category', '').upper()})")
    print(f"Slug: {p['slug']}")
    print("=" * 72)
    print(f"\nHOOK:\n  \"{p.get('hook', '')}\"")

    if p.get('insights'):
        print("\nDEEP SENIOR INSIGHTS:")
        for ins in p['insights']:
            print(f"  • {ins}")

    if p.get('dodont'):
        print("\nDO / DON'T RULES:")
        for dd in p['dodont']:
            print(f"  {dd}")

    if p.get('related'):
        print(f"\nRELATED PATTERNS: {', '.join(p['related'])}")

    print(f"\nReference: {p.get('site', 'https://designmotionhq.com/patterns/' + slug)}")
    print("=" * 72)

def cmd_audit(args):
    target = args.path
    if not os.path.exists(target):
        print(f"Error: Target path '{target}' does not exist.")
        return

    if os.path.isdir(target):
        targets = []
        for root, dirs, files in os.walk(target):
            # Skip build artifacts and dependencies
            if any(part in root.split(os.sep) for part in ['.next', 'node_modules', '.git', 'dist', 'build']):
                continue
            for f in files:
                if f.endswith(('.tsx', '.ts', '.jsx', '.js', '.html', '.css', '.vue', '.svelte')):
                    targets.append(os.path.join(root, f))
        for t in sorted(targets):
            audit_single_file(t)
        return

    audit_single_file(target)

def audit_single_file(target):
    findings = []
    content = ""
    with open(target, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    lines = content.splitlines()

    # Rule 1: No outline removal without replacement
    for idx, line in enumerate(lines, 1):
        if re.search(r'outline\s*:\s*(none|0)', line) and not re.search(r'(focus-visible|ring|box-shadow)', line):
            findings.append((idx, 'Accessibility', 'Removing focus outline without custom ring breaks keyboard accessibility.'))

    # Rule 2: Layout shifting hover scales
    for idx, line in enumerate(lines, 1):
        if re.search(r':hover.*scale\(', line) or (':hover' in line and 'transform' in line and 'scale' in line):
            findings.append((idx, 'Interaction', 'Scale transforms on hover cause adjacent layout jitter. Prefer shadow elevation + color transitions.'))

    # Rule 3: Emoji icons used in UI
    emoji_pattern = re.compile(r'[\U0001F300-\U0001F64F\U0001F680-\U0001F6FF\U0001F900-\U0001F9FF]')
    for idx, line in enumerate(lines, 1):
        if emoji_pattern.search(line):
            findings.append((idx, 'Visual Polish', 'Emoji detected in UI markup. Use consistent SVG icons (Lucide, Heroicons) instead of emoji.'))

    # Rule 4: Plain button without type attribute or submit guard
    for idx, line in enumerate(lines, 1):
        if '<button' in line and 'type=' not in line:
            findings.append((idx, 'Form Safety', 'Button without explicit type attribute defaults to submit, causing unintended form reloads.'))

    # Rule 5: Pure black background (#000000)
    for idx, line in enumerate(lines, 1):
        if '#000000' in line or '#000;' in line:
            findings.append((idx, 'Dark Mode', 'Pure black #000000 flattens elevation. Use near-black base (#0B0F17 or #121212) so depth is perceptible.'))

    # Rule 6: Truncated chart baseline in SVG or canvas
    if 'chart' in content.lower():
        if 'zero' not in content.lower() and 'beginatzero' not in content.lower():
            findings.append((0, 'Data Integrity', 'Chart detected without explicit zero baseline. Verify y-axis does not truncate and mislead.'))

    # Rule 7: State completeness check
    states = ['loading', 'empty', 'error']
    missing_states = [s for s in states if s not in content.lower()]
    if missing_states:
        findings.append((0, 'State Completeness', f"Missing states in view logic: {', '.join(missing_states)}. Every interactive screen requires explicit states."))

    # Rule 8: Numeric tabular alignment check
    if 'deal value' in content.lower() or 'price' in content.lower() or 'amount' in content.lower():
        if 'text-right' not in content.lower() and 'text-align: right' not in content.lower():
            findings.append((0, 'Data Table', 'Numeric and currency columns should be right-aligned with tabular figures for vertical scanning.'))

    # Rule 9: Checkbox selection without bulk actions toolbar
    if 'type="checkbox"' in content or "type='checkbox'" in content:
        if 'bulk' not in content.lower() and 'selected' not in content.lower():
            findings.append((0, 'Interaction', 'Checkboxes detected without bulk action bar. Bulk selection requires an active action surface.'))

    # Rule 10: Solid white badge or select pills in dark mode
    if 'dark' in content.lower():
        if re.search(r'(badge|stage|select|pill)[^;}]*(bg-white|#ffffff|#fff|background:\s*white)', content.lower()):
            findings.append((0, 'Dark Mode', 'Solid white badge or dropdown pill detected in dark mode. Use 15% tinted surface with colored border.'))

    print("=" * 72)
    print(f"UX ENGINE AUDIT: {target}")
    print("=" * 72)
    if not findings:
        print("[✓] Clean pass! No blatant senior UI/UX anti-patterns detected.")
    else:
        print(f"Found {len(findings)} UI/UX violations or enhancement opportunities:\n")
        for line_num, cat, desc in findings:
            loc = f"Line {line_num}" if line_num > 0 else "Global"
            print(f"  [{cat}] ({loc}): {desc}")
    print("=" * 72)

def cmd_checklist(args):
    print("""
========================================================================
UX ENGINE: 15-POINT PRE-DELIVERY SENIOR CHECKLIST
========================================================================
[ ] 01. Boot Guard: AppGuard script loaded first; automatic reload on script failure.
[ ] 02. Error Screen: Full-page friendly recovery on uncaught errors with Reload/Home.
[ ] 03. Offline Banner: Realtime navigator.onLine listener holding mutation buttons.
[ ] 04. State Completeness: Explicit designs for loading, empty, error, and populated.
[ ] 05. Submit Guard: Double-click prevention with pending/done/error feedback.
[ ] 06. Destructive Friction: Danger actions named, separated from primary CTA, with undo.
[ ] 07. Feedback Microcopy: Honest error and success copy in user language, not tech codes.
[ ] 08. Concentric Radii: Inner radius = Outer radius - Padding (concentric curves).
[ ] 09. Icon Uniformity: 100% SVG icons with fixed viewBox (no emojis as UI controls).
[ ] 10. Motion Weight: Entrances 200-300ms ease-out; hover transitions 150-200ms.
[ ] 11. Contrast Ratio: WCAG AA verified (4.5:1 body copy, 3:1 large display text).
[ ] 12. Touch Targets: Minimum 44x44px clickable target bounding box.
[ ] 13. Mobile 390px Check: Input text >= 16px (no iOS zoom); zero horizontal scroll.
[ ] 14. Focus States: 2px offset contrast ring visible on keyboard Tab traversal.
[ ] 15. Doherty Threshold: Visual response under 400ms for every user interaction.
========================================================================
""")

def cmd_list(args):
    catalog = load_json(CATALOG_PATH)
    category = args.category.lower() if args.category else None

    grouped = {}
    for p in catalog:
        cat = p.get('category', 'other')
        grouped.setdefault(cat, []).append(p)

    for cat, items in sorted(grouped.items()):
        if category and cat != category:
            continue
        print(f"\n=== CATEGORY: {cat.upper()} ({len(items)} patterns) ===")
        for p in items:
            print(f"  • {p['slug']:<28} - {p.get('hook', '')[:70]}")

def cmd_tokens(args):
    if os.path.exists(TOKENS_PATH):
        with open(TOKENS_PATH, 'r', encoding='utf-8') as f:
            print(f.read())
    else:
        print("Tokens file not found.")

def main():
    parser = argparse.ArgumentParser(description="UX Engine by DesignMotionHQ CLI")
    subparsers = parser.add_subparsers(dest="command")

    # route
    p_route = subparsers.add_parser("route", help="Route module to primary/secondary patterns")
    p_route.add_argument("module", nargs="*", help="Module name (e.g., settings, table, checkout)")

    # search
    p_search = subparsers.add_parser("search", help="Search 112 patterns catalog")
    p_search.add_argument("query", nargs="+", help="Keywords to search")
    p_search.add_argument("-n", "--limit", type=int, default=10, help="Max results")

    # pattern
    p_pattern = subparsers.add_parser("pattern", help="Inspect a specific pattern")
    p_pattern.add_argument("slug", help="Pattern slug (e.g. accordion-disclosure)")

    # audit
    p_audit = subparsers.add_parser("audit", help="Audit code file for UI/UX anti-patterns")
    p_audit.add_argument("path", help="Path to file to audit")

    # checklist
    subparsers.add_parser("checklist", help="Print 15-point senior pre-delivery checklist")

    # list
    p_list = subparsers.add_parser("list", help="List patterns by category")
    p_list.add_argument("category", nargs="?", help="Optional category (content, feedback, forms, interaction, motion, navigation, visual)")

    # tokens
    subparsers.add_parser("tokens", help="Print semantic design tokens CSS")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    cmds = {
        'route': cmd_route,
        'search': cmd_search,
        'pattern': cmd_pattern,
        'audit': cmd_audit,
        'checklist': cmd_checklist,
        'list': cmd_list,
        'tokens': cmd_tokens
    }

    cmds[args.command](args)

if __name__ == '__main__':
    main()
