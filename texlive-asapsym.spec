Name:		texlive-asapsym
Version:	40201
Release:	1
Summary:	Using the free ASAP Symbol font with LaTeX and Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/asapsym
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asapsym.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asapsym.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asapsym.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros (usable with LaTeX or Plain TeX)
for using the freely available ASAP Symbol font, which is also
included. The font is distributed in OpenType format, and makes
extensive use of OpenType features. Therefore, at this time,
only XeTeX and LuaTeX are supported. An error message is issued
if an OTF-capable engine is not detected.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/asapsym
%{_texmfdistdir}/tex/plain/asapsym
%{_texmfdistdir}/tex/latex/asapsym
%{_texmfdistdir}/tex/generic/asapsym
%{_texmfdistdir}/fonts/opentype/omnibus-type/asapsym
%doc %{_texmfdistdir}/doc/fonts/asapsym

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
