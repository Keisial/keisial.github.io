# $Id$
#
# This file is part of the pydns project.
# Homepage: http://pydns.sourceforge.net
#
# This code is covered by the standard Python License.
#

# __init__.py for DNS class.

__version__ = '0.0.1'

Error='DNS API error'
import Type,Opcode,Status,Class
from Base import *
from Lib import *
from lazy import *
Request = DnsRequest
Result = DnsResult

#
# $Log$
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
