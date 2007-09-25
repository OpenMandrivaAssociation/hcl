%define name hcl
%define version 1.4
%define release %mkrel 1

Summary: Collect hardware information
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System/Configuration/Hardware
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0: %name-%version.tar.bz2
BuildArch: noarch
Requires: perl tar bzip2
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
