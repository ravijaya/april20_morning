import os  # haven't used it
from os.path import isfile, isdir, islink, getsize, getatime, getmtime, getctime, dirname, basename
from time import ctime

file_name = 'passwd.txt'
print(isfile(file_name))
print(isdir(file_name))
print()
print(getsize(file_name))
print()
print(getatime(file_name))
print(getmtime(file_name))
print(getctime(file_name))  # unix ts, epoch
print()
print(ctime(getatime(file_name)))
print(ctime(getmtime(file_name)))
print(ctime(getctime(file_name)))  # unix ts, epoch
print()

abs_path = '/home/ravijaya/Downloads/invoice308.pdf'
print(basename(abs_path))
print(dirname(abs_path))