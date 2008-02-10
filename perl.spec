# unpackaged:
#   /usr/lib/perl5/5.10.0/i686-pld-linux-thread-multi/.packlist
#   /usr/lib/perl5/5.10.0/i686-pld-linux-thread-multi/auto/sdbm/extralibs.ld
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
%bcond_without	threads		# build without support for threads
%bcond_without	gdbm		# build without the GDBM_File module
%bcond_without	microperl	# build microperl (needs fixing)
#
# TODO:
# - fix "FIXME"s, review "XXX"s
# - add the {O,N}DBM_File modules
# - review the perldiag.pod issue
# - consider disabling ithreads by default
# - what about "prove" (binary+manual)? (conflicts with standalone Test-Harness)
# - patch MakeMaker to get rid of empty *.bs files (MM_Unix::dynamic_bs())
# - %{__cc}: cc -c -o uhv.o -DPERL_CORE -DPERL_MICRO -DSTANDARD_C -DPERL_USE_SAFE_PUTENV -O2 -march=i686  hv.c
#
# TODO for perl-dependent packages:
# - change all "R/BR: perl" to one of perl-{base,modules,devel}
#

%define _abi	5.10.0

%define		perlthread	%{?with_threads:-thread-multi}

%define		perl_privlib	%{_datadir}/perl5/%{version}
%define		perl_archlib	%{_libdir}/perl5/%{version}/%{_target_platform}%{perlthread}
%define		perl_sitelib	%{_usr}/local/share/perl5
%define		perl_sitearch	%{_usr}/local/lib/perl5/%{_abi}/%{_target_platform}%{perlthread}
%define		perl_vendorlib	%{_datadir}/perl5/vendor_perl
%define		perl_vendorarch	%{_libdir}/perl5/vendor_perl/%{_abi}/%{_target_platform}%{perlthread}

%define		rel	2.1
Summary:	Practical Extraction and Report Language (Perl)
Summary(cs.UTF-8):	Programovací jazyk Perl
Summary(da.UTF-8):	Programmeringssproget Perl
Summary(de.UTF-8):	Praktische Extraktions- und Berichtsprache
Summary(es.UTF-8):	Lenguaje práctica de extracción y listado
Summary(fr.UTF-8):	Langage de programmation Perl
Summary(id.UTF-8):	Bahasa pemrograman Perl
Summary(is.UTF-8):	Forritunarmálið Perl
Summary(it.UTF-8):	Perl: linguaggio di programmazione
Summary(ja.UTF-8):	Perl プログラミング言語
Summary(ko.UTF-8):	펄 프로그래밍 언어
Summary(nb.UTF-8):	Programmeringsspråket Perl
Summary(pl.UTF-8):	Interpreter języka Perl (Practical Extraction and Report Language)
Summary(pt.UTF-8):	A linguagem de programação Perl
Summary(pt_BR.UTF-8):	Linguagem prática de extração e relatório
Summary(ru.UTF-8):	Язык программирования Perl
Summary(sk.UTF-8):	Programovací jazyk Perl
Summary(sl.UTF-8):	Programski jezik Perl
Summary(sv.UTF-8):	Programmeringsspråket Perl
Summary(tr.UTF-8):	Kabuk yorumlama dili
Summary(zh_CN.UTF-8):	Perl 编程语言。
Name:		perl
Version:	5.10.0
Release:	%{rel}%{!?with_threads:_nothr}
Epoch:		1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/src/%{name}-%{version}.tar.gz
# Source0-md5:	d2c39b002ebfd2c3c5dba589365c5a71
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	de47d7893f49ad7f41ba69c78511c0db
Source2:	%{name}.prov
Patch0:		%{name}_581-noroot_install.patch
Patch1:		%{name}_581-INC.patch
Patch2:		%{name}_580-errno_h-parsing.patch
Patch3:		%{name}_580-use-LD_PRELOAD-for-libperl.so.patch
Patch4:		%{name}_581-soname.patch
Patch5:		%{name}-test-noproc.patch
Patch6:		%{name}_585-microperl_uconfig.patch
Patch7:		%{name}-write-permissions.patch
Patch8:		%{name}-timer-test.patch
Patch9:		%{name}-h2ph-includes.patch
URL:		http://dev.perl.org/perl5/
%ifarch ppc
# gcc 3.3.x miscompiles pp_hot.c
BuildRequires:	gcc >= 5:4.1
%endif
%{?with_gdbm:BuildRequires:	gdbm-devel}
# asm-generic, merged x86 asm dirs
BuildRequires:	linux-libc-headers >= 7:2.6.24
# required for proper Provides generation (older are not supported by spec)
BuildRequires:	rpm-build >= 4.3-0.20040107.4
BuildRequires:	rpmbuild(macros) >= 1.426
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	%{name}-doc-reference = %{epoch}:%{version}-%{release}
Requires:	perldoc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		__perl		%{_builddir}/perl-%{version}/runperl
%define		__perl_provides %{__perl} %{SOURCE2}

%description
Perl is an interpreted language optimized for scanning arbitrary text
files, extracting information from those text files, and printing
reports based on that information. It's also a good language for many
system management tasks. The language is intended to be practical
(easy to use, efficient, complete) rather than beautiful (tiny,
elegant, minimal).

%description -l cs.UTF-8
Perl je vyšší programovací jazyk s kořeny v jazyce C, sed, awk a
shellových skriptech. Perl je vhodný pro manipulace s procesy a
soubory, ale obzvláště se hodí ke zpracovávání textů. Perl vyniká
praktičností účinností. I když se používá prakticky na cokoli, většina
Perlových programů slouží jako správcovské utility nebo programy pro
WWW. V Perlu je napsáno velmi mnoho CGI skriptů pro WWW servery na
celém světě.

%description -l da.UTF-8
Perl er et høgniveauprogramsprog med røtter i C, sed, awk og
skalskript. Perl er godt på at behandle processer og filer, og er
særskilt godt på at behandle text. Utmærkende for Perl er at det er
praktisk og effektivt. Det bruges for at gøre en mængd forskellige
saker, men de almindeligeste programmerne er systemadministration og
webbprogrammering. En stor andel af CGI-skripten på webben er skrivna
i Perl. Du behøver installere pakken Perl på dit system så at ditt
system kan behandle Perlskript.

%description -l de.UTF-8
Perl ist eine Interpreter-Sprache, die zum Durchsuchen beliebiger
Text- dateien, Extrahieren von Informationen aus diesen Dateien und
Drucken von auf diesen Informationen basierenden Berichten optimiert
ist. Die Sprache eignet sich außerdem für viele
Systemverwaltungsaufgaben. Sie ist eher praktisch (einfache
Anwendung,effizient, vollständig) als schön (winzig, elegant,
minimal).

%description -l es.UTF-8
Perl es un lenguaje interpretado, optimizado para manejar archivos
texto, extrayendo información de estos archivos y mostrando listados
basados en esta información. También es un buen lenguaje para varias
tareas de administración de sistema. El lenguaje busca ser más
práctico (fácil de usar, eficiente, completo) que bonito (minúsculo,
elegante, mínimo).

%description -l fr.UTF-8
Perl est un langage interprété, optimisé pour filtrer des fichiers
texte, extraire des informations de ces fichiers, et imprimer des
rapports basés sur ces informations. C'est aussi un bon langage pour
de nombreuses procédures de gestion système. Ce langage se veut
pratique (simple à utiliser, efficace, complet) autant qu'agréable
(conscrit, élégant, minimal).

%description -l id.UTF-8
Perl adalah sebuah bahasa pemrograman tingkat tinggi yang didasarkan
pada C, sed, awk, dan bahasa shell. Perl memiliki kemampuan penanganan
proses dan file yang bagus, tapi terutama kemampuan penanganan teksnya
yang baik. Ciri khas Perl adalah kepraktisan dan efisiensi. Meski
digunakan untuk berbagai hal, aplikasi Perl yang paling umum adalah
utilitas sistem administrasi dan pemrograman web. Sebagian besar skrip
CGI yang ada di web ditulis dalam Perl. Anda Perlu memasang paket Perl
di sistem agar dapat menjalankan skrip-skrip Perl.

