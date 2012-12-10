%global packname  RGtk2
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.20.21
Release:          1
Summary:          R bindings for Gtk 2.8.0 and above
Group:            Sciences/Mathematics
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    gtk2-devel	 
BuildRequires:    pkgconfig(libglade-2.0)
%rename R-cran-RGtk2

%description
Facilities in the R language for programming graphical interfaces using
Gtk, the Gimp Tool Kit.

%prep
%setup -q -c -n %{packname}

%build

%install
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


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.20.21-1
+ Revision: 775070
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.20.19-1
+ Revision: 774756
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Thu Jan 28 2010 Frederik Himpe <fhimpe@mandriva.org> 2.12.17-1mdv2010.1
+ Revision: 497690
- Really update to 2.12.17
- update to new version 2.12.17

* Sun Jul 19 2009 Frederik Himpe <fhimpe@mandriva.org> 2.12.15-1mdv2010.0
+ Revision: 397445
- Update to new version 2.12.15

* Sun Aug 10 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.12.5.3-1mdv2009.0
+ Revision: 270295
- update to new version 2.12.5-3

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 2.12.2-6mdv2009.0
+ Revision: 260179
- rebuild
- rebuild

* Fri Feb 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.12.2-3mdv2008.1
+ Revision: 176955
- remove requires on libR.so

* Sun Feb 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.12.2-2mdv2008.1
+ Revision: 169428
- add missing buildrequires on libglade2-devel
- fix url

* Thu Feb 14 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.12.2-1mdv2008.1
+ Revision: 167240
- add source and spec file
- Created package structure for R-cran-RGtk2.

