import csv
import chardet

input_file = "input.csv"
output_file = "output.csv"

# ファイルのエンコーディングを自動検出
with open(input_file, 'rb') as rawfile:
    raw_data = rawfile.read()
    detected = chardet.detect(raw_data)
    encoding = detected['encoding']

print(f"検出されたエンコーディング: {encoding}")

# 検出されたエンコーディングを使用してファイルを開く
with open(input_file, mode='r', newline='', encoding=encoding) as infile:
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile, delimiter=',', quotechar='"')
        writer = csv.writer(outfile, delimiter=';', quotechar='"')
        for row in reader:
            writer.writerow(row)

print(f"変換したファイルは {output_file} に保存されました。")