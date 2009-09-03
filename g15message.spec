Name:                   g15message
Version:                1.0.0
Release:                %mkrel 4
Summary:                Simple message/alert tool for g15daemon and the Logitech G15
License:                GPL
Group:                  System/Configuration/Hardware
URL:                    http://g15daemon.sourceforge.net/
Source0:                http://downloads.sourceforge.net/g15daemon/g15message-%{version}.tar.bz2
BuildRequires:          g15-devel
BuildRequires:          g15daemon_client-devel
BuildRequires:          g15render-devel
BuildRequires:          X11-devel
BuildRoot:              %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A simple message/alert tool for g15daemon and the Logitech G15.
By default (with no additional options) it will display the text on the
commandline for 5seconds, then exit.

Requires libg15render devel package to compile.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} -r %{buildroot}%{_docdir}

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%defattr(-,root,root,0755)
%{_bindir}/g15message
