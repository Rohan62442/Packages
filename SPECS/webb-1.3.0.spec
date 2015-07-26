Summary: Create & Manage Web Applications
Name: webb
Version: 1.3.0
Release: 1%{?dist}
License: GPLv3+
Group: Applications/Productivity
URL: http://rohan62442.github.io/webb/
Source0: https://github.com/Rohan62442/webb/archive/v%{version}.tar.gz
BuildArch: noarch
Requires: python3

%description
Webb is a script for managing web applications based on GNOME's Epiphany web browser, which is now simply known as Web.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/share/%{name}
mkdir -p %{buildroot}/usr/bin
rm -rf %{buildroot}/usr/share/%{name}/*
cp -rf * %{buildroot}/usr/share/%{name}

%post
ln -s -t /usr/bin /usr/share/%{name}/%{name}

%files
%defattr(-,root,root)
%doc README.md COPYING CHANGELOG
%{_datadir}/%{name}


