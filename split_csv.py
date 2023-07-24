♯ 巨大なCSVを分割するコードのサンプル
# pandasを使わないパターン
import csv

def write_chunk(file_name, headers, rows):
    with open(file_name, 'w', newline='') as out_file:
        csv_writer = csv.writer(out_file)
        csv_writer.writerow(headers)
        for row in rows:
            csv_writer.writerow(row)

def split_csv(input_file_name, lines_per_file=10000):
    with open(input_file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)
        file_no = 0
        rows = []
        for row in csv_reader:
            if len(rows) == lines_per_file:
                write_chunk(f'chunked_{input_file_name}_{file_no}.csv', headers, rows)
                file_no += 1
                rows = []
            rows.append(row)
        if rows:
            write_chunk(f'chunked_{input_file_name}_{file_no}.csv', headers, rows)

# pandasを使うパターン
import pandas as pd

def split_csv(file_name, chunk_size=10000):
    chunk_no = 1
    for chunk in pd.read_csv(file_name, chunksize=chunk_size):
        new_file_name = f"chunked_{file_name}_{chunk_no}.csv"
        chunk.to_csv(new_file_name, index=False)
        chunk_no += 1
