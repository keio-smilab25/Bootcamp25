file1 = 'col1.txt'
file2 = 'col2.txt'
output_file = 'merge.txt'

with open(file1, 'r', encoding='utf-8') as f1, \
     open(file2, 'r', encoding='utf-8') as f2, \
     open(output_file, 'w', encoding='utf-8') as f_out:
    
    for line1, line2 in zip(f1, f2):
        new_line = line1.strip() + '\t' + line2.strip() + '\n'
        f_out.write(new_line)

# UNIX command:
# paste col1.txt col2.txt > merge.txt