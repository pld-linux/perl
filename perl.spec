%define		perlver 5.005
%define		perlrel 03
%define		perlthread -thread

Summary:	Practical Extraction and Report Language
Summary(de):	Praktische Extraktions- und Berichtsprache 
Summary(fr):	Practical Extraction and Report Language (Perl)
Summary(pl):	Practical Extraction and Report Language (Perl)
Summary(tr):	Kabuk yorumlama dili
Name:		perl
Version:	%{perlver}_%{perlrel}
Release:	3
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Source:		ftp://ftp.perl.org/pub/perl/CPAN/src/5.0/%{name}%{version}.tar.gz
Patch0:		perl-noroot_install.patch
Patch1:		perl-db1.patch
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

%package -n	sperl
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
installprefix=$RPM_BUILD_ROOT/usr
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
	-Darchname=%{_target} \
	-Dprefix=/usr \
	-Dman3dir=/usr/man/man3 \
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
install utils/pl2pm $RPM_BUILD_ROOT/usr/bin/pl2pm


(cd /usr/include ;
PERL5LIB=$RPM_BUILD_ROOT/usr/lib/perl5 $RPM_BUILD_ROOT/usr/bin/perl \
$RPM_BUILD_ROOT/usr/lib/perl5/%{perlver}%{perlrel}/${_target}%{perlthread} \
$RPM_BUILD_ROOT/usr/bin/h2ph \
-d $RPM_BUILD_ROOT/usr/lib/perl5/${_target}/%{perlver}%{perlrel}/ \
*.h sys/*.h linux/*.h asm/*.h net/*.h netinet/*.h arpa/*.h )

( cd $RPM_BUILD_ROOT/usr/lib/perl5/%{perlver}%{perlrel}/%{_target}%{perlthread}/

mv .packlist .packlist.old
sed "s|$RPM_BUILD_ROOT||g" < .packlist.old > .packlist
rm -f .packlist.old

mv Config.pm Config.pm.old
sed "s|$RPM_BUILD_ROOT||g" < Config.pm.old > Config.pm
rm -f Config.pm.old )

gzip -9fn $RPM_BUILD_ROOT/usr/man/man*/* \
	README Change*

find $RPM_BUILD_ROOT/usr/lib/perl5 -name \*.so -exec strip --strip-unneeded {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz Change*

%attr(755,root,root) /usr/bin/a2p
%attr(755,root,root) /usr/bin/c2ph
%attr(755,root,root) /usr/bin/find2perl
%attr(755,root,root) /usr/bin/h2ph
%attr(755,root,root) /usr/bin/h2xs
%attr(755,root,root) /usr/bin/perl
%attr(755,root,root) /usr/bin/perl%{perlver}%{perlrel}
%attr(755,root,root) /usr/bin/perlbug
%attr(755,root,root) /usr/bin/perlcc
%attr(755,root,root) /usr/bin/perldoc
%attr(755,root,root) /usr/bin/pl2pm
%attr(755,root,root) /usr/bin/pod2html
%attr(755,root,root) /usr/bin/pod2latex
%attr(755,root,root) /usr/bin/pod2man
%attr(755,root,root) /usr/bin/pod2text
%attr(755,root,root) /usr/bin/pstruct
%attr(755,root,root) /usr/bin/s2p
%attr(755,root,root) /usr/bin/splain

%dir /usr/lib/perl5
%attr( - ,root,root) /usr/lib/perl5/*
%attr(644,root,root) /usr/man/man[13]/*

%files -n sperl
%attr(4755,root,root) /usr/bin/sperl%{perlver}%{perlrel}
%attr(4755,root,root) /usr/bin/suidperl

%changelog
* Wed Apr 28 1999 Artur Frysiak <wiget@pld.org.pl>
  [5.005_03-3]
- added db1 patch from RH 6.0

* Tue Apr 20 1999 Artur Frysiak <wiget@pld.org.pl>
  [5.005_03-2]
- updated to 5.005_03
- changed source URL
- added -Dman3dir=/usr/man/man3 -Dman3ext=3pm -Duseshrplib to Configure
- corrected .packlist
- changed --strip-debug to --strip-unneeded
- gzipped %doc (instead bzipping2)
- commpiled on rpm 3

* Mon Oct 26 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [5.005_02-2]
- added using $RPM_OPT_FLAGS during compile,
- added stripping modules,
- added URL,
- added sperl subpackage with suid perl binaries.

* Tue Sep 15 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [5.005_02-1]
- updated to 5.005_02
  (based on Ian Macdonald <ianmacd@xs4all.nl> spec files),
- install -d instead mkdir -p,
- added %defattr, but It's still unable to build from non root's account,
- man3 subdirectory moved to /usr/man/man3,
- minor modifications of spec file.   

* Mon Jun 15 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [5.005_01-1]
- added pl translation,
- moved %changelog to end of spec,
- removed all old patches. 
- start at RH spec file.
