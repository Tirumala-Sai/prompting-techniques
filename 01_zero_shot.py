import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper import get_completion

prompt = """
Translate the following sentence into Telugu:

"Artificial Intelligence is changing the world."
"""

response = get_completion(prompt)
print(response)