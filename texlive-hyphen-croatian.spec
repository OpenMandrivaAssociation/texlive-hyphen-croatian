Name:		texlive-hyphen-croatian
Version:	58652
Release:	2
Summary:	Croatian hyphenation patterns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/hrhyph.tex
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-croatian.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Croatian in T1/EC and UTF-8 encodings.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-croatian
%_texmf_language_def_d/hyphen-croatian
%_texmf_language_lua_d/hyphen-croatian
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-croatian <<EOF
\%% from hyphen-croatian:
croatian loadhyph-hr.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-croatian
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-croatian <<EOF
\%% from hyphen-croatian:
\addlanguage{croatian}{loadhyph-hr.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-croatian
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-croatian <<EOF
-- from hyphen-croatian:
	['croatian'] = {
		loader = 'loadhyph-hr.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-hr.pat.txt',
		hyphenation = '',
	},
EOF
