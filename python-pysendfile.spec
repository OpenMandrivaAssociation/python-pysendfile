%define pypi_name pysendfile

Name:           python-pysendfile
Version:        2.0.1
Release:        %mkrel 3
Summary:        Python interface to the sendfile(2) system call
Group:          Development/Python

License:        MIT
URL:            https://github.com/giampaolo/pysendfile
Source0:        https://github.com/giampaolo/pysendfile/archive/release-%{version}/%{pypi_name}-release-%{version}.tar.gz

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools

%description
sendfile(2) is a system call which provides a "zero-copy" way of copying data
from one file descriptor to another (a socket). The phrase "zero-copy" refers
to the fact that all of the copying of data between the two descriptors is done
entirely by the kernel, with no copying of data into user-space buffers. This is
particularly useful when sending a file over a socket (e.g. FTP).

%package -n python3-%{pypi_name}
Summary:        Python interface to the sendfile(2) system call
Group:          Development/Python
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
sendfile(2) is a system call which provides a "zero-copy" way of copying data
from one file descriptor to another (a socket). The phrase "zero-copy" refers
to the fact that all of the copying of data between the two descriptors is done
entirely by the kernel, with no copying of data into user-space buffers. This is
particularly useful when sending a file over a socket (e.g. FTP).

%prep
%setup -q -n %{pypi_name}-release-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH="%{buildroot}%{python3_sitearch}" %{__python3} test/test_sendfile.py

%files -n python3-%{pypi_name}
%doc README.rst HISTORY.rst
%license LICENSE
%{python3_sitearch}/sendfile*.so
%{python3_sitearch}/pysendfile-%{version}-py?.?.egg-info
