%define beta	rc1_3
%define fbeta	rc1-2

Summary:	Advanced Linux Sound Architecture (ALSA) graphical mixer
Name:		alsamixergui
Version:	0.9.0
Release:	%mkrel 0.11%{beta}
License:	GPL
Group:		Sound
URL:		http://www.iua.upf.es/~mdeboer/projects/alsamixergui/
Source0:	ftp://www.iua.upf.es/pub/mdeboer/projects/alsamixergui/%{name}-%{version}%{fbeta}.tar.bz2
Patch0:		alsamixergui-0.9.0rc1-fixes.patch
Patch1:		alsamixer-0.9.0rc1-2-fltk.patch
Patch2:		alsamixer-0.9.0rc1-2-fltk2.patch
Patch3:		alsamixergui-0.9.0rc1-memleak.patch
Patch4:		alsamisergui-fix-compile-gcc-3.4.patch
Patch5:		alsamixergui-0.9.0rc1-lock.patch
BuildRequires:	XFree86-devel
BuildRequires:	kernel-headers >= 2.4.0
BuildRequires:	libalsa-devel >= %{version}
BuildRequires:	libslang-devel
BuildRequires:	fltk-devel >= 1.1
Requires:	kernel >= 2.4.18
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Alsamixergui is a FLTK based frontend for alsamixer. It is written
directly on top of the alsamixer source, leaving the original source
intact, only adding a couple of ifdefs, and some calls to the gui
part, so it provides exactly the same functionality, but with a 
graphical userinterface.

%prep

%setup -q -n %{name}-%{version}%{fbeta}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1 -b .fix_gcc_3.4
%patch5 -p0

%build
autoconf
%configure
%make all

%install
rm -rf %{buildroot}

%makeinstall

# MDK menu entry
mkdir -p %{buildroot}%{_menudir}
cat << EOF > %{buildroot}%{_menudir}/%{name}
?package(%{name}): \
command="%{name}" \
icon="sound_section.png" \
section="Multimedia/Sound" \
title="AlsaMixerGUI" \
longtitle="ALSA \
connection mixer" \
needs="x11"
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/%{name}
%{_menudir}/%{name}

