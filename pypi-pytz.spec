#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-pytz
Version  : 2023.3.post1
Release  : 112
URL      : https://files.pythonhosted.org/packages/69/4f/7bf883f12ad496ecc9514cd9e267b29a68b3e9629661a2bbc24f80eff168/pytz-2023.3.post1.tar.gz
Source0  : https://files.pythonhosted.org/packages/69/4f/7bf883f12ad496ecc9514cd9e267b29a68b3e9629661a2bbc24f80eff168/pytz-2023.3.post1.tar.gz
Summary  : World timezone definitions, modern and historical
Group    : Development/Tools
License  : MIT
Requires: pypi-pytz-license = %{version}-%{release}
Requires: pypi-pytz-python = %{version}-%{release}
Requires: pypi-pytz-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi-pytest
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
============================================

%package license
Summary: license components for the pypi-pytz package.
Group: Default

%description license
license components for the pypi-pytz package.


%package python
Summary: python components for the pypi-pytz package.
Group: Default
Requires: pypi-pytz-python3 = %{version}-%{release}

%description python
python components for the pypi-pytz package.


%package python3
Summary: python3 components for the pypi-pytz package.
Group: Default
Requires: python3-core
Provides: pypi(pytz)

%description python3
python3 components for the pypi-pytz package.


%prep
%setup -q -n pytz-2023.3.post1
cd %{_builddir}/pytz-2023.3.post1
pushd ..
cp -a pytz-2023.3.post1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695154493
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])")
pytest || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pytz
cp %{_builddir}/pytz-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pytz/a2641684130f5e32505fdc2a92ad836f0a13200a || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pytz/a2641684130f5e32505fdc2a92ad836f0a13200a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
