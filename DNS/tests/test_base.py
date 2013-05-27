#!/usr/bin/python3
# -*- coding: utf-8 -*-

import DNS
import unittest

def assertIsByte(b):
    assert b >= 0
    assert b <= 255
    
class TestBase(unittest.TestCase):
    def testParseResolvConf(self):
        # reset elments set by Base._DiscoverNameServers
        DNS.defaults['server'] = []
        if 'domain' in  DNS.defaults:
            del DNS.defaults['domain']
        self.assertEqual(len(DNS.defaults['server']), 0)
        resolv = ['# a comment',
                  'domain example.org',
                  'nameserver 127.0.0.1',
                 ]
        DNS.ParseResolvConfFromIterable(resolv)
        self.assertEqual(len(DNS.defaults['server']), 1)
        self.assertEqual(DNS.defaults['server'][0], '127.0.0.1')
        self.assertEqual(DNS.defaults['domain'], 'example.org')
        
    def testDnsRequestA(self):
        # try with asking for strings, and asking for bytes
        dnsobj = DNS.DnsRequest('example.org')
        
        a_response = dnsobj.req(qtype='A', resulttype='text')
        self.assertTrue(a_response.answers)
        # is the result vaguely ipv4 like?
        self.assertEqual(a_response.answers[0]['data'].count('.'), 3)
        self.assertEqual(a_response.answers[0]['data'],'192.0.43.10')

        ad_response = dnsobj.req(qtype='A')
        self.assertTrue(ad_response.answers)
        # is the result vaguely ipv4 like?
        self.assertEqual(ad_response.answers[0]['data'].count('.'), 3)
        self.assertEqual(a_response.answers[0]['data'],'192.0.43.10')

        ab_response = dnsobj.req(qtype='A', resulttype='binary')
        self.assertTrue(ab_response.answers)
        # is the result ipv4 binary like?
        self.assertEqual(len(ab_response.answers[0]['data']), 4)
        for b in ab_response.answers[0]['data']:
            assertIsByte(b)
        self.assertEqual(ab_response.answers[0]['data'],b'\xc0\x00+\n')

        ai_response = dnsobj.req(qtype='A', resulttype='integer')
        self.assertTrue(ai_response.answers)
        # is the result ipv4 decimal like?
        self.assertEqual(type(ab_response.answers[0]['data']), 'int')
        self.assertEqual(ai_response.answers[0]['data'],3221236490)


    def testDnsRequestAAAA(self):
        dnsobj = DNS.DnsRequest('example.org')
        
        aaaa_response = dnsobj.req(qtype='AAAA', resulttype='text')
        self.assertTrue(aaaa_response.answers)
        # does the result look like an ipv6 address?
        self.assertTrue(':' in aaaa_response.answers[0]['data'])
        self.assertEqual(aaaa_response.answers[0]['data'],'2001:500:88:200::10')

        # default is returning binary instead of text
        aaaad_response = dnsobj.req(qtype='AAAA')
        self.assertTrue(aaaad_response.answers)
        # does the result look like a binary ipv6 address?
        self.assertEqual(len(aaaad_response.answers[0]['data']) , 16)
        for b in aaaad_response.answers[0]['data']:
            assertIsByte(b)
        self.assertEqual(aaaad_response.answers[0]['data'],b' \x01\x05\x00\x00\x88\x02\x00\x00\x00\x00\x00\x00\x00\x00\x10')
        
        aaaab_response = dnsobj.req(qtype='AAAA', resulttype='binary')
        self.assertTrue(aaaab_response.answers)
        # is it ipv6 looking?
        self.assertEqual(len(aaaab_response.answers[0]['data']) , 16)
        for b in aaaab_response.answers[0]['data']:
            assertIsByte(b)
        self.assertEqual(aaaab_response.answers[0]['data'],b' \x01\x05\x00\x00\x88\x02\x00\x00\x00\x00\x00\x00\x00\x00\x10')

    def testDnsRequestEmptyMX(self):
        dnsobj = DNS.DnsRequest('example.org')

        mx_empty_response = dnsobj.req(qtype='MX')
        self.assertFalse(mx_empty_response.answers)

    def testDnsRequestMX(self):
        dnsobj = DNS.DnsRequest('ietf.org')
        mx_response = dnsobj.req(qtype='MX')
        self.assertTrue(mx_response.answers[0])
        # is hard coding a remote address a good idea?
        # I think it's unavoidable. - sk
        self.assertEqual(mx_response.answers[0]['data'], (0, 'mail.ietf.org'))

        m = DNS.mxlookup('ietf.org')
        self.assertEqual(mx_response.answers[0]['data'], m[0])

    def testDnsRequestSrv(self):
        dnsobj = DNS.Request(qtype='srv')
        resp = dnsobj.req('_ldap._tcp.openldap.org', resulttype='text')
        self.assertTrue(resp.answers)
        data = resp.answers[0]['data']
        self.assertEqual(len(data), 4)
        self.assertEqual(data[2], 389)
        self.assertTrue('openldap.org' in data[3])

    def testDkimRequest(self):
        q = '20120113._domainkey.google.com'
        dnsobj = DNS.Request(q, qtype='txt')
        resp = dnsobj.req()
        
        self.assertTrue(resp.answers)
        # should the result be bytes or a string?
        data = resp.answers[0]['data']
        self.assertTrue(isinstance(data[0], str))
        self.assertTrue(data[0].startswith('k='))

    def testIDN(self):
        """Can we lookup an internationalized domain name?"""
        dnsobj = DNS.DnsRequest('xn--hxajbheg2az3al.xn--jxalpdlp')
        unidnsobj = DNS.DnsRequest('παράδειγμα.δοκιμή')
        a_resp = dnsobj.req(qtype='AAAA', resulttype='text')
        ua_resp = unidnsobj.req(qtype='AAAA', resulttype='text')
        self.assertTrue(a_resp.answers)
        self.assertTrue(ua_resp.answers)
        self.assertEqual(ua_resp.answers[0]['data'], 
                         a_resp.answers[0]['data'])
            
def test_suite():
    from unittest import TestLoader
    return TestLoader().loadTestsFromName(__name__)

if __name__ == "__main__":
    unittest.main()
