#specfile originally created for Fedora, modified for Moblin Linux
Name: MAKEDEV
Version: 3.24
Release: 1
Group: System/Base
License: GPLv2
# This is a Red Hat maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
Source: MAKEDEV-%{version}-1.tar.gz
Summary: A program used for creating device files in /dev
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL: http://www.lanana.org/docs/device-list/
Requires(pre): shadow-utils, /usr/bin/getent

%description
This package contains the MAKEDEV program, which makes it easier to create
and maintain the files in the /dev directory.  /dev directory files
correspond to a particular device supported by Linux (serial or printer
ports, scanners, sound cards, tape drives, CD-ROM drives, hard drives,
etc.) and interface with the drivers in the kernel.

You should install the MAKEDEV package because the MAKEDEV utility makes
it easy to manage the /dev directory device files.

%prep
%setup -q

%build
make OPTFLAGS="$RPM_OPT_FLAGS" 

%install
make install DESTDIR=$RPM_BUILD_ROOT devdir=/dev makedevdir=/sbin
rm -f $RPM_BUILD_ROOT/dev/MAKEDEV

%clean
rm -fr $RPM_BUILD_ROOT

%pre
# Add the floppy group and the vcsa user.
getent group floppy >/dev/null || groupadd -g 19 -r floppy
getent passwd vcsa >/dev/null || \
useradd -r -d /dev -s /sbin/nologin -u 69 \
    -c "virtual console memory owner" vcsa
exit 0

%files
%defattr(-,root,root)
%doc COPYING devices-2.6+.txt
%doc %{_mandir}/man8/*
%{_sbindir}/mksock
/sbin/MAKEDEV
%config(noreplace) %{_sysconfdir}/makedev.d
%exclude /etc/makedev.d/01ia64
%exclude /etc/makedev.d/01ibcs
%exclude /etc/makedev.d/01cdrom
%exclude /etc/makedev.d/01ftape
%exclude /etc/makedev.d/01ide
%exclude /etc/makedev.d/01ipfilter
%exclude /etc/makedev.d/01isdn
%exclude /etc/makedev.d/01linux1394
%exclude /etc/makedev.d/01mouse
%exclude /etc/makedev.d/01qic
%exclude /etc/makedev.d/01raid
%exclude /etc/makedev.d/01s390
%exclude /etc/makedev.d/01sound
%exclude /etc/makedev.d/01v4l
%exclude /etc/makedev.d/02cciss
%exclude /etc/makedev.d/02dac960
%exclude /etc/makedev.d/02ida 
