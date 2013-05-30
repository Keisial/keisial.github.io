%define __python python3
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python3-pydns
Version:        3.1.0
Release:        1%{?dist}
Summary:        Python module for DNS (Domain Name Service).

Group:          Development/Languages
License:        Python Software Foundation License
URL:            http://pydns.sourceforge.net/
Source0:        pydns-%{version}.tar.gz
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
%setup -q -n %{namewithoutpythonprefix}-%{version}
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
%doc CREDITS.txt PKG-INFO README-guido.txt README.txt
%{python_sitelib}/DNS/*.py*

%changelog
* Tue Jun 09 2009 Stuart Gathman <stuart@bmsi.com> 2.3.4-1
- Support IDNA label encoding
- Optionally support M$ compatible UTF-8 label encoding.
* Thu Sep 25 2008 Stuart Gathman <stuart@bmsi.com> 2.3.3-3
- Accept unicode names, encode to ascii with exception if non-ascii
* Thu Sep 25 2008 Stuart Gathman <stuart@bmsi.com> 2.3.3-2
- Support IPv6 queries
* Fri Aug 01 2008 Stuart Gathman <stuart@bmsi.com> 2.3.3-1
- Support IPv6 nameservers
* Thu Jul 24 2008 Stuart Gathman <stuart@bmsi.com> 2.3.2-2
- Fix tcp timeout
* Thu Jul 24 2008 Stuart Gathman <stuart@bmsi.com> 2.3.2-1
- Randomize TID and source port, CVE-2008-4099 CVE-2008-4126
* Tue May 22 2007 Stuart Gathman <stuart@bmsi.com> 2.3.1-1
- Bug fix release
- BTS Patches:
- 01resolv-conf-parse patch, thanks to Arnaud Fontaine <arnaud@andesi.org>
  (closes: #378991)
- Changes from Ubuntu (SF = Sourceforge project bug #) (closes: #411138):
- 02utf-8 patch for files with UTF-8 content
- 03socket-error-trap patch, Added DNSError trap for socket.error.
- 04lazy-init SF 1563723 lazy should initilize defaults['server']
- 05addr2bin2addr SF 863364 Mac OS X, Win2000 DHCP, addr2bin and bin2addr.
- 06win32-fix SF 1180344 win32dns.py fails on windows server 2003
- 07unpacker SF 954095 Bug in DNS.Lib.Unpacker.getbyte()
- 08import-lib SF 658601 Missing "import Lib"; for TCP protocol
* Tue Aug 29 2006 Sean Reifschneider <jafo@tummy.com> 2.3.0-1
- Initial RPM spec file.
