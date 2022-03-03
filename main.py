import re
from nltk.util import ngrams
import nltk
nltk.download("brown")
from nltk.corpus import brown
import pytrec_eval
import json

# With the brown corpus
s = brown.words()
s = " ".join(s).lower()
s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
tokens = [token for token in s.split(" ") if token != ""]
output = list(ngrams(tokens, 10))
print(output)

# With Birbeck corpus

f = open("APPLING1DAT.643","r")
s = f.readlines()

s = " ".join(s).lower()
s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
tokens = [token for token in s.split(" ") if token != ""]
output = list(ngrams(tokens, 1))
print(output)


# Evaluation with pytrec_eval

qrel = {
    'q1': {
        'd1': 1,
        'd2': 5,
        'd3': 10,
    },
    'q2': {
        'd2': 1,
        'd3': 1,
    },
}

run = {
    'q1': {
        'd1': 1.0,
        'd2': 0.0,
        'd3': 1.5,
    },
    'q2': {
        'd1': 1.5,
        'd2': 0.2,
        'd3': 0.5,
    }
}

evaluator = pytrec_eval.RelevanceEvaluator(
    qrel, {'map', 'ndcg'})

print(json.dumps(evaluator.evaluate(run), indent=1))