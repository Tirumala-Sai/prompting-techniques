import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper import get_completion

prompt = """
A person buys 3 items at ₹100 each.

Explain step by step:
1. Total cost
2. If he pays ₹500, remaining balance
"""

response = get_completion(prompt)
print(response)