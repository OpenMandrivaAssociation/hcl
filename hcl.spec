%define name hcl
%define version 1.0
%define release %mkrel 1

Summary: Collect hardware information
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System/Configuration/Hardware
Source0: %name-%version.tar.bz2
BuildArch: noarch
Requires: hwreport
Requires: perl
Requires: lshw

%description
hcl uploads your hardware information on Mandriva server to create a hardware
database and getting help on support.

%prep
%setup -q -n %{name}-%version

%build

%install
rm -rf %buildroot

mkdir -p %buildroot/%_sbindir

install hclcollector hclGUI hcldmidecodeinfo hcllshwinfo hclcpuinfo hclupload %buildroot/%_sbindir

%clean
rm -rf %buildroot/

%files
%doc AUTHORS COPYING README
%_sbindir/*
