%define		__find_provides	%{_builddir}/%{name}-%{version}/find-perl-provides
%define		perlthread %{?_with_perl_threads:-thread-multi}
Summary:	Practical Extraction and Report Language (Perl)
Summary(de):	Praktische Extraktions- und Berichtsprache
Summary(pl):	Interpreter jÍzyka Perl (Practical Extraction and Report Language)
Summary(tr):	Kabuk yorumlama dili
Name:		perl
Version:	5.6.1
Release:	17
Epoch:		1
License:	GPL
Group:		Applications/Text
Group(cs):	Aplikace/Text
Group(da):	Programmer/Tekst
Group(de):	Applikationen/Text
Group(es):	Aplicaciones/Texto
Group(fr):	Applications/Texte
Group(is):	Forrit/Texti
Group(it):	Applicazioni/Testo
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•∆•≠•π•»
Group(no):	Applikasjoner/Tekst
Group(pl):	Aplikacje/Tekst
Group(pt):	AplicaÁıes/Texto
Group(ru):	“…Ãœ÷≈Œ…—/Ù≈À”‘œ◊Ÿ≈ ’‘…Ã…‘Ÿ
Group(sl):	Programi/Besedilo
Group(sv):	Till‰mpningar/Text
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/Ù≈À”‘œ◊¶ ’‘…Ã¶‘…
Source0:	ftp://ftp.perl.org/pub/perl/CPAN/src/%{name}-%{version}.tar.gz
Source1:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-noroot_install.patch
Patch1:		%{name}-nodb.patch
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-find-provides.patch
Patch4:		%{name}-prereq.patch
Patch5:		%{name}-syslog.patch
Patch6:		%{name}-CGI-upload-tmpdir.patch
Patch7:		%{name}-LD_RUN_PATH.patch
Patch8:		%{name}-errno_h-parsing.patch
Patch9:		%{name}-use-LD_PRELOAD-for-libperl.so.patch
Patch10:	%{name}-sitearch.patch
Patch11:	%{name}-soname.patch
Patch12:	%{name}-db3.patch
URL:		http://www.perl.org/
BuildRequires:	db3-devel
BuildRequires:	gdbm-devel
Provides:	perl(DynaLoader)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-lib
Obsoletes:	perl-mod-skel
Obsoletes:	perl-base

%description
Perl is an interpreted language optimized for scanning arbitrary text
files, extracting information from those text files, and printing
reports based on that information. It's also a good language for many
system management tasks. The language is intended to be practical
(easy to use, efficient, complete) rather than beautiful (tiny,
elegant, minimal).

%description -l de
Perl ist eine Interpreter-Sprache, die zum Durchsuchen beliebiger
Text- dateien, Extrahieren von Informationen aus diesen Dateien und
Drucken von auf diesen Informationen basierenden Berichten optimiert
ist. Die Sprache eignet sich auﬂerdem f¸r viele
Systemverwaltungsaufgaben. Sie ist eher praktisch (einfache
Anwendung,effizient, vollst‰ndig) als schˆn (winzig, elegant,
minimal).

%description -l fr
Perl est un langage interprÈtÈ, optimisÈ pour filtrer des fichiers
texte, extraire des informations de ces fichiers, et imprimer des
rapports basÈs sur ces informations. C'est aussi un bon langage pour
de nombreuses procÈdures de gestion systËme. Ce langage se veut
pratique (simple ‡ utiliser, efficace, complet) autant qu'agrÈable
(conscrit, ÈlÈgant, minimal).

%description -l pl
Perl jest jÍzykiem przeznaczonym do skanowania plikÛw tekstowych,
wyci±gania z nich informacji i drukowania raportu bazuj±cego na tych
informacjach. Jest rÛwnieø doskona≥ym jÍzykiem do wielu prac
zwi±zanych z nadzorem systemu. JÍzyk ten jest w zamierzeniu bardziej
praktyczny (≥atwy w uøyciu, wydajny, kompletny) niø piÍkny (skromny,
elegancki, minimalny).

