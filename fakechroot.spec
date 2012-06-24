Summary:	Provides a fake chroot environment to programs
Summary(pl):	Fa�szywe �rodowisko chroot dla program�w
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

%description -l pl
fakechroot udost�pnia fa�szywe �rodowisko chroot dla program�w.
Fa�szywy chroot umo�liwia uruchamianie program�w wymagaj�cych
uprawnie� roota ze zwyk�ego konta u�ytkownika. Mo�na na przyk�ad
tworzy� bootstrap Debiana lub �rodowisko programistyczne i budowa�
pakiety wewn�trz chrootowanego systemu przy u�yciu zwyk�ego konta.
Mo�na nast�pnie u�y� polecenia apt-get do zainstalowania innych
pakiet�w bez uprawnie� roota.

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

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/scripts
cp -a doc/[!M]* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -a scripts/[!M]* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/scripts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}
%attr(755,root,root) %{_libdir}/libfakechroot.so
%{_mandir}/man1/*
