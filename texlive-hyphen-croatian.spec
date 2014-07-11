# revision 23085
# category TLCore
# catalog-ctan /language/hyphenation/hrhyph.tex
# catalog-date 2011-06-08 00:02:48 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-hyphen-croatian
Version:	20110608
Release:	9
Summary:	Croatian hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/hrhyph.tex
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-croatian.tar.xz
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
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


%changelog
* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110608-3
+ Revision: 767519
- Add workaround to rpm bug that broke hyphenation files
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110608-2
+ Revision: 759903
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110608-1
+ Revision: 718644
- texlive-hyphen-croatian
- texlive-hyphen-croatian
- texlive-hyphen-croatian
- texlive-hyphen-croatian

