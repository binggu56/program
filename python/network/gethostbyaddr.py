#!/usr/bin/env python
# Basic gethostbyaddr() example

import sys,socket
def getipaddrs(hostname):
    """Get a list of IP addresses from a given hostname."""
    result = socket.getaddrinfo(hostname,None,0,socket.SOCK_STREAM)
    return [x[4][0] for x in result]

def gethostname(ipaddr):
    """Get the hostname from a given IP address."""
    return socket.gethostbyaddr(ipaddr)[0]

try:
    hostname = gethostname(sys.argv[1]) 
    ipaddrs = getipaddrs(hostname)
except socket.herror as e:
    print("No host name available for %s; this may be normal." % sys.argv[1])
    sys.exit(0)
except socket.gaierror as e:
    print("Got hostname %s, but it could not be forward-resolved: %s" %(hostname,str(e)))
    sys.exit(1)

if not sys.argv[1] in ipaddrs:
    print("Got hostname %s, but on forward lookup," %hostname)
    print("original IP %s did not appear in IP address list." %sys.argv[1])
    sys.exit(1)

print("Validated hostname:",hostname)
