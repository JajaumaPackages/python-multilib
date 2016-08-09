Name:       python-multilib
Version:    1.1
Release:    5%{?dist}
Summary:    A module for determining if a package is multilib or not
License:    GPLv2
URL:        https://github.com/Zyzyx/%{name}
Source0:    https://github.com/Zyzyx/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Summary:        Python library for determining if a package is multilib enabled

Provides:  python2-multilib = %{version}-%{release}

%description
A Python module that supports several multilib "methods" useful for determining \
if a 32-bit package should be included with its 64-bit analogue in a compose.

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
# testing requires complete composes available locally, which no buildsystem
# would ever want included in a build root

%files
%license LICENSE
%doc README.md
%{python_sitelib}/*
%config(noreplace) %{_sysconfdir}/multilib.conf

%changelog
* Tue Aug 09 2016 Dennis Gilmore <dennis@ausil.us> - 1.1-5
- add provides python2-multilib

* Mon May 10 2016 Jay Greguske <jgregusk@redhat.com> - 1.1-4
- EPEL 7 related changes to packaging

* Thu Apr 07 2016 Dennis Gilmore <dennis@ausil.us> - 1.1-2
- setup to make python3 down the road.
- spec and srpm named python-multilib
- fix license

* Tue Jul 21 2009 Jay Greguske <jgregusk@redhat.com> - 1.1-1
- consider dependencies in multilib testing
- fix a couple import errors

* Tue Jul 21 2009 Jay Greguske <jgregusk@redhat.com> - 1.0-1
- Initial RPM release
