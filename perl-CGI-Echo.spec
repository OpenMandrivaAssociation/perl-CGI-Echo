%define upstream_name    CGI-Echo
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	CGI-Echo module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tgz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module accepts form data, cleans it, and echos it.
It is designed for a HTML/CGI student enviroment. It lets, indeed encourages,
students to design forms and gives their long-suffering instructors a simple
way to provide a CGI script which accepts the form data, and just echos it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README META.yml
%{perl_vendorlib}/CGI/Echo.pm
%{_mandir}/*/*
