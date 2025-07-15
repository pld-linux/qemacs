#
%define		_cvs	cvs.20050713
#
Summary:	A small heavy featured editor
Summary(pl.UTF-8):	Mały, ciężko wyposażony edytor
Name:		qemacs
Version:	0.3.1
Release:	%{_cvs}.1
License:	LGPL
Group:		Applications/Editors
Source0:	http://ftp.debian.org/debian/pool/main/q/qemacs/%{name}_%{version}.%{_cvs}.orig.tar.gz
# Source0-md5:	c4c8feeb1076d5b5de76e0169a2b5661
# http://ftp.de.debian.org/debian/pool/main/q/qemacs/qemacs_0.3.1.cvs.20050713-5.diff.gz
Patch0:		%{name}-html2png-libpng.patch
Patch1:		%{name}-Makefile.patch
URL:		http://fabrice.bellard.free.fr/qemacs/
BuildRequires:	libpng-devel
#BuildRequires:	tons of xorgs-foo-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QEmacs (for Quick Emacs) is a very small but powerful editor with an
Emacs look and feel. Its features include:
 - "All" Emacs common features,
 - Works on any VT100 terminals without termcap,
 - X11 support, with multiple simultaneous proportional fonts. Xft
   extension supported for anti aliased font display.
 - Highly optimized handling of huge files,
 - Full UTF-8 support, including Unicode-conformant bidirectional
   editing, with Arabic and Indic scripts handling (in progress),
 - WYSIWYG HTML/XML/CSS2 mode graphical editing, with lynx-like
   rendering for VT100 terminals,
 - WYSIWYG DocBook mode based on XML/CSS2 renderer,
 - C mode with coloring with immediate update and emacs-like
   auto-indent,
 - Interactive-shell mode using colorized VT100 emulation,
 - Compile mode with next/prev error,
 - Input methods for most languages (from the Yudit editor) including
   Chinese,
 - X Input methods,
 - Hexadecimal editing mode with insertion and block commands,
 - Unicode hexa editing of UTF-8 files,
 - UTF-8 VT100 support with double width glyphs,
 - Small (full version is 150kB big).

%description -l pl.UTF-8
QEmacs (Quick Emacs) to bardzo mały, ale potężny edytor o zachowaniu
Emacsa. Jego możliwości obejmują:
 - "wszystkie" główne cechy Emacsa,
 - działanie na dowolnym terminalu VT100 bez termcapa,
 - obsługę X11 z wieloma jednoczesnymi fontami propocjonalnymi;
   obsługiwane jest rozszerzenie Xft dla antyaliasingu;
 - dobrze zoptymalizowaną obsługę dużych plików,
 - pełną obsługę UTF-8, w tym zgodną z Unikodem edycję dwukierunkową
   wraz z obsługą alfabetów arabskich i indyjskich (w trakcie rozwoju),
 - edycję WYSIWYG HTML-a/XML-a/CSS2 w trybie graficznym, z
   renderowaniem w stylu lynksa na terminalach VT100,
 - tryb WYSIWYG dla DocBooka oparty na renderingu XML/CSS2,
 - tryb C z kolorowaniem składni o natychmiastowym uaktualnianiu i
   automatycznymi wcięciami w stylu emacsa,
 - tryb interaktywnej powłoki wykorzystujący kolorową emulację VT100,
 - tryb kompilacji z przechodzeniem do następnego/poprzedniego błędu,
 - metody wprowadzania znaków dla większości języków (z edytora Yudit),
   w tym chińskiego,
 - metody wprowadzania znaków X Input
 - tryb edycji szesnastkowej z wstawianiem i poleceniami blokowymi,
 - szesnatkową edycję Unikodu w plikach UTF-8,
 - obsługę UTF-8 na VT100 ze znakami podwójnej szerokości,
 - niewielki rozmiar (pełna wersja ma 150kB).

%prep
%setup -q -n %{name}
%patch -P0 -p1
%patch -P1 -p1

%build
CFLAGS="%{rpmcflags}" \
%configure \
	--cc="%{__cc}" \
	--disable-x11 \
	--disable-xv \
	--disable-xrender \
	--disable-png

%{__make} -j1 \
	LDFLAGS="%{rpmldflags}"
mv -f qe qemacs-nox

CFLAGS="%{rpmcflags}" \
%configure \
	--cc="%{__cc}"

%{__make} -j1 \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/qemacs

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install qe.h config.h cutils.h display.h qestyles.h $RPM_BUILD_ROOT%{_includedir}/qemacs
install qemacs-nox $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/qe
%{_mandir}/man1/qemacs.1*
%dir %{_includedir}/qemacs
%{_includedir}/qemacs/*.h
