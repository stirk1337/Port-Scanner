%global lowname port_scanner
%global upname port-scanner

Name:           %{upname}
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
%autosetup -n %{upname}

%build
%py3_build


%install
%py3_install


%files -n %{upname}
%doc README.md
%{python3_sitelib}/%{upname}
%{python3_sitelib}/%{lowname}-%{version}-py3.10.egg-info/

%changelog
* Fri Jun 03 2022 stirk
- Create port scanner