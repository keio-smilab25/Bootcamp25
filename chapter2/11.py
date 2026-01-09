# 11.py
with open('popular-names.txt', 'r') as f:
    text = f.read()

# タブをスペースに置換
print(text.replace('\t', ' '), end='')