%description -l tr
Perl, metin dosyalar˝n˝ taramak, bu metin dosyalar˝ndan bilgi Á˝karmak
ve bu bilgiye dayal˝ raporlar haz˝rlamak icin geli˛tirilmi˛ bir
yorumlamal˝ dildir. Ayr˝ca pek Áok sistem yˆnetimi gˆrevleri iÁin de
yararl˝ yetenekleri vard˝r. Perl, g¸zel (ufak, zarif, minimum)
olmaktan Áok, pratik olmaya yˆnelik (kullan˝m˝ kolay, verimli,
eksiksiz) olarak tasarlanm˝˛t˝r.

%package devel
Summary:	Perl development files
Summary(pl):	Pliki deweloperskie perla
Group:		Development/Libraries
Group(cs):	V˝vojovÈ prost¯edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	ﬁrÛunartÛl/Agerasˆfn
Group(it):	Sviluppo/Librerie
Group(ja):	≥´»Ø/•È•§•÷•È•Í
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(sl):	Razvoj/Knjiænice
Group(sv):	Utveckling/Bibliotek
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Requires:	%{name}-modules = %{version}
Obsoletes:	perl-lib-devel

%description devel
Files for developing applications which embed a Perl interpreter.

%description devel -l pl
Pliki do tworzenia aplikacji opartych na perlu.

%package -n sperl
Summary:	Practical Extraction and Report Language (SUID root binary)
Summary(pl):	Practical Extraction and Report Language (binaria SUID root)
Group:		Applications/Text
Group(cs):	Aplikace/Text
Group(da):	Programmer/Tekst
Group(de):	Applikationen/Text
Group(es):	Aplicaciones/Texto
Group(fr):	Applications/Texte
Group(is):	Forrit/Texti
Group(it):	Applicazioni/Testo
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•∆•≠•π•»
Group(no):	Applikasjoner/Tekst
Group(pl):	Aplikacje/Tekst
Group(pt):	AplicaÁıes/Texto
Group(ru):	“…Ãœ÷≈Œ…—/Ù≈À”‘œ◊Ÿ≈ ’‘…Ã…‘Ÿ
Group(sl):	Programi/Besedilo
Group(sv):	Till‰mpningar/Text
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/Ù≈À”‘œ◊¶ ’‘…Ã¶‘…
Requires:	%{name} = %{version}

%description -n sperl
Practical Extraction and Report Language (SUID root binary).

%description -n sperl -l pl
Practical Extraction and Report Language (binaria SUID root).

%package modules
Summary:	Practical Extraction and Report Language - modules
Summary(pl):	Practical Extraction and Report Language - modu≥y
Group:		Applications/Text
Group(cs):	Aplikace/Text
Group(da):	Programmer/Tekst
Group(de):	Applikationen/Text
Group(es):	Aplicaciones/Texto
Group(fr):	Applications/Texte
Group(is):	Forrit/Texti
Group(it):	Applicazioni/Testo
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•∆•≠•π•»
Group(no):	Applikasjoner/Tekst
Group(pl):	Aplikacje/Tekst
Group(pt):	AplicaÁıes/Texto
Group(ru):	“…Ãœ÷≈Œ…—/Ù≈À”‘œ◊Ÿ≈ ’‘…Ã…‘Ÿ
Group(sl):	Programi/Besedilo
Group(sv):	Till‰mpningar/Text
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/Ù≈À”‘œ◊¶ ’‘…Ã¶‘…
Prereq:		%{name} = %{version}
Provides:	perl-ANSIColor
Provides:	perl-Devel-Peek
Provides:	perl-DProf
Provides:	perl-PodParser
Obsoletes:	perl-ANSIColor
Obsoletes:	perl-Devel-Peek
Obsoletes:	perl-DProf
Obsoletes:	perl-PodParser

%description modules
Practical Extraction and Report Language - modules.

%description modules -l pl
Practical Extraction and Report Language - modu≥y.

