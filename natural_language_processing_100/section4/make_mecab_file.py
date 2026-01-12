import MeCab

input_file = "neko.txt"
output_file = "neko.txt.mecab"

tagger = MeCab.Tagger()

with (
    open(input_file, "r", encoding="utf-8") as f_in,
    open(output_file, "w", encoding="utf-8") as f_out,
):
    for line in f_in:
        if not line.strip():
            continue

        parsed = tagger.parse(line)
        f_out.write(parsed)

print("Done!")
