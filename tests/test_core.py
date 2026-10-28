import hashlib, unittest
from wildre.core import summarize_log, extract_iocs, sha256_text, draft_yara_rule

class CoreTests(unittest.TestCase):
    def test_summary(self):
        r = summarize_log("INFO started\nERROR failed\n\nwarning disk")
        self.assertEqual(r["total_lines"], 4); self.assertEqual(r["blank_lines"], 1)
        self.assertEqual(r["level_counts"]["error"], 1)
    def test_empty_summary(self):
        self.assertIsNone(summarize_log("")["first_timestamp_seen"])
    def test_iocs(self):
        r = extract_iocs("https://example.com/path 192.0.2.10 " + "a"*64)
        self.assertIn("https://example.com/path", r["urls"]); self.assertIn("192.0.2.10", r["ipv4"])
        self.assertIn("a"*64, r["hashes"]); self.assertIn("example.com", r["domains"])
    def test_ioc_dedup(self):
        self.assertEqual(extract_iocs("192.0.2.1 192.0.2.1")["ipv4"], ["192.0.2.1"])
    def test_hash(self):
        self.assertEqual(sha256_text("abc")["hex"], hashlib.sha256(b"abc").hexdigest())
    def test_yara(self):
        r = draft_yara_rule(['abc"def', "abc", "abc"], "demo-rule")
        self.assertIn("rule demo_rule", r); self.assertIn(r'abc\"def', r); self.assertIn("any of them", r)
    def test_yara_single(self):
        self.assertIn("condition:\n        $s1", draft_yara_rule(["marker"], "1demo"))
    def test_yara_limits(self):
        with self.assertRaises(ValueError): draft_yara_rule(["", " "])
        with self.assertRaises(ValueError): draft_yara_rule([f"x{i}" for i in range(51)])
        with self.assertRaises(ValueError): draft_yara_rule(["x"*501])

if __name__ == "__main__": unittest.main()
