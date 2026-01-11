filename = "popular-names.txt"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

lines.sort(key=lambda line: int(line.split("\t")[2]), reverse=True)

for line in lines:
    print(line, end="")

# UNIX command:
# sort -k 3 -r -n popular-names.txt
