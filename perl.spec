%define		perlver 5.005
%define		perlrel 03
%define		perlthread -thread
%define 	__find_provides	%{_builddir}/%{name}%{version}/find-perl-provides
Summary:	Practical Extraction and Report Language
Summary(de):	Praktische Extraktions- und Berichtsprache 
Summary(fr):	Practical Extraction and Report Language (Perl)
Summary(pl):	Practical Extraction and Report Language (Perl)
Summary(tr):	Kabuk yorumlama dili
Name:		perl
Version:	%{perlver}_%{perlrel}
Release:	12
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narz�dzia/Tekst
Source:		ftp://ftp.perl.org/pub/perl/CPAN/src/5.0/%{name}%{version}.tar.gz
Patch0:		perl-noroot_install.patch
Patch1:		perl-DESTDIR.patch
Patch2:		perl-File-Spec-0.7.patch
Patch3:		perl-CPAN-1.50.patch
Patch4:		perl-find-provides.patch
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
eignet sich au�erdem f�r viele Systemverwaltungsaufgaben. Sie ist eher 
praktisch (einfache Anwendung,effizient, vollst�ndig) als sch�n (winzig,
elegant, minimal).

%description -l fr
Perl est un langage interpr�t�, optimis� pour filtrer des fichiers texte,
extraire des informations de ces fichiers, et imprimer des rapports bas�s
sur ces informations. C'est aussi un bon langage pour de nombreuses proc�dures
de gestion syst�me. Ce langage se veut pratique (simple � utiliser, efficace,
complet) autant qu'agr�able (conscrit, �l�gant, minimal).

%description -l pl
Perl jest j�zykiem przeznaczonym do skanowania plik�w tekstowych, wyci�gania
z nich informacji i drukowania raportu bazuj�cego na tych informacjach. Jest
r�wnie� doskona�ym j�zykiem dla wielu narz�dzi do nadzoru systemu. J�zyk ten
jest w zamierzeniu praktycznym (�atwym w u�yciu, efektywnym, kompletnym) 
bardziej ni� pi�kny ;) (skromny, elegancki, minimalny).

%description -l tr
Perl, metin dosyalar�n� taramak, bu metin dosyalar�ndan bilgi ��karmak ve
bu bilgiye dayal� raporlar haz�rlamak icin geli�tirilmi� bir yorumlamal�
dildir. Ayr�ca pek �ok sistem y�netimi g�revleri i�in de yararl� yetenekleri
vard�r. Perl, g�zel (ufak, zarif, minimum) olmaktan �ok, pratik olmaya
y�nelik (kullan�m� kolay, verimli, eksiksiz) olarak tasarlanm��t�r.

%package -n sperl
Summary:	Practical Extraction and Report Language (SUID root binary)
Summary(pl):	Practical Extraction and Report Language (SUID root binaria)
Group:		Utilities/Text
Group(pl):	Narz�dzia/Tekst
Requires:	%{name} = %{version}

%description -n sperl
Practical Extraction and Report Language (SUID root binary).

%description -n sperl -l pl
Practical Extraction and Report Language (SUID root binaria).

%prep
%setup  -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

for i in find-* ; do
  mv $i $i.old
  sed "s|FPPATH|%{_builddir}/%{name}%{version}|g" < $i.old > $i
  chmod 755 $i; rm -f $i.old
done

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
	-Dscriptdir=%{_bindir} \
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
%attr(755,root,root) %{_bindir}/pstruct
%attr(755,root,root) %{_bindir}/s2p
%attr(755,root,root) %{_bindir}/splain

%dir %{_libdir}/perl5
%attr( - ,root,root) %{_libdir}/perl5/*
#%dir %{_libdir}/site_perl
#%attr( - ,root,root) %{_libdir}/site_perl/*
%{_mandir}/man[13]/*

%files -n sperl
%attr(4755,root,root) %{_bindir}/sperl%{perlver}%{perlrel}
%attr(4755,root,root) %{_bindir}/suidperl
