import socket
import libssh2
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('arg.chem.sc.edu', 22))
session = libssh2.Session()
session.startup(sock)
session.userauth_password("bing", "gb900603")
channel = session.channel()
channel.execute('ls -l')

stdout = []
stderr = []
while not channel.eof:
    data = channel.read(1024)
    if data:
        stdout.append(data)

    data = channel.read(1024, libssh2.STDERR)
    if data:
        stderr.append(data)


print(b"".join(stdout).decode('utf-8'))
print(b"".join(stderr).decode('utf-8'))

