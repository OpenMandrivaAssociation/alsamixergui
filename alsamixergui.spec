%define beta	rc1_5
%define fbeta	rc1-2

Summary:	Advanced Linux Sound Architecture (ALSA) graphical mixer
Name:		alsamixergui
Version:	0.9.0
Release:	%mkrel 0.14%{beta}.1
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
Patch6:		alsamixergui-0.9.0rc1-2-mdv-fix-str-fmt.patch
BuildRequires:	kernel-headers >= 2.4.0
BuildRequires:	libalsa-devel >= %{version}
BuildRequires:	fltk-devel >= 1.1
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
%patch6 -p1 -b .strfmt

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

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
Categories=Audio;Mixer;
EOF

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