%description -l is.UTF-8
Perl er hás stigs forritunar tungumál sem á rætur sínar að rekja til
C, sed, awk, og skeljar forritunar. Perl er góð í að meðhöndla
processa og skrár og er sérstaklega góð í að meðhöndla texta. Perls
kostir eru nytsamleiki og virkni. Á meðan það er notað til að gera
marga mismunandi hluti, Perl mest notuðu forrit eru krefisstjórnunar
tól og vef forritun Stór hluti af CGI forritum á vefnum eru skrifaðar
í Perl. Þú þarft Perl pakkann settan upp á þínu krefi svo þitt kerfi
geti notað Perl scriptur.

%description -l it.UTF-8
Perl è un linguaggio di programmazione di alto livello derivato dal
linguaggio C, da sed, da awk e dallo scripting delle shell. E' adatto
per la gestione di processi, di file e in particolare di file di
testo. Perl è un linguaggio semplice ed efficiente. Viene utilizzato
per numerosi scopi, ma le sue applicazioni più diffuse sono le utility
di amministrazione del sistema e la programmazione Web. Una grossa
parte degli script CGI nel Web sono scritti in Perl. È consigliabile
installare il pacchetto Perl in modo che il sistema sia in grado di
gestire gli script di Perl.

%description -l ja.UTF-8
Perl は C言語、sed, awk、及び シェルスクリプティングに根源を
持つハイレベルな プログラム言語です。Perl はプロセスやファイルの処理に
適切で 、特に テキスト処理には最適です。さまざまな作業に
使用されますが、 Perlの最も頻繁な活用はシステムアドミニストレーション
ユーティリティと webプログラミングです。web上の 大部分のCGI"
スクリプトがPerlで書かれています。 システムがPerlスクリプトを
処理出来るようにするためには Perlパッケージを インストールする
必要があります。

%description -l pl.UTF-8
Perl jest językiem przeznaczonym do skanowania plików tekstowych,
wyciągania z nich informacji i drukowania raportu bazującego na tych
informacjach. Jest również doskonałym językiem do wielu prac
związanych z nadzorem systemu. Język ten jest w zamierzeniu bardziej
praktyczny (łatwy w użyciu, wydajny, kompletny) niż piękny (skromny,
elegancki, minimalny).

%description -l pt.UTF-8
O Perl é uma linguagem de programação de alto nível que tem como
raizes o C, sed, awk, e 'shell scripting'. O Perl é bom a manipular
processos e ficheiros, e é especialmente bom para manipular texto.
Características do Perl são a eficiência e o uso prático. As
aplicações mais comuns do Perl são utilitários de administração de
sistema e programação Web. Uma grande parte dos 'scripts' CGI na Web
são escritos em Perl. Você precisa do pacote Perl instalado no seu
sistema de maneira a que este possa tratar de 'scripts' de Perl.

%description -l pt_BR.UTF-8
Perl é uma linguagem interpretada, otimizada para tratar arquivos
texto, extraindo informação desses arquivos e mostrando relatórios
baseados nessa informação. Também é uma boa linguagem para várias
tarefas de administração de sistema. A linguagem procura ser mais
prática (fácil de usar, eficiente, completa) do que bonita (minúscula,
elegante, mínima).

%description -l ru.UTF-8
Perl - это интерпретируемый язык программирования, уходящий корнями в
C, sed, awk и языки командных оболочек (shell). Perl хорош для работы
с процессами и файлами, а особенно хорош для задач обработки текстов.
Особенности Perl - практичность и эффективность. Хотя он и
используется для решения самых разных задач, наиболее распространенные
применения (и то, в чем он силен) это, вероятно, утилиты системного
администрирования и web-программирование. Большая часть CGI скриптов
написана на Perl.

%description -l sk.UTF-8
Perl je programovací jazyk vyššej úrovne s koreňmi v C, sed, awk, a
shell skriptoch. Perl má vhodné vlastnosti pre spracovanie procesov a
súborov a je zvlášť vhodný pre spracovanie textu. Jeho cieľmi sú
praktičnosť a efektivita. Aj keď je používaný pre množstvo rozličných
činností, jeho najčastejším použitím (a kde vyniká najviac) sú
pravdepodobne nástroje pre správu systému a programovanie na Webe.
Veľká časť CGI skriptov na Webe je napísaná v Perle. Balík Perl
potrebujete mať nainštalovaný, aby bol váš systém schopný spracovať
Perl skripty.

%description -l sv.UTF-8
Perl är ett högnivåprogramspråk med rötter i C, sed, awk och
skalskript. Perl är bra på att hantera processer och filer, och är
särskilt bra på att hantera text. Utmärkande för Perl är att det är
praktiskt och effektivt. Det används för att göra en mängd olika
saker, men de vanligaste tillämpningarna är systemadministration och
webbprogrammering. En stor andel av CGI-skripten på webben är skrivna
i Perl. Du behöver installera paketet Perl på ditt system så att ditt

%description -l tr.UTF-8
Perl, metin dosyalarını taramak, bu metin dosyalarından bilgi çıkarmak
ve bu bilgiye dayalı raporlar hazırlamak icin geliştirilmiş bir
yorumlamalı dildir. Ayrıca pek çok sistem yönetimi görevleri için de
yararlı yetenekleri vardır. Perl, güzel (ufak, zarif, minimum)
olmaktan çok, pratik olmaya yönelik (kullanımı kolay, verimli,
eksiksiz) olarak tasarlanmıştır.

%description -l uk.UTF-8
Perl - це інтерпретована мова програмування, що запозичує ідеї в C,
sed, awk та мовах командних оболонок (shell). Perl добре підходить для
роботи з процесами та файлами, а найкраще - для обробки текстів.
Особливості Perl - практичність та ефективність. Хоча сфера його
використання дуже широка, найбільш поширене його застосування (та
найсильніша сторона) це, імовірно, утиліти системного адміністрування
та web-програмування. Більша частина CGI скриптів написана на Perl.

%description -l zh_CN.UTF-8
Perl 是一种高级编程语言，起源于 C、sed、awk 和 shell 脚本。
它善于处理进程和文件，尤其是处理文本。Perl
的特点在于其实用性和有效性。
尽管它可用于执行许多不同的任务，但是通常多应用于系统管理实用程序和 Web
编程。\n Web 上的大部分 CGI 脚本均使用 Perl
语言进行编写。您必须在系统中安装 Perl 软件包， 以便处理 Perl 脚本。

%package libs
Summary:	Shared Perl library
Summary(pl.UTF-8):	Biblioteka współdzielona Perla
Group:		Libraries
Conflicts:	perl-base < 1:5.8.8-8.1

%description libs
Shared Perl library.

%description libs -l pl.UTF-8
Biblioteka współdzielona Perla.

%package base
Summary:	Base Perl components for a minimal installation
Summary(pl.UTF-8):	Podstawowe składniki potrzebne do minimalnej instalacji Perla
Group:		Development/Languages/Perl
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	perl-dirs(%{_target_cpu})
Provides:	perl(largefiles)
Provides:	perl-File-Compare = 1.1003
Provides:	perl-File-Spec = 3.12
Provides:	perl-File-Temp = 0.16
Provides:	perl-IO = 1.22
Provides:	perl-Safe = 2.12
Provides:	perl-Socket = 1.78
Provides:	perl-Tie-File = 0.97
# broken, unsupported modules
Obsoletes:	perl-SOAP
Obsoletes:	perl-Sort-PolySort
Conflicts:	perl < 1:5.8.0

%description base
Base components, files, core modules, etc. -- a minimal usable Perl
installation. You are encouraged to install a full Perl (the perl
package) whenever possible.

%description base -l pl.UTF-8
Podstawowe składniki, pliki, główne moduły itp. - minimalna instalacja
Perla, nadająca się do użytku. Zaleca się instalację pełnego Perla
(pakietu perl), jeśli to tylko możliwe.

