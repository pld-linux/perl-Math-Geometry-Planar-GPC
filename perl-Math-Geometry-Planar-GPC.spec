#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Geometry-Planar-GPC
Summary:	Math::Geometry::Planar::GPC - Perl wrapper for Alan Murta's gpc library
Summary(pl.UTF-8):	Math::Geometry::Planar::GPC - interfejs perlowy do biblioteki gpc Alana Murty
Name:		perl-Math-Geometry-Planar-GPC
Version:	1.04
Release:	7
# perl interface is under "Artistic" license, but gpc itself is non-commercial
License:	non-commercial use, freely distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0f059f596abba73eee7f0ffcee134567
URL:		http://search.cpan.org/dist/Math-Geometry-Planar-GPC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-Math-Geometry-GPC
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is just a wrapper around the gpc (Generic Polygon
Clipping) C library written by Alan Murta.

%description -l pl.UTF-8
Ten moduł jest interfejsem do biblioteki C gpc (Generic Polygon
Clipping - ogólnego obcinania wielokątów) autorstwa Alana Murty.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/Math/Geometry
%dir %{perl_vendorarch}/Math/Geometry/Planar
%{perl_vendorarch}/Math/Geometry/Planar/GPC.pm
%dir %{perl_vendorarch}/auto/Math/Geometry
%dir %{perl_vendorarch}/auto/Math/Geometry/Planar
%dir %{perl_vendorarch}/auto/Math/Geometry/Planar/GPC
%attr(755,root,root) %{perl_vendorarch}/auto/Math/Geometry/Planar/GPC/GPC.so
%{_mandir}/man3/*
