import re
from collections import Counter

def freq(filename, number):
  with open(filename) as file:
    text = file.read()
    text = re.split(r'[;,\s\n\n]+', text)
    text = Counter(text)
  
  return [x for x, c in sorted(text.items(), key=lambda i: i[1])[::-1] if c >= number]
