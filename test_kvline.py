import unittest

from kvline import parse_kv


class KvlineTest(unittest.TestCase):
    def test_pairs(self) -> None:
        text = "# note\nname: Ada\n\ncity: Orlando\n"
        self.assertEqual(parse_kv(text), {"name": "Ada", "city": "Orlando"})
        with self.assertRaises(ValueError):
            parse_kv("nope\n")


if __name__ == "__main__":
    unittest.main()