%package pod
Summary:	Perl POD documentation
Summary(pl):	Dokumentacja Perla w formacie POD
Group:		Applications/Text
Group(cs):	Aplikace/Text
Group(da):	Programmer/Tekst
Group(de):	Applikationen/Text
Group(es):	Aplicaciones/Texto
Group(fr):	Applications/Texte
Group(is):	Forrit/Texti
Group(it):	Applicazioni/Testo
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•∆•≠•π•»
Group(no):	Applikasjoner/Tekst
Group(pl):	Aplikacje/Tekst
Group(pt):	AplicaÁıes/Texto
Group(ru):	“…Ãœ÷≈Œ…—/Ù≈À”‘œ◊Ÿ≈ ’‘…Ã…‘Ÿ
Group(sl):	Programi/Besedilo
Group(sv):	Till‰mpningar/Text
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/Ù≈À”‘œ◊¶ ’‘…Ã¶‘…
Prereq:		%{name} = %{version}

%description pod
Practical Extraction and Report Language - POD docs.

%description pod -l pl
Practical Extraction and Report Language - dokumentacja w formacie
POD.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

for i in find-* ; do
	mv -f $i $i.old
	sed "s|FPPATH|%{_builddir}/%{name}-%{version}|g" < $i.old > $i
	chmod 755 $i; rm -f $i.old
done

