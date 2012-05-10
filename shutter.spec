Summary:	Feature-rich screenshot application
Name:		shutter
Version:	0.88.3
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
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_iconsdir}/ubuntu-mono-light/scalable/apps/
%{_iconsdir}/ubuntu-mono-dark/scalable/apps/
%{_iconsdir}/ubuntu-mono-light/*/apps/*.png
%{_iconsdir}/ubuntu-mono-dark/*/apps/*.png
%{_datadir}/pixmaps/%{name}.png
%doc README
