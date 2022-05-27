def read_bytes(file_name):
    print("Reading file: " + file_name)
    byte_list = []

    file_stream = open(file_name, "rb")
    while True:
        piece = file_stream.read(1024)
        if not piece:
            break

        byte_list.append(piece)
    file_stream.close()

    return byte_list
