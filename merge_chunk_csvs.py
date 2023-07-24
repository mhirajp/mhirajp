# CSV Bをすべてメモリに読み込むパターン

import csv
import os

def create_id_mapping_from_B(chunk_files_B):
    mapping = {}
    for file in chunk_files_B:
        with open(file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            header_B = next(reader)
            for row in reader:
                mapping[row[0]] = row[1:]  # assuming ID is the first column
    return header_B, mapping

def merge_chunks_A_with_B(chunk_files_A, chunk_files_B, output_dir):
    header_B, mapping_B = create_id_mapping_from_B(chunk_files_B)

    for file_A in chunk_files_A:
        with open(file_A, 'r') as csv_file_A:
            reader_A = csv.reader(csv_file_A)
            header_A = next(reader_A)

            output_file = os.path.join(output_dir, os.path.basename(file_A))
            with open(output_file, 'w', newline='') as csv_file_output:
                writer = csv.writer(csv_file_output)
                writer.writerow(header_A + header_B[1:])  # merge headers without repeating ID

                for row_A in reader_A:
                    row_B = mapping_B.get(row_A[0], [None] * (len(header_B) - 1))  # get corresponding row from B using ID
                    writer.writerow(row_A + row_B)


# CSV Bをメモリに読み込まないパターン
import csv
import os

def find_matching_row_in_B(id_A, chunk_files_B):
    for file_B in chunk_files_B:
        with open(file_B, 'r') as csv_file_B:
            reader_B = csv.reader(csv_file_B)
            next(reader_B)  # skip header
            for row_B in reader_B:
                if row_B[0] == id_A:
                    return row_B[1:]
    return None  # not found

def merge_chunks_A_with_B(chunk_files_A, chunk_files_B, output_dir):
    for file_A in chunk_files_A:
        with open(file_A, 'r') as csv_file_A:
            reader_A = csv.reader(csv_file_A)
            header_A = next(reader_A)

            output_file = os.path.join(output_dir, os.path.basename(file_A))
            with open(output_file, 'w', newline='') as csv_file_output:
                writer = csv.writer(csv_file_output)
                
                header_B = None
                for file_B in chunk_files_B:
                    with open(file_B, 'r') as csv_file_B:
                        reader_B = csv.reader(csv_file_B)
                        header_B = next(reader_B)
                    break
                
                writer.writerow(header_A + header_B[1:])  # merge headers without repeating ID

                for row_A in reader_A:
                    row_B = find_matching_row_in_B(row_A[0], chunk_files_B)
                    if row_B is not None:
                        writer.writerow(row_A + row_B)
