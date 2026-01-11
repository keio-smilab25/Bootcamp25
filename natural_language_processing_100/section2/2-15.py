import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 0

filename = "popular-names.txt"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines[-n:]:
        print(line, end="")

# UNIX command:
# tail -n N popular-names.txt
