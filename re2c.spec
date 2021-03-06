#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : re2c
Version  : 2.1.1
Release  : 14
URL      : https://github.com/skvadrik/re2c/releases/download/2.1.1/re2c-2.1.1.tar.xz
Source0  : https://github.com/skvadrik/re2c/releases/download/2.1.1/re2c-2.1.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Public-Domain
Requires: re2c-bin = %{version}-%{release}
Requires: re2c-data = %{version}-%{release}
Requires: re2c-license = %{version}-%{release}
Requires: re2c-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-golang

%description
The following benchmarks have been taken from the Kleenex repository
(https://github.com/diku-kmc/kleenexlang) and are licensed under the MIT
license (together with the data generators):

%package bin
Summary: bin components for the re2c package.
Group: Binaries
Requires: re2c-data = %{version}-%{release}
Requires: re2c-license = %{version}-%{release}

%description bin
bin components for the re2c package.


%package data
Summary: data components for the re2c package.
Group: Data

%description data
data components for the re2c package.


%package license
Summary: license components for the re2c package.
Group: Default

%description license
license components for the re2c package.


%package man
Summary: man components for the re2c package.
Group: Default

%description man
man components for the re2c package.


%prep
%setup -q -n re2c-2.1.1
cd %{_builddir}/re2c-2.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617057863
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1617057863
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/re2c
cp %{_builddir}/re2c-2.1.1/LICENSE %{buildroot}/usr/share/package-licenses/re2c/4bc5a5deebfea79e0d2d5b428a6bfd9a6d239959
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/re2c
/usr/bin/re2go

%files data
%defattr(-,root,root,-)
/usr/share/re2c/stdlib/unicode_categories.re

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/re2c/4bc5a5deebfea79e0d2d5b428a6bfd9a6d239959

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/re2c.1
/usr/share/man/man1/re2go.1
