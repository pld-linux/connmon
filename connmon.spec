# TODO:
# - pack gconnmon to separate package
Summary:	Connection Monitor
Summary(pl.UTF-8):   Monitor połączeń
Name:		connmon
Version:	0.13.0
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	http://www.student.lu.se/~nbi98oli/src/%{name}-%{version}.tar.gz
# Source0-md5:	b898f86769eb44ad6847bfa8f0a379f7
URL:		http://www.student.lu.se/~nbi98oli/
BuildRequires:	adns-devel
BuildRequires:	bison
BuildRequires:	gtk+-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Connection Monitor is a connection and bandwidth monitoring program
with a console-based user interface. It displays a list of open TCP
and UDP connections with transfer rate (in bytes per second) for each
connection. This requires a linux 2.4 kernel with Netfilter connection
tracking facilities. A small patch (included with ConnMon) is
necessary to get the transfer rates displayed.

%description -l pl.UTF-8
Connection Monitor to program monitorujący połączenia i przepustowość
z konsolowym interfejsem użytkownika. Wyświetla listę otwartych
połączeń TCP i UDP wraz z prędkością przesyłu danych (w bajtach na
sekundę) dla każdego połączenia. Wymaga jądra 2.4 z możliwościami
śledzenia połączeń w Netfilterze. Potrzebna jest mała łata (załączona
z programem), aby otrzymywać prędkości przesyłu danych.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="-DHAVE_CONFIG_H -Wall `gtk-config --cflags` -I/usr/include/ncurses -I../compat -I../libconnmon -I../libhpnl -I.. -I. %{rpmcflags}"

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
