import csv

input_file = "input.csv"
output_file = "output.csv"

with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile, delimiter=',', quotechar='"')
        writer = csv.writer(outfile, delimiter=';', quotechar='"')
        for row in reader:
            writer.writerow(row)

print(f"変換したファイルは {output_file} に保存されました。")
