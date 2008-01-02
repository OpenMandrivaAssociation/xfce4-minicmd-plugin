Summary:	Minicmd plugin for the Xfce panel
Name:		xfce4-minicmd-plugin
Version:	0.4.0
Release:	%mkrel 4
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://xfce4-goodies.berlios.de
Source0:	%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-minicmd-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Minicmd panel plugin for the Xfce Desktop Environment.

It displays a mini-command line on the Xfce panel. It uses
the same history file as xfrun4. Use <Up> and <Down> to scroll
through history. <Enter> executes the command and <Ctrl>-<Enter>
executes the command in a terminal.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm %{buildroot}%{_libdir}/xfce4/panel-plugins/*.*a

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
