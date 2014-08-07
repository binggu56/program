#!/usr/bin/evn python

# Copyright 2009 James Crickmere <james.crickmere@googlemail.com>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0

try:
    import gtk
except ImportError:
    print "Please install the Python GTK libraries first."
    exit()

import sys, os
from distutils.core import setup

if len(sys.argv) == 2:
    if sys.argv[1] == 'uninstall':
        files_to_remove = ['/usr/local/bin/pyadis-config', 
            '/usr/local/bin/pyadis-deamon', 
            '/usr/local/lib/python2.6/dist-packages/lib_pyadis.py', 
            #'/usr/local/lib/python2.6/dist-packages/pYadis-0.1.egg-info',
            '/usr/local/lib/python2.6/dist-packages/lib_pyadis.pyc',
            #os.environ['HOME'] + '/.pyadis-config',
            #os.environ['HOME'] + '/.pyadis-index.sqlite3',
        ]
        for f in files_to_remove:
            os.remove(f)
        
        exit()


setup(
    name='pYadis',
    version='0.1r15',
    description='Automatic backup tool.',
    url='http://pyadis.googlecode.com/',
    author='James Crickmere',
    author_email='james.crickmere@googlemail.com',
    py_modules=['lib_pyadis', ],
    scripts=['pyadis-config', 'pyadis-deamon']
)

