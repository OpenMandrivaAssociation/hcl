%define name hcl
%define version 1.2
%define release %mkrel 2

Summary: Collect hardware information
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System/Configuration/Hardware
Source0: %name-%version.tar.bz2
BuildArch: noarch
Requires: hwreport
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
%find_lang drakhcl

%clean
rm -rf %buildroot/

%files -f drakhcl.lang
%doc AUTHORS COPYING README
%_sbindir/*
