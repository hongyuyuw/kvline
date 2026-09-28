# kvline

Parse lines of the form `key: value`. Comments start with `#`. This is not an `.env` parser: the separator is a colon.

```python
from kvline import parse_kv

parse_kv("name: Ada\n")
```

```bash
python -m unittest test_kvline.py
```

MIT
