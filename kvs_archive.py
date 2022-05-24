#!/usr/bin/env python

import glob
import argparse

from utils import read_bytes

parser = argparse.ArgumentParser(description="AOT2 .ktsl2stbin files archiving tool.")
parser.add_argument("folder", help="folder with .kvs files")
args = parser.parse_args()
k_folder = args.folder


def write_file(name):
    print("Writing file " + name)
    # First 96 bytes (0x60)
    # This probably only works with AOT2 because the header might be different in each game
    header = b"KTSR\x02\x94\xdd\xfc\x01\x00\x00\x016\x0e\xf4\x05\x00\x00\x00\x00\x00\x00\x00\x00\x10\xf7\x05&\x10\xf7\x05&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\xd4\xf4\x15 \xe9\x88\x00\xca\xab\xa8\xa9 \x00\x00\x00\xf7\xe8\x88\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

    new_file_stream = open(name, "wb")
    new_file_stream.write(header + b"".join(file_bytes))
    new_file_stream.close()


files = glob.glob(k_folder + "/*.[kK][vV][sS]")
file_bytes = []

for file in files:
    file_bytes.append(b"".join(read_bytes(file)))

write_file("mod.ktsl2stbin")
