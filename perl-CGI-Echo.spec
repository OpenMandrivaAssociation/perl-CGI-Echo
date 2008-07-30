%define real_name CGI-Echo

Summary:	CGI-Echo module for perl 
Name:		perl-%{real_name}
Version:	1.04
Release: %mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module accepts form data, cleans it, and echos it.
It is designed for a HTML/CGI student enviroment. It lets, indeed encourages,
students to design forms and gives their long-suffering instructors a simple
way to provide a CGI script which accepts the form data, and just echos it.

%prep
%setup -q -n %{real_name}-%{version} 

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
%doc Changes.txt README
%{perl_vendorlib}/CGI/Echo.pm
%{_mandir}/*/*




