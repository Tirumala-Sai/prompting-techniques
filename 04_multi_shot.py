import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper import get_completion

prompt = """
Convert numbers into words.

1 → One
2 → Two
3 → Three
4 → Four
5 → Five
6 → Six
7 → Seven
8 → Eight

9 →
"""

response = get_completion(prompt)
print(response)