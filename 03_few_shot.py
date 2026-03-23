import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper import get_completion

prompt = """
Classify the category: Sports, Technology, or Health

Text: Football match was exciting
Category: Sports

Text: New AI model released
Category: Technology

Text: Tips for healthy eating
Category: Health

Text: Laptop performance is improving
Category:
"""

response = get_completion(prompt)
print(response)