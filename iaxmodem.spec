Summary:	IAX software fax modem
Summary(pl.UTF-8):	Programowy faxmodem komunikujący się za pomocą protokołu IAX
Name:		iaxmodem
Version:	1.2.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/iaxmodem/%{name}-%{version}.tar.gz
# Source0-md5:	f8b26cfeed188e5c1dcbc5ae5ef923b3
Source2:	%{name}.init
Source3:	%{name}-sysconfig
Source4:	%{name}.ttyIAX
URL:		http://iaxmodem.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires(post,preun):   /sbin/chkconfig

%description
IAXmodem is a software modem written in C that uses an IAX channel
(commonly provided by an Asterisk PBX system) instead of a traditional
phone line and uses a DSP library instead of DSP hardware chipsets.

%description -l pl.UTF-8
IAXmodem jest programowym faxmodemem, napisanym w języku C, który
używa protokołu IAX (zwykle udostępnianego przez centralę Asterisk) i
bibliotekę DSP zamiast sprzętowych chipsetów DSP.

%prep
%setup -q

%build
./build static

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir} \
	$RPM_BUILD_ROOT{/etc/{rc.d/init.d,sysconfig},%{_sysconfdir}/%{name}} \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT/var/log/%{name}

install %{name} $RPM_BUILD_ROOT%{_sbindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/ttyIAX
touch $RPM_BUILD_ROOT/var/log/%{name}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "Please check your new iax entry in /etc/iaxmodem/ttyIAX is correct."
/sbin/chkconfig --add iaxmodem
%service iaxmodem restart

%preun
%service iaxmodem stop
/sbin/chkconfig --del iaxmodem

%files
%defattr(644,root,root,755)
%doc TODO README FAQ CHANGES *.ttyIAX
%attr(755,root,root) %{_sbindir}/*
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_mandir}/man1/*
%dir /var/log/%{name}
%ghost /var/log/%{name}/%{name}
