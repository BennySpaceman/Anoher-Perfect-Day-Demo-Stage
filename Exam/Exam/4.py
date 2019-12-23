import json
from collections import Counter

with open('file.json') as f:
    data = json.load(f)

final = Counter()

for d in data:
    final.update(d)

final = dict(final)
max_key_len = len(max(final))

for i in final:
    print(f"{i}:{' ' * (max_key_len - len(i))} {'*' * (final[i] // 10)}")
