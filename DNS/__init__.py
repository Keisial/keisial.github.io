# $Id$
#
# This file is part of the pydns project.
# Homepage: http://pydns.sourceforge.net
#
# This code is covered by the standard Python License.
#

# __init__.py for DNS class.

Error='DNS API error'
import Type,Opcode,Status,Class
from Base import *
from Lib import *
from lazy import *
Request = DnsRequest
Result = DnsResult

# 
# $Log$
# Revision 1.2  2001/07/19 06:57:07  anthony
# cvs keywords added
#
#
