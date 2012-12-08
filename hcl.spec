%define name hcl
%define version 1.7.1
%define release 7

Summary: Collect hardware information
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System/Configuration/Hardware
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0: %name-%version.tar.bz2
BuildArch: noarch
Requires: perl tar bzip2 perl-SOAP-Lite
Requires: lshw

%description
hcl uploads your hardware information on Mandriva server to create a hardware
database and getting help on support.

%prep
%setup -q -n %{name}-%version

%build
%make

%install
rm -rf %buildroot
%makeinstall_std
install hclGUI hclcollector hclupload %buildroot/%_sbindir
mkdir -p -m 0755 %{buildroot}%{_prefix}/lib/libDrakX
install -D hclcollector.pm %{buildroot}%{_prefix}/lib/libDrakX
%find_lang drakhcl

%clean
rm -rf %buildroot/

%files -f drakhcl.lang
%doc AUTHORS COPYING README
%_sbindir/hclGUI
%_sbindir/hclcollector
%_sbindir/hclupload
%{_prefix}/lib/libDrakX/hclcollector.pm


%changelog
* Thu Aug 18 2011 Sergio Rafael Lemke <sergio@mandriva.com> 1.7.1-6
+ Revision: 695214
- Added perl-SOAP-Lite as requires #64003

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7.1-5
+ Revision: 665404
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7.1-4mdv2011.0
+ Revision: 605852
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7.1-3mdv2010.1
+ Revision: 522845
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.7.1-2mdv2010.0
+ Revision: 425140
- rebuild

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 1.7.1-1mdv2009.1
+ Revision: 367522
- updated translation

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.7-4mdv2009.1
+ Revision: 351230
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.7-3mdv2009.0
+ Revision: 221124
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.7-2mdv2008.1
+ Revision: 150251
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Oct 03 2007 Thierry Vignaud <tv@mandriva.org> 1.7-1mdv2008.0
+ Revision: 95088
- updated translation

* Mon Oct 01 2007 Thierry Vignaud <tv@mandriva.org> 1.6-1mdv2008.0
+ Revision: 94237
- updated translation

* Thu Sep 27 2007 Thierry Vignaud <tv@mandriva.org> 1.5-1mdv2008.0
+ Revision: 93284
- cleanups
- less verbose
- typo fixes (adam)

* Tue Sep 25 2007 Thierry Vignaud <tv@mandriva.org> 1.4-1mdv2008.0
+ Revision: 92894
- cleanups
- kill old source

  + Chandrasegaran Parassouramane <chandra@mandriva.com>
    - shifting report file

* Tue Sep 25 2007 Chandrasegaran Parassouramane <chandra@mandriva.com> 1.3-1mdv2008.0
+ Revision: 92739
- new version

* Mon Sep 24 2007 Thierry Vignaud <tv@mandriva.org> 1.2-2mdv2008.0
+ Revision: 92594
- fix %%find_lang
- cleanups
- fix crash when switching desktop
- require tar & bzip2
- add translations
- cleanups
- close fd leaks
- we now have files to build
- use %%makeinstall_std

* Wed Sep 19 2007 Pixel <pixel@mandriva.com> 1.0-1mdv2008.0
+ Revision: 90968
- cleanup
- import hcl


* Wed Sep 19 2007 Chandrasegaran PARASSOURAMANE <chandra@mandriva.com> 1.0-1mdv2008.0
- added new scripts : hclcollector, hclGUI, hcldmidecodeinfo, hcllshwinfo, hclcpuinfo, hclupload. Modifying initscripts /etc/init.d/mandrake_firsttime for adding /usr/sbin.
* Tue Sep 04 2007 Chandrasegaran PARASSOURAMANE <chandra@mandriva.com> 1.0-1mdv2008.0
- added documents
* Thu Aug 29 2007 Chandrasegaran PARASSOURAMANE <chandra@mandriva.com> 1.0-1mdv2008.0
- working on the first package
