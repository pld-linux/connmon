# TODO:
# - pack gconnmon to separate package
Summary:	Connection Monitor
Summary(pl):	Monitor po³±czeñ
Name:		connmon
Version:	0.13.0
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	http://www.student.lu.se/~nbi98oli/src/%{name}-%{version}.tar.gz
# Source0-md5:	b898f86769eb44ad6847bfa8f0a379f7
URL:		http://www.student.lu.se/~nbi98oli/
BuildRequires:	adns-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Connection Monitor is a connection and bandwidth monitoring program
with a console-based user interface. It displays a list of open TCP
and UDP connections with transfer rate (in bytes per second) for each
connection. This requires a linux 2.4 kernel with Netfilter connection
tracking facilities. A small patch (included with ConnMon) is
necessary to get the transfer rates displayed.

%description -l pl
Connection Monitor to program monitoruj±cy po³±czenia i przepustowo¶æ
z konsolowym interfejsem u¿ytkownika. Wy¶wietla listê otwartych
po³±czeñ TCP i UDP wraz z prêdko¶ci± przesy³u danych (w bajtach na
sekundê) dla ka¿dego po³±czenia. Wymaga j±dra 2.4 z mo¿liwo¶ciami
¶ledzenia po³±czeñ w Netfilterze. Potrzebna jest ma³a ³ata (za³±czona
z programem), aby otrzymywaæ prêdko¶ci przesy³u danych.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="-DHAVE_CONFIG_H -Wall `gtk-config --cflags` -I%{_includedir}/ncurses -I../compat -I../libconnmon -I../libhpnl -I.. -I. %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install src/connmon/connmon $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc kernel ChangeLog NEWS README TODO
%attr(755,root,root) %{_sbindir}/*
