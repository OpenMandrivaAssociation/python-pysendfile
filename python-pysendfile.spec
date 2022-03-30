%define pypi_name pysendfile

Name:           python-pysendfile
Version:        2.0.1
Release:        2
Summary:        Python interface to the sendfile(2) system call
Group:          Development/Python

License:        MIT
URL:            https://github.com/giampaolo/pysendfile
Source0:        https://github.com/giampaolo/pysendfile/archive/release-%{version}/%{pypi_name}-release-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools

%description
sendfile(2) is a system call which provides a "zero-copy" way of copying data
from one file descriptor to another (a socket). The phrase "zero-copy" refers
to the fact that all of the copying of data between the two descriptors is done
entirely by the kernel, with no copying of data into user-space buffers. This is
particularly useful when sending a file over a socket (e.g. FTP).

%prep
%setup -q -n %{pypi_name}-release-%{version}

%build
%py_build

%install
%py_install

%check
PYTHONPATH="%{buildroot}%{python_sitearch}" %{__python} test/test_sendfile.py

%files
%doc README.rst HISTORY.rst
%license LICENSE
%{python_sitearch}/sendfile*.so
%{python_sitearch}/pysendfile-%{version}-py*.*.egg-info
