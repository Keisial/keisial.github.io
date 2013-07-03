%define __python python3
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python3-pydns
Version:        3.1.0
Release:        1%{?dist}
Summary:        Python module for DNS (Domain Name Service).

Group:          Development/Languages
License:        Python Software Foundation License
URL:            http://pydns.sourceforge.net/
Source0:        py3dns-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	python3
BuildArch:      noarch

%description
This is a another release of the pydns code, as originally written by
Guido van Rossum, and with a hopefully nicer API bolted over the
top of it by Anthony Baxter <anthony@interlink.com.au>.

This package contains a module (dnslib) that implements a DNS
(Domain Name Server) client, plus additional modules that define some
symbolic constants used by DNS (dnstype, dnsclass, dnsopcode).

This version was ported to Python3 by Scott Kitterman <scott@kitterman.com>

%define namewithoutpythonprefix %(echo %{name} | sed 's/^python-//')
%prep
%setup -q -n py3dns-%{version}
#patch -p1 -b .sdg

%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CREDITS.txt PKG-INFO README-guido.txt README.txt LICENSE CHANGES
%{python_sitelib}/DNS/*.py*
%{python_sitelib}/DNS/__pycache__/*.py*
%{python_sitelib}/py3dns-3.1.0-py3.2.egg-info

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

