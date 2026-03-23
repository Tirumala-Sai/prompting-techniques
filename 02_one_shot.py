import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper import get_completion

prompt = """
Rewrite the sentence in a polite tone.

Example:
Input: Give me the report now
Output: Could you please share the report?

Now do the same:
Input: Send the details quickly
Output:
"""

response = get_completion(prompt)
print(response)