Summary:	Connection Monitor
Name:		connmon
Version:	0.8.0
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://www.student.lu.se/~nbi98oli/src/%{name}-%{version}.tar.gz
URL:		http://www.student.lu.se/~nbi98oli/
Requires:	adns-devel
Requires:	ncurses-devel >= 5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Connection Monitor is a connection and bandwidth monitoring program
with a console-based user interface. It displays a list of open TCP
and UDP connections with transfer rate (in bytes per second) for each
connection. This requires a linux 2.4 kernel with Netfilter connection
tracking facilities. A small patch (included with ConnMon) is
necessary to get the transfer rates displayed.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install src/connmon/connmon $RPM_BUILD_ROOT%{_sbindir}

gzip -9nf ChangeLog NEWS README TODO
%clean
rm -rf "${RPM_BUILD_ROOT}"

%files
%defattr(644,root,root,755)
%doc *.gz kernel
%attr(755,root,root) %{_sbindir}/*
