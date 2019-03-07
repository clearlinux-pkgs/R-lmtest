#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lmtest
Version  : 0.9.36
Release  : 59
URL      : https://cran.r-project.org/src/contrib/lmtest_0.9-36.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lmtest_0.9-36.tar.gz
Summary  : Testing Linear Regression Models
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-lmtest-lib
Requires: R-car
Requires: R-strucchange
Requires: R-zoo
BuildRequires : R-car
BuildRequires : R-strucchange
BuildRequires : R-zoo
BuildRequires : clr-R-helpers

%description
for diagnostic checking in linear regression models. Furthermore,
 some generic tools for inference in parametric models are provided.

%package lib
Summary: lib components for the R-lmtest package.
Group: Libraries

%description lib
lib components for the R-lmtest package.


%prep
%setup -q -c -n lmtest

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523314251

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523314251
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lmtest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lmtest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lmtest
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library lmtest|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lmtest/CITATION
/usr/lib64/R/library/lmtest/DESCRIPTION
/usr/lib64/R/library/lmtest/INDEX
/usr/lib64/R/library/lmtest/Meta/Rd.rds
/usr/lib64/R/library/lmtest/Meta/data.rds
/usr/lib64/R/library/lmtest/Meta/features.rds
/usr/lib64/R/library/lmtest/Meta/hsearch.rds
/usr/lib64/R/library/lmtest/Meta/links.rds
/usr/lib64/R/library/lmtest/Meta/nsInfo.rds
/usr/lib64/R/library/lmtest/Meta/package.rds
/usr/lib64/R/library/lmtest/Meta/vignette.rds
/usr/lib64/R/library/lmtest/NAMESPACE
/usr/lib64/R/library/lmtest/NEWS
/usr/lib64/R/library/lmtest/R/lmtest
/usr/lib64/R/library/lmtest/R/lmtest.rdb
/usr/lib64/R/library/lmtest/R/lmtest.rdx
/usr/lib64/R/library/lmtest/data/Rdata.rdb
/usr/lib64/R/library/lmtest/data/Rdata.rds
/usr/lib64/R/library/lmtest/data/Rdata.rdx
/usr/lib64/R/library/lmtest/doc/index.html
/usr/lib64/R/library/lmtest/doc/lmtest-intro.R
/usr/lib64/R/library/lmtest/doc/lmtest-intro.Rnw
/usr/lib64/R/library/lmtest/doc/lmtest-intro.pdf
/usr/lib64/R/library/lmtest/help/AnIndex
/usr/lib64/R/library/lmtest/help/aliases.rds
/usr/lib64/R/library/lmtest/help/lmtest.rdb
/usr/lib64/R/library/lmtest/help/lmtest.rdx
/usr/lib64/R/library/lmtest/help/paths.rds
/usr/lib64/R/library/lmtest/html/00Index.html
/usr/lib64/R/library/lmtest/html/R.css
/usr/lib64/R/library/lmtest/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lmtest/libs/lmtest.so
/usr/lib64/R/library/lmtest/libs/lmtest.so.avx2
/usr/lib64/R/library/lmtest/libs/lmtest.so.avx512
