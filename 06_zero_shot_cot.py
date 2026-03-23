import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper import get_completion

prompt = """
A person buys 2 items at ₹150 each.

Find total cost and remaining money if he pays ₹500.

Let's think step by step.
"""

response = get_completion(prompt)
print(response)