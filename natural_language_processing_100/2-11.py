filename = 'popular-names.txt'

with open(filename, 'r') as f:
    text = f.read()

text_replaced = text.replace('\t', ' ')

print(text_replaced)

# UNIX command:
# tr '\t' ' ' < popular-names.txt