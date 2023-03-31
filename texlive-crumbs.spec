Name:		texlive-crumbs
Version:	64602
Release:	2
Summary:	Add a Navigation Path to the page header
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/crumbs
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crumbs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crumbs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crumbs.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package adds a navigation path ("breadcrumb trail") at the
header of a presentation, just like some websites do in order
to simplify navigation.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/crumbs
%{_texmfdistdir}/tex/latex/crumbs
%doc %{_texmfdistdir}/doc/latex/crumbs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
