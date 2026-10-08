import unittest
import os
import json
import subprocess
import sys

PLUGIN_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_PATH = os.path.join(PLUGIN_ROOT, 'data', 'catalog.json')
ROUTING_PATH = os.path.join(PLUGIN_ROOT, 'data', 'routing.json')
TOKENS_PATH = os.path.join(PLUGIN_ROOT, 'data', 'tokens.css')
GUARD_PATH = os.path.join(PLUGIN_ROOT, 'data', 'app-guard.js')
CLI_PATH = os.path.join(PLUGIN_ROOT, 'scripts', 'ux_engine.py')

class TestUXEngine(unittest.TestCase):

    def test_catalog_integrity(self):
        self.assertTrue(os.path.exists(CATALOG_PATH), "catalog.json must exist")
        with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
            catalog = json.load(f)
        self.assertEqual(len(catalog), 112, "Catalog must contain exactly 112 patterns")
        
        categories = set()
        for p in catalog:
            self.assertIn('slug', p)
            self.assertIn('title', p)
            self.assertIn('category', p)
            self.assertIn('hook', p)
            categories.add(p['category'])
            
        expected_categories = {'visual', 'interaction', 'forms', 'feedback', 'content', 'navigation', 'motion'}
        self.assertTrue(expected_categories.issubset(categories), "All 7 expected categories must be represented")

    def test_routing_table(self):
        self.assertTrue(os.path.exists(ROUTING_PATH), "routing.json must exist")
        with open(ROUTING_PATH, 'r', encoding='utf-8') as f:
            routing = json.load(f)
        self.assertGreaterEqual(len(routing), 31, "Routing table must contain at least 31 modules")

        with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
            catalog_slugs = {p['slug'] for p in json.load(f)}

        for key, mod in routing.items():
            self.assertIn('name', mod)
            self.assertIn('primary', mod)
            self.assertIn('secondary', mod)
            self.assertIn('anti_patterns', mod)
            self.assertIn('required_states', mod)
            
            # Verify primary slugs exist in catalog
            for s in mod['primary']:
                # either in catalog or app-guard
                self.assertTrue(s in catalog_slugs or s == 'app-guard', f"Slug {s} in module {key} must be valid")

    def test_tokens_file(self):
        self.assertTrue(os.path.exists(TOKENS_PATH), "tokens.css must exist")
        with open(TOKENS_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('--color-bg-base', content)
        self.assertIn('--radius-md', content)
        self.assertIn('--duration-fast', content)
        self.assertIn('prefers-color-scheme: dark', content)

    def test_app_guard(self):
        self.assertTrue(os.path.exists(GUARD_PATH), "app-guard.js must exist")
        with open(GUARD_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('window.AppGuard', content)
        self.assertIn('unhandledrejection', content)
        self.assertIn('data-guard-submitting', content)

    def test_cli_route(self):
        res = subprocess.run([sys.executable, CLI_PATH, 'route', 'settings'], capture_output=True, text=True)
        self.assertEqual(res.returncode, 0)
        self.assertIn('UX ENGINE ROUTING', res.stdout)
        self.assertIn('PRIMARY PATTERNS', res.stdout)

    def test_cli_search(self):
        res = subprocess.run([sys.executable, CLI_PATH, 'search', 'accordion'], capture_output=True, text=True)
        self.assertEqual(res.returncode, 0)
        self.assertIn('accordion-disclosure', res.stdout)

    def test_cli_pattern(self):
        res = subprocess.run([sys.executable, CLI_PATH, 'pattern', 'accordion-disclosure'], capture_output=True, text=True)
        self.assertEqual(res.returncode, 0)
        self.assertIn('ACCORDION DISCLOSURE', res.stdout)
        self.assertIn('DEEP SENIOR INSIGHTS', res.stdout)

    def test_cli_checklist(self):
        res = subprocess.run([sys.executable, CLI_PATH, 'checklist'], capture_output=True, text=True)
        self.assertEqual(res.returncode, 0)
        self.assertIn('15-POINT PRE-DELIVERY SENIOR CHECKLIST', res.stdout)

    def test_cli_audit(self):
        # Create temporary file with known anti-patterns
        test_file = '/tmp/test_anti_patterns.html'
        with open(test_file, 'w') as f:
            f.write("""
            <div style="background: #000000;">
              <button style="outline: none;">Submit 🚀</button>
            </div>
            """)
        try:
            res = subprocess.run([sys.executable, CLI_PATH, 'audit', test_file], capture_output=True, text=True)
            self.assertEqual(res.returncode, 0)
            self.assertIn('Accessibility', res.stdout)
            self.assertIn('Dark Mode', res.stdout)
            self.assertIn('Visual Polish', res.stdout)
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)

if __name__ == '__main__':
    unittest.main()
