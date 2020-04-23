"""variable len arg's, archive"""

"""reuse python script as module, library, custom or user defined python module"""

from zipfile import ZipFile
from tarfile import TarFile

# print('custom modules')


def make_archive(archive_name, *args):
    zf = ZipFile(archive_name, mode='w')

    for filename in args:
        zf.write(filename)
        print(f'{filename} : added')

    zf.close()


def make_tarball(archive_name, *args):
    tf = TarFile(archive_name, mode='w')

    for filename in args:
        tf.add(filename)
        print(f'{filename} : added')

    tf.close()


# extract from the archive