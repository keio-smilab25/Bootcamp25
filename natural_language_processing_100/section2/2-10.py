filename = 'popular-names.txt'

with open(filename, 'r') as f:
    lines = f.readlines()
    count = len(lines)

print(count)

# UNIX command:
# wc -l popular-names.txt