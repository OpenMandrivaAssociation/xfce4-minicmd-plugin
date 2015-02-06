Summary:	Minicmd plugin for the Xfce panel
Name:		xfce4-minicmd-plugin
Version:	0.4.0
Release:	12
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://xfce4-goodies.berlios.de
Source0:	%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	pkgconfig(libxfcegui4-1.0)
Obsoletes:	xfce-minicmd-plugin

%description
Minicmd panel plugin for the Xfce Desktop Environment.

It displays a mini-command line on the Xfce panel. It uses
the same history file as xfrun4. Use <Up> and <Down> to scroll
through history. <Enter> executes the command and <Ctrl>-<Enter>
executes the command in a terminal.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*


%changelog
* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-11mdv2010.1
+ Revision: 543429
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.4.0-10mdv2010.0
+ Revision: 446060
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-9mdv2009.1
+ Revision: 349470
- rebuild for xfce-4.6.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-8mdv2009.1
+ Revision: 294999
- rebuild for new Xfce4.6 beta1

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-7mdv2009.0
+ Revision: 262362
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-6mdv2009.0
+ Revision: 256874
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-4mdv2008.1
+ Revision: 110122
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING
- use upstream name

* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-3mdv2008.0
+ Revision: 33224
- spec file clean

