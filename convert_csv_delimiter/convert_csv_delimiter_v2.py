import csv

# 入力ファイルと出力ファイルの名前を指定
input_file = 'input.csv'
output_file = 'output.csv'

# ファイルを開いて変換
with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    # カンマ区切りのCSVリーダーを作成
    csv_reader = csv.reader(infile)
    
    # セミコロン区切りのCSVライターを作成
    csv_writer = csv.writer(outfile, delimiter=';')
    
    # 各行を読み込んで書き込む
    for row in csv_reader:
        csv_writer.writerow(row)

print("変換が完了しました。")