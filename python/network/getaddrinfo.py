#!/usr/bin python
# getaddrinfo-list-broken.py

import sys,socket

# put the list of results inot the "result" variable.
result = socket.getaddrinfo(sys.argv[1], None, 0, socket.SOCK_STREAM)

counter = 0
for item in result:
    # print out the addr tuple for each item
    print("%-2d: %s" %(counter, item[4]))
    counter += 1
