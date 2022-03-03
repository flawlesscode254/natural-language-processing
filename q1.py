import re
from nltk.util import ngrams
import nltk
nltk.download("brown")
from nltk.corpus import brown
s = brown.words()
s = " ".join(s).lower()
s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
tokens = [token for token in s.split(" ") if token != ""]
output = list(ngrams(tokens, 10))
print(output)
