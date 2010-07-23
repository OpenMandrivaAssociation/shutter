Summary:	Feature-rich screenshot application
Name:		shutter
Version:	0.86.2
Release:	%mkrel 1
License:	GPLv3
Group:		Graphical desktop/GNOME
URL:		http://shutter-project.org/
Source:		http://shutter-project.org/wp-content/uploads/releases/tars/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	gettext
Obsoletes:	gscrot <= 0.64-0.ppa10.2mdv2009.1
Requires:	perl-Gnome2-Canvas
Requires:	perl-Gnome2-GConf
Requires:	perl-Gnome2-Wnck
Requires:	perl-WWW-Mechanize
Requires:	perl-X11-Protocol
Suggests:	gnome-web-photo
Suggests:	perl-Goo-Canvas
Suggests:	perl-Gtk2-ImageView
Suggests:	perl-Image-Magick
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Shutter is a feature-rich screenshot program. You can take a screenshot of a
specific area, window, your whole screen, or even of a website - apply different
effects to it, draw on it to highlight points, and then upload to an image
hosting site, all within one window.

%prep
%setup -q -n %{name}-%{version}

# remove own copy of perl-* modules provided by other packages
rm -rf share/shutter/resources/modules/{File,Proc}

# remove unwanted files
rm -f share/app-install/desktop/shutter.desktop
rm -f share/app-install/icons/shutter.svg

%build
# the shipped .mo files aren't uptodate...
for tb in share/shutter/resources/po/*.tar.gz; do
	pname=`basename $tb .tar.gz`
	tar -zxf $tb -C share/shutter/resources/po
	for po in share/shutter/resources/po/$pname/*.po; do
		lang=`basename $po .po`
		if [ -d share/locale/$lang/LC_MESSAGES ]
		then
			rm -f share/locale/$lang/LC_MESSAGES/$pname.mo
		else
			mkdir -p share/locale/$lang/LC_MESSAGES/
		fi
		msgfmt $po -o share/locale/$lang/LC_MESSAGES/$pname.mo
	done
done
rm -rf share/shutter/resources/po

%check

%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}
install -d -m 0755 %{buildroot}/usr
mv bin %{buildroot}/usr
mv share %{buildroot}/usr
%find_lang %{name}
%find_lang %{name}-plugins
cat %{name}-plugins.lang >> %{name}.lang

%clean 
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/shutter
%{_datadir}/shutter/*
%{_datadir}/applications/shutter.desktop
%{_mandir}/man1/*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png
%exclude %{_docdir}/%{name}/COPYING
%doc README

