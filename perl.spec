%define		perlver 5.005
%define		perlrel 61
%define		perlthread -thread

Summary:	Practical Extraction and Report Language
Summary(de):	Praktische Extraktions- und Berichtsprache 
Summary(fr):	Practical Extraction and Report Language (Perl)
Summary(pl):	Practical Extraction and Report Language (Perl)
Summary(tr):	Kabuk yorumlama dili
Name:		perl
Version:	%{perlver}_%{perlrel}
Release:	0.1
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Source:		ftp://ftp.perl.org/pub/perl/CPAN/src/5.0/%{name}%{version}.tar.gz
Patch0:		perl-noroot_install.patch
Patch1:		perl-DESTDIR.patch
URL:		http://www.perl.org/
Requires:	csh
Buildroot:	/tmp/%{name}-%{version}-root

%description
Perl is an interpreted language optimized for scanning arbitrary text
files, extracting information from those text files, and printing reports
based on that information.  It's also a good language for many system
management tasks.  The language is intended to be practical (easy to use,
efficient, complete) rather than beautiful (tiny, elegant, minimal).

This version has support for threads compiled in.

%description -l de
Perl ist eine Interpreter-Sprache, die zum Durchsuchen beliebiger Text-
dateien, Extrahieren von Informationen aus diesen Dateien und Drucken von
auf diesen Informationen basierenden Berichten optimiert ist. Die Sprache
eignet sich außerdem für viele Systemverwaltungsaufgaben. Sie ist eher 
praktisch (einfache Anwendung,effizient, vollständig) als schön (winzig,
elegant, minimal).

%description -l fr
Perl est un langage interprété, optimisé pour filtrer des fichiers texte,
extraire des informations de ces fichiers, et imprimer des rapports basés
sur ces informations. C'est aussi un bon langage pour de nombreuses procédures
de gestion système. Ce langage se veut pratique (simple à utiliser, efficace,
complet) autant qu'agréable (conscrit, élégant, minimal).

%description -l pl
Perl jest jêzykiem przeznaczonym do skanowania plików tekstowych, wyci±gania
z nich informacji i drukowania raportu bazuj±cego na tych informacjach. Jest
równie¿ doskona³ym jêzykiem dla wielu narzêdzi do nadzoru systemu. Jêzyk ten
jest w zamierzeniu praktycznym (³atwym w u¿yciu, efektywnym, kompletnym) 
bardziej ni¿ piêkny ;) (skromny, elegancki, minimalny).

%description -l tr
Perl, metin dosyalarýný taramak, bu metin dosyalarýndan bilgi çýkarmak ve
bu bilgiye dayalý raporlar hazýrlamak icin geliþtirilmiþ bir yorumlamalý
dildir. Ayrýca pek çok sistem yönetimi görevleri için de yararlý yetenekleri
vardýr. Perl, güzel (ufak, zarif, minimum) olmaktan çok, pratik olmaya
yönelik (kullanýmý kolay, verimli, eksiksiz) olarak tasarlanmýþtýr.

%package -n sperl
Summary:	Practical Extraction and Report Language (SUID root binary)
Summary(pl):	Practical Extraction and Report Language (SUID root binaria)
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Requires:	%{name} = %{version}

%description -n sperl
Practical Extraction and Report Language (SUID root binary).

%description -n sperl -l pl
Practical Extraction and Report Language (SUID root binaria).

%prep
%setup  -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1

