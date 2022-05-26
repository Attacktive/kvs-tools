#!/usr/bin/env python

import os
import glob
import argparse

from utils import read_bytes


def main():
    k_folder, files = initialize()

    file_bytes = map(lambda file: b"".join(read_bytes(file)), files)

    out_file_name = os.path.join(k_folder, "mod.ktsl2stbin")
    write_to_file(out_file_name, file_bytes)


def initialize():
    parser = argparse.ArgumentParser(description="AOT2 .ktsl2stbin files archiving tool.")
    parser.add_argument("folder", help="folder with .kvs files")
    args = parser.parse_args()
    k_folder = args.folder
    files = glob.glob(k_folder + "/*.[kK][vV][sS]")

    return k_folder, files


def write_to_file(file_name, file_bytes):
    print("Writing file " + file_name)
    # First 96 bytes (0x60)
    # This probably only works with AOT2 because the header might be different in each game
    header = b"KTSR\x02\x94\xdd\xfc\x01\x00\x00\x01\x36\x0e\xf4\x05\x00\x00\x00\x00\x00\x00\x00\x00\x10\xf7\x05\x26\x10\xf7\x05\x26\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\xd4\xf4\x15\x20\xe9\x88\x00\xca\xab\xa8\xa9\x20\x00\x00\x00\xf7\xe8\x88\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

    new_file_stream = open(file_name, "wb")
    new_file_stream.write(header + b"".join(file_bytes))
    new_file_stream.close()


if __name__ == "__main__":
    main()
