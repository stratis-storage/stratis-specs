%global oname stratis-cli

Name:           stratis
License:        ASL 2.0
Group:          System Environment/Libraries
Summary:        A command-line tool for interacting with the Stratis daemon
Version:        0.0.4
Release:        2%{?dist}
URL:            https://github.com/stratis-storage/%{oname}/
Source:         https://github.com/stratis-storage/%{oname}/archive/GIT-TAG/%{oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel python3-setuptools asciidoc
Requires: python3-dbus-client-gen python3-dbus-client-gen-dbus-python stratisd

%description
stratis provides a command-line interface (CLI) for
interacting with the Stratis daemon, stratisd. stratis
interacts with stratisd via D-Bus.

%prep
%autosetup -n %{oname}-%{version}

%build
%{__python3} setup.py build
cd docs
make

%install
%{__python3} setup.py install --skip-build --root %{buildroot}
install -D -m 644 docs/%{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8

%files
%{python3_sitelib}/*
%{_bindir}/stratis
%{_mandir}/man8/%{name}.8*
%doc README.rst
%license LICENSE

%changelog
* Fri Oct 27 2017 Andy Grover <agrover@redhat.com> - 0.0.4-2
- Add stratisd as a Requires

* Fri Oct 27 2017 Andy Grover <agrover@redhat.com> - 0.0.4-1
- New upstream release

* Thu Sep 28 2017 Andy Grover <agrover@redhat.com> - 0.0.3-1
- New upstream release

* Mon Apr 3 2017 Andy Grover <agrover@redhat.com> - 0.0.2-1
- New upstream release

* Tue Mar 14 2017 Andy Grover <agrover@redhat.com> - 0.0.1-2
- Initial packaging