%package GDBM_File
Summary:	GDBM_File - Perl5 access to the gdbm library
Summary(pl.UTF-8):	GDBM_File - dostęp do biblioteki gdbm w Perlu
Group:		Libraries
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
# FIXME: Set Version: 1.08 and Release: 1 instead of inheriting
#        values from the main package.  Why this causes setting
#        version and release macros up to the end of this spec?

%description GDBM_File
GDBM_File is a module which allows Perl programs to make use of the
facilities provided by the GNU gdbm library.

%description GDBM_File -l pl.UTF-8
GDBM_File jest modułem, który umożliwia programom w Perlu korzystanie
z biblioteki GNU gdbm.

%package devel
Summary:	Perl development files
Summary(pl.UTF-8):	Pliki potrzebne przy tworzeniu własnych aplikacji w Perlu
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento e cabeçalhos para o Perl
Group:		Development/Libraries
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	%{name}-tools-pod = %{epoch}:%{version}-%{release}
Provides:	perl-CPAN = 1.76_02
Provides:	perl-Devel-DProf = 20050603.00
Provides:	perl-Devel-PPPort = 3.06_01
Provides:	perl-Devel-Peek = 1.03
Provides:	perl-ExtUtils-Embed = 1.2506_01
Provides:	perl-ExtUtils-MakeMaker = 6.30
Obsoletes:	perl-lib-devel

%description devel
Components required for developing applications which embed a Perl
interpreter and compiling Perl modules.

%description devel -l pl.UTF-8
Składniki potrzebne do tworzenia aplikacji osadzających interpreter
Perla oraz kompilowania modułów Perla.

%package doc-pod
Summary:	Perl documentation in POD format
Summary(pl.UTF-8):	Dokumentacja Perla w formacie POD
Group:		Documentation
Requires:	perldoc
Obsoletes:	perl-pod

%description doc-pod
Practical Extraction and Report Language - POD docs.

%description doc-pod -l pl.UTF-8
Practical Extraction and Report Language - dokumentacja w formacie
POD.

%package doc-reference
Summary:	Perl reference documentation
Summary(pl.UTF-8):	Dokumentacja Perla
Group:		Documentation

%description doc-reference
Reference documentation for the Practical Extraction and Report
Language and it's interpreter in the man(1) format.

%description doc-reference -l pl.UTF-8
Dokumentacja referencyjna w formacie man do języka Perl (Practical
Extraction and Report Language) i jego interpretera.

%package modules
Summary:	Modules from the core Perl distribution
Summary(pl.UTF-8):	Moduły z podstawowej dystrybucji Perla
Group:		Libraries
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Provides:	perl-Attribute-Handlers = 0.78_02
Provides:	perl-CGI = 3.15
Provides:	perl-Class-ISA = 0.33
Provides:	perl-Digest = 1.14
Provides:	perl-Digest-MD5 = 2.36
Provides:	perl-Filter-Simple = 0.82
Provides:	perl-FindBin = 1.47
#Provides:	perl-Hash-Utils = 0.05	Data::Util is missing
Provides:	perl-I18N-LangTags = 0.35
Provides:	perl-IPC-SysV = 1.04
Provides:	perl-Locale-Codes = 2.07
Provides:	perl-Locale-Maketext = 1.09
Provides:	perl-MIME-Base64 = 3.07
Provides:	perl-Math-BigInt = 1.77
Provides:	perl-Math-BigRat = 0.15
Provides:	perl-Math-Trig = 1.03
Provides:	perl-Memoize = 1.01
Provides:	perl-NEXT = 0.60
Provides:	perl-PerlIO-via-QuotedPrint = 0.06
Provides:	perl-Pod-LaTeX = 0.58
Provides:	perl-Pod-Parser = 1.32
Provides:	perl-Scalar-List-Utils = 1.18
Provides:	perl-Storable = 2.15
Provides:	perl-Term-ANSIColor = 1.10
Provides:	perl-Term-Cap = 1.09
Provides:	perl-Test = 1.25
Provides:	perl-Test-Harness = 2.56
Provides:	perl-Test-Simple = 0.62
Provides:	perl-Text-Balanced = 1.95
Provides:	perl-Text-ParseWords = 3.24
Provides:	perl-Text-Soundex = 1.01
# XXX: I'm not sure what to do with this one...
#Provides:	perl-Text-Tabs+Wrap = 2005.0824(01)
Provides:	perl-Time-HiRes = 1.86
Provides:	perl-UNIVERSAL = 1.01
Provides:	perl-Unicode-Collate = 0.52
Provides:	perl-Unicode-Normalize = 0.32
Provides:	perl-libnet = 1.19
Obsoletes:	perl-Encode-compat
Obsoletes:	perl-lib

%description modules
Practical Extraction and Report Language - modules from the core
distribution.

%description modules -l pl.UTF-8
Practical Extraction and Report Language - moduły z podstawowej
dystrybucji.

%package perldoc
Summary:	perldoc - Look up Perl documentation in pod format
Summary(pl.UTF-8):	perldoc - przeszukiwanie dokumentacji Perla w formacie pod
Group:		Development/Tools
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	%{name}-tools-pod = %{epoch}:%{version}-%{release}
Provides:	perldoc = 3.13@%{version}

%description perldoc
perldoc looks up a piece of documentation in .pod format that is
embedded in the Perl installation tree or in a Perl script, and
displays it via "pod2man | nroff -man | $PAGER". This is primarily
used for the documentation for the Perl library modules.

%description perldoc -l pl.UTF-8
perldoc wyszukuje fragment dokumentacji w formacie .pod osadzony w
drzewie instalacji Perla lub w skypcie perlowym i wyświetla go przez
"pod2man | nroff -man | $PAGER". Program ten używany jest głównie do
dokumentacji modułów z bibliotek Perla.

%package -n sperl
Summary:	Perl setuid root binaries for use with setuid Perl scripts
Summary(de.UTF-8):	sperl zur Verwendung mit setuid Perl-Skripts
Summary(es.UTF-8):	sperl, para uso con los scrips de Perl setuid
Summary(fr.UTF-8):	sperl, à utiliser avec les scripts Perl setuid
Summary(it.UTF-8):	sperl, da usare con gli script di Perl setuid
Summary(ja.UTF-8):	Setuid Perl scripts と一緒に使用するための suidperl
Summary(ko.UTF-8):	Setuid 펄 스크립트와 함께 사용되는 suidperl
Summary(pl.UTF-8):	Binaria setuid root Perla dla setuid-owych skryptów Perla
Summary(pt.UTF-8):	O suidperl, para usar com os programas de Perl 'setuid'
Summary(ru.UTF-8):	SUID версия языка Perl
Summary(sv.UTF-8):	sperl, att användas med setuid perlskript
Summary(uk.UTF-8):	SUID-версія мови Perl
Summary(zh_CN.UTF-8):	sperl，用来与 setuid Perl 脚本一起使用
Group:		Development/Languages/Perl
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Obsoletes:	perl-suidperl

%description -n sperl
sperl is a setuid root binary copy of Perl that allows for (hopefully)
more secure running of setuid Perl scripts.

%description -n sperl -l de.UTF-8
sperl ist eine binäre setuid Kopie von Perl, mit der (hoffentlich)
setuid-Skripts sicherer ausgeführt werden können.

%description -n sperl -l es.UTF-8
sperl es una copia binaria de setuid para Perl que le permite una
ejecución más segura de los scripts de Perl setuid.

%description -n sperl -l fr.UTF-8
sperl est une copie binaire setuid de Perl qui permet une exécution
plus sûre de scripts Perl setuid.

%description -n sperl -l it.UTF-8
sperl è una copia binaria setuid di Perl che consente un'esecuzione
più sicura di script di Perl setuid.

%description -n sperl -l ja.UTF-8
sperl は setuid Perl scripts.をもっと安全に動作できる(期待のある)為の
Perl のsetuid バイナリ コピーです。

