Name:                   g15message
Version:                1.0.0
Release:                %mkrel 6
Summary:                Simple message/alert tool for g15daemon and the Logitech G15
License:                GPL
Group:                  System/Configuration/Hardware
URL:                    http://g15daemon.sourceforge.net/
Source0:                http://downloads.sourceforge.net/g15daemon/g15message-%{version}.tar.bz2
BuildRequires:		g15-devel
BuildRequires:          g15daemon_client-devel
BuildRequires:          g15render-devel
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


%changelog
* Thu Feb 03 2011 Funda Wang <fwang@mandriva.org> 1.0.0-6mdv2011.0
+ Revision: 635479
- x11 is not needed

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-5mdv2011.0
+ Revision: 618388
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0.0-4mdv2010.0
+ Revision: 428983
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-3mdv2009.0
+ Revision: 245590
- rebuild

* Fri Feb 08 2008 David Walluck <walluck@mandriva.org> 1.0.0-1mdv2008.1
+ Revision: 164308
- import g15message


