%define 	__find_provides	%{_builddir}/%{name}-%{version}/find-perl-provides
%define		perlthread %{?bcond_on_perl_threads:-thread-multi}
Summary:	Practical Extraction and Report Language
Summary(de):	Praktische Extraktions- und Berichtsprache 
Summary(fr):	Practical Extraction and Report Language (Perl)
Summary(pl):	Practical Extraction and Report Language (Perl)
Summary(tr):	Kabuk yorumlama dili
Name:		perl
Version:	5.6.1
Release:	6
Epoch:		1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Source0:	ftp://ftp.perl.org/pub/perl/CPAN/src/%{name}-%{version}.tar.gz
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
URL:		http://www.perl.org/
#Requires:	csh
Provides:	perl-ANSIColor
Provides:	perl-Devel-Peek
Provides:	perl-DProf
Provides:	perl-PodParser
Provides:	perl-CGI
Obsoletes:	perl-ANSIColor
Obsoletes:	perl-Devel-Peek
Obsoletes:	perl-DProf
Obsoletes:	perl-PodParser
Obsoletes:	perl-CGI
Prereq:		%{name}-lib = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl is an interpreted language optimized for scanning arbitrary text
files, extracting information from those text files, and printing
reports based on that information. It's also a good language for many
system management tasks. The language is intended to be practical
(easy to use, efficient, complete) rather than beautiful (tiny,
elegant, minimal).

#This version has support for threads compiled in.

%description -l de
Perl ist eine Interpreter-Sprache, die zum Durchsuchen beliebiger
Text- dateien, Extrahieren von Informationen aus diesen Dateien und
Drucken von auf diesen Informationen basierenden Berichten optimiert
ist. Die Sprache eignet sich außerdem für viele
Systemverwaltungsaufgaben. Sie ist eher praktisch (einfache
Anwendung,effizient, vollständig) als schön (winzig, elegant,
minimal).

%description -l fr
Perl est un langage interprété, optimisé pour filtrer des fichiers
texte, extraire des informations de ces fichiers, et imprimer des
rapports basés sur ces informations. C'est aussi un bon langage pour
de nombreuses procédures de gestion système. Ce langage se veut
pratique (simple à utiliser, efficace, complet) autant qu'agréable
(conscrit, élégant, minimal).

%description -l pl
Perl jest jêzykiem przeznaczonym do skanowania plików tekstowych,
wyci±gania z nich informacji i drukowania raportu bazuj±cego na tych
informacjach. Jest równie¿ doskona³ym jêzykiem dla wielu narzêdzi do
nadzoru systemu. Jêzyk ten jest w zamierzeniu praktycznym (³atwym w
u¿yciu, efektywnym, kompletnym) bardziej ni¿ piêkny ;) (skromny,
elegancki, minimalny).

%description -l tr
Perl, metin dosyalarýný taramak, bu metin dosyalarýndan bilgi çýkarmak
ve bu bilgiye dayalý raporlar hazýrlamak icin geliþtirilmiþ bir
yorumlamalý dildir. Ayrýca pek çok sistem yönetimi görevleri için de
yararlý yetenekleri vardýr. Perl, güzel (ufak, zarif, minimum)
olmaktan çok, pratik olmaya yönelik (kullanýmý kolay, verimli,
eksiksiz) olarak tasarlanmýþtýr.

%package lib
Summary:	Shared Perl library and other version dependant files
Group:		Libraries

%description lib
Provides a shared library for programs which embed a Perl interpreter.

%package lib-devel
Summary:	Shared Perl library - development files
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}

%description lib-devel
Files for developing applications which embed a Perl interpreter.

%package doc
Summary:	Perl documentation
Group:		Applications/Text
Requires:	%{name} = %{version}

%description doc
Perl manual pages and POD docs.  If you are writing Perl programs, you
almost certainly need this.

%package -n sperl
Summary:	Practical Extraction and Report Language (SUID root binary)
Summary(pl):	Practical Extraction and Report Language (SUID root binaria)
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Requires:	%{name} = %{version}

%description -n sperl
Practical Extraction and Report Language (SUID root binary).

%description -n sperl -l pl
Practical Extraction and Report Language (SUID root binaria).

%package minimal
Summary:	Practical Extraction and Report Language - base files
Summary(pl):	Practical Extraction and Report Language - pliki podstawowe
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Prereq:		%{name}-lib = %{version}
Conflicts:	%{name}

%description minimal
Practical Extraction and Report Language - base files, usefull
on embedded systems.

%description minimal -l pl
Practical Extraction and Report Language - pliki podstawowe, przydatne
dla systemów osadzonych.


%prep
%setup  -q
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

USETHREADS=%{!?bcond_on_perl_threads:-U}%{?bcond_on_perl_threads:-D}
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
	-Doptimize="$RPM_OPT_FLAGS" \
	${USETHREADS}usethreads \
	-Uuselargefiles \
%ifarch sparc sparc64
	-Ud_longdbl \
%endif
	-Duseshrplib \
	-Dd_dosuid \
	-Ud_setresuid \
	-Ud_setresgid 

