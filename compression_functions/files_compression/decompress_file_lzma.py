import lzma

def decompress_file_lzma(input_file, output_file):
    with lzma.open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            f_out.writelines(f_in)
