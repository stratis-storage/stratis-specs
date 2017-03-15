%global oname stratis-cli

Name:           stratis
License:        ASL 2.0
Group:          System Environment/Libraries
Summary:        A command-line tool for interacting with the Stratis daemon
Version:        0.0.1
Release:        1%{?dist}
URL:            https://github.com/stratis-storage/%{oname}/
Source:         https://github.com/stratis-storage/%{oname}/archive/GIT-TAG/%{oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel python3-setuptools
Requires: python3-stratisd-client-dbus

%description
stratis provides a command-line interface (CLI) for
interacting with the Stratis daemon, stratisd. stratis
interacts with stratisd via D-Bus.

%prep
%autosetup -n %{oname}-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}

%files
%{python3_sitelib}/*
%{_bindir}/stratis
%doc README.rst
%license LICENSE

%changelog
* Tue Mar 14 2017 Andy Grover <agrover@redhat.com> - 0.0.1-1
- Initial packaging
