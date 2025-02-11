%global packname  RGtk2
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.20.27
Release:          2
Summary:          R bindings for Gtk 2.8.0 and above
Group:            Sciences/Mathematics
License:          GPL
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/RGtk2_2.20.27.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    gtk2-devel	 
BuildRequires:    pkgconfig(libglade-2.0)
%rename R-cran-RGtk2

%define Werror_cflags %{nil}

%description
Facilities in the R language for programming graphical interfaces using
Gtk, the Gimp Tool Kit.

%prep
export CFLAGS="%{optflags} -Wno-format-security"
%setup -q -c -n %{packname}

%build

%install
export CFLAGS="%{optflags} -Wno-format-security"
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/ui
