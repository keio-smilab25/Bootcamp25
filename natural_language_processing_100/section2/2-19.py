import collections

filename = "popular-names.txt"

with open(filename, "r", encoding="utf-8-sig") as f:
    names = [line.split("\t")[0] for line in f]

counter = collections.Counter(names)

for name, count in counter.most_common():
    print(f"{count} {name}")

# UNIX command:
# cut -f 1 popular-names.txt | sort | uniq -c | sort -n -r
