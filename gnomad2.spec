Summary:	Software for managing Zen Nomad playlist
Summary(pl):	Oprogramowanie do zarz±dzania list± plików Zen Creative
Name:		gnomad2
Version:	2.6.3
Release:	3
License:	GPL v2
Vendor:		PLD
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/gnomad2/%{name}-%{version}.tar.gz
# Source0-md5:	a969cb089c63c72ab242d94fc0413e62
Source1:	gnomad2.desktop
Source2:	gnomad2.png
Patch0:		%{name}-libnjb.patch
URL:		http://gnomad2.sourceforge.net/
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libnjb-devel
BuildRequires:	pkgconfig
Requires:	libnjb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnomad 2 is a GUI built on top of GTK/GNOME 2, id3lib and libnjb that makes it
possible to transfer tracks and files from/to a Creative Nomad Jukebox (all
brands). It is designed much like an ordinary graphical FTP program.

%description -l pl
Gnomad 2 jest Graficznym Interfejsem U¿ytkownika zbudowanym w oparciu o
bibliotekê GTK, id3lib oraz libnjb.  Umo¿liwia transfer utworów z i do
odtwarzacza Nomad Creative. Zosta³ zaprojektowany na wzór popularnego klienta
FTP.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT/%{_pixmapsdir}

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
