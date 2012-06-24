Summary:	Connection Monitor
Summary(pl):	Monitor po��cze�
Name:		connmon
Version:	0.8.0
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://www.student.lu.se/~nbi98oli/src/%{name}-%{version}.tar.gz
URL:		http://www.student.lu.se/~nbi98oli/
BuildRequires:	adns-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Connection Monitor is a connection and bandwidth monitoring program
with a console-based user interface. It displays a list of open TCP
and UDP connections with transfer rate (in bytes per second) for each
connection. This requires a linux 2.4 kernel with Netfilter connection
tracking facilities. A small patch (included with ConnMon) is
necessary to get the transfer rates displayed.

%description -l pl
Connection Monitor to program monitoruj�cy po��czenia i przepustowo��
z konsolowym interfejsem u�ytkownika. Wy�wietla list� odwartych
po��cze� TCP i UDP wraz z pr�dko�ci� przesy�u danych (w bajtach na
sekund�) dla ka�dego po��czenia. Wymaga j�dra 2.4 z mo�liwo�ciami
�ledzenia po��cze� w Netfilterze. Potrzebna jest ma�a �ata (za��czona
z programem), aby otrzymywa� pr�dko�ci przesy�u danych.

%prep
%setup -q

%build
%{__make} CFLAGS="-DHAVE_CONFIG_H -Wall -I../compat -I../libconnmon -I../libhpnl -I.. -I. %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install src/connmon/connmon $RPM_BUILD_ROOT%{_sbindir}

gzip -9nf ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz kernel
%attr(755,root,root) %{_sbindir}/*
