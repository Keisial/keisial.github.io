# $Id$
#
# This file is part of the pydns project.
# Homepage: http://pydns.sourceforge.net
#
# This code is covered by the standard Python License.
#

# routines for lazy people.
import Base

def revlookup(name): 
    "convenience routine for doing a reverse lookup of an address"
    import string
    a = string.split(name, '.')
    a.reverse()  
    b = string.join(a, '.')+'.in-addr.arpa'
    # this will only return one of any records returned.
    return Base.DnsRequest(b, qtype = 'ptr').req().answers[0]['data']

def mxlookup(name):
    """
    convenience routine for doing an MX lookup of a name. returns a
    sorted list of (preference, mail exchanger) records
    """
       
    a = Base.DnsRequest(name, qtype = 'mx').req().answers
    l = map(lambda x:x['data'], a)
    l.sort()
    return l

# 
# $Log$
# Revision 1.2  2001/07/19 06:57:07  anthony
# cvs keywords added
#
#
