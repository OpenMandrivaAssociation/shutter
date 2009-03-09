%define extraver ppa10
%define mdv_release %mkrel 0.%{extraver}.2

Summary:	Feature-rich screenshot application
Name:		gscrot
Version:	0.64
Release:	%{mdv_release}
License:	GPLV3
Group:		Development/Perl
URL:		http://shutter-project.org/
Source0:	https://launchpad.net/%7Egscrot-testing-team/+archive/+files/%{name}_%{version}~%{extraver}.orig.tar.gz
BuildArch:	noarch
Obsoletes:	gscrot <= 0.64-0.ppa10.2mdv2009.1
Requires:	libgoocanvas3
Requires:	perl-Goo-Canvas
Requires:	perl-Gnome2-Canvas
Requires:	perl-Gnome2-GConf
Requires:	perl-Gnome2-Wnck
Requires:	perl-WWW-Mechanize
Requires:	perl-X11-Protocol
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
GScrot is a feature-rich screenshot program. You can take a screenshot of a
specific area, window, your whole screen, or even of a website - apply different
effects to it, draw on it to highlight points, and then upload to an image
hosting site, all within one window.

%prep
%setup -q -n %{name}-%{version}.orig

%build

%check

%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}
install -d -m 0755 %{buildroot}/usr
mv bin %{buildroot}/usr
mv share %{buildroot}/usr
%find_lang %{name}
%find_lang %{name}-plugins-bash
cat %{name}-plugins-bash.lang >> %{name}.lang

%clean 
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc tools/gen_translation_bash.pl tools/gen_translation.pl tools/to_translate tools/to_translate_bash
%attr(755,root,root) %{_bindir}/gscrot
%{_datadir}/gscrot/*
%{_datadir}/applications/gscrot.desktop
%{_datadir}/pixmaps/gscrot.svg
%{_mandir}/man1/*

