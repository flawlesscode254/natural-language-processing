import re
from nltk.util import ngrams

f = open("APPLING1DAT.643","r")
s = f.readlines()

s = " ".join(s).lower()
s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
tokens = [token for token in s.split(" ") if token != ""]
output = list(ngrams(tokens, 1))
print(output)