%build
# this is gross
cat > config.over <<EOF
installprefix=$RPM_BUILD_ROOT%{_prefix}
test -d \$installprefix || mkdir \$installprefix
test -d \$installprefix/bin || mkdir \$installprefix/bin
installarchlib=\`echo \$installarchlib | sed "s!\$prefix!\$installprefix!"\`
installbin=\`echo \$installbin | sed "s!\$prefix!\$installprefix!"\`
installman1dir=\`echo \$installman1dir | sed "s!\$prefix!\$installprefix!"\`
installman3dir=\`echo \$installman3dir | sed "s!\$prefix!\$installprefix!"\`
installprivlib=\`echo \$installprivlib | sed "s!\$prefix!\$installprefix!"\`
installscript=\`echo \$installscript | sed "s!\$prefix!\$installprefix!"\`
installsitelib=\`echo \$installsitelib | sed "s!\$prefix!\$installprefix!"\`
installsitearch=\`echo \$installsitearch | sed "s!\$prefix!\$installprefix!"\`
EOF

sh Configure \
	-des \
	-Dcc=gcc \
	-Darchname=%{_target_platform} \
	-Dprefix=%{_prefix} \
	-Dman1dir=%{_mandir}/man1 \
	-Dman3dir=%{_mandir}/man3 \
	-Dman3ext=3pm \
	-Doptimize="$RPM_OPT_FLAGS" \
	-Duseshrplib \
	-Dusethreads \
	-Dd_dosuid \
	-Ud_setresuid \
	-Ud_setresgid 

make

# Strip binaries (done now rather than at install)

strip {perl,suidperl,x2p/a2p}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

make install
install utils/pl2pm $RPM_BUILD_ROOT%{_bindir}/pl2pm

(cd %{_includedir} ;
LD_LIBRARY_PATH="%{_builddir}/%{name}%{perlver}_%{perlrel}" \
PERL5LIB=$RPM_BUILD_ROOT%{_libdir}/perl5 $RPM_BUILD_ROOT%{_bindir}/perl \
$RPM_BUILD_ROOT%{_libdir}/perl5/%{perlver}%{perlrel}/%{_target_platform}%{perlthread} \
$RPM_BUILD_ROOT%{_bindir}/h2ph \
-d $RPM_BUILD_ROOT%{_libdir}/perl5/%{_target_platform}/%{perlver}%{perlrel}/ \
*.h sys/*.h linux/*.h asm/*.h net/*.h netinet/*.h arpa/*.h )

( cd $RPM_BUILD_ROOT%{_libdir}/perl5/%{perlver}%{perlrel}/%{_target_platform}%{perlthread}/

mv .packlist .packlist.old
sed "s|$RPM_BUILD_ROOT||g" < .packlist.old > .packlist
rm -f .packlist.old

mv Config.pm Config.pm.old
sed "s|$RPM_BUILD_ROOT||g" < Config.pm.old > Config.pm
rm -f Config.pm.old )

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man*/* \
	README Change*

find $RPM_BUILD_ROOT%{_libdir}/perl5 -name \*.so -exec strip --strip-unneeded {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz Change*

%attr(755,root,root) %{_bindir}/a2p
%attr(755,root,root) %{_bindir}/c2ph
%attr(755,root,root) %{_bindir}/dprofpp
%attr(755,root,root) %{_bindir}/find2perl
%attr(755,root,root) %{_bindir}/h2ph
%attr(755,root,root) %{_bindir}/h2xs
%attr(755,root,root) %{_bindir}/perl
%attr(755,root,root) %{_bindir}/perl%{perlver}%{perlrel}
%attr(755,root,root) %{_bindir}/perlbug
%attr(755,root,root) %{_bindir}/perlcc
%attr(755,root,root) %{_bindir}/perldoc
%attr(755,root,root) %{_bindir}/pl2pm
%attr(755,root,root) %{_bindir}/pod2html
%attr(755,root,root) %{_bindir}/pod2latex
%attr(755,root,root) %{_bindir}/pod2man
%attr(755,root,root) %{_bindir}/pod2text
%attr(755,root,root) %{_bindir}/pod2usage
%attr(755,root,root) %{_bindir}/podchecker
%attr(755,root,root) %{_bindir}/podselect
%attr(755,root,root) %{_bindir}/pstruct
%attr(755,root,root) %{_bindir}/s2p
%attr(755,root,root) %{_bindir}/splain

%dir %{_libdir}/perl5
%attr( - ,root,root) %{_libdir}/perl5/*
%dir %{_libdir}/site_perl
%attr( - ,root,root) %{_libdir}/site_perl/*
%{_mandir}/man[13]/*

%files -n sperl
%attr(4755,root,root) %{_bindir}/sperl%{perlver}%{perlrel}
%attr(4755,root,root) %{_bindir}/suidperl
