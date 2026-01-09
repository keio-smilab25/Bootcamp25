input_file = 'popular-names.txt'
col1_file = 'col1.txt'
col2_file = 'col2.txt'

with open(input_file, 'r', encoding='utf-8') as f_in, \
     open(col1_file, 'w', encoding='utf-8') as f_col1, \
     open(col2_file, 'w', encoding='utf-8') as f_col2:
    
    for line in f_in:
        cols = line.split('\t')

        f_col1.write(cols[0] + '\n')
        f_col2.write(cols[1] + '\n')

# UNIX command:
# cut -f 1 popular-names.txt > col1.txt
# cut -f 2 popular-names.txt > col2.txt