#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"

%define		pdir	Crypt
%define		pnam	OOEnigma
%include	/usr/lib/rpm/macros.perl
Summary:	Crypt::OOEnigma Perl module - flexible interface to Enigma
Summary(pl.UTF-8):	Moduł Perla Crypt::OOEnigma - elastyczny interfejs do Enigmy
Name:		perl-Crypt-OOEnigma
Version:	0.3
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e8c14d05b89a30574d1a5d6cea239cde
URL:		http://search.cpan.org/dist/Crypt-OOEnigma/
BuildRequires:	perl-Test-Simple >= 0.41
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A flexible, object-oriented interface to a WWII Enigma machine.
Commercial and Military Enigmas are provided for use and modification.
You can easily construct your own with any number of rotors, your own
ciphers in each component etc. Those who wish to explore an Enigma
with historically accurate ciphers should try Crypt::Enigma or use
this module to create their own Enigma with WWII ciphers.

%description -l pl.UTF-8
Moduł Crypt::OOEnigma jest elastycznym, zorientowanym obiektowo
interfejsem do maszyny Enigma z II Wojny Światowej. Pozwala używać i
modyfikować komercyjne i militarne wersje Enigmy. Można łatwo
skonstruować własną z dowolną liczbą bębnów, własnymi szyframi dla
każdego komponentu itp. Chcący używać Enigmy z historycznymi szyframi
powinni użyć modułu Crypt::Enigma lub użyć tego modułu do stworzenia
własnej Enigmy z szyframi z IIWŚ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p bin/Enigma.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/OOEnigma.pm
%{perl_vendorlib}/Crypt/OOEnigma
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
