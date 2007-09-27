Name:		iaxmodem
Version:	0.3.1
Release:	1
Summary:	IAX software fax modem
Summary(pl):	Programowy faxmodem komunikuj±cy siê za pomoc± protoko³u IAX
License:	GPL
Group:          Applications/System
URL:		http://iaxmodem.sourceforge.net

Source0:	http://downloads.sourceforge.net/iaxmodem/%{name}-%{version}.tar.gz
# Source0-md5:	de2d1ca6ed6e864ad50f92dfa0933772
Source2:	%{name}.init
Source3:	%{name}-sysconfig
Source4:	%{name}.ttyIAX

Patch0:		%{name}.as-needed.patch

BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IAXmodem is a software modem written in C that uses an IAX channel (commonly provided by an Asterisk PBX system) 
instead of a traditional phone line and uses a DSP library instead of DSP hardware chipsets. 

%description -l pl
IAXmodem jest programowym faxmodemem, napisanym w jêzyku C, który u¿ywa protoko³u IAX (zwykle udostêpnianego
przez centralê Asterisk) i bibliotekê DSP zamiast sprzêtowych chipsetów DSP

%prep
%setup -q
%patch0 -p0

%build
./build static

%install
rm -rf $RPM_BUILD_ROOT
install -d  ${RPM_BUILD_ROOT}%{_sbindir} \
    	    ${RPM_BUILD_ROOT}/etc/{rc.d/init.d,%{name},sysconfig} \
    	    ${RPM_BUILD_ROOT}%{_mandir}/man1 \
	    ${RPM_BUILD_ROOT}/var/log/%{name}

install %{name}    $RPM_BUILD_ROOT/%{_sbindir}
install %{name}.1  $RPM_BUILD_ROOT/%{_mandir}/man1/
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE4} $RPM_BUILD_ROOT/etc/%{name}/ttyIAX

touch $RPM_BUILD_ROOT/var/log/%{name}/%{name}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
/etc/rc.d/init.d/%{name}
%config(noreplace) %{_sysconfdir}/%name/*
/etc/sysconfig/%{name}
%dir /var/log/%{name}
%dir /etc/%{name}
%doc TODO README FAQ CHANGES *.ttyIAX

%ghost /var/log/%{name}/%{name}
