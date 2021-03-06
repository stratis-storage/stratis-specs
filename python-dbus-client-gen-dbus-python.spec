%global oname dbus-python-client-gen

Name:           python3-dbus-client-gen-dbus-python
License:        ASL 2.0
Group:          System Environment/Libraries
Summary:        dbus-client-gen support for dbus-python
Version:        0.5
Release:        2%{?dist}
URL:            https://github.com/stratis-storage/%{oname}/
Source:         https://github.com/stratis-storage/%{oname}/archive/GIT-TAG/%{oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel python3-setuptools
Requires:       python3-dbus python3-into-dbus-python

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
* Wed Jan 3 2018 Andy Grover <agrover@redhat.com> - 0.5-2
- Depend on python3-dbus instead of dbus-python

* Mon Dec 18 2017 Andy Grover <agrover@redhat.com> - 0.5-1
- New upstream version

* Fri Oct 27 2017 Andy Grover <agrover@redhat.com> - 0.4-2
- Initial packaging
