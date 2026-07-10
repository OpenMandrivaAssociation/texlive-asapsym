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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros (usable with LaTeX or Plain TeX) for using
the freely available ASAP Symbol font, which is also included. The font
is distributed in OpenType format, and makes extensive use of OpenType
features. Therefore, at this time, only XeTeX and LuaTeX are supported.
An error message is issued if an OTF-capable engine is not detected.