%description -n sperl -l pl.UTF-8
sperl jest to kopia setuid root programu binarnego Perl umożliwiająca
bezpieczniejsze (miejmy nadzieję) uruchamianie setuidowych skryptów
Perla.

%description -n sperl -l pt.UTF-8
O suidperl é uma cópia do Perl com 'setuid' que permite uma execução
mais segura dos 'scripts' de Perl 'setuid'.

%description -n sperl -l ru.UTF-8
Suid perl испльзуется для того, чтобы дать возможность создавать
скрипты с утановленным битом SUID. Хотя в него встроено достаточно
много проверок, призваных обеспечить безопасность его использования
suid perl все равно представляет собой значительную потенциальную
опасность.

%description -n sperl -l sv.UTF-8
suidperl är en setuid binärkopia av pers som tillåter
(förhoppningsvis) säkrare körning av setuid perlskript.

%description -n sperl -l zh_CN.UTF-8
suidperl 是 Perl 的 setuid 二进制副本。它允许（希望如此） 更安全地运行
setuid perl 脚本。

%package tools
Summary:	Various tools from the core Perl distribution
Summary(pl.UTF-8):	Różne narzędzia z podstawowej dystrybucji Perla
Group:		Applications
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description tools
Various tools from the core Perl distribution:
a2p		- Awk to Perl translator
find2perl	- translate find command lines to Perl code
piconv		- iconv(1), reinvented in Perl
psed, s2p	- a stream editor
and others.

%description tools -l pl.UTF-8
Różne narzędzia z podstawowej dystrybucji Perla:
a2p		- translator skryptów Awka do Perla
find2perl	- tłumaczenie linii poleceń programu find na kod w Perlu
piconv		- iconv(1) napisany w Perlu
psed, s2p	- edytor strumieniowy
i inne.

%package tools-devel
Summary:	Developer's tools from the core Perl distribution
Summary(pl.UTF-8):	Narzędzia z podstawowej dystrybucji Perla, przeznaczone dla programistów
Group:		Development/Tools
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description tools-devel
Various tools from the core Perl distribution:
c2ph, pstruct	- Dump C structures as generated from C<cc -g -S> stabs
dprofpp		- display Perl profile data
enc2xs		- Perl Encode Module Generator
h2ph		- convert .h C header files to .ph Perl header files
h2xs		- convert .h C header files to Perl extensions
perlcc		- generate executables from Perl programs
perlivp		- Perl Installation Verification Procedure
pl2pm		- Rough tool to translate Perl4 .pl files to Perl5 .pm modules.
splain		- force verbose warning diagnostics

%description tools-devel -l pl.UTF-8
Różne narzędzia z podstawowej dystrybucji Perla:
c2ph, pstruct	- zrzucanie struktur C w postaci generowanej z tablic
		  symboli z cc -g -S
dprofpp		- wyświetlanie perlowych danych profilujących
enc2xs	 	- generator modułów kodujących w Perlu
h2ph		- konwerter plików nagłówkowych .h z C na perlowe pliki
	 	  nagłówkowe .ph
h2xs	 	- konwerter plików nagłówkowych .h z C na rozszerzenia
		  Perla
perlcc	 	- generator binarek z programów w Perlu
perlivp	 	- procedura weryfikacji instalacji Perla
pl2pm		- zgrubne narzędzie do tłumaczenia plików pl Perla 4 na
		  moduły .pm Perla 5
splain		- wymuszenie obszernych ostrzeżeń diagnostycznych

%package tools-pod
Summary:	Tools for manipulating files in the POD format
Summary(pl.UTF-8):	Narzędzia do przetwarzania plików w formacie POD
Group:		Applications
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description tools-pod
Tools for manipulating files in the POD (Plain Old Documentation)
format:
pod2html	- convert .pod files to .html files
pod2latex	- convert pod documentation to LaTeX format
pod2man		- convert POD data to formatted *roff input
pod2text	- convert POD data to formatted ASCII text
pod2usage	- print usage messages from embedded pod docs in files
podchecker	- check the syntax of POD format documentation files
podselect	- print selected sections of pod documentation

%description tools-pod -l pl.UTF-8
Narzędzia do przetwarzania plików w formacie POD (Plain Old
Documentation):
pod2html	- konwerter plików .pod do plików .html
pod2latex	- konwerter dokumentacji pod do formatu LaTeX
pod2man		- konwerter danych POD na wejście sformatowane dla *roffa
pod2text	- konwerter danych POD na sformatowany tekst ASCII
pod2usage	- wypisanie informacji o używaniu programu z dokumentacji
		  osadzonej w plikach
podchecker	- kontrola składni dokumentacji w formacie POD
podselect	- wypisanie wybranych sekcji z dokumentacji POD

%package -n microperl
Summary:	A really minimal Perl, even more minimal than miniperl
Summary(pl.UTF-8):	Naprawdę minimalny Perl, nawet bardziej minimalny niż miniperl
# XXX: is there a more appropiate group?
Group:		Applications

%description -n microperl
microperl is supposed to be able a really minimal Perl, even more
minimal than miniperl. No Configure is needed to build microperl, on
the other hand this means that interfaces between Perl and your
operating system are left very -- minimal.

All this is experimental. If you don't know what to do with microperl
you probably shouldn't. Do not report bugs in microperl; fix the bugs.

%description -n microperl -l pl.UTF-8
microperl ma być naprawdę minimalnym Perlem, nawet bardziej minimalnym
od miniperla. Uruchamianie Configure nie jest potrzebne do zbudowania
microperla, z drugiej strony oznacza to, że interfejs między Perlem a
systemem operacyjnym pozostaje bardzo minimalny.

Całość jest eksperymentalna. Jeśli nie wiesz co zrobić z microperlem,
prawdopodobnie nie powinieneś tego robić. Nie zgłaszaj błędów w
microperlu - popraw je.

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

%build
unset LD_SYMBOLIC_FUNCTIONS || :
sh Configure \
	-des \
	-Dcc="%{__cc}" \
	-Darchname=%{_target_platform} \
	-Dcccdlflags='-fPIC' \
	-Dccdlflags='-rdynamic' \
	-Dldlibpthname=none \
	-Dldflags="%{rpmldflags}" \
	-Dlddlflags="-shared %{rpmldflags}" \
	-Doptimize="%{rpmcflags}" \
	%{?debug:-DDEBUGGING} \
	-Duseshrplib \
	-Dd_dosuid \
	-Dman1dir=%{_mandir}/man1 -Dman1ext=1 \
	-Dman3dir=%{_mandir}/man3 -Dman3ext=3perl \
	-Dvendorman1dir=%{_mandir}/man1 -Dvendorman1ext=1p \
	-Dvendorman3dir=%{_mandir}/man3 -Dvendorman3ext=3pm \
	-Dsiteman1dir=%{_usr}/local/man/man1 -Dsiteman1ext=1p \
	-Dsiteman3dir=%{_usr}/local/man/man3 -Dsiteman3ext=3pm \
	-Dprefix=%{_prefix} -Dvendorprefix=%{_prefix} -Dsiteprefix=%{_usr}/local \
	-Dlibpth="%{_libdir} /%{_lib}" \
	-Dprivlib=%{perl_privlib} -Darchlib=%{perl_archlib} \
	-Dsitelib=%{perl_sitelib} -Dsitearch=%{perl_sitearch} \
	-Dvendorlib=%{perl_vendorlib} -Dvendorarch=%{perl_vendorarch} \
	-Ui_db \
	%{!?with_gdbm: -Ui_dbm -Ui_gdbm -Ui_ndbm} \
	%{?with_gdbm: -Ui_dbm -Di_gdbm -Ui_ndbm} \
	-Dlibswanted="dl m c crypt %{?with_gdbm:gdbm}" \
	-%{?with_threads:D}%{!?with_threads:U}usethreads \
	-Duselargefiles

