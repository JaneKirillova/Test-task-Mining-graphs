import os
import sys
from os import walk
from parser import get_file_methods


def get_all_files(files_directory):
    files = []
    for dirpath, dirnames, filenames in walk(files_directory):
        for filename in [f for f in filenames if f.endswith(".php")]:
            files.append(os.path.join(dirpath, filename))
    return files


def write_result_to_files(files_directory):
    files_list = get_all_files(files_directory)
    with open("result.txt", "w") as res_file:
        for file in files_list:
            try:
                methods = get_file_methods(file)
                if len(methods) > 0:
                    res_file.write(f'{file} methods:\n')
                    for method in methods:
                        res_file.write(str(method))
            # files in repositories can be incorrect
            # if it happens, we just skip the file
            except:
                continue


if __name__ == "__main__":
    if len(sys.argv) < 2:
        dataset = "dataset"
    else:
        dataset = sys.argv[1]
    write_result_to_files(dataset)
