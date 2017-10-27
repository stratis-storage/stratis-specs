%global oname dbus-python-client-gen

Name:           python3-dbus-client-gen-dbus-python
License:        ASL 2.0
Group:          System Environment/Libraries
Summary:        dbus-client-gen support for dbus-python
Version:        0.4
Release:        2%{?dist}
URL:            https://github.com/stratis-storage/%{oname}/
Source:         https://github.com/stratis-storage/%{oname}/archive/GIT-TAG/%{oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel python3-setuptools
Requires:       dbus-python python3-into-dbus-python

%description
This library generates classes and methods useful to a D-Bus client. This
package contains code dependent on using the "dbus-python" Python D-Bus
library.

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
* Fri Oct 27 2017 Andy Grover <agrover@redhat.com> - 0.4-2
- Initial packaging
