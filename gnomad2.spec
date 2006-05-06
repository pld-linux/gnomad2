Summary:	Software for managing Zen Nomad playlist
Summary(pl):	Oprogramowanie do zarz�dzania list� plik�w Zen Creative
Name:		gnomad2
Version:	2.8.3
Release:	2
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/gnomad2/%{name}-%{version}.tar.gz
# Source0-md5:	cc2d29265e84c2460075ff2b78c2f119
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-libnjb.patch
Patch1:		%{name}-mtp-0.0.2-to-0.0.4.patch
URL:		http://gnomad2.sourceforge.net/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libid3tag-devel >= 0.15
BuildRequires:	libmtp-devel >= 0.0.4
BuildRequires:	libnjb-devel >= 2.2.4
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnomad 2 is a GUI built on top of GTK+/GNOME 2, libid3tag and libnjb
that makes it possible to transfer tracks and files from/to a Creative
Nomad Jukebox (all brands). It is designed much like an ordinary
graphical FTP program.

%description -l pl
Gnomad 2 jest graficznym interfejsem u�ytkownika zbudowanym w oparciu
o biblioteki GTK+/GNOME, libid3tag oraz libnjb. Umo�liwia przesy�anie
utwor�w z i do odtwarzacza Nomad Creative. Zosta� zaprojektowany na
wz�r zwyk�ego graficznego klienta FTP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/gnomad2.desktop
%{_pixmapsdir}/gnomad2.png
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/gnomad2.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/gnomad2.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/gnomad2.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/gnomad2.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/gnomad2.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/gnomad2.mo
%lang(no) %{_datadir}/locale/no/LC_MESSAGES/gnomad2.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/gnomad2.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/gnomad2.mo

%{_mandir}/man1/*