## why were these three undefined?
#	-Ud_setresgid \
#	-Ud_setresuid \
## what's the problem with this one?
# %ifarch sparc sparc64
#	-Ud_longdbl
# %endif

## {Scalar,List}::Util should be in perl_archlib (it's a bit tricky and should
## probably be done in %%prep, but then Configure would complain (->MANIFEST))
mv ext/List/Util/lib/List/Util.pm ext/List/Util
%{__rm} ext/List/Util/Makefile.PL
cat <<'EOF' > ext/List/Util/Makefile.PL
use ExtUtils::MakeMaker;
WriteMakefile(NAME=>"List::Util", VERSION_FROM=>"Util.pm", DEFINE=>"-DPERL_EXT");
EOF

%{__make} \
	LIBPERL_SONAME=libperl.so.%{_abi} \
	LDDLFLAGS="%{rpmcflags} -shared"

cat > runperl <<'EOF'
#!/bin/sh
LD_PRELOAD="%{_builddir}/%{name}-%{version}/libperl.so.%{_abi}" \
PERL5LIB="%{buildroot}%{perl_privlib}:%{buildroot}%{perl_archlib}" \
exec %{buildroot}%{_bindir}/perl $*
EOF
chmod a+x runperl

## microperl
%if %{with microperl}
%{__rm} uconfig.h
#chmod u+w uconfig.sh
#echo "usemallocwrap='define'" >> uconfig.sh
%{__make} -f Makefile.micro \
	archlib=%{perl_archlib} \
	archlibexp=%{perl_archlib} \
	privlib=%{perl_privlib} \
	privlibexp=%{perl_privlib} \
	archname=%{_target_platform}%{perlthread} \
	osname=%{_host} \
	bin=%{_bindir} \
	scriptdir=%{_bindir} \
	scriptdirexp=%{_bindir} \
	usemallocwrap='define' \
	OPTIMIZE="%{rpmcflags}"
%endif

%{?with_tests:%{__make} test -j1}
#%{?with_tests:%{__make} minitest}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/{ja,ko,zh_CN,zh_TW}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{?with_microperl:install microperl $RPM_BUILD_ROOT%{_bindir}}

## use symlinks instead of hardlinks
%{__ln_s} -f perl%{version}	$RPM_BUILD_ROOT%{_bindir}/perl
%{__ln_s} -f perl%{version}	$RPM_BUILD_ROOT%{_bindir}/suidperl
%{__ln_s} -f c2ph		$RPM_BUILD_ROOT%{_bindir}/pstruct
%{__ln_s} -f psed		$RPM_BUILD_ROOT%{_bindir}/s2p

## Fix lib
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/CORE/libperl.so
%{__ln_s} `%{__perl} -e '$_="'%{perl_archlib}/CORE/libperl.so.%{_abi}'";s|^'%{_libdir}'/*||;print'` \
	$RPM_BUILD_ROOT%{_libdir}/libperl.so.%{_abi}
%{__ln_s} libperl.so.%{_abi} $RPM_BUILD_ROOT%{_libdir}/libperl.so

## Fix Config.pm: remove buildroot path and change man pages extensions
%{__perl} -pi -e 's,%{buildroot}/*,/,g'			$RPM_BUILD_ROOT%{perl_archlib}/Config.pm
%{__perl} -pi -e "s,^man1ext='1',man1ext='1p',"		$RPM_BUILD_ROOT%{perl_archlib}/Config_heavy.pl
%{__perl} -pi -e "s,^man3ext='3perl',man3ext='3pm',"	$RPM_BUILD_ROOT%{perl_archlib}/Config_heavy.pl

## Generate the *.ph files
owd="`pwd`"
cd /usr/include
H2PH=$RPM_BUILD_ROOT%{_bindir}/h2ph
PHDIR=$RPM_BUILD_ROOT%{perl_archlib}
WANTED='
	syscall.h
	syslog.h
	termios.h
	wait.h
	asm/termios.h
	sys/ioctl.h
	sys/socket.h
	sys/syscall.h
	sys/time.h
	linux/posix_types.h
	linux/stddef.h
'
# why it returns non-zero???
%{__perl} $H2PH -a -d $PHDIR $WANTED || :
cd "$owd"

## remove man pages for other operating systems
%{__rm}	$RPM_BUILD_ROOT%{_mandir}/man1/perl{aix,amiga,apollo,beos,bs2000,ce,cygwin,dgux,dos}* \
	$RPM_BUILD_ROOT%{_mandir}/man1/perl{freebsd,hpux,machten,macos,mpeix,os2,os390}* \
	$RPM_BUILD_ROOT%{_mandir}/man1/perl{qnx,solaris,vmesa,vms,vos,win32}*

## symlink perldelta.1.gz -> perlFOOdelta.1.gz
[ -e $RPM_BUILD_ROOT%{_mandir}/man1/perl%(echo %{version} | tr -d .)delta.1 ] || exit 1
rm $RPM_BUILD_ROOT%{_mandir}/man1/perldelta.1
echo ".so perl%(echo %{version} | tr -d .)delta.1" >$RPM_BUILD_ROOT%{_mandir}/man1/perldelta.1

## These File::Spec submodules are for non-Unix systems
%{__rm} $RPM_BUILD_ROOT%{perl_privlib}/File/Spec/[EMOVW]*.pm
rm $RPM_BUILD_ROOT%{_mandir}/man3/File::Spec::{Epoc,Mac,OS2,VMS,Win32}.3perl*

