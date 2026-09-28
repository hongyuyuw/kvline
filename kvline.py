"""Parse `key: value` lines. Blank lines and # comments are skipped."""
from __future__ import annotations


def parse_kv(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"缺少冒号: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        if not key:
            raise ValueError("键为空")
        out[key] = value.strip()
    return out
