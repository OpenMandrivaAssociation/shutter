Summary:	Feature-rich screenshot application
Name:		shutter
Version:	0.94.3
Release:	1
License:	GPLv3
Group:		Graphical desktop/GNOME
URL:		http://shutter-project.org/
Source0:	http://shutter-project.org/wp-content/uploads/releases/tars/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	gettext
%rename gscrot

%description
Shutter is a feature-rich screenshot program. You can take a screenshot of a
specific area, window, your whole screen, or even of a website - apply
different effects to it, draw on it to highlight points, and then upload
to an image hosting site, all within one window.

%prep
%setup -q

%build

%install
install -d -m 0755 %{buildroot}
install -d -m 0755 %{buildroot}/%{_prefix}
cp -a bin %{buildroot}/%{_prefix}
cp -a share %{buildroot}/%{_prefix}
%find_lang %{name}
%find_lang %{name}-upload-plugins
%find_lang %{name}-plugins
cat %{name}-upload-plugins.lang >> %{name}.lang
cat %{name}-plugins.lang >> %{name}.lang

%files -f %{name}.lang
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/shutter
%{_datadir}/shutter/*
%{_datadir}/applications/shutter.desktop
%{_mandir}/man1/*
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/HighContrast/*/apps/*
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_iconsdir}/ubuntu-mono-light/scalable/apps/
%{_iconsdir}/ubuntu-mono-dark/scalable/apps/
%{_iconsdir}/ubuntu-mono-light/*/apps/*.png
%{_iconsdir}/ubuntu-mono-dark/*/apps/*.png
%{_datadir}/pixmaps/%{name}.png
%doc README


%changelog
* Sat Dec  8 2012 Arkady L. Shane <ashejn@rosalab.ru> 0.89.1-1
- update to 0.89.1

* Thu May 10 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.88.3-1
+ Revision: 797874
- update to 0.88.3

* Sun Feb 26 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.88.2-1
+ Revision: 780932
- update to 0.88.2
- specfile cleanup

* Mon Dec 12 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.88.1-1
+ Revision: 740490
- version update 0.88.1

  + Jon Dill <dillj@mandriva.org>
    - update to 0.87.3

  + Sandro Cazzaniga <kharec@mandriva.org>
    - update to 0.86.2

* Fri Apr 16 2010 Frederik Himpe <fhimpe@mandriva.org> 0.86.1-1mdv2010.1
+ Revision: 535584
- update to new version 0.86.1

* Sun Apr 04 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.86-1mdv2010.1
+ Revision: 531233
- update to 0.86

* Thu Dec 10 2009 Frederik Himpe <fhimpe@mandriva.org> 0.85.1-1mdv2010.1
+ Revision: 476133
- Update to new version 0.85.1

* Fri Nov 20 2009 Frederik Himpe <fhimpe@mandriva.org> 0.85-1mdv2010.1
+ Revision: 467760
- Update to new version 0.85
- Make mo creation script not fail if directory for a certain locale
  does not exist yet

* Sun Oct 04 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.80.1-3mdv2010.0
+ Revision: 453267
- Make sure i18n files are uptodate (#53496).

* Sat Oct 03 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.80.1-2mdv2010.0
+ Revision: 453236
- Suggests perl-Image-Magic (optional, only some plugins require it)
  Closes #53496

* Fri Aug 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0.80.1-1mdv2010.0
+ Revision: 411308
- Update to new version 0.80.1

* Thu Jul 09 2009 Frederik Himpe <fhimpe@mandriva.org> 0.80-1mdv2010.0
+ Revision: 394010
- Update to new version 0.80

* Tue Mar 17 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.70.1-0.ppa2.3mdv2009.1
+ Revision: 356637
- Remove own copy of perl-* modules provided by other packages, issue
  reported by Frederic Crozat.

* Thu Mar 12 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.70.1-0.ppa2.2mdv2009.1
+ Revision: 354274
- Suggests gnome-web-photo (optional, enables screenshots of websites
  feature).

* Wed Mar 11 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.70.1-0.ppa2.1mdv2009.1
+ Revision: 353965
- Updated to version 0.70.1-0.ppa2
- Removed requires for libgoocanvas, already required by perl-Goo-Canvas
- Replaced Requires for perl-Goo-Canvas by Suggests, it is optional
  (drawing tool disabled if not installed).
- Suggests perl-Gtk2-ImageView (optional, advanced seletion disabled if
  not installed).

* Wed Mar 11 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.70-0.ppa11.3mdv2009.1
+ Revision: 353900
- Change Group tag from "Development/Perl" to "Graphical desktop/GNOME",
  reported by Greg Harris.

* Wed Mar 11 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.70-0.ppa11.2mdv2009.1
+ Revision: 353864
- shutter must require libgoocanvas, not libgoocanvas3 (x86_64 lib64
  prefix), reported by Olivier Blin.

* Mon Mar 09 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.70-0.ppa11.1mdv2009.1
+ Revision: 353230
- Updated to version 0.70-0.ppa11
- Finish rename gscrot->shutter on spec.
- Split requires entries by line.
- Update shutter homepage URL entry.
- Obsolete current gscrot version in Mandriva cooker (gscrot renamed to
  shutter).
- Rename spec file (gscrot renamed to shutter).
- gscrot was renamed to shutter, change svn entry.

* Sat Jan 17 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.64-0.ppa10.2mdv2009.1
+ Revision: 330438
- Rebuild for fixed package changelog.

* Fri Jan 16 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.64-0.ppa10.1mdv2009.1
+ Revision: 330174
- Fix summary ended with dot.
- Line break description.
- Import gscrot package, made/sent by Ednilson Miura.