## We already have these *.pod files as man pages
%{__rm} $RPM_BUILD_ROOT%{perl_privlib}/{Encode,Test,Net,Locale{,/Maketext}}/*.pod
rm $RPM_BUILD_ROOT%{perl_privlib}/pod/a2p.pod
%{__rm} $RPM_BUILD_ROOT%{perl_privlib}/*.pod
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/*.pod

## this object file looks unused; why is it there?
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/CORE/sperl.o

install -d doc-base/{Getopt/Long,Switch} \
	doc-devel/ExtUtils \
	doc-modules/{Attribute/Handlers,Filter/Simple,I18N/LangTags,Locale/{Codes,Maketext},Memoize,NEXT,Net/Ping,Term/ANSIColor,Test/Simple,Text/{Balanced,TabsWrap},Unicode/Collate,unicore}

# needed only for tests
%{__rm} $RPM_BUILD_ROOT%{perl_privlib}/Unicode/Collate/keys.txt
mv -f $RPM_BUILD_ROOT%{perl_privlib}/unicore/ReadMe.txt \
	doc-modules/unicore
# source for *.pl
%{__rm} $RPM_BUILD_ROOT%{perl_privlib}/unicore/{*.txt,mktables}
# cpan tools, we use rpm instead of cpan for managing packages (some search tool would be nice to have but...)
%{__rm} $RPM_BUILD_ROOT%{_bindir}/cpan*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/cpan*
# others
%{__rm} $RPM_BUILD_ROOT%{_bindir}/config_data
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/config_data*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/XS::APItest*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/XS::Typemap*

## dir tree for other perl modules
install -d $RPM_BUILD_ROOT{%{perl_vendorlib},%{perl_vendorarch},%{perl_vendorarch}/auto}
owd="`pwd`"

## non-english man pages
%{__bzip2} -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

mv -f $RPM_BUILD_ROOT%{_mandir}/man1/perlcn.* $RPM_BUILD_ROOT%{_mandir}/zh_CN/man1
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/perljp.* $RPM_BUILD_ROOT%{_mandir}/ja/man1
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/perlko.* $RPM_BUILD_ROOT%{_mandir}/ko/man1
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/perltw.* $RPM_BUILD_ROOT%{_mandir}/zh_TW/man1

sed -i -e 's#^\(ld.*=.*\)-Wl,--as-needed\(.*\)#\1 \2#g' $RPM_BUILD_ROOT%{perl_archlib}/Config*.pl

rm -rf $RPM_BUILD_ROOT%{_mandir}/README.perl-non-english-man-pages

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libperl.so.*
%dir %{_libdir}/perl5
%dir %{_libdir}/perl5/%{version}
%dir %{perl_archlib}
%dir %{perl_archlib}/CORE
%attr(755,root,root) %{perl_archlib}/CORE/libperl.so.%{_abi}

%files base
%defattr(644,root,root,755)
%doc doc-base/*
%attr(755,root,root) %{_bindir}/perl
%attr(755,root,root) %{_bindir}/perl%{version}
%{_mandir}/man1/perl.*
%lang(fi) %{_mandir}/fi/man1/perl*
%lang(pl) %{_mandir}/pl/man1/perl*

%dir %{_datadir}/perl5
%dir %{perl_privlib}
%dir %{perl_archlib}/auto

%dir %{_libdir}/perl5/vendor_perl
%dir %{_libdir}/perl5/vendor_perl/%{_abi}
%{perl_vendorarch}
%{perl_vendorlib}

## pragmas
%{perl_privlib}/base.pm
%{_mandir}/man3/base.*
%{perl_privlib}/constant.pm
%{_mandir}/man3/constant.*
%{perl_privlib}/diagnostics.pm
%{_mandir}/man3/diagnostics.*
%{perl_privlib}/feature.pm
%{_mandir}/man3/feature.*
%{perl_privlib}/fields.pm
%{_mandir}/man3/fields.*
%{perl_privlib}/integer.pm
%{_mandir}/man3/integer.*
%{perl_privlib}/overload.pm
%{_mandir}/man3/overload.*
%{perl_privlib}/sort.pm
%{_mandir}/man3/sort.*
%{perl_privlib}/strict.pm
%{_mandir}/man3/strict.*
%{perl_privlib}/subs.pm
%{_mandir}/man3/subs.*
%{perl_privlib}/vars.pm
%{_mandir}/man3/vars.*
%{perl_privlib}/warnings*
%{_mandir}/man3/warnings*

%{perl_archlib}/lib.pm
%{_mandir}/man3/lib.*

## arch-_IN_dependent modules
%{perl_privlib}/Auto*
%{_mandir}/man3/Auto*
%{perl_privlib}/Carp*
%{_mandir}/man3/Carp*
%dir %{perl_privlib}/Class
%{perl_privlib}/Class/Struct*
%{_mandir}/man3/Class::Struct*
%{perl_privlib}/Exporter*
%{_mandir}/man3/Exporter*
%{perl_privlib}/English*
%{_mandir}/man3/English*
%{perl_privlib}/Getopt*
%{_mandir}/man3/Getopt*
%{perl_privlib}/IPC
%{_mandir}/man3/IPC::Open*
%{_mandir}/man3/IPC::Cmd*
%{perl_privlib}/SelectSaver.pm
%{_mandir}/man3/SelectSaver.*
%{perl_privlib}/Symbol.pm
%{_mandir}/man3/Symbol.*
%{perl_privlib}/Tie
%{_mandir}/man3/Tie::*

## arch-dependent modules
%{perl_archlib}/Config*
%{_mandir}/man3/Config.*
%{perl_archlib}/DynaLoader*
%{perl_archlib}/auto/DynaLoader
%{_mandir}/man3/DynaLoader*
%{perl_archlib}/Errno*
%{_mandir}/man3/Errno*
%{perl_archlib}/Safe*
%{_mandir}/man3/Safe*
%{perl_archlib}/XSLoader*
%{_mandir}/man3/XSLoader*

%{perl_archlib}/Cwd.*
%dir %{perl_archlib}/auto/Cwd
%attr(755,root,root) %{perl_archlib}/auto/Cwd/*.so
#%{perl_archlib}/auto/Cwd/*.bs
%{_mandir}/man3/Cwd.*

%{perl_archlib}/Fcntl.*
%dir %{perl_archlib}/auto/Fcntl
%attr(755,root,root) %{perl_archlib}/auto/Fcntl/*.so
#%{perl_archlib}/auto/Fcntl/*.bs
%{_mandir}/man3/Fcntl.*

%{perl_privlib}/File*
%{perl_archlib}/File
%dir %{perl_archlib}/auto/File
%dir %{perl_archlib}/auto/File/*/
%attr(755,root,root) %{perl_archlib}/auto/File/*/*.so
#%{perl_archlib}/auto/File/*/*.bs
%{_mandir}/man3/File*

%{perl_privlib}/IO
%{perl_archlib}/IO*
%dir %{perl_archlib}/auto/IO
%attr(755,root,root) %{perl_archlib}/auto/IO/*.so
%{_mandir}/man3/IO*

%{perl_archlib}/Opcode.*
%dir %{perl_archlib}/auto/Opcode
%attr(755,root,root) %{perl_archlib}/auto/Opcode/*.so
%{_mandir}/man3/Opcode.*

%{perl_privlib}/PerlIO*
%{perl_archlib}/PerlIO
%dir %{perl_archlib}/auto/PerlIO
%dir %{perl_archlib}/auto/PerlIO/*/
%attr(755,root,root) %{perl_archlib}/auto/PerlIO/*/*.so
%{_mandir}/man3/PerlIO*

%{perl_archlib}/POSIX*
%dir %{perl_archlib}/auto/POSIX
%attr(755,root,root) %{perl_archlib}/auto/POSIX/*.so
%{perl_archlib}/auto/POSIX/*.al
%{perl_archlib}/auto/POSIX/*.ix
%{perl_archlib}/auto/POSIX/SigAction
%{perl_archlib}/auto/POSIX/SigRt
%{_mandir}/man3/POSIX.*

%{perl_archlib}/Socket.*
%dir %{perl_archlib}/auto/Socket
%attr(755,root,root) %{perl_archlib}/auto/Socket/*.so
%{_mandir}/man3/Socket.*


%if %{with gdbm}
%files GDBM_File
%defattr(644,root,root,755)
%{perl_archlib}/GDBM_File.*
%dir %{perl_archlib}/auto/GDBM_File
%attr(755,root,root) %{perl_archlib}/auto/GDBM_File/*.so
%{_mandir}/man3/GDBM_File.*
%endif


%files devel
%defattr(644,root,root,755)
%doc doc-devel/*
%attr(755,root,root) %{_libdir}/libperl.so
%{perl_archlib}/CORE/*.h
%{_mandir}/man3/CORE*

# FIXME: Changes file to _docdir (and rm MANIFEST.SKIP?)
%{perl_privlib}/ExtUtils
%{_mandir}/man3/ExtUtils*
%{perl_privlib}/vmsish.pm
%{_mandir}/man3/vmsish.*
%{perl_privlib}/CPAN*
%{_mandir}/man3/CPAN*
%{perl_privlib}/DB.*
%{_mandir}/man3/DB.*
%{perl_privlib}/Module/Build*
%{_mandir}/man3/Module::Build*

%{perl_archlib}/O.*
%{_mandir}/man3/O.*

%{perl_archlib}/B
%{perl_archlib}/B.pm
%dir %{perl_archlib}/auto/B
%attr(755,root,root) %{perl_archlib}/auto/B/*.so
%{_mandir}/man3/B[.:]*

#%{perl_archlib}/ByteLoader.*
#%dir %{perl_archlib}/auto/ByteLoader
#%attr(755,root,root) %{perl_archlib}/auto/ByteLoader/*.so
#%{perl_archlib}/auto/ByteLoader/*.bs
#%{_mandir}/man3/ByteLoader.*

%{perl_privlib}/Devel
%{perl_archlib}/Devel
%dir %{perl_archlib}/auto/Devel
%dir %{perl_archlib}/auto/Devel/*/
%attr(755,root,root) %{perl_archlib}/auto/Devel/*/*.so
#%{perl_archlib}/auto/Devel/*/*.bs
%{_mandir}/man3/Devel::*

#%{perl_archlib}/XS
#%dir %{perl_archlib}/auto/XS
#%dir %{perl_archlib}/auto/XS/*/
#%attr(755,root,root) %{perl_archlib}/auto/XS/*/*.so
#%{perl_archlib}/auto/XS/*/*.bs
#%{_mandir}/man3/XS::*