mv Makefile Makefile.bak
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
GCCH    = \$(filter \$(GCCDIR)/%%, \$(shell rpm -q --queryformat '[%%{FILENAMES}\n]' gcc))

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

gzip -9nf README Change*

%clean
rm -rf $RPM_BUILD_ROOT

%post lib -p /sbin/ldconfig
%postun lib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.gz Change*

%attr(755,root,root) %{_bindir}/a2p
%attr(755,root,root) %{_bindir}/c2ph
%attr(755,root,root) %{_bindir}/find2perl
%attr(755,root,root) %{_bindir}/h2ph
%attr(755,root,root) %{_bindir}/h2xs
%attr(755,root,root) %{_bindir}/perl
%attr(755,root,root) %{_bindir}/perl%{version}
%attr(755,root,root) %{_bindir}/perlbug
%attr(755,root,root) %{_bindir}/perlcc
%attr(755,root,root) %{_bindir}/pl2pm
%attr(755,root,root) %{_bindir}/pod2html
%attr(755,root,root) %{_bindir}/pod2latex
%attr(755,root,root) %{_bindir}/pod2man
%attr(755,root,root) %{_bindir}/pod2text
%attr(755,root,root) %{_bindir}/podselect
%attr(755,root,root) %{_bindir}/pstruct
%attr(755,root,root) %{_bindir}/s2p
%attr(755,root,root) %{_bindir}/splain

%dir %{_libdir}/perl5
%dir %{_libdir}/perl5/%{version}
%dir %{_libdir}/perl5/site_perl
%dir %{_libdir}/perl5/site_perl/%{_target_platform}*
%dir %{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}

%attr( - ,root,root) %{_libdir}/perl5/%{version}/[A-Z]*
%attr( - ,root,root) %{_libdir}/perl5/%{version}/[a-z]*.*
%attr( - ,root,root) %{_libdir}/perl5/%{version}/auto
%attr( - ,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*
%attr( - ,root,root) %{_libdir}/perl5/%{version}/unicode
%attr( - ,root,root) %{_libdir}/perl5/%{version}/warnings

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files lib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so

%files doc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perldoc
%{_mandir}/man[13]/*
%{_libdir}/perl5/%{version}/pod/*

%files -n sperl
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/sperl%{version}
%attr(4755,root,root) %{_bindir}/suidperl

%files minimal
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perl
%attr(755,root,root) %{_bindir}/perl%{version}

%dir %{_libdir}/perl5
%dir %{_libdir}/perl5/%{version}
%dir %{_libdir}/perl5/site_perl
%dir %{_libdir}/perl5/site_perl/%{_target_platform}*
%dir %{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}

%{_libdir}/perl5/%{version}/AutoLoader.pm
%{_libdir}/perl5/%{version}/Carp.pm
%{_libdir}/perl5/%{version}/Cwd.pm
%{_libdir}/perl5/%{version}/DirHandle.pm
%{_libdir}/perl5/%{version}/Exporter.pm
%{_libdir}/perl5/%{version}/File/Basename.pm
%{_libdir}/perl5/%{version}/File/Find.pm
%{_libdir}/perl5/%{version}/File/Path.pm
%{_libdir}/perl5/%{version}/File/Spec.pm
%{_libdir}/perl5/%{version}/File/Spec/Unix.pm
%{_libdir}/perl5/%{version}/FileHandle.pm
%{_libdir}/perl5/%{version}/IO/Socket/INET.pm
%{_libdir}/perl5/%{version}/IO/Socket/UNIX.pm
%{_libdir}/perl5/%{version}/IPC/Open2.pm
%{_libdir}/perl5/%{version}/IPC/Open3.pm
%{_libdir}/perl5/%{version}/SelectSaver.pm
%{_libdir}/perl5/%{version}/Symbol.pm
%{_libdir}/perl5/%{version}/Text/Tabs.pm
%{_libdir}/perl5/%{version}/Text/Wrap.pm
%{_libdir}/perl5/%{version}/Time/Local.pm
%{_libdir}/perl5/%{version}/attributes.pm
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
%{_libdir}/perl5/%{version}/warnings/register.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/Config.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/DynaLoader.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/IO.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/IO/*.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/POSIX.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/Socket.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/XSLoader.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DynaLoader/dl_findfile.al
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/IO/IO.so
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/POSIX/POSIX.so
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/POSIX/tmpfile.al
%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Socket/Socket.so

%dir %{_libdir}/perl5/%{version}/File
%dir %{_libdir}/perl5/%{version}/File/Spec
%dir %{_libdir}/perl5/%{version}/IO
%dir %{_libdir}/perl5/%{version}/IO/Socket
%dir %{_libdir}/perl5/%{version}/IPC
%dir %{_libdir}/perl5/%{version}/Text
%dir %{_libdir}/perl5/%{version}/Time
%dir %{_libdir}/perl5/%{version}/warnings
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/IO
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DynaLoader
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/IO
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/POSIX
%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/Socket
