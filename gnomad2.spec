Summary:	Software for managing Zen Nomad playlist
Summary(pl.UTF-8):	Oprogramowanie do zarządzania listą plików Zen Creative
Name:		gnomad2
Version:	2.9.1
Release:	5
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/gnomad2/%{name}-%{version}.tar.gz
# Source0-md5:	817888f2e952525ad649027e4e4baf38
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://gnomad2.sourceforge.net/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libid3tag-devel >= 0.15.1b-4
BuildRequires:	libmtp-devel >= 0.1.3
BuildRequires:	libnjb-devel >= 2.2.4
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnomad 2 is a GUI built on top of GTK+/GNOME 2, libid3tag and libnjb
that makes it possible to transfer tracks and files from/to a Creative
Nomad Jukebox (all brands). It is designed much like an ordinary
graphical FTP program.

%description -l pl.UTF-8
Gnomad 2 jest graficznym interfejsem użytkownika zbudowanym w oparciu
o biblioteki GTK+/GNOME, libid3tag oraz libnjb. Umożliwia przesyłanie
utworów z i do odtwarzacza Nomad Creative. Został zaprojektowany na
wzór zwykłego graficznego klienta FTP.

%prep
%setup -q

%build
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/libnjb"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{no,nb}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/cs{_CZ,}
# unsupported by glibc (2.7)
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/sco
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/gnomad2.desktop
%{_pixmapsdir}/gnomad2*.png
%{_mandir}/man1/*
%{_datadir}/application-registry/gnomad2.applications
