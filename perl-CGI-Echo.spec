%define upstream_name    CGI-Echo
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:    3

Summary:	CGI-Echo module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tgz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module accepts form data, cleans it, and echos it.
It is designed for a HTML/CGI student enviroment. It lets, indeed encourages,
students to design forms and gives their long-suffering instructors a simple
way to provide a CGI script which accepts the form data, and just echos it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc CHANGES README META.yml
%{perl_vendorlib}/CGI/Echo.pm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.80.0-2mdv2011.0
+ Revision: 680685
- mass rebuild

* Tue Aug 24 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.80.0-1mdv2011.0
+ Revision: 572699
- update to 1.08

* Sun Jul 12 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.50.0-1mdv2011.0
+ Revision: 395000
- update to 1.05
- using %%perl_convert_version
- fixed license field

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.04-5mdv2009.0
+ Revision: 255715
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-3mdv2008.1
+ Revision: 136903
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.04-2mdv2007.0
+ Revision: 73358
- import perl-CGI-Echo-1.04-2mdk

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.04-2mdk
- Fix SPEC Using perl Policies
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.04-1mdk
- initial Mandriva package

