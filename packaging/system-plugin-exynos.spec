###########################
# Default feature config. #
###########################
# SMACK
%define WITH_SMACK 1
%define WITH_BOOT_PARTITION 0

Name: system-plugin-exynos
Summary: system-plugin for exynos system
Version: 0.1.01
Release: 0
License: Apache License v2
Group: System/Base
ExclusiveArch: %arm
Source: %{name}-%{version}.tar.gz
Source1001: %{name}.manifest

BuildRequires: autoconf
BuildRequires: automake
%if %{WITH_SMACK}
BuildRequires: libacl-devel
BuildRequires: smack-devel
%endif

Requires: e2fsprogs
Requires: /bin/grep
Requires: /usr/bin/awk
Requires: psmisc
Requires: system-plugin-common
Requires(post): coreutils

%description
Startup files

%prep
%setup -q

%build
cp %{SOURCE1001} .

aclocal
automake --add-missing
autoconf
%configure \
        --prefix=%{_prefix} \
%if %{WITH_SMACK}
        --enable-smack \
%endif
%if %{WITH_BOOT_PARTITION}
        --enable-boot-partition \
%endif

make %{?_smp_mflags}

%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/license
cat LICENSE > $RPM_BUILD_ROOT%{_datadir}/license/%{name}

%post

%files
%defattr(-,root,root,-)
%{_datadir}/license/%{name}
%{_sysconfdir}/fstab
%{_bindir}/cpu-governor.sh
%{_libdir}/udev/rules.d/51-tizen-system-plugin.rules

# systemd service units
%{_libdir}/systemd/system/cpu-governor.service
%{_libdir}/systemd/system/default.target.wants/cpu-governor.service

# systemd mount units
%{_libdir}/systemd/system/usr-share-locale.mount
%{_libdir}/systemd/system/local-fs.target.wants/usr-share-locale.mount
%if %{WITH_BOOT_PARTITION}
%{_sysconfdir}/systemd/system/boot.mount
%{_sysconfdir}/systemd/system/local-fs.target.wants/boot.mount
%endif
%{_sysconfdir}/systemd/system/csa.mount
%{_sysconfdir}/systemd/system/local-fs.target.wants/csa.mount
%{_sysconfdir}/systemd/system/opt-system-csc.mount
%{_sysconfdir}/systemd/system/local-fs.target.wants/opt-system-csc.mount
%{_sysconfdir}/systemd/system/opt-usr.mount
%{_sysconfdir}/systemd/system/local-fs.target.wants/opt-usr.mount
%{_sysconfdir}/systemd/system/opt.mount
%{_sysconfdir}/systemd/system/local-fs.target.wants/opt.mount
%manifest %{name}.manifest

