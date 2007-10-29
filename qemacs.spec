#
%define		_cvs	cvs.20050713
#
Summary:	A small heavy featured editor
#Summary(pl.UTF-8):	-
Name:		qemacs
Version:	0.3.1
Release:	%{_cvs}.0.1
License:	LGPL
Group:		Applications/Editors
Source0:	http://ftp.de.debian.org/debian/pool/main/q/%{name}/%{name}_%{version}.%{_cvs}.orig.tar.gz
# http://ftp.de.debian.org/debian/pool/main/q/qemacs/qemacs_0.3.1.cvs.20050713-5.diff.gz
Patch0:		%{name}-html2png-libpng.patch
Patch1:		%{name}-Makefile.patch
URL:		http://fabrice.bellard.free.fr/qemacs/
BuildRequires:	libpng-devel
#BuildRequires:	tons of xorgs-foo-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QEmacs (for Quick Emacs) is a very small but powerful editor with an Emacs look and feel. Its features include: 
 * "All" Emacs common features,
 * Works on any VT100 terminals without termcap,
 * X11 support, with multiple simultaneous proportional fonts. Xft extension
   supported for anti aliased font display.
 * Highly optimized handling of huge files,
 * Full UTF8 support, including Unicode-conformant bidirectional editing,
   with Arabic and Indic scripts handling (in progress),
 * WYSIWYG HTML/XML/CSS2 mode graphical editing, with lynx-like rendering
   for VT100 terminals,
 * WYSIWYG DocBook mode based on XML/CSS2 renderer,
 * C mode with coloring with immediate update and emacs-like auto-indent,
 * Interactive-shell mode using colorized VT100 emulation,
 * Compile mode with next/prev error,
 * Input methods for most languages (from the Yudit editor) including Chinese,
 * X Input methods,
 * Hexadecimal editing mode with insertion and block commands,
 * Unicode hexa editing of UTF8 files,
 * UTF8 VT100 support with double width glyphs,
 * Small (full version is 150KB big).

#%description -l pl.UTF-8

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%configure \
	--cc="%{__cc}"

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
