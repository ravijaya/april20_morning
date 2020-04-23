from os import getcwd, listdir, getpid


print('current process : ', getpid())
print()
print(getcwd())
print()

def ls(path='.'):
    for item in listdir(path):
        print(item)


ls()