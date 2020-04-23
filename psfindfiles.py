from os import walk
from os.path import join


def find_files(top, search_pattern):
    for dirpath, dirnames, filenames in walk(top):
        for filename in filenames:
            if filename.endswith(search_pattern):
                print(join(dirpath, filename))


find_files('/home/ravijaya', '.pdf')
print()
find_files('/home/ravijaya', '.txt')