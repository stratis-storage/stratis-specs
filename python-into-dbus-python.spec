%global oname into-dbus-python

Name:           python3-into-dbus-python
License:        ASL 2.0
Group:          System Environment/Libraries
Summary:        A transformer to dbus-python types
Version:        0.06
Release:        1%{?dist}
URL:            https://github.com/stratis-storage/%{oname}/
Source:         https://github.com/stratis-storage/%{oname}/archive/GIT-TAG/%{oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel python3-setuptools
Requires: python3-dbus-signature-pyparsing

%description
Facilities for converting an object that inhabits core Python
types, e.g., lists, ints, dicts, to an object that inhabits
dbus-python types, e.g., dbus.Array, dbus.UInt32, dbus.Dictionary
based on a specified dbus signature.

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
* Tue Mar 14 2017 Andy Grover <agrover@redhat.com> - 0.06-1
- Initial packaging
