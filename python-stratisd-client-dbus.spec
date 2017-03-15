%global oname stratisd-client-dbus

Name:           python3-stratisd-client-dbus
License:        ASL 2.0
Group:          System Environment/Libraries
Summary:        A wrapper for a stratisd D-Bus client
Version:        0.08
Release:        1%{?dist}
URL:            https://github.com/stratis-storage/%{oname}/
Source:         https://github.com/stratis-storage/%{oname}/archive/GIT-TAG/%{oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel python3-setuptools
Requires: python3-into-dbus-python

%description
This library is a simple wrapper for use by a client of the
stratisd D-Bus API. It is built on top of the dbus-python
library. It ensures that the values placed on the dbus by
the client conform to the expected types.

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
* Tue Mar 14 2017 Andy Grover <agrover@redhat.com> - 0.08-1
- Initial packaging
