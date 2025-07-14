Summary:	LPairs - a classic memory game for Linux
Summary(pl.UTF-8):	LPairs - klasyczna gra pamięciowa pod Linuksa
Name:		lpairs2
Version:	2.3
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	https://downloads.sourceforge.net/lgames/%{name}-%{version}.tar.gz
# Source0-md5:	a40461e91b688617431377502cbe8348
Patch0:		%{name}-icondir.patch
URL:		https://lgames.sourceforge.net/LPairs
BuildRequires:	SDL2-devel >= 2.0
BuildRequires:	SDL2_image-devel >= 2.0
BuildRequires:	SDL2_mixer-devel >= 2.0
BuildRequires:	SDL2_ttf-devel >= 2.0
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libstdc++-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LPairs - a classic memory game for Linux.

%description -l pl.UTF-8
LPairs - klasyczna gra pamięciowa pod Linuksa.

%prep
%setup -q
%patch -P0 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no translations yet
#find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
# -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/lpairs2
%{_datadir}/lpairs2
%{_desktopdir}/lpairs2.desktop
%{_pixmapsdir}/lpairs2.png
