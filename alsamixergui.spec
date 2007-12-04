%define beta	rc1_3
%define fbeta	rc1-2

Summary:	Advanced Linux Sound Architecture (ALSA) graphical mixer
Name:		alsamixergui
Version:	0.9.0
Release:	%mkrel 0.12%{beta}
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
BuildRequires:	X11-devel
BuildRequires:	kernel-headers >= 2.4.0
BuildRequires:	libalsa-devel >= %{version}
BuildRequires:	libslang-devel
BuildRequires:	fltk-devel >= 1.1
Requires:	kernel >= 2.4.18
%if %mdkversion >= 200700
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
%endif
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
needs="x11" \
xdg="true"
EOF

# XDG menu
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=AlsaMixerGUI
Comment=%{summary}
Exec=%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;Audio;Mixer;
EOF

%post
%update_menus
%if %mdkversion >= 200700
%update_desktop_database
%endif

%postun
%clean_menus
%if %mdkversion >= 200700
%clean_desktop_database
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/%{name}
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

