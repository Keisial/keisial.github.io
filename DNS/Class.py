"""
$Id$

 This file is part of the pydns project.
 Homepage: http://pydns.sourceforge.net

 This code is covered by the standard Python License.

 CLASS values (section 3.2.4)
"""


IN = 1		# the Internet
CS = 2		# the CSNET class (Obsolete - used only for examples in
                # some obsolete RFCs)
CH = 3		# the CHAOS class
HS = 4		# Hesiod [Dyer 87]

# QCLASS values (section 3.2.5)

ANY = 255	# any class


# Construct reverse mapping dictionary

_names = dir()
classmap = {}
for _name in _names:
        if _name[0] != '_': classmap[eval(_name)] = _name

def classstr(klass):
        if classmap.has_key(klass): return classmap[klass]
        else: return `klass`

# 
# $Log$
# Revision 1.3  2001/08/09 09:08:55  anthonybaxter
# added identifying header to top of each file
#
# Revision 1.2  2001/07/19 06:57:07  anthony
# cvs keywords added
#
#
