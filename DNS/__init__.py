# -*- encoding: utf-8 -*-
# $Id$
#
# This file is part of the pydns project.
# Homepage: http://pydns.sourceforge.net
#
# This code is covered by the standard Python License.
#

# __init__.py for DNS class.

__version__ = '2.3.1'

import Type,Opcode,Status,Class
from Base import DnsRequest, DNSError
from Lib import DnsResult
from Base import *
from Lib import *
Error=DNSError
from lazy import *
Request = DnsRequest
Result = DnsResult

#
# This random generator is used for transaction ids and port selection.  This
# is important to prevent spurious results from lost packets, and malicious
# cache poisoning.  This doesn't matter if you are behind a caching nameserver
# or your app is a primary DNS server only. To install your own generator,
# replace DNS.random.  SystemRandom uses /dev/urandom or similar source.  
#
try:
  from random import SystemRandom
  random = SystemRandom()
except:
  import random

#
# $Log$
# Revision 1.8.2.2  2007/05/22 21:06:52  customdesigned
# utf-8 in __init__.py
#
# Revision 1.8.2.1  2007/05/22 20:39:20  customdesigned
# Release 2.3.1
#
# Revision 1.8  2002/05/06 06:17:49  anthonybaxter
# found that the old README file called itself release 2.2. So make
# this one 2.3...
#
# Revision 1.7  2002/05/06 06:16:15  anthonybaxter
# make some sort of reasonable version string. releasewards ho!
#
# Revision 1.6  2002/03/19 13:05:02  anthonybaxter
# converted to class based exceptions (there goes the python1.4 compatibility :)
#
# removed a quite gross use of 'eval()'.
#
# Revision 1.5  2002/03/19 12:41:33  anthonybaxter
# tabnannied and reindented everything. 4 space indent, no tabs.
# yay.
#
# Revision 1.4  2001/11/26 17:57:51  stroeder
# Added __version__
#
# Revision 1.3  2001/08/09 09:08:55  anthonybaxter
# added identifying header to top of each file
#
# Revision 1.2  2001/07/19 06:57:07  anthony
# cvs keywords added
#
#
