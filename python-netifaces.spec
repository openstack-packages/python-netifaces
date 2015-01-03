%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from %distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from %distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:           python-netifaces
Version:        0.10
Release:        1%{?dist}
Summary:        Python library to retrieve information about network interfaces

Group:          Development/Libraries
License:        MIT
URL:            http://alastairs-place.net/netifaces/
Source0:        http://alastairs-place.net/2007/03/netifaces/netifaces-0.5.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  python2-devel
BuildRequires:  python-setuptools-devel

Requires:       python2

%description
This package provides a cross platform API for getting address information
from network interfaces.


%prep
%setup -q -n netifaces-%{upstream_version}


%build
python setup.py build


%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT
chmod -x $RPM_BUILD_ROOT%{python_sitearch}/netifaces-*.egg-info/*


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{python_sitearch}/netifaces-*.egg-info/
%{python_sitearch}/netifaces.so

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 1 2011 Ryan Rix <ry@n.rix.si> 0.5-1
- Initial packaging effort
