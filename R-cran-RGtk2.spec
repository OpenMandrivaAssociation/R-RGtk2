%define modulename RGtk2
%define realver %{version}
%define r_library %{_libdir}/R/library
%define _requires_exceptions libR.so

Summary:	A GTK+ bindings for R
Name:		R-cran-%{modulename}
Version:	2.12.17
Release:	%mkrel 1
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
BuildRequires:	gtk2-devel
BuildRequires:	libglade2-devel
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
RGtk2 is a binding for R to the GTK2 library and dependent 
libraries. You can use it to construct arbitrarily complex GUI's from R.

%prep
%setup -q -c

%build

R CMD build %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# (tpg) install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# (tpg) provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
