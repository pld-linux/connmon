%define name		connmon
%define version	0.6.0
%define release	1

%define prefix		/usr

Summary:			Connection Monitor
Name:				%{name}
Version:			%{version}
Release:			%{release}
Source:			%{name}-%{version}.tar.gz
URL:				http://www.student.lu.se/~nbi98oli/
Group:			System Environment/Networking
Packager:		Pascal Bleser <guru@linuxbe.org>
Copyright:		GPL
BuildRoot:		/var/tmp/build-%{name}-%{version}
Prefix:			%{prefix}
Requires:      ncurses >= 5.0, adns

%description
Connection Monitor is a connection and bandwidth monitoring program
with a console-based user interface. It displays a list of open TCP
and UDP connections with transfer rate (in bytes per second) for each
connection. This requires a linux 2.4 kernel with Netfilter
connection tracking facilities. A small patch (included with ConnMon)
is necessary to get the transfer rates displayed.

Author:
-------
    Oskar Liljeblad <oskar@osk.mine.nu>

%changelog
* Fri Nov 16 2001 Pascal Bleser <guru@linuxbe.org>
- first RPM

%prep
%setup -q

%build
make

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p "${RPM_BUILD_ROOT}%{prefix}/sbin"
install -s -m0755 src/connmon/connmon \
	 "${RPM_BUILD_ROOT}%{prefix}/sbin/"

%clean
rm -rf "${RPM_BUILD_ROOT}"

%files
%defattr(-,root,root)
%doc COPYING ChangeLog NEWS README TODO kernel
%{prefix}/sbin/*
