Summary:	Software for managing Zen Nomad playlist
Summary(pl):	Oprogramowanie do zarz±dzania list± odtwarzania Zen Creative
Name:		gnomad2
Version:	2.6.3
Release:	1
License:	BSD
Vendor:		PLD
Group:		Applications/Communications
Source0:	%{name}-%{version}.tar.gz
Source1:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source1-md5:	a969cb089c63c72ab242d94fc0413e62
URL:		http://gnomad2.sourceforge.net/
BuildRequires:	libnjb
Requires:	libnjb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
(2 b done)

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO

%attr(755,root,root) %{_bindir}/*
