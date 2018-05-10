#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : re2c
Version  : 1.0.3
Release  : 4
URL      : https://github.com/skvadrik/re2c/releases/download/1.0.3/re2c-1.0.3.tar.gz
Source0  : https://github.com/skvadrik/re2c/releases/download/1.0.3/re2c-1.0.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Public-Domain
Requires: re2c-bin
Requires: re2c-doc
BuildRequires : bison

%description
re2c
--------------------------------------------------------------------------------

%package bin
Summary: bin components for the re2c package.
Group: Binaries

%description bin
bin components for the re2c package.


%package doc
Summary: doc components for the re2c package.
Group: Documentation

%description doc
doc components for the re2c package.


%prep
%setup -q -n re2c-1.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1510234918
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1510234918
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/re2c

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
