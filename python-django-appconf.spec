%global pypi_name django-appconf

Name:           python-%{pypi_name}
Version:        0.5
Release:        1
Summary:        A helper class for handling configuration defaults of packaged apps gracefully
Group:		Development/Python

License:        BSD
URL:            https://pypi.python.org/pypi/django-appconf/0.5
Source0:        http://pypi.python.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-sphinx

Requires:   python-django

%description
A helper class for handling configuration
defaults of packaged Django
apps gracefully.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# generate html docs 
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc html README.rst LICENSE
%{python_sitelib}/appconf
%{python_sitelib}/django_appconf-%{version}-py?.?.egg-info
