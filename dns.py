import sys
import getopt
import socket
import string
import dnslib,dnstype,dnsclass,dnsopcode

defaults= { 'protocol':'udp', 'port':53, 'opcode':dnsopcode.QUERY, 
            'qtype':dnstype.A, 'rd':1, 'timing':1 }

defaults['server']=['192.35.59.35']

def ParseResolvConf():
    import string
    global defaults
    lines=open("/etc/resolv.conf").readlines()
    for line in lines:
	string.strip(line)
	if line[0]==';' or line[0]=='#':
	    continue
	fields=string.split(line)
	if fields[0]=='domain':
	    defaults['domain']=fields[1]
	if fields[0]=='search':
	    pass
	if fields[0]=='options':
	    pass
	if fields[0]=='sortlist':
	    pass
	if fields[0]=='nameserver':
	    defaults['server'].append(fields[1])

def revlookup(name):
    import string
    a=string.split(name,'.')
    a.reverse()
    print a
    b=string.join(a,'.')+'.in-addr.arpa'
    print b
    return lookup(b,qtype='ptr')

def lookup(*name,**args):
    import timing,sys
    if len(name) == 1:
	args['name']=name[0]
    for i in defaults.keys():
	if not args.has_key(i):
	    args[i]=defaults[i]
    protocol = args['protocol']
    if type(args['server']) == type(''):
	server = [args['server']]
    else:
	server = args['server']
    port = args['port']
    opcode = args['opcode']
    rd = args['rd']
    if type(args['qtype']) == type('foo'):
	try:
	    qtype = eval(string.upper(args['qtype']), dnstype.__dict__)
	except (NameError,SyntaxError):
	    raise 'dnsapi.error','unknown query type'
    else:
	qtype=args['qtype']
    if not args.has_key('name'):
	raise 'dnsapi.error','nothing to lookup'
    qname = args['name']
    if qtype == dnstype.AXFR:
	print 'Query type AXFR, protocol forced to TCP'
	protocol = 'tcp'
    #print 'QTYPE %d(%s)' % (qtype, dnstype.typestr(qtype))
    m = dnslib.Mpacker()
    m.addHeader(0,
	  0, opcode, 0, 0, rd, 0, 0, 0,
	  1, 0, 0, 0)
    m.addQuestion(qname, qtype, dnsclass.IN)
    request = m.getbuf()
    if protocol == 'udp':
	reply=None
	for ns in server:
	    try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect((ns, port))
		timing.start()
		s.send(request)
		reply = s.recv(1024)
		timing.finish()
	    except socket.error:
		continue
	    break
	if not reply:
	    raise 'dns.error','no working nameservers found'
	args['server']=ns
    else:
	reply=None
	for ns in server:
	    try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		timing.start()
		s.connect((server, port))
		s.send(pack16bit(len(request)) + request)
		s.shutdown(1)
		f = s.makefile('r')
		header = f.read(2)
		if len(header) < 2:
			raise 'dns.error','EOF'
		count = dnslib.unpack16bit(header)
		reply = f.read(count)
		if len(reply) != count:
		    raise 'dns.error','incomplete reply'
		timing.finish()
	    except socket.error:
		continue
	    break
	if not reply:
	    raise 'dns.error','no working nameservers found'
	args['server']=ns
    args['elapsed']=timing.milli()
    u = dnslib.Munpacker(reply)
    r=dnslib.DnsResult(u,args)
    r.args=args
    return r
    if protocol == 'tcp' and qtype == dnstype.AXFR:
	while 1:
	    header = f.read(2)
	    if len(header) < 2:
		print '========== EOF =========='
		break
	    count = dnslib.unpack16bit(header)
	    if not count:
		print '========== ZERO COUNT =========='
		break
	    print '========== NEXT =========='
	    reply = f.read(count)
	    if len(reply) != count:
		print '*** Incomplete reply ***'
		break
	    u = dnslib.Munpacker(reply)
	    dnslib.dumpM(u)


