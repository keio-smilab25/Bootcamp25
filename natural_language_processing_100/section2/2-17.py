filename = "popular-names.txt"

with open(filename, "r", encoding="utf-8-sig") as f:
    names = set(line.split("\t")[0] for line in f)

for name in sorted(names):
    print(name)

# UNIX command:
# cut -f 1 popular-names.txt | sort | uniq
