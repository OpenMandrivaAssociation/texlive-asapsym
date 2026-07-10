%global tl_name asapsym
%global tl_revision 40201

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Using the free ASAP Symbol font with LaTeX and Plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/asapsym
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asapsym.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asapsym.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asapsym.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros (usable with LaTeX or Plain TeX) for using
the freely available ASAP Symbol font, which is also included. The font
is distributed in OpenType format, and makes extensive use of OpenType
features. Therefore, at this time, only XeTeX and LuaTeX are supported.
An error message is issued if an OTF-capable engine is not detected.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/opentype
%dir %{_datadir}/texmf-dist/source/fonts
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/tex/plain
%dir %{_datadir}/texmf-dist/doc/fonts/asapsym
%dir %{_datadir}/texmf-dist/fonts/opentype/omnibus-type
%dir %{_datadir}/texmf-dist/source/fonts/asapsym
%dir %{_datadir}/texmf-dist/tex/generic/asapsym
%dir %{_datadir}/texmf-dist/tex/latex/asapsym
%dir %{_datadir}/texmf-dist/tex/plain/asapsym
%dir %{_datadir}/texmf-dist/fonts/opentype/omnibus-type/asapsym
%doc %{_datadir}/texmf-dist/doc/fonts/asapsym/README.md
%doc %{_datadir}/texmf-dist/doc/fonts/asapsym/asapsym.pdf
%{_datadir}/texmf-dist/fonts/opentype/omnibus-type/asapsym/Asap-Symbol.otf
%doc %{_datadir}/texmf-dist/source/fonts/asapsym/asapsym.dtx
%doc %{_datadir}/texmf-dist/source/fonts/asapsym/asapsym.ins
%{_datadir}/texmf-dist/tex/generic/asapsym/asapsym-generic.tex
%{_datadir}/texmf-dist/tex/latex/asapsym/asapsym.sty
%{_datadir}/texmf-dist/tex/plain/asapsym/asapsym.code.tex
