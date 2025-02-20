%define beta	rc1_5
%define fbeta	rc1-2

Summary:	Advanced Linux Sound Architecture (ALSA) graphical mixer
Name:		alsamixergui
Version:	0.9.0
Release:	0.14%{beta}.3
License:	GPL
Group:		Sound
URL:		https://www.iua.upf.es/~mdeboer/projects/alsamixergui/
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


%changelog
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 0.9.0-0.14rc1_5.1mdv2011.0
+ Revision: 634997
- rebuild
- tighten BR

* Mon Jan 18 2010 Jérôme Brenier <incubusss@mandriva.org> 0.9.0-0.14rc1_5mdv2011.0
+ Revision: 493232
- rebuild for new fltk
- fix str fmt

* Sun Dec 07 2008 Thierry Vignaud <tv@mandriva.org> 0.9.0-0.14rc1_4mdv2009.1
+ Revision: 311681
- rebuild for new fltk

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.9.0-0.13rc1_4mdv2009.0
+ Revision: 218429
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 16 2008 Thierry Vignaud <tv@mandriva.org> 0.9.0-0.13rc1_4mdv2008.1
+ Revision: 153719
- remove useless kernel require
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 10 2007 Funda Wang <fwang@mandriva.org> 0.9.0-0.12rc1_4mdv2008.1
+ Revision: 116837
- drop old menu

  + Thierry Vignaud <tv@mandriva.org>
    - buildrequires X11-devel instead of XFree86-devel

* Wed May 23 2007 Christiaan Welvaart <spturtle@mandriva.org> 0.9.0-0.12rc1_3mdv2008.0
+ Revision: 30393
- sync with 0.9.0-0.12rc1_3mdv2007.1 src rpm
  o add xdg menu stuff


* Fri Sep 29 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-0.11rc1_3
- sync with mille-xterm

* Mon Dec 13 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.0-0.10rc1_3mdk
- rebuild
- spec cosmetics
- do parallell build

* Wed Jun 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9.0-0.9rc1_3mdk
- Rebuild

