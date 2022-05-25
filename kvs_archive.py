#!/usr/bin/env python

import os
import glob
import argparse

from utils import read_bytes


def main():
    parser = argparse.ArgumentParser(description="AOT2 .ktsl2stbin files archiving tool.")
    parser.add_argument("folder", help="folder with .kvs files")
    args = parser.parse_args()
    k_folder = args.folder

    files = glob.glob(k_folder + "/*.[kK][vV][sS]")
    file_bytes = get_bytes_from_files(files)

    out_file_name = os.path.join(k_folder, "mod.ktsl2stbin")
    write_file(out_file_name, file_bytes)


def get_bytes_from_files(files):
    return map(lambda file: b"".join(read_bytes(file)), files)


def write_file(name, file_bytes):
    print("Writing file " + name)
    # First 96 bytes (0x60)
    # This probably only works with AOT2 because the header might be different in each game
    header = b"KTSR\x02\x94\xdd\xfc\x01\x00\x00\x016\x0e\xf4\x05\x00\x00\x00\x00\x00\x00\x00\x00\x10\xf7\x05&\x10\xf7\x05&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\xd4\xf4\x15 \xe9\x88\x00\xca\xab\xa8\xa9 \x00\x00\x00\xf7\xe8\x88\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

    new_file_stream = open(name, "wb")
    new_file_stream.write(header + b"".join(file_bytes))
    new_file_stream.close()


main()
