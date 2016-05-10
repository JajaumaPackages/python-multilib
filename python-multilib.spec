Name:       python-multilib
Version:    1.1
Release:    4%{?dist}
Summary:    A module for determining if a package is multilib or not
License:    GPLv2
URL:        https://github.com/Zyzyx/%{name}
Source0:    https://github.com/Zyzyx/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

%global _description \
A Python module that supports several multilib "methods" useful for determining \
if a 32-bit package should be included with its 64-bit analogue in a compose.

%description %{_description}

%package -n python2-multilib
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-multilib}
%description -n python2-multilib %{_description}

%package -n python3-multilib
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-multilib}
%description -n python3-multilib %{_description}


%prep
%setup -q


%build
%py2_build
#py3_build

%install
%py2_install
#py3_install

%check
# testing requires complete composes available locally, which no buildsystem
# would ever want included in a build root
#{__python2} setup.py test
#{__python3} setup.py test

%files -n python2-multilib
%license LICENSE
%doc README.md
%{python2_sitelib}/*
%config(noreplace) %{_sysconfdir}/multilib.conf

#files -n python3-multilib
#license LICENSE
#doc README.md
#{python3_sitelib}/*

%changelog
* Thu Apr 07 2016 Dennis Gilmore <dennis@ausil.us> - 1.1-2
- setup to make python3 down the road.
- spec and srpm named python-multilib
- fix license

* Tue Jul 21 2009 Jay Greguske <jgregusk@redhat.com> - 1.1-1
- consider dependencies in multilib testing
- fix a couple import errors

* Tue Jul 21 2009 Jay Greguske <jgregusk@redhat.com> - 1.0-1
- Initial RPM release
