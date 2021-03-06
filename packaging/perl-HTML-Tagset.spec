Name:           perl-HTML-Tagset
Version:        3.20
Release:        8
Summary:        HTML::Tagset - data tables useful in parsing HTML

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/HTML-Tagset/
Source0:        %{name}-%{version}.tar.gz
Source1001:     packaging/perl-HTML-Tagset.manifest 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker), perl(Test::Pod)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module contains several data tables useful in various kinds of
HTML parsing operations, such as tag and entity names.


%prep
%setup -q

%build
cp %{SOURCE1001} .
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT


%files
%manifest perl-HTML-Tagset.manifest
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/HTML/*
#%doc %{_mandir}/man3/HTML::Tagset.3pm*


