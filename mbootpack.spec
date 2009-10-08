Summary:	Turns a multiboot kernel and modules (eg Xen) into a single file
Name:		mbootpack
Version:	0.4a
Release:	%mkrel 5
License:	BSD 
Group:		System/Kernel and hardware
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.tjd.phlegethon.org/software/#mbootpack
Source:	http://www.tjd.phlegethon.org/software/%{name}-%{version}.tar.bz2
Patch0:	mbootpack-0.4a-fix-build-new-kernel-headers.patch
Patch1:	mbootpack-0.4a-x86_64-build-fix.patch

%description
This is a tool that takes a multiboot kernel and modules (e.g. a Xen VMM, linux
kernel and initrd), and packages them up as a single file that looks like a
bzImage linux kernel. The aim is to allow you to boot multiboot kernels (in
particular, Xen) using bootloaders that don't support multiboot (i.e. pretty
much anything except GRUB and SYSLINUX).

%prep
%setup -q
%patch0 -p1 -b .fix-build-new-kernel-headers
%patch1 -p1 -b .x86_64-build-fix

%build
CFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE"
%make

%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT/%_bindir
install -m 755 mbootpack $RPM_BUILD_ROOT/%_bindir/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_bindir}/*



