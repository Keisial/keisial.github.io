#! /usr/bin/env python
# 
# $Id$
#

from distutils.core import setup

from DNS import __version__

setup(
        #-- Package description
        name = 'pydns',
        license = 'Python license',
        version = __version__,
        description = 'Python DNS library',
        long_description = """Python DNS library:
""",
        author = '', 
        author_email = 'pydns-developer@lists.sourceforge.net',
        url = 'http://pydns.sourceforge.net/',
        packages = ['DNS'],
)

#
# $Log$
# Revision 1.1  2001/08/09 13:42:38  anthonybaxter
# initial setup.py. That was easy. :)
#
#
