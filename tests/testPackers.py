#!/usr/bin/env python

#
# Tests of the packet assembler/disassembler routines.
#
# only tests the simple packers for now. next is to test the 
# classes: Packer/Unpacker, RRpacker/RRunpacker, Hpacker/Hunpacker,
# Qpacker/Unpacker, then Mpacker/Munpacker
#

import DNS
import unittest

class Int16Packing(unittest.TestCase):
    knownValues = ( ( 10, '\x00\n'),
                   ( 500, '\x01\xf4' ),
                   ( 5340, '\x14\xdc' ),
                   ( 51298, '\xc8b'),
                   ( 65535, '\xff\xff'),
                   )

    def test16bitPacking(self):
        """ pack16bit should give known output for known input """
        for i,s in self.knownValues:
            result = DNS.Lib.pack16bit(i)
            self.assertEqual(s,result)

    def test16bitUnpacking(self):
        """ unpack16bit should give known output for known input """
        for i,s in self.knownValues:
            result = DNS.Lib.unpack16bit(s)
            self.assertEqual(i,result)

class Int32Packing(unittest.TestCase):
    knownValues = ( ( 10, '\x00\x00\x00\n'),
                   ( 500, '\x00\x00\x01\xf4' ),
                   ( 5340, '\x00\x00\x14\xdc' ),
                   ( 51298, '\x00\x00\xc8b'),
                   ( 65535, '\x00\x00\xff\xff'),
                   ( 33265535, '\x01\xfb\x97\x7f' ),
                   ( 147483647, '\x08\xcak\xff' ),
                   ( 2147483647, '\x7f\xff\xff\xff' ),
                   )
    def test32bitPacking(self):
        """ pack32bit should give known output for known input """
        for i,s in self.knownValues:
            result = DNS.Lib.pack32bit(i)
            self.assertEqual(s,result)

    def test32bitUnpacking(self):
        """ unpack32bit should give known output for known input """
        for i,s in self.knownValues:
            result = DNS.Lib.unpack32bit(s)
            self.assertEqual(i,result)

            
class IPaddrPacking(unittest.TestCase):
    knownValues = ( 
                    ('127.0.0.1', 2130706433 ), 
                    ('10.99.23.13', 174266125 ),
                    ('192.35.59.45', -1071432915 ), # signed, sigh
                    ('255.255.255.255', -1),
                    )

    def testIPaddrPacking(self):
        """ addr2bin should give known output for known input """
        for i,s in self.knownValues:
            result = DNS.Lib.addr2bin(i)
            self.assertEqual(s,result)

    def testIPaddrUnpacking(self):
        """ bin2addr should give known output for known input """
        for i,s in self.knownValues:
            result = DNS.Lib.bin2addr(s)
            self.assertEqual(i,result)


# more to come...



if __name__ == "__main__":
    unittest.main()
