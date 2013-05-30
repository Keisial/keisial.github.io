# -*- encoding: utf-8 -*-
# $Id$
#
# This file is part of the py3dns project.
# Homepage: https://launchpad.net/py3dns
#
# Changes for Python3 port © 2011 Scott Kitterman <scott@kitterman.com>
#
# This code is covered by the standard Python License. See LICENSE for details.

# __init__.py for DNS class.

__version__ = '3.1.0'

from . import Type
from . import Opcode
from . import Status
from . import Class
from .Base import DnsRequest
from .Base import DNSError
from .Lib import DnsResult
from .Base import *
from .Lib import *
Error=DNSError
from .lazy import *
Request = DnsRequest
Result = DnsResult

Base._DiscoverNameServers()

