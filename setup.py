#! /usr/bin/env python
# 
# $Id$
#

import sys,os

sys.path.insert(0,os.getcwd())

from distutils.core import setup

import DNS

setup(
        #-- Package description
        name = 'pydns',
        license = 'Python license',
        version = DNS.__version__,
        description = 'Python DNS library',
        long_description = """Python DNS library:
""",
        author = 'Anthony Baxter and others', 
        author_email = 'pydns-developer@lists.sourceforge.net',
        url = 'http://pydns.sourceforge.net/',
        packages = ['DNS'],
)

#
# $Log$
# Revision 1.3  2001/11/23 19:43:57  stroeder
# Prepend current directory to sys.path to enable import of DNS.
#
# Revision 1.2  2001/11/23 19:36:35  stroeder
# Use DNS.__version__ as package version and corrected name
#
# Revision 1.1  2001/08/09 13:42:38  anthonybaxter
# initial setup.py. That was easy. :)
#
#
