%global lowname port_scanner
%global upname port-scanner

Name:           python3-${upname}
Version:        1.0
Release:        1%{?dist}
Summary:        Port Scanner
BuildArch: 	noarch  

License:        MIT
URL:            https://github.com/stirk1337/%{upname}
Source0:        https://github.com/stirk1337/%{upname}/releases/download/%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Port Scanner

%prep
%autosetup -n port-scanner-%{version}

%build
%py3_build


%install
%py3_install


%files -n port-scanner
%doc README.md
%{python3_sitelib}/port-scanner
%{python3_sitelib}/port_scanner-1.0-py3.10.egg-info/

%changelog
* Fri Jun 03 2022 stirk
- Create port scanner
