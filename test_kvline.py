import unittest

from kvline import emit_kv, get_value, parse_kv


class KvlineTest(unittest.TestCase):
    def test_pairs(self) -> None:
        text = "# note\nname: Ada\n\ncity: North\n"
        self.assertEqual(parse_kv(text), {"name": "Ada", "city": "North"})
        self.assertEqual(parse_kv(emit_kv({"name": "Ada"})), {"name": "Ada"})
        parsed = parse_kv(text)
        self.assertEqual(get_value(parsed, "name"), "Ada")
        self.assertEqual(get_value(parsed, "missing", "no"), "no")
        with self.assertRaises(ValueError):
            parse_kv("nope\n")


if __name__ == "__main__":
    unittest.main()
