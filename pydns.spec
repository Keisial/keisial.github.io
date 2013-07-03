%define name py3dns
%define version 3.1.0

Summary: Python DNS library
Name: py3dns
Version: 3.1.0
Release: 1
Source0: %{name}-%{version}.tar.gz
License: Python license
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Anthony Baxter and others <pydns-developer@lists.sourceforge.net>
Packager: Stuart D. Gathman <stuart@bmsi.com>
Url: https://launchpad.net/py3dns/
Requires: python3

%description
This is a another release of the pydns code, as originally written by
Guido van Rossum, and with a hopefully nicer API bolted over the
top of it by Anthony Baxter <anthony@interlink.com.au>.

This package contains a module (dnslib) that implements a DNS
(Domain Name Server) client, plus additional modules that define some
symbolic constants used by DNS (dnstype, dnsclass, dnsopcode).

This version was ported to Python3 by Scott Kitterman <scott@kitterman.com>

%prep
%setup

%build
python3 setup.py build

%install
python3 setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Wed Jul 03 2013 Stuart Gathman <stuart@gathman.org> 3.1.0-1
- Add options for 'resulttype' to DnsResult.req to allow for binary, integer,
  or text data to be returned for IP addresses
- New unittest based test suite - thanks to Diane Trout

* Wed May 29 2013 Stuart Gathman <stuart@gathman.org> 3.0.3-1
- Revert returning IPv6 addresses from AAAA lookups as string.  Causing
  incompatiblities that are deeply annoying to fix on the other end.

* Thu Jan 19 2012 Stuart Gathman <stuart@gathman.org> 3.0.2-1
- Add more granular exception sub classes of DNSError, see SF #3388075
  o Thanks to Julian Mehnle for the patch
- Add AAAA record support, works like A records
  o Thanks to Shane Kerr for the patch

* Mon Jul 18 2011 Stuart Gathman <stuart@gathman.org> 3.0.1-1
- Add CHANGES to document post-Python 3 port changes
- Add LICENSE file
- Port pydns 2.3.5 changes to py3dns
  o Handle large TCP replies (change to blocking IO with timeout)
  o Add new lazy.dnslookup function to retrieve answer data for any query
    type
  o Add large TCP reply test to tests/test.py
- Add automatic name server discovery for OS X

* Wed Feb  9 2011 Stuart Gathman <stuart@gathman.org> 3.0.0-1
- Ported to Python3 by Scott Kitterman <scott@kitterman.com>.  This is mostly a
  minimal port to work with Python3 (tested with python3.2) plus addition of
  some of the patches that people have submitted on Sourceforge.  It should be
  fully API compatible with 2.3.

