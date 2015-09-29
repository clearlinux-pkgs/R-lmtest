#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lmtest
Version  : 0.9
Release  : 15
URL      : http://cran.r-project.org/src/contrib/lmtest_0.9-33.tar.gz
Source0  : http://cran.r-project.org/src/contrib/lmtest_0.9-33.tar.gz
Summary  : Testing Linear Regression Models
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-zoo
BuildRequires : R-zoo
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n lmtest

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library lmtest
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library lmtest


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lmtest/CITATION
/usr/lib64/R/library/lmtest/DESCRIPTION
/usr/lib64/R/library/lmtest/INDEX
/usr/lib64/R/library/lmtest/Meta/Rd.rds
/usr/lib64/R/library/lmtest/Meta/data.rds
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
/usr/lib64/R/library/lmtest/libs/lmtest.so
/usr/lib64/R/library/lmtest/libs/symbols.rds
