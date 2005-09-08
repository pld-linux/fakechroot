Summary:	Provides a fake chroot environment to programs
Name:		fakechroot
Version:	2.3
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.debian.org/debian/pool/main/f/fakechroot/%{name}_%{version}.tar.gz
# Source0-md5:	9df72412f6a209a63bdac02d3088d604
URL:		http://fakechroot.alioth.debian.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{_prefix}/%{_lib}/libfakechroot

%description
fakechroot provides a fake chroot environment to programs. A fake
chroot allows you to run programs which require root privileges on an
unprivileged user account. For example, you can create a Debian
bootstrap or a development environment and build packages inside a
chroot'ed system using a standard non-root user account. You can then
use the apt-get command to install other packages without root
privileges.

%prep
%setup -q

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}
%attr(755,root,root) %{_libdir}/libfakechroot.so
%{_mandir}/man1/*