%files doc-pod
%defattr(644,root,root,755)
%{perl_privlib}/pod/perl.pod
%{perl_privlib}/pod/perl[5abceghijklmnopqrstuvwx]*.pod
%{perl_privlib}/pod/perld[!i]*.pod
%{perl_privlib}/pod/perlf[!au]*.pod


%files doc-reference
%defattr(644,root,root,755)
%{_mandir}/man1/perl[5aefghlmnoprstuvwx]*
%{_mandir}/man1/perlbo*
%{_mandir}/man1/perlcall.*
%{_mandir}/man1/perlcheat.*
%{_mandir}/man1/perlclib.*
%{_mandir}/man1/perlcommunity.*
%{_mandir}/man1/perlcompile.*
%{_mandir}/man1/perld[!o]*
%{_mandir}/man1/perli[!v]*

%lang(zh_CN) %{_mandir}/zh_CN/man1/perlcn.*
%lang(ja) %{_mandir}/ja/man1/perljp.*
%lang(ko) %{_mandir}/ko/man1/perlko.*
%lang(zh_TW) %{_mandir}/zh_TW/man1/perltw.*


%files modules
%defattr(644,root,root,755)
%doc doc-modules/*

%{perl_privlib}/unicore

## pragmas
%{perl_privlib}/attributes.pm
%{_mandir}/man3/attributes.*
%{perl_privlib}/autouse.pm
%{_mandir}/man3/autouse.*
%{perl_privlib}/big*.pm
%{_mandir}/man3/big*
%{perl_privlib}/blib.pm
%{_mandir}/man3/blib.*
%{perl_privlib}/bytes.pm
%{_mandir}/man3/bytes.*
%{perl_privlib}/charnames.pm
%{_mandir}/man3/charnames.*
%{perl_privlib}/encoding
%{_mandir}/man3/encoding::*
%{perl_privlib}/filetest.pm
%{_mandir}/man3/filetest.*
%{perl_privlib}/if.pm
%{_mandir}/man3/if.*
%{perl_privlib}/less.pm
%{_mandir}/man3/less.*
%{perl_privlib}/locale.pm
%{_mandir}/man3/locale.*
%{perl_privlib}/mro.pm
%{_mandir}/man3/mro.*
%{perl_privlib}/open.pm
%{_mandir}/man3/open.*
%{perl_privlib}/sigtrap.pm
%{_mandir}/man3/sigtrap.*
%{perl_privlib}/utf8.pm
%{_mandir}/man3/utf8.*
%{perl_privlib}/version.pm
%{_mandir}/man3/version.*

%{perl_archlib}/attrs.pm
%dir %{perl_archlib}/auto/attrs
%attr(755,root,root) %{perl_archlib}/auto/attrs/*.so
%{_mandir}/man3/attrs.*
%{perl_archlib}/re.pm
%dir %{perl_archlib}/auto/re
%attr(755,root,root) %{perl_archlib}/auto/re/*.so
%{_mandir}/man3/re.*
%{perl_archlib}/encoding.pm
%{_mandir}/man3/encoding.*
%{perl_archlib}/ops.pm
%{_mandir}/man3/ops.*

%if %{with threads}
%{perl_archlib}/threads*
%dir %{perl_archlib}/auto/threads
%dir %{perl_archlib}/auto/threads/shared
%attr(755,root,root) %{perl_archlib}/auto/threads/*.so
%attr(755,root,root) %{perl_archlib}/auto/threads/shared/*.so
%{_mandir}/man3/t*
%endif

## old *.pl files
%{perl_privlib}/*.pl

## *.ph files (could be made a separate package, but an autohelper's support is needed)
%{perl_archlib}/*.ph
%{perl_archlib}/asm
%{perl_archlib}/asm-generic
%ifarch sparc64
%{perl_archlib}/asm-sparc
%{perl_archlib}/asm-sparc64
%endif
%{perl_archlib}/bits
%{perl_archlib}/gnu
%{perl_archlib}/linux
%{perl_archlib}/sys

%{perl_archlib}/Compress
%dir %{perl_archlib}/auto/Compress
%dir %{perl_archlib}/auto/Compress/Raw
%dir %{perl_archlib}/auto/Compress/Raw/Zlib
%attr(755,root,root) %{perl_archlib}/auto/Compress/Raw/Zlib/*.so
%{perl_archlib}/auto/Compress/Raw/Zlib/*.ix
%dir %{perl_archlib}/auto/Compress/Zlib
%{perl_archlib}/auto/Compress/Zlib/*.ix
%{_mandir}/man3/Compress*

%{perl_archlib}/Data
%dir %{perl_archlib}/auto/Data
%dir %{perl_archlib}/auto/Data/Dumper
%attr(755,root,root) %{perl_archlib}/auto/Data/Dumper/*.so
%{_mandir}/man3/Data*

%{perl_privlib}/Digest*
%{perl_archlib}/Digest
%dir %{perl_archlib}/auto/Digest
%dir %{perl_archlib}/auto/Digest/*/
%attr(755,root,root) %{perl_archlib}/auto/Digest/*/*.so
%{_mandir}/man3/Digest*

# FIXME: Changes file
%{perl_privlib}/DBM_Filter*
%{_mandir}/man3/DBM_Filter*

# FIXME: *.h to devel(?), check out the use for *.e2x files
%{perl_privlib}/Encode
%{perl_archlib}/Encode*
%dir %{perl_archlib}/auto/Encode
%dir %{perl_archlib}/auto/Encode/*/
%attr(755,root,root) %{perl_archlib}/auto/Encode/*/*.so
%{_mandir}/man3/Encode*

# FIXME: README and Changes files
%{perl_privlib}/Filter
%{perl_archlib}/Filter
%dir %{perl_archlib}/auto/Filter
%dir %{perl_archlib}/auto/Filter/Util
%dir %{perl_archlib}/auto/Filter/Util/Call
%attr(755,root,root) %{perl_archlib}/auto/Filter/Util/Call/*.so
%{_mandir}/man3/Filter*

%{perl_archlib}/Hash
%dir %{perl_archlib}/auto/Hash
%dir %{perl_archlib}/auto/Hash/*/
%dir %{perl_archlib}/auto/Hash/*/FieldHash
%attr(755,root,root) %{perl_archlib}/auto/Hash/*/*.so
%attr(755,root,root) %{perl_archlib}/auto/Hash/*/*/*.so
%{_mandir}/man3/Hash::*

%{perl_privlib}/I18N
%{perl_archlib}/I18N
%dir %{perl_archlib}/auto/I18N
%dir %{perl_archlib}/auto/I18N/*/
%attr(755,root,root) %{perl_archlib}/auto/I18N/*/*.so
%{perl_archlib}/auto/I18N/*/*.ix
%{_mandir}/man3/I18N::*

%{perl_archlib}/IPC
%dir %{perl_archlib}/auto/IPC
%dir %{perl_archlib}/auto/IPC/*/
%attr(755,root,root) %{perl_archlib}/auto/IPC/*/*.so
%{_mandir}/man3/IPC::[MS]*

%{perl_archlib}/List
%dir %{perl_archlib}/auto/List
%dir %{perl_archlib}/auto/List/*/
%attr(755,root,root) %{perl_archlib}/auto/List/*/*.so
%{_mandir}/man3/List::*

%{perl_privlib}/Math
%{perl_archlib}/Math
%dir %{perl_archlib}/auto/Math
%dir %{perl_archlib}/auto/Math/*/
%dir %{perl_archlib}/auto/Math/*/*/
%attr(755,root,root) %{perl_archlib}/auto/Math/*/*/*.so
%{_mandir}/man3/Math::*

