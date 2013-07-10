%define		module oursql
Summary:	Set of MySQL bindings for python 2.4+
Summary(pl.UTF-8):	Zestaw dowiązań do MySQLa dla Pythona
Name:		python-%{module}
Version:	0.9.3.1
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/o/%{module}/%{module}-%{version}.tar.bz2
# Source0-md5:	5ffab98306dbc5328ed1c436b85bfbe9
URL:		http://launchpad.net/oursql/
BuildRequires:	mysql-devel
BuildRequires:	python-Cython
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
oursql is a set of MySQL bindings for python 2.4+ with a focus on
wrapping the `MYSQL_STMT API`__ to provide real parameterization and
real server-side cursors. MySQL 4.1.2 or better is required.

Python 2.x version.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py \
	install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYING README
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.egg-info
