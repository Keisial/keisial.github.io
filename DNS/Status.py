"""
 $Id$

 This file is part of the pydns project.
 Homepage: http://pydns.sourceforge.net

 This code is covered by the standard Python License.

 Status values in message header
"""

NOERROR       = 0
FORMERR       = 1
SERVFAIL      = 2
NXDOMAIN      = 3
NOTIMP        = 4
REFUSED       = 5

# Construct reverse mapping dictionary

_names = dir()
statusmap = {}
for _name in _names:
	if _name[0] != '_': statusmap[eval(_name)] = _name

def statusstr(status):
	if statusmap.has_key(status): return statusmap[status]
	else: return `status`

#
# $Log$
# Revision 1.3  2001/08/09 09:08:55  anthonybaxter
# added identifying header to top of each file
#
# Revision 1.2  2001/07/19 06:57:07  anthony
# cvs keywords added
#
#