%{perl_archlib}/MIME
%dir %{perl_archlib}/auto/MIME
%dir %{perl_archlib}/auto/MIME/Base64
%attr(755,root,root) %{perl_archlib}/auto/MIME/Base64/*.so
%{_mandir}/man3/MIME::*

%{perl_archlib}/SDBM_File.*
%dir %{perl_archlib}/auto/SDBM_File
%attr(755,root,root) %{perl_archlib}/auto/SDBM_File/*.so
%{_mandir}/man3/SDBM_File.*

%{perl_archlib}/Storable.*
%dir %{perl_archlib}/auto/Storable
%attr(755,root,root) %{perl_archlib}/auto/Storable/*.so
%{perl_archlib}/auto/Storable/*.al
%{perl_archlib}/auto/Storable/*.ix
%{_mandir}/man3/Storable.*

%{perl_archlib}/Sys
%dir %{perl_archlib}/auto/Sys
%dir %{perl_archlib}/auto/Sys/*/
%attr(755,root,root) %{perl_archlib}/auto/Sys/*/*.so
%{perl_archlib}/auto/Sys/*/*.ix
%{_mandir}/man3/Sys::*

%{perl_archlib}/Text
%dir %{perl_archlib}/auto/Text
%dir %{perl_archlib}/auto/Text/Soundex
%attr(755,root,root) %{perl_archlib}/auto/Text/Soundex/*.so
#%{_mandir}/man3/Text::Soundex*	# listed later

%{perl_privlib}/Time
%{perl_archlib}/Time
%dir %{perl_archlib}/auto/Time
%dir %{perl_archlib}/auto/Time/*/
%attr(755,root,root) %{perl_archlib}/auto/Time/*/*.so
%{_mandir}/man3/Time::*

%dir %{perl_privlib}/Unicode
%{perl_privlib}/Unicode/*.pm
%{perl_privlib}/Unicode/Collate
%{perl_archlib}/Unicode
%dir %{perl_archlib}/auto/Unicode
%dir %{perl_archlib}/auto/Unicode/*
%attr(755,root,root) %{perl_archlib}/auto/Unicode/*/*.so
%{_mandir}/man3/Unicode::*

%{perl_privlib}/AnyDBM*
%{_mandir}/man3/AnyDBM*
%{perl_privlib}/Archive*
%{_mandir}/man3/Archive*
%{perl_privlib}/Attribute
%{_mandir}/man3/Attribute*
%{perl_privlib}/Benchmark*
%{_mandir}/man3/Benchmark*
%{perl_privlib}/CGI*
%{_mandir}/man3/CGI*
%{perl_privlib}/Class/ISA*
%{_mandir}/man3/Class::ISA*
%{perl_privlib}/Config
%{_mandir}/man3/Config::*
%{perl_privlib}/DirHandle*
%{_mandir}/man3/DirHandle*
%{perl_privlib}/Dumpvalue.*
%{_mandir}/man3/Dumpvalue.*
%{perl_privlib}/Env.*
%{_mandir}/man3/Env.*
%{perl_privlib}/Fatal.*
%{_mandir}/man3/Fatal.*
%{perl_privlib}/FindBin.*
%{_mandir}/man3/FindBin.*
# FIXME: README and Changes files
%{perl_privlib}/IPC
%{perl_privlib}/Log
%{_mandir}/man3/Log::*
%{perl_privlib}/Locale
%{_mandir}/man3/Locale::*
%{perl_privlib}/Memoize*
%{_mandir}/man3/Memoize*
%dir %{perl_privlib}/Module
%{perl_privlib}/Module/[CLP]*
%{_mandir}/man3/Module::[CLP]*
%{perl_privlib}/NEXT.pm
%{_mandir}/man3/NEXT*
# FIXME: README and Changes files
%dir %{perl_privlib}/Net
%{perl_privlib}/Net/*.eg
%{perl_privlib}/Net/*.pm
%{perl_privlib}/Net/FTP
%{_mandir}/man3/Net::*
%{perl_privlib}/Object
%{_mandir}/man3/Object::*
%{perl_privlib}/Package
%{_mandir}/man3/Package::*
%{perl_privlib}/Params
%{_mandir}/man3/Params::*
%{perl_privlib}/Pod
%{_mandir}/man3/Pod::*
%{perl_archlib}/Scalar
%{_mandir}/man3/Scalar::*
%{perl_privlib}/Search
%{_mandir}/man3/Search::*
%{perl_privlib}/SelfLoader.*
%{_mandir}/man3/SelfLoader.*
%{perl_privlib}/Shell.*
%{_mandir}/man3/Shell.*
# FIXME: README and Changes files
%{perl_privlib}/Switch.*
%{_mandir}/man3/Switch.*
# FIXME: README and Changes files
%{perl_privlib}/Term
%{_mandir}/man3/Term::*
# FIXME: README and Changes files
%{perl_privlib}/Test*
%{_mandir}/man3/Test*
%{perl_privlib}/Text
%{_mandir}/man3/Text::*
%if %{with threads}
%{perl_privlib}/Thread*
%{_mandir}/man3/Thread*
%endif
# XXX: to perl-base?
%{perl_privlib}/UNIVERSAL.*
%{_mandir}/man3/UNIVERSAL.*
# FIXME: README and Changes files
%{perl_privlib}/User
%{_mandir}/man3/User::*


%files perldoc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perldoc
%dir %{perl_privlib}/pod
%{perl_privlib}/pod/perldiag.pod
%{perl_privlib}/pod/perlfaq*.pod
%{perl_privlib}/pod/perlfunc.pod
%{_mandir}/man1/perldoc.*


%files -n sperl
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/sperl%{version}
%attr(755,root,root) %{_bindir}/suidperl

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/a2p
%{_mandir}/man1/a2p.*
%attr(755,root,root) %{_bindir}/corelist
%{_mandir}/man1/corelist.*
%attr(755,root,root) %{_bindir}/find2perl
%{_mandir}/man1/find2perl.*
%attr(755,root,root) %{_bindir}/instmodsh
%{_mandir}/man1/instmodsh.*
%attr(755,root,root) %{_bindir}/libnetcfg
%{_mandir}/man1/libnetcfg.*
%attr(755,root,root) %{_bindir}/piconv
%{_mandir}/man1/piconv.*
%attr(755,root,root) %{_bindir}/psed
%{_mandir}/man1/psed.*
%attr(755,root,root) %{_bindir}/ptar
%{_mandir}/man1/ptar.*
%attr(755,root,root) %{_bindir}/ptardiff
%{_mandir}/man1/ptardiff.*
%attr(755,root,root) %{_bindir}/s2p
%{_mandir}/man1/s2p.*
%attr(755,root,root) %{_bindir}/shasum
%{_mandir}/man1/shasum.*

%files tools-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perlbug
%{_mandir}/man1/perlbug.*
%attr(755,root,root) %{_bindir}/c2ph
%attr(755,root,root) %{_bindir}/pstruct
%{_mandir}/man1/c2ph.*
%{_mandir}/man1/pstruct.*
%attr(755,root,root) %{_bindir}/dprofpp
%{_mandir}/man1/dprofpp.*
%attr(755,root,root) %{_bindir}/enc2xs
%{_mandir}/man1/enc2xs.*
%attr(755,root,root) %{_bindir}/h2ph
%{_mandir}/man1/h2ph.*
%attr(755,root,root) %{_bindir}/h2xs
%{_mandir}/man1/h2xs.*
#%attr(755,root,root) %{_bindir}/perlcc
#%{_mandir}/man1/perlcc.*
%attr(755,root,root) %{_bindir}/perlivp
%{_mandir}/man1/perlivp.*
%attr(755,root,root) %{_bindir}/pl2pm
%{_mandir}/man1/pl2pm.*
%attr(755,root,root) %{_bindir}/prove
%{_mandir}/man1/prove.*
%attr(755,root,root) %{_bindir}/splain
%{_mandir}/man1/splain.*
%attr(755,root,root) %{_bindir}/xsubpp
%{_mandir}/man1/xsubpp.*

%files tools-pod
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pod*
%{_mandir}/man1/pod*

%if %{with microperl}
%files -n microperl
%defattr(644,root,root,755)
%doc README.micro Todo.micro
%attr(755,root,root) %{_bindir}/microperl
%endif
