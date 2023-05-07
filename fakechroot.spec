Summary:	Provides a fake chroot environment to programs
Summary(pl.UTF-8):	Fałszywe środowisko chroot dla programów
Name:		fakechroot
Version:	2.20.1
Release:	1
License:	LGPL v2.1+
Group:		Development/Tools
Source0:	https://github.com/dex4er/fakechroot/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bf67c9b3a5f282f310ba8beda2fc6057
Patch0:		statx.patch
Patch1:		glibc-2.34.patch
BuildRequires:	perl-tools-pod
URL:		https://github.com/dex4er/fakechroot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fakechroot provides a fake chroot environment to programs. A fake
chroot allows you to run programs which require root privileges on an
unprivileged user account. For example, you can create a Debian
bootstrap or a development environment and build packages inside a
chroot'ed system using a standard non-root user account. You can then
use the apt-get command to install other packages without root
privileges.

%description -l pl.UTF-8
fakechroot udostępnia fałszywe środowisko chroot dla programów.
Fałszywy chroot umożliwia uruchamianie programów wymagających
uprawnień roota ze zwykłego konta użytkownika. Można na przykład
tworzyć bootstrap Debiana lub środowisko programistyczne i budować
pakiety wewnątrz chrootowanego systemu przy użyciu zwykłego konta.
Można następnie użyć polecenia apt-get do zainstalowania innych
pakietów bez uprawnień roota.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/fakechroot/libfakechroot.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS.md README.md THANKS.md scripts/*{.sh,.env,fakechroot,.pl}
%attr(755,root,root) %{_bindir}/env.fakechroot
%attr(755,root,root) %{_bindir}/fakechroot
%attr(755,root,root) %{_bindir}/ldd.fakechroot
%attr(755,root,root) %{_sbindir}/chroot.fakechroot
%dir %{_libdir}/fakechroot
%attr(755,root,root) %{_libdir}/fakechroot/libfakechroot.so
%{_mandir}/man1/fakechroot.1*
