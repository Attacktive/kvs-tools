#!/usr/bin/env python

import os
import argparse

parser = argparse.ArgumentParser(description=".ktsl2stbin files extraction tool.")
parser.add_argument("file", help=".ktsl2stbin file")
args = parser.parse_args()
k_file = args.file


def read_bytes(file_name):
    print("Reading file: " + file_name)
    b_list = []

    file_stream = open(file_name, "rb")
    while True:
        piece = file_stream.read(1024)
        if not piece:
            break

        b_list.append(piece)
    file_stream.close()

    return b_list


def write_file(name, start, end):
    print("Writing file: " + name)
    new_file_stream = open(name, "wb")
    new_file_stream.write(byte_str[start:end])
    new_file_stream.close()


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return

        yield start
        start += len(sub)


byte_str = b"".join(read_bytes(k_file))

ext = ".kvs"
files_start = list(find_all(byte_str, b"KOVS"))

if not files_start:
    files_start = list(find_all(byte_str, b"KTSS"))
    ext = ".kns"

last_offset = os.path.getsize(k_file) - 1

out_directory_name = os.path.join(os.path.dirname(k_file), os.path.basename(k_file).split(".")[0])
os.makedirs(out_directory_name, exist_ok=True)

size = len(files_start)
number_of_digits = len(str(size - 1))
print(size, " files")

for i in range(size):
    file_index = str(i).rjust(number_of_digits, "0")
    out_file_name = os.path.join(out_directory_name, file_index + ext)

    if i == (size - 1):
        offset = last_offset
    else:
        offset = files_start[i + 1]

    write_file(out_file_name, files_start[i], offset)
