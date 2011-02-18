# $Id$
#
# This file is part of the pydns project.
# Homepage: http://pydns.sourceforge.net
#
# This code is covered by the standard Python License.
#

# routines for lazy people.
from . import Base

class NoDataError(IndexError): pass
class StatusError(IndexError): pass

def revlookup(name):
    "convenience routine for doing a reverse lookup of an address"
    if Base.defaults['server'] == []: Base.DiscoverNameServers()
    a = name.split('.')
    a.reverse()
    b = '.'.join(a)+'.in-addr.arpa'
    # this will only return one of any records returned.
    result = Base.DnsRequest(b, qtype = 'ptr').req()
    if result.header['status'] != 'NOERROR':
        raise StatusError("DNS query status: %s" % result.header['status'])
    elif len(result.answers) == 0:
        raise NoDataError("No PTR records for %s" % name)
    else:
        return result.answers[0]['data']

def revlookupfull(name):
    "convenience routine for doing a reverse lookup of an address"
    if Base.defaults['server'] == []: Base.DiscoverNameServers()
    a = name.split('.')
    a.reverse()
    b = '.'.join(a)+'.in-addr.arpa'
    # this will return all records.
    names = list(map(lambda x: x['data'], Base.DnsRequest(b, qtype = 'ptr').req().answers))
    if len(names)==0 and Base.defaults['server_rotate']: # check with next DNS server
        names = list(map(lambda x: x['data'], Base.DnsRequest(b, qtype = 'ptr').req().answers))
    names.sort(key=str.__len__)
    return names

def mxlookup(name):
    """
    convenience routine for doing an MX lookup of a name. returns a
    sorted list of (preference, mail exchanger) records
    """
    if Base.defaults['server'] == []: Base.DiscoverNameServers()
    a = Base.DnsRequest(name, qtype = 'mx').req().answers
    l = [x['data'] for x in a]
    l.sort()
    return l

#
# $Log$
# Revision 1.5.2.1  2007/05/22 20:23:38  customdesigned
# Lazy call to DiscoverNameServers
#
# Revision 1.5  2002/05/06 06:14:38  anthonybaxter
# reformat, move import to top of file.
#
# Revision 1.4  2002/03/19 12:41:33  anthonybaxter
# tabnannied and reindented everything. 4 space indent, no tabs.
# yay.
#
# Revision 1.3  2001/08/09 09:08:55  anthonybaxter
# added identifying header to top of each file
#
# Revision 1.2  2001/07/19 06:57:07  anthony
# cvs keywords added
#
#
