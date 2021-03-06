Name:           stratisd
License:        MPL 2.0
Group:          System Environment/Libraries
Summary:        A daemon that manages block devices to create filesystems
Version:        0.1.4
Release:        1%{?dist}
URL:            https://github.com/stratis-storage/{%name}/
Source:         https://github.com/stratis-storage/%{name}/archive/GIT-TAG/%{name}-%{version}.tar.gz
Patch0:         stratisd-customize-release-profile.diff
BuildRequires:  rust cargo dbus-devel systemd-devel

%description
A daemon that manages block devices to create filesystems.

%prep
%autosetup -n %{name}-%{version}

%build
cargo build --release

%install
install -D -m 755 target/release/stratisd %{buildroot}%{_bindir}/stratisd
install -D -m 644 stratisd.conf %{buildroot}%{_sysconfdir}/dbus-1/system.d/stratisd.conf

%files
%{_bindir}/stratisd
%{_sysconfdir}/dbus-1/system.d/stratisd.conf
%doc README.md
%license LICENSE

%changelog
* Mon Dec 18 2017 Andy Grover <agrover@redhat.com> - 0.1.4-1
- New upstream release

* Tue Oct 31 2017 Andy Grover <agrover@redhat.com> - 0.1.2-1
- New upstream release

* Fri Sep 29 2017 Andy Grover <agrover@redhat.com> - 0.1.1-1
- New upstream release

* Wed Aug 2 2017 Andy Grover <agrover@redhat.com> - 0.1.0-1
- New upstream release

* Wed Apr 19 2017 Andy Grover <agrover@redhat.com> - 0.0.3-1
- New upstream release
- Put stratisd.conf in correct spot since system bus in use now

* Tue Mar 14 2017 Andy Grover <agrover@redhat.com> - 0.0.2-2
- Initial packaging
