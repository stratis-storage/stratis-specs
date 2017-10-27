%global oname dbus-client-gen

Name:           python3-dbus-client-gen
License:        ASL 2.0
Group:          System Environment/Libraries
Summary:        Generates classes and methods useful to a D-Bus client
Version:        0.2
Release:        4%{?dist}
URL:            https://github.com/stratis-storage/%{oname}/
Source:         https://github.com/stratis-storage/%{oname}/archive/GIT-TAG/%{oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel python3-setuptools

%description
Thi library generates classes and methods useful to a D-Bus client. This
package contains code not dependent on the particular Python D-Bus library
being used, such as dbus-python or gdbus.

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
* Fri Oct 27 2017 Andy Grover <agrover@redhat.com> - 0.2-4
- Initial packaging
