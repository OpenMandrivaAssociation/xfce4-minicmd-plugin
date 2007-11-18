Summary:	Minicmd plugin for the Xfce panel
Name:		xfce-minicmd-plugin
Version:	0.4.0
Release:	%mkrel 3
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://xfce4-goodies.berlios.de
Source0:	xfce4-minicmd-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.3.0
BuildRequires:	xfce-panel-devel >= 4.3.0
BuildRequires:	perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Minicmd panel plugin for the Xfce Desktop Environment.

It displays a mini-command line on the Xfce panel. It uses
the same history file as xfrun4. Use <Up> and <Down> to scroll
through history. <Enter> executes the command and <Ctrl>-<Enter>
executes the command in a terminal.

%prep
%setup -qn xfce4-minicmd-plugin-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm %{buildroot}%{_libdir}/xfce4/panel-plugins/*.*a

%find_lang xfce4-minicmd

%clean
rm -rf %{buildroot}

%files -f xfce4-minicmd.lang
%defattr(-,root,root)
%doc README ChangeLog COPYING AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
