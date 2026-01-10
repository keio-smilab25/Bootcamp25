file_name = "popular-names.txt"

with open(file_name, 'r', encoding='utf-8') as f:
    text = f.read().replace('\t', ' ')
    print(text)