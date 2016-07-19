Name:       python-multilib
Version:    1.1
Release:    6%{?dist}
Summary:    A module for determining if a package is multilib or not
Group:      Development/Libraries
License:    GPLv2
URL:        https://github.com/Zyzyx/%{name}/
Source0:    https://github.com/Zyzyx/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:  noarch
Patch01:     001-python-six.patch


%global _description \
A Python module that supports several multilib "methods" useful for \
determining if a 32-bit package should be included with its 64-bit analogue \
in a compose.

%description %{_description}

%package conf
Summary:        Configuration files for %{name}

%description conf
This package provides the configuration files for %{name}.

%package -n python2-multilib
Summary:        %{summary}
%{?python_provide:%python_provide python2-multilib}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-six
Requires:       python2-six
Requires:       python2
Requires:       %{name}-conf = %{version}-%{release}

%description -n python2-multilib %{_description}

%package -n python3-multilib
Summary:        %{summary}
%{?python_provide:%python_provide python3-multilib}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
Requires:       python3-six
Requires:       python3
Requires:       %{name}-conf = %{version}-%{release}

%description -n python3-multilib %{_description}


%prep
%setup -q
%patch01 -p1

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
# testing requires complete composes available locally, which no buildsystem
# would ever want included in a build root
#{__python2} setup.py test
#{__python3} setup.py test

%files conf
%config(noreplace) %{_sysconfdir}/multilib.conf

%files -n python2-multilib
%license LICENSE
%doc README.md
%{python2_sitelib}/*

%files -n python3-multilib
%license LICENSE
%doc README.md
%{python3_sitelib}/*


%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 Jay Greguske <jgregusk@redhat.com> - 1.1-5
- Package up for Fedora rawhide

* Sun May 01 2016 Neal Gompa <ngompa13@gmail.com> - 1.1-3
- Port to Python 3 and enable its subpackage
- Split config file to its own subpackage

* Thu Apr 07 2016 Dennis Gilmore <dennis@ausil.us> - 1.1-2
- setup to make python3 down the road.
- spec and srpm named python-multilib
- fix license

* Tue Jul 21 2009 Jay Greguske <jgregusk@redhat.com> - 1.1-1
- consider dependencies in multilib testing
- fix a couple import errors

* Tue Jul 21 2009 Jay Greguske <jgregusk@redhat.com> - 1.0-1
- Initial RPM release
