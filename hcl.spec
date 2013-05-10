Summary:	Collect hardware information
Name:		hcl
Version:	1.7.1
Release:	7
License:	GPLv2
Group:		System/Configuration/Hardware
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	perl tar bzip2 perl-SOAP-Lite
Requires:	lshw

%description
hcl uploads your hardware information on Mandriva server to create a hardware
database and getting help on support.

%prep
%setup -q

%build
%make

%install
%makeinstall_std
install hclGUI hclcollector hclupload %{buildroot}/%{_sbindir}
mkdir -p -m 0755 %{buildroot}%{_prefix}/lib/libDrakX
install -D hclcollector.pm %{buildroot}%{_prefix}/lib/libDrakX
%find_lang drakhcl

%files -f drakhcl.lang
%doc AUTHORS COPYING README
%{_sbindir}/hclGUI
%{_sbindir}/hclcollector
%{_sbindir}/hclupload
%{_prefix}/lib/libDrakX/hclcollector.pm

