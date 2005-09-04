Summary:	Marathi dictionary for aspell
Summary(pl):	S³ownik marathijski dla aspella
Name:		aspell-mr
Version:	0.10
%define	subv	0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/mr/aspell6-mr-%{version}-%{subv}.tar.bz2
# Source0-md5:	489ac0c368d3012525134758f8572cac
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Marathi dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik marathijski (lista s³ów) dla aspella.

%prep
%setup -q -n aspell6-mr-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
