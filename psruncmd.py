"""how to run command (cli)/ demo for the bytes """


from sys import platform  # cherry picking
from subprocess import check_output

if platform == 'linux':
    cmd = ['ls', '-l', '/etc/passwd']
elif platform == 'win32':
    cmd = ['ipconfig']  # list

op = check_output(cmd)
print(op)
print()
print(op.decode())  # convert bytes into str
