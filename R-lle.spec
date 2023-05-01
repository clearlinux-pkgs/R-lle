#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lle
Version  : 1.1
Release  : 46
URL      : https://cran.r-project.org/src/contrib/lle_1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lle_1.1.tar.gz
Summary  : Locally linear embedding
Group    : Development/Tools
License  : GPL-3.0
Requires: R-scatterplot3d
Requires: R-snowfall
BuildRequires : R-scatterplot3d
BuildRequires : R-snowfall
BuildRequires : buildreq-R

%description
data into a lower dimensional (intrinsic) space. This package
        provides the main functions to performs the LLE alogrithm
        including some enhancements like subset selection, calculation
        of the intrinsic dimension etc.

%prep
%setup -q -c -n lle
cd %{_builddir}/lle

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641047656

%install
export SOURCE_DATE_EPOCH=1641047656
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lle
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lle
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lle
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc lle || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lle/DESCRIPTION
/usr/lib64/R/library/lle/INDEX
/usr/lib64/R/library/lle/Meta/Rd.rds
/usr/lib64/R/library/lle/Meta/data.rds
/usr/lib64/R/library/lle/Meta/demo.rds
/usr/lib64/R/library/lle/Meta/features.rds
/usr/lib64/R/library/lle/Meta/hsearch.rds
/usr/lib64/R/library/lle/Meta/links.rds
/usr/lib64/R/library/lle/Meta/nsInfo.rds
/usr/lib64/R/library/lle/Meta/package.rds
/usr/lib64/R/library/lle/NAMESPACE
/usr/lib64/R/library/lle/R/lle
/usr/lib64/R/library/lle/R/lle.rdb
/usr/lib64/R/library/lle/R/lle.rdx
/usr/lib64/R/library/lle/data/lle_scurve_data.rda
/usr/lib64/R/library/lle/data/lle_wave.rda
/usr/lib64/R/library/lle/demo/lle.R
/usr/lib64/R/library/lle/help/AnIndex
/usr/lib64/R/library/lle/help/aliases.rds
/usr/lib64/R/library/lle/help/figures/rect.png
/usr/lib64/R/library/lle/help/lle.rdb
/usr/lib64/R/library/lle/help/lle.rdx
/usr/lib64/R/library/lle/help/paths.rds
/usr/lib64/R/library/lle/html/00Index.html
/usr/lib64/R/library/lle/html/R.css
