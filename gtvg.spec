#
Summary:	gTVG - TV Guide news
Summary(pl.UTF-8):	gTVG - program telewizyjny
Name:		gtvg
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/gtvg/%{name}-%{version}.tar.gz
# Source0-md5:	6e3dd67f7f98a3217e4a960fb2eb5466
URL:		http://gtvg.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk+2-devel >= 2.8
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 2.6.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnomecanvas-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
Suggests:	xmltv-grabbers
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gTVG TV Guide is a simple TV program schedule viewer, which allows
you to quickly see what is on TV at the moment or later, and be
reminded of when your favourite shows start.

%prep
%setup -q

%build
#%%{__intltoolize}
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gtvg.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
/etc/gconf/schemas/*.schemas
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*
