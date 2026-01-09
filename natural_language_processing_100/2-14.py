import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])

filename = "popular-names.txt"

with open(filename, "r", encoding="utf-8") as f:
    for i in range(n):
        line = f.readline()
        if not line:
            break
        print(line, end="")


# UNIX command:
# head -n N popular-names.txt
