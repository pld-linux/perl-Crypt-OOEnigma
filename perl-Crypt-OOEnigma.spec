#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OOEnigma
Summary:	Crypt::OOEnigma Perl module - flexible interface to Enigma
Summary(pl):	Modu³ Perla Crypt::OOEnigma - elastyczny interfejs do Enigmy
Name:		perl-Crypt-OOEnigma
Version:	0.3
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Storable >= 0.6.1.11
BuildRequires:	perl-Test-Simple >= 0.41
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	perl-Storable >= 0.6.1.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A flexible, object-oriented interface to a WWII Enigma machine.
Commercial and Military Enigmas are provided for use and modification.
You can easily construct your own with any number of rotors, your own
ciphers in each component etc. Those who wish to explore an Enigma
with historically accurate ciphers should try Crypt::Enigma or use
this module to create their own Enigma with WWII ciphers.

%description -l pl
Modu³ Crypt::OOEnigma jest elastycznym, zorientowanym obiektowo
interfejsem do maszyny Enigma z II Wojny ¦wiatowej. Pozwala u¿ywaæ i
modyfikowaæ komercyjne i militarne wersje Enigmy. Mo¿na ³atwo
skonstruowaæ w³asn± z dowoln± liczb± bêbnów, w³asnymi szyframi dla
ka¿dego komponentu itp. Chc±cy u¿ywaæ Enigmy z historycznymi szyframi
powinni u¿yæ modu³u Crypt::Enigma lub u¿yæ tego modu³u do stworzenia
w³asnej Enigmy z szyframi z IIW¦.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install bin/Enigma.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Crypt/OOEnigma.pm
%{perl_sitelib}/Crypt/OOEnigma
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
