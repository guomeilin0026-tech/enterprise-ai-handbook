import math
import re
from collections import Counter

TOKEN_PATTERN = re.compile(r"[\u4e00-\u9fff]|[a-zA-Z0-9_]+")


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_PATTERN.findall(text)]


def vectorize(text: str) -> dict[str, float]:
    counts = Counter(tokenize(text))
    length = math.sqrt(sum(value * value for value in counts.values())) or 1.0
    return {key: value / length for key, value in counts.items()}


def cosine_similarity(left: dict[str, float], right: dict[str, float]) -> float:
    return sum(left[key] * right[key] for key in set(left) & set(right))

