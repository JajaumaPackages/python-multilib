Name:       python-multilib
Version:    1.2
Release:    4%{?dist}
Summary:    A module for determining if a package is multilib or not
Group:      Development/Libraries
License:    GPLv2
URL:        https://pagure.io/releng/python-multilib
Source0:    https://releases.pagure.org/releng/python-multilib/%{name}-%{version}.tar.bz2

BuildArch:  noarch


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
%if 0%{?fedora}
BuildRequires:  python2-setuptools
BuildRequires:  python2-six
Requires:       python2-six
%else
BuildRequires:  python-setuptools
BuildRequires:  python-six
Requires:       python-six
%endif
Requires:       python2
Requires:       %{name}-conf = %{version}-%{release}

%description -n python2-multilib %{_description}

%if 0%{?fedora}
%package -n python%{python3_pkgversion}-multilib
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-multilib}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}
Requires:       %{name}-conf = %{version}-%{release}

%description -n python%{python3_pkgversion}-multilib %{_description}
%endif


%prep
%setup -q

%build
%py2_build
%{?fedora:%py3_build}

%install
%py2_install
%{?fedora:%py3_install}

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

%if 0%{?fedora}
%files -n python%{python3_pkgversion}-multilib
%license LICENSE
%doc README.md
%{python3_sitelib}/*
%endif

%changelog
* Fri Oct 13 2017 Jajauma's Packages <jajauma@yandex.ru> - 1.2-4
- Skip python3 on RHEL

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 20 2017 Lubomír Sedlář <lsedlar@redhat.com> - 1.2-2
- Update requires for epel builds

* Thu Mar 02 2017 Lubomír Sedlář <lsedlar@redhat.com> - 1.2-1
- New upstream version with support for DNF package objects
- Updated URL to point to new upstream on Pagure.io

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1-7
- Rebuild for Python 3.6

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