%build
# this is gross
# i added more ugly stuff here
# i know that is ugly way to set that but i dont know how do it better
cat > config.over <<EOF
installprefix=$RPM_BUILD_ROOT%{_prefix}
test -d \$installprefix || mkdir -p \$installprefix
test -d \$installprefix/bin || mkdir -p \$installprefix/bin
installarchlib=\`echo \$installarchlib | sed "s!\$prefix!\$installprefix!"\`
installbin=\`echo \$installbin | sed "s!\$prefix!\$installprefix!"\`
installman1dir=\`echo \$installman1dir | sed "s!\$prefix!\$installprefix!"\`
installman3dir=\`echo \$installman3dir | sed "s!\$prefix!\$installprefix!"\`
installprivlib=\`echo \$installprivlib | sed "s!\$prefix!\$installprefix!"\`
installscript=\`echo \$installscript | sed "s!\$prefix!\$installprefix!"\`
installsitelib=\`echo \$installsitelib | sed "s!\$prefix!\$installprefix!"\`
installsitearch=\`echo \$installsitearch | sed "s!\$prefix!\$installprefix!"\`
dynamic_ext=\`echo \$dynamic_ext GDBM_File NDBM_File\`
EOF

USETHREADS=%{!?_with_perl_threads:-U}%{?_with_perl_threads:-D}
sh Configure \
	-des \
	-Dcc=%{__cc} \
	-Darchname=%{_target_platform} \
	-Dcccdlflags='-fPIC' \
	-Dccdlflags='-rdynamic' \
	-Dprefix=%{_prefix} \
	-Dscriptdir=%{_bindir} \
	-Dsitelib=%{_libdir}/perl5/site_perl \
	-Dman1dir=%{_mandir}/man1 \
	-Dman3dir=%{_mandir}/man3 \
	-Dman3ext=3pm \
	-Doptimize="%{rpmcflags}" \
	${USETHREADS}usethreads \
	-Uuselargefiles \
%ifarch sparc sparc64
	-Ud_longdbl \
%endif
	-Duseshrplib \
	-Dd_dosuid \
	-Ud_setresuid \
	-Ud_setresgid

mv -f Makefile Makefile.bak
sed -e 's#^CCDLFLAGS = -rdynamic -Wl,-rpath,/usr/lib/perl5/.*#CCDLFLAGS = -rdynamic#' \
	Makefile.bak > Makefile

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install
install utils/pl2pm $RPM_BUILD_ROOT%{_bindir}/pl2pm

## Generate *.ph files with a trick (based on RH).

%{__make} all -f - <<EOF
PKGS	= glibc-devel gdbm-devel gpm-devel libgr-devel libjpeg-devel \
	libpng-devel libtiff-devel ncurses-devel popt-devel \
	zlib-devel binutils libelf e2fsprogs-devel pam-devel pwdb-devel \
	rpm-devel
STDH	= \$(filter /usr/include/%%, \$(shell rpm -q --queryformat '[%%{FILENAMES}\n]' \$(PKGS)))
STDH	+= \$(wildcard /usr/include/linux/*.h) \$(wildcard /usr/include/asm/*.h) \$(wildcard /usr/include/scsi/*.h)
GCCDIR	= \$(shell gcc --print-file-name include)
GCCH	= \$(filter \$(GCCDIR)/%%, \$(shell rpm -q --queryformat '[%%{FILENAMES}\n]' gcc))

LIBPATH = %{_builddir}/%{name}-%{version}
PERLLIB = $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}
PERLBIN = $RPM_BUILD_ROOT%{_bindir}/perl
PERL	= LD_LIBRARY_PATH=\$(LIBPATH) PERL5LIB=\$(PERLLIB) \$(PERLBIN)
PHDIR	= \$(PERLLIB)/%{_target_platform}%{perlthread}
PHBIN	= $RPM_BUILD_ROOT%{_bindir}/h2ph
H2PH	= \$(PERL) \$(PHBIN) -d \$(PHDIR)/

all: std-headers gcc-headers

std-headers: \$(STDH)
	cd /usr/include && \$(H2PH) \$(STDH:/usr/include/%%=%%)

gcc-headers: \$(GCCH)
	cd \$(GCCDIR) && \$(H2PH) \$(GCCH:\$(GCCDIR)/%%=%%)

EOF

## Fix paths
(
cd $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/%{_target_platform}%{perlthread}
sed -e "s|$RPM_BUILD_ROOT||g" < Config.pm > Config.pm.new
mv -f Config.pm.new Config.pm
sed -e "s|$RPM_BUILD_ROOT||g" < .packlist > .packlist.new
mv -f .packlist.new .packlist
)

## Fix permissions
find $RPM_BUILD_ROOT%{_libdir}/perl5 -name \*.ph -exec chmod 444 {} \;
find $RPM_BUILD_ROOT%{_libdir}/perl5 -type d -exec chmod 755 {} \;

## Fix lib
rm -f $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/*/CORE/libperl.so*
install libperl.so.%{version} $RPM_BUILD_ROOT%{_libdir}/
ln -sf libperl.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libperl.so

## Fix installed man pages list
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/perl{5004delta,5005delta,aix,amiga,bs2000}* \
	$RPM_BUILD_ROOT%{_mandir}/man1/perl{cygwin,dos,hpux,machten,macos}* \
	$RPM_BUILD_ROOT%{_mandir}/man1/perl{mpeix,os2,os390,solaris,vmesa,vms,vos,win32}*

# dir tree for other perl modules
(cd $RPM_BUILD_ROOT%{_libdir}/perl5/site_perl
install -d B Date Devel ExtUtils File Font HTML HTTP I18N IO/Socket \
	Mail News Net Parse RPC Text Tie Time XML auto/Mail
cd %{_target_platform}*/%{version}
install -d Apache BSD Compress Net Term auto/{Apache,BSD,Compress,Net,Term}
)

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/a2p
%attr(755,root,root) %{_bindir}/find2perl
%attr(755,root,root) %{_bindir}/perl
%attr(755,root,root) %{_bindir}/perl%{version}
%attr(755,root,root) %{_bindir}/s2p
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%dir %{_libdir}/perl5
%dir %{_libdir}/perl5/%{version}

%dir %{_libdir}/perl5/site_perl
%{_libdir}/perl5/site_perl/Date
%{_libdir}/perl5/site_perl/Devel
%{_libdir}/perl5/site_perl/ExtUtils
%{_libdir}/perl5/site_perl/File
%{_libdir}/perl5/site_perl/Font
%{_libdir}/perl5/site_perl/HTML
%{_libdir}/perl5/site_perl/HTTP
%{_libdir}/perl5/site_perl/I18N
%{_libdir}/perl5/site_perl/IO
%{_libdir}/perl5/site_perl/Mail
%{_libdir}/perl5/site_perl/News
%{_libdir}/perl5/site_perl/Net
%{_libdir}/perl5/site_perl/Parse
%{_libdir}/perl5/site_perl/RPC
%{_libdir}/perl5/site_perl/Text
%{_libdir}/perl5/site_perl/Tie
%{_libdir}/perl5/site_perl/Time
%{_libdir}/perl5/site_perl/XML
%{_libdir}/perl5/site_perl/auto
%dir %{_libdir}/perl5/site_perl/%{_target_platform}*
%dir %{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/BSD
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Compress
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Net
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Term
%dir %{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/BSD
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Compress
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Term

%{_libdir}/perl5/%{version}/AutoLoader.pm
%{_libdir}/perl5/%{version}/Carp
%{_libdir}/perl5/%{version}/Carp.pm
%{_libdir}/perl5/%{version}/Cwd.pm
%{_libdir}/perl5/%{version}/DirHandle.pm
%{_libdir}/perl5/%{version}/Exporter
%{_libdir}/perl5/%{version}/Exporter.pm
%dir %{_libdir}/perl5/%{version}/File
%{_libdir}/perl5/%{version}/File/Basename.pm
%{_libdir}/perl5/%{version}/File/Find.pm
%{_libdir}/perl5/%{version}/File/Path.pm
%{_libdir}/perl5/%{version}/File/Spec.pm
%{_libdir}/perl5/%{version}/File/stat.pm
%dir %{_libdir}/perl5/%{version}/File/Spec
%{_libdir}/perl5/%{version}/File/Spec/Unix.pm
%{_libdir}/perl5/%{version}/FileHandle.pm
%dir %{_libdir}/perl5/%{version}/IO
%dir %{_libdir}/perl5/%{version}/IO/Socket
%{_libdir}/perl5/%{version}/IO/Socket/INET.pm
%{_libdir}/perl5/%{version}/IO/Socket/UNIX.pm
%dir %{_libdir}/perl5/%{version}/IPC
%{_libdir}/perl5/%{version}/IPC/Open2.pm
%{_libdir}/perl5/%{version}/IPC/Open3.pm
%{_libdir}/perl5/%{version}/SelectSaver.pm
%{_libdir}/perl5/%{version}/Symbol.pm
%dir %{_libdir}/perl5/%{version}/Text
%{_libdir}/perl5/%{version}/Text/Tabs.pm
%{_libdir}/perl5/%{version}/Text/Wrap.pm
%dir %{_libdir}/perl5/%{version}/Time
%{_libdir}/perl5/%{version}/Time/Local.pm
%{_libdir}/perl5/%{version}/attributes.pm
%{_libdir}/perl5/%{version}/autouse.pm
%{_libdir}/perl5/%{version}/base.pm
%{_libdir}/perl5/%{version}/constant.pm
%{_libdir}/perl5/%{version}/fields.pm
%{_libdir}/perl5/%{version}/integer.pm
%{_libdir}/perl5/%{version}/lib.pm
%{_libdir}/perl5/%{version}/locale.pm
%{_libdir}/perl5/%{version}/overload.pm
%{_libdir}/perl5/%{version}/strict.pm
%{_libdir}/perl5/%{version}/vars.pm
%{_libdir}/perl5/%{version}/warnings.pm
%dir %{_libdir}/perl5/%{version}/warnings
%{_libdir}/perl5/%{version}/warnings/register.pm
%dir %{_libdir}/perl5/%{version}/pod
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*
%{_libdir}/perl5/%{version}/%{_target_platform}*/Config.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/DynaLoader.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/Errno.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/Fcntl.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/IO.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/IO
%{_libdir}/perl5/%{version}/%{_target_platform}*/POSIX.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/Socket.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/XSLoader.pm
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DynaLoader
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DynaLoader/dl_findfile.al
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Fcntl
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Fcntl/Fcntl.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Fcntl/Fcntl.so
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/IO
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/IO/IO.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/IO/IO.so
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/POSIX
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/POSIX/POSIX.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/POSIX/POSIX.so
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/POSIX/tmpfile.al
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Socket
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Socket/Socket.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Socket/Socket.so

%{_mandir}/man1/a2p.1*
%{_mandir}/man1/dprofpp.1*
%{_mandir}/man1/find2perl.1*
%{_mandir}/man1/perl.1*
%{_mandir}/man1/s2p.1*
%{_mandir}/man1/xsubpp.1*
%lang(fi) %{_mandir}/fi/man1/perl.1*
%lang(pl) %{_mandir}/pl/man1/perl.1*


%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/c2ph
%attr(755,root,root) %{_bindir}/dprofpp
%attr(755,root,root) %{_bindir}/h2ph
%attr(755,root,root) %{_bindir}/h2xs
%attr(755,root,root) %{_bindir}/perlbug
%attr(755,root,root) %{_bindir}/perlcc
%attr(755,root,root) %{_bindir}/perldoc
%attr(755,root,root) %{_bindir}/pl2pm
%attr(755,root,root) %{_bindir}/pod*
%attr(755,root,root) %{_bindir}/pstruct
%attr(755,root,root) %{_bindir}/splain

%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man1/c2ph.1*
%{_mandir}/man1/h2ph.1*
%{_mandir}/man1/h2xs.1*
%{_mandir}/man1/perl[a-z]*.1*
%{_mandir}/man1/pl2pm.1*
%{_mandir}/man1/pod2html.1*
%{_mandir}/man1/pod2man.1*
%{_mandir}/man1/pod2text.1*
%{_mandir}/man1/pod2usage.1*
%{_mandir}/man1/podchecker.1*
%{_mandir}/man1/podselect.1*
%{_mandir}/man1/pstruct.1*
%{_mandir}/man1/splain.1*
%{_mandir}/man3/[A-BD-Za-z]*
%{_mandir}/man3/CPAN*
%{_mandir}/man3/C[a-z]*
%lang(fi) %{_mandir}/fi/man1/perl[a-z]*.1*
%lang(pl) %{_mandir}/pl/man1/perl[a-z]*.1*

%{_libdir}/perl5/%{version}/%{_target_platform}*/CORE

%files -n sperl
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/sperl%{version}
%attr(4755,root,root) %{_bindir}/suidperl

%files modules
%defattr(644,root,root,755)
%{_libdir}/perl5/site_perl/B
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Apache
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Apache
%{_libdir}/perl5/%{version}/B
%{_libdir}/perl5/%{version}/CPAN
%{_libdir}/perl5/%{version}/Class
%{_libdir}/perl5/%{version}/Devel
%{_libdir}/perl5/%{version}/ExtUtils
%{_libdir}/perl5/%{version}/File/CheckTree.pm
%{_libdir}/perl5/%{version}/File/Compare.pm
%{_libdir}/perl5/%{version}/File/Copy.pm
%{_libdir}/perl5/%{version}/File/DosGlob.pm
%{_libdir}/perl5/%{version}/File/Temp.pm
%{_libdir}/perl5/%{version}/File/Spec/[A-OV-Z]*.pm
%{_libdir}/perl5/%{version}/Getopt
%{_libdir}/perl5/%{version}/I18N
%{_libdir}/perl5/%{version}/Math
%{_libdir}/perl5/%{version}/Net
%{_libdir}/perl5/%{version}/Pod
%{_libdir}/perl5/%{version}/Search
%{_libdir}/perl5/%{version}/Term
%{_libdir}/perl5/%{version}/Test
%{_libdir}/perl5/%{version}/Text/Abbrev.pm
%{_libdir}/perl5/%{version}/Text/ParseWords.pm
%{_libdir}/perl5/%{version}/Text/Soundex.pm
%{_libdir}/perl5/%{version}/Tie
%{_libdir}/perl5/%{version}/Time/[!L]*
%{_libdir}/perl5/%{version}/User
%{_libdir}/perl5/%{version}/auto
%{_libdir}/perl5/%{version}/pod/perldiag.pod
%{_libdir}/perl5/%{version}/unicode
%{_libdir}/perl5/%{version}/*.pl
%{_libdir}/perl5/%{version}/AnyDBM_File.pm
%{_libdir}/perl5/%{version}/AutoSplit.pm
%{_libdir}/perl5/%{version}/Benchmark.pm
%{_libdir}/perl5/%{version}/blib.pm
%{_libdir}/perl5/%{version}/bytes.pm
%{_libdir}/perl5/%{version}/charnames.pm
%{_libdir}/perl5/%{version}/CPAN.pm
%{_libdir}/perl5/%{version}/DB.pm
%{_libdir}/perl5/%{version}/diagnostics.pm
%{_libdir}/perl5/%{version}/Dumpvalue.pm
%{_libdir}/perl5/%{version}/English.pm
%{_libdir}/perl5/%{version}/Env.pm
%{_libdir}/perl5/%{version}/Fatal.pm
%{_libdir}/perl5/%{version}/FileCache.pm
%{_libdir}/perl5/%{version}/filetest.pm
%{_libdir}/perl5/%{version}/FindBin.pm
%{_libdir}/perl5/%{version}/less.pm
%{_libdir}/perl5/%{version}/open.pm
%{_libdir}/perl5/%{version}/SelfLoader.pm
%{_libdir}/perl5/%{version}/Shell.pm
%{_libdir}/perl5/%{version}/sigtrap.pm
%{_libdir}/perl5/%{version}/subs.pm
%{_libdir}/perl5/%{version}/Test.pm
%{_libdir}/perl5/%{version}/UNIVERSAL.pm
%{_libdir}/perl5/%{version}/utf8.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/B
%{_libdir}/perl5/%{version}/%{_target_platform}*/Data
%{_libdir}/perl5/%{version}/%{_target_platform}*/Devel
%{_libdir}/perl5/%{version}/%{_target_platform}*/File
%{_libdir}/perl5/%{version}/%{_target_platform}*/IPC
%{_libdir}/perl5/%{version}/%{_target_platform}*/Sys
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/B
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/B/B.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/B/B.so
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/ByteLoader
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/ByteLoader/ByteLoader.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/ByteLoader/ByteLoader.so
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DB_File
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DB_File/autosplit.ix
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DB_File/DB_File.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DB_File/DB_File.so
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Data
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Data/Dumper
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Data/Dumper/Dumper.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Data/Dumper/Dumper.so
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Devel
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Devel/DProf
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Devel/DProf/DProf.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Devel/DProf/DProf.so
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Devel/Peek
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Devel/Peek/Peek.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Devel/Peek/Peek.so
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DynaLoader/DynaLoader.a
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DynaLoader/autosplit.ix
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DynaLoader/dl_expandspec.al
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DynaLoader/dl_find_symbol_anywhere.al
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DynaLoader/extralibs.ld
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/File
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/File/Glob
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/File/Glob/autosplit.ix
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/File/Glob/Glob.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/File/Glob/Glob.so
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/GDBM_File
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/GDBM_File/autosplit.ix
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/GDBM_File/GDBM_File.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/GDBM_File/GDBM_File.so
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/IPC
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/IPC/SysV
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/IPC/SysV/SysV.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/IPC/SysV/SysV.so
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/NDBM_File
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/NDBM_File/NDBM_File.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/NDBM_File/NDBM_File.so
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Opcode
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Opcode/Opcode.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Opcode/Opcode.so
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/POSIX/[a-su-w]*.al
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/POSIX/time.al
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/POSIX/tolower.al
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/POSIX/toupper.al
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/POSIX/*.ix
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/SDBM_File
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/SDBM_File/SDBM_File.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/SDBM_File/SDBM_File.so
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Sys
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Sys/Hostname
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Sys/Hostname/autosplit.ix
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Sys/Hostname/Hostname.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Sys/Hostname/Hostname.so
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Sys/Syslog
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Sys/Syslog/Syslog.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Sys/Syslog/Syslog.so
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/attrs
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/attrs/attrs.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/attrs/attrs.so
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/re
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/re/re.bs
%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/re/re.so
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/sdbm
%{_libdir}/perl5/%{version}/%{_target_platform}*/B.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/ByteLoader.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/DB_File.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/attrs.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/GDBM_File.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/NDBM_File.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/Opcode.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/O.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/ops.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/re.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/Safe.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/SDBM_File.pm

%files pod
%defattr(644,root,root,755)
%{_libdir}/perl5/%{version}/pod/perl[^d]*
%{_libdir}/perl5/%{version}/pod/perld[^i]*
