import tarfile

def decompress_file_tar(input_tar, output_dir):
    with tarfile.open(input_tar, 'r:gz') as tar:
        tar.extractall(path=output_dir)
