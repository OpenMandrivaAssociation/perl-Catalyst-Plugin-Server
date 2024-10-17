%define upstream_name    Catalyst-Plugin-Server
%define upstream_version 0.28

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Server extensions for Catalyst
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Clone::Fast)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(RPC::XML)
BuildRequires:	perl(RPC::XML::Parser)
BuildRequires:	perl(Class::Data::Inheritable)
BuildArch:	noarch

%description
Base plugin for XMLRPC and our future SOAP server. For further information,
see one of the Server plugins

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/rpc_client


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.280.0-2mdv2011.0
+ Revision: 654264
- rebuild for updated spec-helper

* Fri Nov 05 2010 Olivier Thauvin <nanardon@mandriva.org> 0.280.0-1mdv2011.0
+ Revision: 593726
- import perl-Catalyst-Plugin-Server

