%global oname dbus-signature-pyparsing

Name:           python3-dbus-signature-pyparsing
License:        ASL 2.0
Group:          System Environment/Libraries
Summary:        A D-Bus signature parser generated using the pyparsing library
Version:        0.03
Release:        1%{?dist}
URL:            https://github.com/stratis-storage/%{oname}/
Source:         https://github.com/stratis-storage/%{oname}/archive/GIT-TAG/%{oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel python3-setuptools
Requires: python3-pyparsing

%description
A D-Bus signature parser generated using the pyparsing library.

%prep
%autosetup -n %{oname}-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}

%files
%{python3_sitelib}/*
%doc README.rst
%license LICENSE

%changelog
* Tue Mar 14 2017 Andy Grover <agrover@redhat.com> - 0.03-1
- Initial packaging
