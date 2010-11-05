%define upstream_name    Catalyst-Plugin-Server
%define upstream_version 0.28

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Server extensions for Catalyst
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Catalyst)
BuildRequires: perl(Clone::Fast)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(RPC::XML)
BuildRequires: perl(RPC::XML::Parser)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Base plugin for XMLRPC and our future SOAP server. For further information,
see one of the Server plugins

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml README Changes
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/rpc_client

