"""
steps

1. search & locates modules src file
2. execute
3. object for the imported module
"""
from glob import glob
from psmakearchive import make_archive, make_tarball

file_list = glob('*.py')
make_archive('source.zip', *file_list)  # content of the list as arguments
make_tarball('source.tar', *file_list)
