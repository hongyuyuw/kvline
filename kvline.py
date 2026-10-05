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


def get_value(data: dict[str, str], key: str, default: str = "") -> str:
    return data.get(key, default)


def key_names(text: str) -> list[str]:
    return list(parse_kv(text))


def emit_kv(data: dict[str, str]) -> str:
    lines = []
    for key, value in data.items():
        if not str(key).strip() or ":" in str(key):
            raise ValueError(f"键不合法: {key}")
        lines.append(f"{key}: {value}")
    return "\n".join(lines) + ("\n" if lines else "")
