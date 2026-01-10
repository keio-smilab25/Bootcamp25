file_name = "popular-names.txt"

count = 0
with open(file_name, 'r', encoding='utf-8') as f:
    for line in f:
        count += 1

print(count)