Name:           stratisd
License:        MPL 2.0
Group:          System Environment/Libraries
Summary:        A daemon that manages a block devices to create filesystems
Version:        0.0.2
Release:        2%{?dist}
URL:            https://github.com/stratis-storage/{%name}/
Source:         https://github.com/stratis-storage/%{name}/archive/GIT-TAG/%{name}-%{version}.tar.gz
BuildRequires:  rust cargo dbus-devel
#Requires:	dbus-libs

%description
A daemon that manages a block devices to create filesystems.

%prep
%autosetup -n %{name}-%{version}

%build
cargo build --release

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 target/release/stratisd %{buildroot}/%{_bindir}

%files
%{_bindir}/stratisd
%doc README.md
%license LICENSE

%changelog
* Tue Mar 14 2017 Andy Grover <agrover@redhat.com> - 0.0.2-2
- Initial packaging
