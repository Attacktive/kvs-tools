#!/usr/bin/env python

import os
import argparse

from utils import read_bytes
from archive_type import ArchiveType


def main():
    k_file, last_offset, out_directory_name = initialize()

    byte_concatenation = b"".join(read_bytes(k_file))
    archive_type, files_start = get_archive_type_and_files_start(byte_concatenation)

    os.makedirs(out_directory_name, exist_ok=True)

    size = len(files_start)
    number_of_digits = len(str(size - 1))
    print(size, " files")

    for i in range(size):
        file_index = str(i).rjust(number_of_digits, "0")
        out_file_name = os.path.join(out_directory_name, file_index + archive_type.extension)

        if i == (size - 1):
            offset = last_offset
        else:
            offset = files_start[i + 1]

        write_to_file(out_file_name, byte_concatenation, files_start[i], offset)


def initialize():
    parser = argparse.ArgumentParser(description=".ktsl2stbin files extraction tool.")
    parser.add_argument("file", help=".ktsl2stbin file")
    args = parser.parse_args()

    k_file = args.file

    last_offset = os.path.getsize(k_file) - 1

    out_subdirectory_name = os.path.basename(k_file).split(".")[0]
    out_directory_name = os.path.join(os.path.dirname(k_file), out_subdirectory_name)

    return k_file, last_offset, out_directory_name


def get_archive_type_and_files_start(byte_concatenation):
    files_start = list(find_all(byte_concatenation, ArchiveType.KOVS.signature))
    if files_start:
        archive_type = ArchiveType.KOVS
    else:
        files_start = list(find_all(byte_concatenation, ArchiveType.KTSS.signature))
        archive_type = ArchiveType.KTSS

    if not files_start:
        raise "The input file is not recognized!"

    return archive_type, files_start


def write_to_file(file_name, byte_str, start, end):
    print("Writing file: " + file_name)
    new_file_stream = open(file_name, "wb")
    new_file_stream.write(byte_str[start:end])
    new_file_stream.close()


def find_all(byte_concatenation, sub):
    start = 0
    while True:
        start = byte_concatenation.find(sub, start)
        if start == -1:
            return

        yield start
        start += len(sub)


if __name__ == "__main__":
    main()
