"""
 $Id$

 This file is part of the pydns project.
 Homepage: http://pydns.sourceforge.net

 This code is covered by the standard Python License.

 Opcode values in message header (section 4.1.1)
"""



QUERY = 0
IQUERY = 1
STATUS = 2

# Construct reverse mapping dictionary

_names = dir()
opcodemap = {}
for _name in _names:
	if _name[0] != '_': opcodemap[eval(_name)] = _name

def opcodestr(opcode):
	if opcodemap.has_key(opcode): return opcodemap[opcode]
	else: return `opcode`

#
# $Log$
# Revision 1.3  2001/08/09 09:08:55  anthonybaxter
# added identifying header to top of each file
#
# Revision 1.2  2001/07/19 06:57:07  anthony
# cvs keywords added
#
#
