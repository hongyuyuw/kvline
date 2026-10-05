# kvline

Parse lines of the form `key: value`. Comments start with `#`. This is not an `.env` parser: the separator is a colon.

```python
from kvline import parse_kv, emit_kv, get_value, key_names

parse_kv("name: Ada\n")
emit_kv({"name": "Ada"})
get_value({"name": "Ada"}, "name")  # "Ada"
```

```bash
python -m unittest test_kvline.py
```

MIT
