#
# Conditional build:
# _without_tests      - do not perform "make test"
# _without_threads    - build without support for threads
# _without_largefiles - build without large file support
#
# TODO:
# - Think about unicore.  If uf8*.pm, encode.pm, charnamess.pm (and
#   probably others) are in the perl-base package, unicore should also
#   be there.  But it's 5MB...
# - Think about the package separation.  Split between perl, perl-base
#   and perl-modules is far from obvius.
# - find out why *.so and *.bs files for some pragmas are ,,listed twice''
# - merge some fixes from 5.6.1 on HEAD
# - fix "FIXME"s, review "XXX"s
# - fix perl.prov's handling in rpm -- it should use the __perl macro
# - include gdbm-dependent modules, they aren't distributed standalone
#   anymore
# - fix some duplicate files
# - *TESTING*
#

%define		__find_provides	%{_builddir}/%{name}-%{version}/find-perl-provides.sh
%define		perlthread	%{?!_without_threads:-thread-multi}

%define		perl_privlib	%{_datadir}/perl5/%{version}
%define		perl_archlib	%{_libdir}/perl5/%{version}/%{_target_platform}%{perlthread}
%define		perl_sitelib	%{_usr}/local/share/perl5
%define		perl_sitearch	%{_usr}/local/lib/perl5/%{version}/%{_target_platform}%{perlthread}
%define		perl_vendorlib	%{_datadir}/perl5/vendor_perl
%define		perl_vendorarch	%{_libdir}/perl5/vendor_perl/%{version}/%{_target_platform}%{perlthread}

Summary:	Practical Extraction and Report Language (Perl)
Summary(cs):	Programovací jazyk Perl
Summary(da):	Programmeringssproget Perl
Summary(de):	Praktische Extraktions- und Berichtsprache
Summary(es):	Lenguaje práctica de extracción y listado
Summary(fr):	Langage de programmation Perl
Summary(id):	Bahasa pemrograman Perl
Summary(is):	Forritunarmáliğ Perl
Summary(it):	Perl: linguaggio di programmazione
Summary(ja):	Perl ¥×¥í¥°¥é¥ß¥ó¥°¸À¸ì
Summary(ko):	ÆŞ ÇÁ·Î±×·¡¹Ö ¾ğ¾î
Summary(no):	Programmeringsspråket Perl
Summary(pl):	Interpreter jêzyka Perl (Practical Extraction and Report Language)
Summary(pt):	A linguagem de programação Perl
Summary(pt_BR):	Linguagem prática de extração e relatório
Summary(ru):	ñÚÙË ĞÒÏÇÒÁÍÍÉÒÏ×ÁÎÉÑ Perl
Summary(sk):	Programovací jazyk Perl
Summary(sl):	Programski jezik Perl
Summary(sv):	Programmeringsspråket Perl
Summary(tr):	Kabuk yorumlama dili
Summary(zh_CN):	Perl ±à³ÌÓïÑÔ¡£
Name:		perl
Version:	5.8.0
Release:	0.23%{?_without_threads:_nothr}%{?_without_largefiles:_nolfs}
Epoch:		1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/src/%{name}-%{version}.tar.gz
Source1:	%{name}-non-english-man-pages.tar.bz2
Source2:	%{name}.prov
Source3:	find-perl-provides.sh
Patch0:		%{name}_580-noroot_install.patch
Patch1:		%{name}_580-INC.patch
Patch2:		%{name}_580-MakeMaker.patch
# failed
#Patch5:	%{name}-syslog.patch
# failed
#Patch6:	%{name}-CGI-upload-tmpdir.patch
# what is this f* one for?!
#Patch7:	%{name}-LD_RUN_PATH.patch
Patch8:		%{name}_580-errno_h-parsing.patch
Patch9:		%{name}_580-use-LD_PRELOAD-for-libperl.so.patch
# *weird*
#Patch10:	%{name}-sitearch.patch
Patch11:	%{name}_580-soname.patch
# failed; is it still necessary?
#Patch13:	%{name}-gcc3.patch
Patch14:	%{name}_580-perluniintro.patch
Patch15:	%{name}_580-Safe.patch
URL:		http://www.perl.com/
%{?!_without_largefiles:Provides:	perl(largefiles)}
Requires:	%{name}-base = %{version}
Requires:	%{name}-modules = %{version}
Requires:	perldoc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl is an interpreted language optimized for scanning arbitrary text
files, extracting information from those text files, and printing
reports based on that information. It's also a good language for many
system management tasks. The language is intended to be practical
(easy to use, efficient, complete) rather than beautiful (tiny,
elegant, minimal).

%description -l cs
Perl je vy¹¹í programovací jazyk s koøeny v jazyce C, sed, awk a
shellovıch skriptech. Perl je vhodnı pro manipulace s procesy a
soubory, ale obzvlá¹tì se hodí ke zpracovávání textù. Perl vyniká
praktièností úèinností. I kdy¾ se pou¾ívá prakticky na cokoli, vìt¹ina
Perlovıch programù slou¾í jako správcovské utility nebo programy pro
WWW. V Perlu je napsáno velmi mnoho CGI skriptù pro WWW servery na
celém svìtì.

%description -l da
Perl er et høgniveauprogramsprog med røtter i C, sed, awk og
skalskript. Perl er godt på at behandle processer og filer, og er
særskilt godt på at behandle text. Utmærkende for Perl er at det er
praktisk og effektivt. Det bruges for at gøre en mængd forskellige
saker, men de almindeligeste programmerne er systemadministration og
webbprogrammering. En stor andel af CGI-skripten på webben er skrivna
i Perl. Du behøver installere pakken perl på dit system så at ditt
system kan behandle Perlskript.

%description -l de
Perl ist eine Interpreter-Sprache, die zum Durchsuchen beliebiger
Text- dateien, Extrahieren von Informationen aus diesen Dateien und
Drucken von auf diesen Informationen basierenden Berichten optimiert
ist. Die Sprache eignet sich außerdem für viele
Systemverwaltungsaufgaben. Sie ist eher praktisch (einfache
Anwendung,effizient, vollständig) als schön (winzig, elegant,
minimal).

%description -l es
Perl es un lenguaje interpretado, optimizado para manejar archivos
texto, extrayendo información de estos archivos y mostrando listados
basados en esta información. También es un buen lenguaje para varias
tareas de administración de sistema. El lenguaje busca ser más
práctico (fácil de usar, eficiente, completo) que bonito (minúsculo,
elegante, mínimo).

%description -l fr
Perl est un langage interprété, optimisé pour filtrer des fichiers
texte, extraire des informations de ces fichiers, et imprimer des
rapports basés sur ces informations. C'est aussi un bon langage pour
de nombreuses procédures de gestion système. Ce langage se veut
pratique (simple à utiliser, efficace, complet) autant qu'agréable
(conscrit, élégant, minimal).

%description -l id
Perl adalah sebuah bahasa pemrograman tingkat tinggi yang didasarkan
pada C, sed, awk, dan bahasa shell. Perl memiliki kemampuan penanganan
proses dan file yang bagus, tapi terutama kemampuan penanganan teksnya
yang baik. Ciri khas Perl adalah kepraktisan dan efisiensi. Meski
digunakan untuk berbagai hal, aplikasi Perl yang paling umum adalah
utilitas sistem administrasi dan pemrograman web. Sebagian besar skrip
CGI yang ada di web ditulis dalam Perl. Anda perlu memasang paket perl
di sistem agar dapat menjalankan skrip-skrip Perl.

%description -l is
Perl er hás stigs forritunar tungumál sem á rætur sínar ağ rekja til
C, sed, awk, og skeljar forritunar. Perl er góğ í ağ meğhöndla
processa og skrár og er sérstaklega góğ í ağ meğhöndla texta. Perls
kostir eru nytsamleiki og virkni. Á meğan şağ er notağ til ağ gera
marga mismunandi hluti, Perl mest notuğu forrit eru krefisstjórnunar
tól og vef forritun Stór hluti af CGI forritum á vefnum eru skrifağar
í Perl. Şú şarft perl pakkann settan upp á şínu krefi svo şitt kerfi
geti notağ Perl scriptur.

%description -l it
Perl è un linguaggio di programmazione di alto livello derivato dal
linguaggio C, da sed, da awk e dallo scripting delle shell. E' adatto
per la gestione di processi, di file e in particolare di file di
testo. Perl è un linguaggio semplice ed efficiente. Viene utilizzato
per numerosi scopi, ma le sue applicazioni più diffuse sono le utility
di amministrazione del sistema e la programmazione Web. Una grossa
parte degli script CGI nel Web sono scritti in Perl. È consigliabile
installare il pacchetto perl in modo che il sistema sia in grado di
gestire gli script di Perl.

%description -l ja
Perl ¤Ï C¸À¸ì¡¢sed, awk¡¢µÚ¤Ó ¥·¥§¥ë¥¹¥¯¥ê¥×¥Æ¥£¥ó¥°¤Ëº¬¸»¤ò
»ı¤Ä¥Ï¥¤¥ì¥Ù¥ë¤Ê ¥×¥í¥°¥é¥à¸À¸ì¤Ç¤¹¡£Perl ¤Ï¥×¥í¥»¥¹¤ä¥Õ¥¡¥¤¥ë¤Î½èÍı¤Ë
Å¬ÀÚ¤Ç ¡¢ÆÃ¤Ë ¥Æ¥­¥¹¥È½èÍı¤Ë¤ÏºÇÅ¬¤Ç¤¹¡£¤µ¤Ş¤¶¤Ş¤Êºî¶È¤Ë
»ÈÍÑ¤µ¤ì¤Ş¤¹¤¬¡¢ Perl¤ÎºÇ¤âÉÑÈË¤Ê³èÍÑ¤Ï¥·¥¹¥Æ¥à¥¢¥É¥ß¥Ë¥¹¥È¥ì¡¼¥·¥ç¥ó
¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤È web¥×¥í¥°¥é¥ß¥ó¥°¤Ç¤¹¡£web¾å¤Î ÂçÉôÊ¬¤ÎCGI"
¥¹¥¯¥ê¥×¥È¤¬Perl¤Ç½ñ¤«¤ì¤Æ¤¤¤Ş¤¹¡£ ¥·¥¹¥Æ¥à¤¬Perl¥¹¥¯¥ê¥×¥È¤ò
½èÍı½ĞÍè¤ë¤è¤¦¤Ë¤¹¤ë¤¿¤á¤Ë¤Ï perl¥Ñ¥Ã¥±¡¼¥¸¤ò ¥¤¥ó¥¹¥È¡¼¥ë¤¹¤ë
É¬Í×¤¬¤¢¤ê¤Ş¤¹¡£

%description -l pl
Perl jest jêzykiem przeznaczonym do skanowania plików tekstowych,
wyci±gania z nich informacji i drukowania raportu bazuj±cego na tych
informacjach. Jest równie¿ doskona³ym jêzykiem do wielu prac
zwi±zanych z nadzorem systemu. Jêzyk ten jest w zamierzeniu bardziej
praktyczny (³atwy w u¿yciu, wydajny, kompletny) ni¿ piêkny (skromny,
elegancki, minimalny).

%description -l pt
O perl é uma linguagem de programação de alto nível que tem como
raizes o C, sed, awk, e 'shell scripting'. O perl é bom a manipular
processos e ficheiros, e é especialmente bom para manipular texto.
Características do Perl são a eficiência e o uso prático. As
aplicações mais comuns do Perl são utilitários de administração de
sistema e programação Web. Uma grande parte dos 'scripts' CGI na Web
são escritos em Perl. Você precisa do pacote perl instalado no seu
sistema de maneira a que este possa tratar de 'scripts' de Perl.

%description -l pt_BR
Perl é uma linguagem interpretada, otimizada para tratar arquivos
texto, extraindo informação desses arquivos e mostrando relatórios
baseados nessa informação. Também é uma boa linguagem para várias
tarefas de administração de sistema. A linguagem procura ser mais
prática (fácil de usar, eficiente, completa) do que bonita (minúscula,
elegante, mínima).

%description -l ru
Perl - ÜÔÏ ÉÎÔÅÒĞÒÅÔÉÒÕÅÍÙÊ ÑÚÙË ĞÒÏÇÒÁÍÍÉÒÏ×ÁÎÉÑ, ÕÈÏÄÑİÉÊ ËÏÒÎÑÍÉ ×
C, sed, awk É ÑÚÙËÉ ËÏÍÁÎÄÎÙÈ ÏÂÏÌÏŞÅË (shell). Perl ÈÏÒÏÛ ÄÌÑ ÒÁÂÏÔÙ
Ó ĞÒÏÃÅÓÓÁÍÉ É ÆÁÊÌÁÍÉ, Á ÏÓÏÂÅÎÎÏ ÈÏÒÏÛ ÄÌÑ ÚÁÄÁŞ ÏÂÒÁÂÏÔËÉ ÔÅËÓÔÏ×.
ïÓÏÂÅÎÎÏÓÔÉ Perl - ĞÒÁËÔÉŞÎÏÓÔØ É ÜÆÆÅËÔÉ×ÎÏÓÔØ. èÏÔÑ ÏÎ É
ÉÓĞÏÌØÚÕÅÔÓÑ ÄÌÑ ÒÅÛÅÎÉÑ ÓÁÍÙÈ ÒÁÚÎÙÈ ÚÁÄÁŞ, ÎÁÉÂÏÌÅÅ ÒÁÓĞÒÏÓÔÒÁÎÅÎÎÙÅ
ĞÒÉÍÅÎÅÎÉÑ (É ÔÏ, × ŞÅÍ ÏÎ ÓÉÌÅÎ) ÜÔÏ, ×ÅÒÏÑÔÎÏ, ÕÔÉÌÉÔÙ ÓÉÓÔÅÍÎÏÇÏ
ÁÄÍÉÎÉÓÔÒÉÒÏ×ÁÎÉÑ É web-ĞÒÏÇÒÁÍÍÉÒÏ×ÁÎÉÅ. âÏÌØÛÁÑ ŞÁÓÔØ CGI ÓËÒÉĞÔÏ×
ÎÁĞÉÓÁÎÁ ÎÁ Perl.

%description -l sk
Perl je programovací jazyk vy¹¹ej úrovne s koreòmi v C, sed, awk, a
shell skriptoch. Perl má vhodné vlastnosti pre spracovanie procesov a
súborov a je zvlá¹» vhodnı pre spracovanie textu. Jeho cieµmi sú
praktiènos» a efektivita. Aj keï je pou¾ívanı pre mno¾stvo rozliènıch
èinností, jeho najèastej¹ím pou¾itím (a kde vyniká najviac) sú
pravdepodobne nástroje pre správu systému a programovanie na Webe.
Veµká èas» CGI skriptov na Webe je napísaná v Perle. Balík perl
potrebujete ma» nain¹talovanı, aby bol vá¹ systém schopnı spracova»
Perl skripty.

%description -l sv
Perl är ett högnivåprogramspråk med rötter i C, sed, awk och
skalskript. Perl är bra på att hantera processer och filer, och är
särskilt bra på att hantera text. Utmärkande för Perl är att det är
praktiskt och effektivt. Det används för att göra en mängd olika
saker, men de vanligaste tillämpningarna är systemadministration och
webbprogrammering. En stor andel av CGI-skripten på webben är skrivna
i Perl. Du behöver installera paketet perl på ditt system så att ditt

%description -l tr
Perl, metin dosyalarını taramak, bu metin dosyalarından bilgi çıkarmak
ve bu bilgiye dayalı raporlar hazırlamak icin geliştirilmiş bir
yorumlamalı dildir. Ayrıca pek çok sistem yönetimi görevleri için de
yararlı yetenekleri vardır. Perl, güzel (ufak, zarif, minimum)
olmaktan çok, pratik olmaya yönelik (kullanımı kolay, verimli,
eksiksiz) olarak tasarlanmıştır.

%description -l uk
Perl - ÃÅ ¦ÎÔÅÒĞÒÅÔÏ×ÁÎÁ ÍÏ×Á ĞÒÏÇÒÁÍÕ×ÁÎÎÑ, İÏ ÚÁĞÏÚÉŞÕ¤ ¦ÄÅ§ × C,
sed, awk ÔÁ ÍÏ×ÁÈ ËÏÍÁÎÄÎÉÈ ÏÂÏÌÏÎÏË (shell). Perl ÄÏÂÒÅ Ğ¦ÄÈÏÄÉÔØ ÄÌÑ
ÒÏÂÏÔÉ Ú ĞÒÏÃÅÓÁÍÉ ÔÁ ÆÁÊÌÁÍÉ, Á ÎÁÊËÒÁİÅ - ÄÌÑ ÏÂÒÏÂËÉ ÔÅËÓÔ¦×.
ïÓÏÂÌÉ×ÏÓÔ¦ Perl - ĞÒÁËÔÉŞÎ¦ÓÔØ ÔÁ ÅÆÅËÔÉ×Î¦ÓÔØ. èÏŞÁ ÓÆÅÒÁ ÊÏÇÏ
×ÉËÏÒÉÓÔÁÎÎÑ ÄÕÖÅ ÛÉÒÏËÁ, ÎÁÊÂ¦ÌØÛ ĞÏÛÉÒÅÎÅ ÊÏÇÏ ÚÁÓÔÏÓÕ×ÁÎÎÑ (ÔÁ
ÎÁÊÓÉÌØÎ¦ÛÁ ÓÔÏÒÏÎÁ) ÃÅ, ¦ÍÏ×¦ÒÎÏ, ÕÔÉÌ¦ÔÉ ÓÉÓÔÅÍÎÏÇÏ ÁÄÍ¦Î¦ÓÔÒÕ×ÁÎÎÑ
ÔÁ web-ĞÒÏÇÒÁÍÕ×ÁÎÎÑ. â¦ÌØÛÁ ŞÁÓÔÉÎÁ CGI ÓËÒÉĞÔ¦× ÎÁĞÉÓÁÎÁ ÎÁ Perl.

%description -l zh_CN
Perl ÊÇÒ»ÖÖ¸ß¼¶±à³ÌÓïÑÔ£¬ÆğÔ´ÓÚ C¡¢sed¡¢awk ºÍ shell ½Å±¾¡£
ËüÉÆÓÚ´¦Àí½ø³ÌºÍÎÄ¼ş£¬ÓÈÆäÊÇ´¦ÀíÎÄ±¾¡£Perl
µÄÌØµãÔÚÓÚÆäÊµÓÃĞÔºÍÓĞĞ§ĞÔ¡£
¾¡¹ÜËü¿ÉÓÃÓÚÖ´ĞĞĞí¶à²»Í¬µÄÈÎÎñ£¬µ«ÊÇÍ¨³£¶àÓ¦ÓÃÓÚÏµÍ³¹ÜÀíÊµÓÃ³ÌĞòºÍ Web
±à³Ì¡£\n Web ÉÏµÄ´ó²¿·Ö CGI ½Å±¾¾ùÊ¹ÓÃ Perl
ÓïÑÔ½øĞĞ±àĞ´¡£Äú±ØĞëÔÚÏµÍ³ÖĞ°²×° perl Èí¼ş°ü£¬ ÒÔ±ã´¦Àí Perl ½Å±¾¡£

%package base
Summary:	Base perl components for a minimal installation
Summary(pl):	Podstawowe sk³adniki potrzebne do minimalnej instalacji perla
Group:		Text/Applications
Provides:	perl-File-Compare = 1.1003
Provides:	perl-File-Spec = 0.83
Provides:	perl-File-Temp = 0.13
Provides:	perl-Safe = 2.09

%description base
Base components, files, core modules, etc. -- a minimal usable perl
installation.  You are encouraged to install a full perl (the perl
package) whenever possible.

%description base -l pl
Podstawowe sk³adniki, pliki, g³ówne modu³y itp. - minimalna u¿ywalna
instalacja Perla. Zaleca siê instalacjê pe³nego Perla (pakietu perl)
je¶li to tylko mo¿liwe.

%package devel
Summary:	Perl development files
Summary(pl):	Pliki potrzebne przy tworzeniu w³asnych aplikacji w perlu
Summary(pt_BR):	Arquivos de desenvolvimento e cabeçalhos para o perl
Group:		Development/Libraries
Requires:	%{name}-base = %{version}
Requires:	%{name}-modules = %{version}
Requires:	%{name}-tools-pod
Provides:	perl-CPAN = 1.61
Provides:	perl-Devel-DProf = 20000000.00_01
Provides:	perl-Devel-PPPort = 2.0002
Provides:	perl-Devel-Peek = 1.00_03
Provides:	perl-ExtUtils-MakeMaker = 6.03
Provides:	perl-ExtUtils-Embed = 1.250601
Obsoletes:	perl-lib-devel

%description devel
Components required for developing applications which embed a Perl
interpreter and compiling perl modules.

%description devel -l pl
Sk³adniki potrzebne do tworzenia aplikacji osadzaj±cych interpreter
Perla oraz kompilowania modu³ów Perla.

%package doc-pod
Summary:	Perl documentation in POD format
Summary(pl):	Dokumentacja Perla w formacie POD
Group:		Documentation
Obsoletes:	perl-pod

%description doc-pod
Practical Extraction and Report Language - POD docs.

%description doc-pod -l pl
Practical Extraction and Report Language - dokumentacja w formacie
POD.

%package doc-reference
Summary:	Perl reference documentation
Summary(pl):	Dokumentacja Perla
Group:		Documentation
Requires:	man

%description doc-reference
Reference documentation for the Practical Extraction and Report Language
and it's interpreter in the man(1) format.

%description doc-reference -l pl
Dokumentacja referencyjna w formacie man do jêzyka Perl (Practical
Extraction and Report Language) i jego interpretera.

%package modules
Summary:	Modules from the core perl distribution
Summary(pl):	Modu³y z podstawowej dystrybucji perla
Group:		Development/Libraries
Requires:	%{name}-base = %{version}
Provides:	perl-Attribute-Handlers = 0.77
Provides:	perl-CGI = 2.81
Provides:	perl-Class-ISA = 0.32
Provides:	perl-Digest = 1.00
Provides:	perl-Digest-MD5 = 2.20
Provides:	perl-Filter-Simple = 0.78
Provides:	perl-FindBin = 1.43
#Provides:	perl-Hash-Utils = 0.04	Data::Util is missing
Provides:	perl-IO = 1.20
Provides:	perl-IPC-SysV = 1.03_00
Provides:	perl-Locale-Maketext = 1.03
Provides:	perl-MIME-Base64 = 2.12
Provides:	perl-Math-BigInt = 1.60
Provides:	perl-Math-BigRat = 0.07
Provides:	perl-Math-Trig = 1.01
Provides:	perl-Memoize = 1.01
Provides:	perl-NEXT = 0.50
Provides:	perl-PerlIO-via-QuotedPrint = 0.04
Provides:	perl-Pod-LaTeX = 0.54
Provides:	perl-Pod-Parser = 1.13
Provides:	perl-Scalar-List-Utils = 1.07_00
Provides:	perl-Socket = 1.75
Provides:	perl-Storable = 2.04
Provides:	perl-Term-ANSIColor = 1.05
Provides:	perl-Term-Cap = 1.07
Provides:	perl-Test = 1.20
Provides:	perl-Test-Harness = 2.26
Provides:	perl-Test-Simple = 0.45
Provides:	perl-Text-Balanced = 1.89
Provides:	perl-Text-ParseWords = 3.21
Provides:	perl-Text-Soundex = 1.01
Provides:	perl-Text-Tabs+Wrap = 2001.0929
Provides:	perl-Tie-File = 0.93
Provides:	perl-Time-HiRes = 1.20_00
Provides:	perl-UNIVERSAL = 1.00
Provides:	perl-Unicode-Collate = 0.12
Provides:	perl-Unicode-Normalize = 0.17
Obsoletes:	perl-lib

%description modules
Practical Extraction and Report Language - modules from the core
distribution.

%description modules -l pl
Practical Extraction and Report Language - modu³y z podstawowej
dystrybucji.

%package perldoc
Summary:	perldoc - Look up Perl documentation in pod format
Summary(pl):	perldoc - przeszukiwanie dokumentacji Perla w formacie pod
Provides:	perldoc = 2.03@%{version}
Requires:	%{name}-base
Group:		Development/Tools

%description perldoc
perldoc looks up a piece of documentation in .pod format that is
embedded in the perl installation tree or in a perl script, and
displays it via "pod2man | nroff -man | $PAGER". This is primarily
used for the documentation for the perl library modules.

%description perldoc -l pl
perldoc wyszukuje fragment dokumentacji w formacie .pod osadzony w
drzewie instalacji perla lub w skypcie perlowym i wy¶wietla go przez
"pod2man | nroff -man | $PAGER". Program ten u¿ywany jest g³ównie do
dokumentacji modu³ów z bibliotek Perla.

%package -n sperl
Summary:	Perl setuid root binaries for use with setuid Perl scripts
Summary(de):	sperl zur Verwendung mit setuid Perl-Skripts
Summary(es):	sperl, para uso con los scrips de Perl setuid
Summary(fr):	sperl, à utiliser avec les scripts Perl setuid
Summary(it):	sperl, da usare con gli script di Perl setuid
Summary(ja):	Setuid Perl scripts ¤È°ì½ï¤Ë»ÈÍÑ¤¹¤ë¤¿¤á¤Î suidperl
Summary(ko):	Setuid ÆŞ ½ºÅ©¸³Æ®¿Í ÇÔ²² »ç¿ëµÇ´Â suidperl
Summary(pl):	Binaria setuid root Perla dla setuid-owych skryptów Perla
Summary(pt):	O suidperl, para usar com os programas de Perl 'setuid'
Summary(ru):	SUID ×ÅÒÓÉÑ ÑÚÙËÁ Perl
Summary(sv):	sperl, att användas med setuid perlskript
Summary(uk):	SUID-×ÅÒÓ¦Ñ ÍÏ×É Perl
Summary(zh_CN):	sperl£¬ÓÃÀ´Óë setuid perl ½Å±¾Ò»ÆğÊ¹ÓÃ
Group:		Development/Languages/Perl
Requires:	%{name}-base = %{version}
Obsoletes:	perl-suidperl

%description -n sperl
sperl is a setuid root binary copy of perl that allows for (hopefully)
more secure running of setuid Perl scripts.

%description -n sperl -l de
sperl ist eine binäre setuid Kopie von Perl, mit der (hoffentlich)
setuid-Skripts sicherer ausgeführt werden können.

%description -n sperl -l es
sperl es una copia binaria de setuid para perl que le permite una
ejecución más segura de los scripts de Perl setuid.

%description -n sperl -l fr
sperl est une copie binaire setuid de perl qui permet une exécution
plus sûre de scripts Perl setuid.

%description -n sperl -l it
sperl è una copia binaria setuid di perl che consente un'esecuzione
più sicura di script di Perl setuid.

%description -n sperl -l ja
sperl ¤Ï setuid Perl scripts.¤ò¤â¤Ã¤È°ÂÁ´¤ËÆ°ºî¤Ç¤­¤ë(´üÂÔ¤Î¤¢¤ë)°Ù¤Î
perl ¤Îsetuid ¥Ğ¥¤¥Ê¥ê ¥³¥Ô¡¼¤Ç¤¹¡£

%description -n sperl -l pl
sperl jest to kopia setuid root programu binarnego perl umo¿liwiaj±ca
bezpieczniejsze (miejmy nadziejê) uruchamianie setuidowych skryptów
Perla.

%description -n sperl -l pt
O suidperl é uma cópia do perl com 'setuid' que permite uma execução
mais segura dos 'scripts' de Perl 'setuid'.

%description -n sperl -l ru
Suid perl ÉÓĞÌØÚÕÅÔÓÑ ÄÌÑ ÔÏÇÏ, ŞÔÏÂÙ ÄÁÔØ ×ÏÚÍÏÖÎÏÓÔØ ÓÏÚÄÁ×ÁÔØ
ÓËÒÉĞÔÙ Ó ÕÔÁÎÏ×ÌÅÎÎÙÍ ÂÉÔÏÍ SUID. èÏÔÑ × ÎÅÇÏ ×ÓÔÒÏÅÎÏ ÄÏÓÔÁÔÏŞÎÏ
ÍÎÏÇÏ ĞÒÏ×ÅÒÏË, ĞÒÉÚ×ÁÎÙÈ ÏÂÅÓĞÅŞÉÔØ ÂÅÚÏĞÁÓÎÏÓÔØ ÅÇÏ ÉÓĞÏÌØÚÏ×ÁÎÉÑ
suid perl ×ÓÅ ÒÁ×ÎÏ ĞÒÅÄÓÔÁ×ÌÑÅÔ ÓÏÂÏÊ ÚÎÁŞÉÔÅÌØÎÕÀ ĞÏÔÅÎÃÉÁÌØÎÕÀ
ÏĞÁÓÎÏÓÔØ.

%description -n sperl -l sv
suidperl är en setuid binärkopia av pers som tillåter
(förhoppningsvis) säkrare körning av setuid perlskript.

%description -n sperl -l zh_CN
suidperl ÊÇ perl µÄ setuid ¶ş½øÖÆ¸±±¾¡£ËüÔÊĞí£¨Ï£ÍûÈç´Ë£© ¸ü°²È«µØÔËĞĞ
setuid perl ½Å±¾¡£

%package tools
Summary:	Various tools from the core perl distribution
Summary(pl):	Ró¿ne narzêdzia z podstawowej dystrybucji perla
Group:		Applications
Requires:	%{name}-base = %{version}

%description tools
Various tools from the core perl distribution:

 a2p       - Awk to Perl translator
 find2perl - translate find command lines to Perl code
 piconv    - iconv(1), reinvented in perl
 psed, s2p - a stream editor

%description modules -l pl
Ró¿ne narzêdzia z podstawowej dystrybucji Perla:

 a2p       - translator skryptów Awka do Perla
 find2perl - t³umaczenie linii poleceñ programu find na kod w Perlu
 piconv    - iconv(1) napisany w Perlu
 psed, s2p - edytor strumieniowy

%package tools-devel
Summary:	Developer's tools from the core perl distribution
Summary(pl):	Narzêdzia z podstawowej dystrybucji perla, przeznaczone dla programistów
Group:		Development/Tools
Requires:	%{name}-base = %{version}
Requires:	%{name}-devel = %{version}

%description tools-devel
Various tools from the core perl distribution:

 c2ph, pstruct - Dump C structures as generated from C<cc -g -S> stabs
 dprofpp       - display perl profile data
 enc2xs        - Perl Encode Module Generator
 h2ph          - convert .h C header files to .ph Perl header files
 h2xs          - convert .h C header files to Perl extensions
 perlcc        - generate executables from Perl programs
 perlivp       - Perl Installation Verification Procedure
 pl2pm         - Rough tool to translate Perl4 .pl files to Perl5 .pm modules.
 splain        - force verbose warning diagnostics

%description tools-devel -l pl
Ró¿ne narzêdzia z podstawowej dystrybucji Perla:

 c2ph, pstruct - zrzucanie struktur C w postaci generowanej z tablic
                 symboli z cc -g -S
 dprofpp       - wy¶wietlanie perlowych danych profiluj±cych
 enc2xs        - generator modu³ów koduj±cych w Perlu
 h2ph          - konwerter plików nag³ówkowych .h z C na perlowe pliki
                 nag³ówkowe .ph
 h2xs          - konwerter plików nag³ówkowych .h z C na rozszerzenia
                 Perla
 perlcc        - generator binarek z programów w Perlu
 perlivp       - procedura weryfikacji instalacji Perla
 pl2pm         - zgrubne narzêdzie do t³umaczenia plików pl Perla 4 na
                 modu³y .pm Perla 5
 splain        - wymuszenie obszernych ostrze¿eñ diagnostycznych

%package tools-pod
Summary:	Tools for manipulating files in the POD format
Summary(pl):	Narzêdzia do przetwarzania plików w formacie POD
Group:		Applications
Requires:	%{name}-base = %{version}

%description tools-pod
Tools for manipulating files in the POD (Plain Old Documentation)
format:

 pod2html   - convert .pod files to .html files
 pod2latex  - convert pod documentation to LaTeX format
 pod2man    - convert POD data to formatted *roff input
 pod2text   - convert POD data to formatted ASCII text
 pod2usage  - print usage messages from embedded pod docs in files
 podchecker - check the syntax of POD format documentation files
 podselect  - print selected sections of pod documentation

%description tools-pod
Narzêdzia do przetwarzania plików w formacie POD (Plain Old
Documentation):

 pod2html   - konwerter plików .pod do plików .html
 pod2latex  - konwerter dokumentacji pod do formatu LaTeX
 pod2man    - konwerter danych POD na wej¶cie sformatowane dla *roffa
 pod2text   - konwerter danych POD na sformatowany tekst ASCII
 pod2usage  - wypisanie informacji o u¿ywaniu programu z dokumentacji
              osadzonej w plikach
 podchecker - kontrola sk³adni dokumentacji w formacie POD
 podselect  - wypisanie wybranych sekcji z dokumentacji POD

%package -n microperl
Summary:	A really minimal perl, even more minimal than miniperl
Summary(pl):	Naprawdê minimalny Perl, nawet bardziej minimalny ni¿ miniperl
# XXX: is there a more appropiate group?
Group:		Applications

%description -n microperl
microperl is supposed to be able a really minimal perl, even more
minimal than miniperl.  No Configure is needed to build microperl, on
the other hand this means that interfaces between Perl and your
operating system are left very -- minimal.

All this is experimental.  If you don't know what to do with microperl
you probably shouldn't.  Do not report bugs in microperl; fix the bugs.

%description -n microperl -l pl
microperl ma byæ naprawdê minimalnym Perlem, nawet bardziej minimalnym
od miniperla. Uruchamianie Configure nie jest potrzebne do zbudowania
microperla, z drugiej strony oznacza to, ¿e interfejs miêdzy Perlem a
systemem operacyjnym pozostaje bardzo minimalny.

Ca³o¶æ jest eksperymentalna. Je¶li nie wiesz co zrobiæ z microperlem,
prawdopodobnie nie powiniene¶ tego robiæ. Nie zg³aszaj b³êdów w
microperlu - popraw je.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch8 -p1
%patch9 -p1
%patch11 -p1
%patch14 -p0
%patch15 -p1

install -m 0755 %{SOURCE2} $PWD/find-perl.prov
install -m 0755 %{SOURCE3} $PWD/find-perl-provides.sh

%build
sh Configure \
	-des \
	-Dcc=%{__cc} \
	-Darchname=%{_target_platform} \
	-Dcccdlflags='-fPIC' \
	-Dccdlflags='-rdynamic' \
	-Doptimize="%{rpmcflags}" \
	-Duseshrplib \
	-Dd_dosuid \
	-Dman1dir=%{_mandir}/man1 -Dman1ext=1 \
	-Dman3dir=%{_mandir}/man3 -Dman3ext=3perl \
	-Dvendorman1=%{_mandir}/man1 -Dvendorman1ext=1p \
	-Dvendorman3=%{_mandir}/man3 -Dvendorman3ext=3pm \
	-Dsiteman1=%{_usr}/local/share/man/man1 -Dsiteman1ext=1p \
	-Dsiteman3=%{_usr}/local/share/man/man3p -Dsiteman3ext=3pm \
	-Dprefix=%{_prefix} -Dvendorprefix=%{_prefix} -Dsiteprefix=%{_usr}/local \
	-Dprivlib=%{perl_privlib}     -Darchlib=%{perl_archlib} \
	-Dsitelib=%{perl_sitelib}     -Dsitearch=%{perl_sitearch} \
	-Dvendorlib=%{perl_vendorlib} -Dvendorarch=%{perl_vendorarch} \
	-Dinstallprefix=$RPM_BUILD_ROOT%{_prefix} \
	-Ui_dbm -Ui_gdbm -Ui_ndbm -Ui_db \
	-Dlibswanted="dl m c crypt" \
	-%{?_without_threads:U}%{?!_without_threads:D}usethreads \
	-%{?_without_largefiles:U}%{?!_without_largefiles:D}uselargefiles

## why were these three undefined?
#	-Ud_setresgid \
#	-Ud_setresuid \
## what's the problem with this one?
# %ifarch sparc sparc64
#	-Ud_longdbl
# %endif

%{__make}
%{__make} -f Makefile.micro \
	OPTIMIZE="%{rpmcflags}"

%{?!_without_tests:%{__make} test}
#%{?!_without_tests:%{__make} minitest}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install
install miniperl  $RPM_BUILD_ROOT%{_bindir}
install microperl $RPM_BUILD_ROOT%{_bindir}

## use symlinks instead of hardlinks
%{__ln_s} -f  perl%{version} $RPM_BUILD_ROOT%{_bindir}/perl
%{__ln_s} -f sperl%{version} $RPM_BUILD_ROOT%{_bindir}/suidperl
%{__ln_s} -f  c2ph           $RPM_BUILD_ROOT%{_bindir}/pstruct
%{__ln_s} -f  psed           $RPM_BUILD_ROOT%{_bindir}/s2p

## Fix lib
rm -f $RPM_BUILD_ROOT%{perl_archlib}/CORE/libperl.so*
install libperl.so.%{version} $RPM_BUILD_ROOT%{_libdir}
%{__ln_s} -f libperl.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libperl.so


%define		__perl	LD_LIBRARY_PATH="%{_builddir}/%{name}-%{version}" PERL5LIB="%{buildroot}/%{perl_privlib}:%{buildroot}/%{perl_archlib}" %{buildroot}/%{_bindir}/perl

## Fix Config.pm: remove buildroot path and change man pages extensions
%{__perl} -pi -e 's,%{buildroot}/*,/,g'              $RPM_BUILD_ROOT%{perl_archlib}/Config.pm
%{__perl} -pi -e "s,^man1ext='1',man1ext='1p',"      $RPM_BUILD_ROOT%{perl_archlib}/Config.pm
%{__perl} -pi -e "s,^man3ext='3perl',man3ext='3pm'," $RPM_BUILD_ROOT%{perl_archlib}/Config.pm

## prepare scripts for finding provides
%{__perl} -pi -e 's,\@perl_build_dir\@,%{_builddir}/%{name}-%{version},g' find-perl-provides.sh
%{__perl} -pi -e 's,\@perl\@,%{__perl},g'                                 find-perl-provides.sh

## Generate the *.ph files
(
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
'
%{__perl} $H2PH -a -d $PHDIR $WANTED
)

## remove man pages for other operating systems
rm -f	$RPM_BUILD_ROOT%{_mandir}/man1/perl{aix,amiga,apollo,beos,bs2000,ce,cygwin,dgux,dos}* \
	$RPM_BUILD_ROOT%{_mandir}/man1/perl{freebsd,hpux,machten,macos,mpeix,os2,os390}* \
	$RPM_BUILD_ROOT%{_mandir}/man1/perl{qnx,solaris,vmesa,vms,vos,win32}*

## These File::Spec submodules are for non-Unix systems
rm -f $RPM_BUILD_ROOT%{perl_privlib}/File/Spec/[EMOVW]*.pm
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/File::Spec::{Epoc,Mac,OS2,VMS,Win32}.3pm*

## We already have these *.pod files as man pages
rm -f $RPM_BUILD_ROOT%{perl_privlib}/{Encode,Test,Net,Locale{,/Maketext}}/*.pod
rm -f $RPM_BUILD_ROOT%{perl_privlib}/*.pod
rm -f $RPM_BUILD_ROOT%{perl_archlib}/*.pod

## this object file looks unused; why is it there?
rm -f $RPM_BUILD_ROOT%{perl_archlib}/CORE/sperl.o

## dir tree for other perl modules
install -d $RPM_BUILD_ROOT{%{perl_vendorlib},%{perl_vendorarch},%{perl_vendorarch}/auto}
(
cd $RPM_BUILD_ROOT%{perl_vendorlib}
install -d AI/NeuralNet Algorithm Apache Archive Array Astro Attribute \
	Audio Authen B Bundle Business CGI Cache Chart Class Config \
	Convert Crypt DBD Data Date Devel Device Digest Error ExtUtils File \
	Filesys Font Games Getopt GnuPG Graph HTML HTTP I18N IO/Socket IPC \
	Image Inline Language Lingua/EN List Locale LockFile Log MIME Mail \
	Math Module Net/SMTP NetServer Netscape News Number OLE Parse Pod \
	PostScript Proc RADIUS RPC RPM Regexp SOAP/Transport SQL Schedule \
	Set Sort Speech Spreadsheet Statistics String Sub Sys TeX Test \
	Text/Query Tie Time Tree Unicode WWW XML/{Filter,Handler,Parser} \
	auto/{AI,Array,Config,Crypt,Data,Mail,Net,Schedule,Statistics,Text,WWW}

cd $RPM_BUILD_ROOT%{perl_vendorarch}
install -d Astro Audio Authen B BSD Bit Compress Crypt/OpenSSL Data Devel \
	Digest File IPC Inline Locale Math Net Speech/Recognizer String Term \
	Text Unicode XML \
	auto/{Astro,Audio,Authen,BSD,Bit,Compress,Crypt/OpenSSL,Data,Devel} \
	auto/{Digest,File,IPC,Inline,Locale,Math,Net,Speech/Recognizer,String} \
	auto/{Term,Text,Unicode,XML}
)

## non-english man pages
%{__bzip2} -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}


%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%lang(cn) %doc README.cn
%lang(jp) %doc README.jp
%lang(ko) %doc README.ko
%lang(tw) %doc README.tw

%{perl_vendorlib}
%dir %{_libdir}/perl5/vendor_perl
%dir %{_libdir}/perl5/vendor_perl/%{version}
%{perl_vendorarch}
#%dir %{perl_vendorarch}/auto


%files base
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perl
%attr(755,root,root) %{_bindir}/perl%{version}
%{_mandir}/man1/perl.*
%lang(fi) %{_mandir}/fi/man1/perl*
%lang(pl) %{_mandir}/pl/man1/perl*

%dir %{_datadir}/perl5
%dir %{perl_privlib}
%dir %{_libdir}/perl5
%dir %{_libdir}/perl5/%{version}
%dir %{perl_archlib}
%dir %{perl_archlib}/auto

# pragmas
%{perl_privlib}/[a-z]*.pm
%{perl_privlib}/[a-z]*.pl
%{perl_privlib}/warnings
%{perl_archlib}/[a-z]*.pm
%{perl_archlib}/threads
%dir %{perl_archlib}/auto/attrs
%dir %{perl_archlib}/auto/re
%dir %{perl_archlib}/auto/threads
%dir %{perl_archlib}/auto/threads/shared
%attr(755,root,root) %{perl_archlib}/auto/attrs/*.so
%attr(755,root,root) %{perl_archlib}/auto/re/*.so
%attr(755,root,root) %{perl_archlib}/auto/threads/*.so
%attr(755,root,root) %{perl_archlib}/auto/threads/shared/*.so
%{perl_archlib}/auto/attrs/*.bs
%{perl_archlib}/auto/re/*.bs
%{perl_archlib}/auto/threads/*.bs
%{perl_archlib}/auto/threads/shared/*.bs
%{_mandir}/man3/[a-z]*

# arch-_IN_dependent modules
%{perl_privlib}/Auto*
%{_mandir}/man3/Auto*
%{perl_privlib}/Carp*
%{_mandir}/man3/Carp*
%{perl_privlib}/Exporter*
%{_mandir}/man3/Exporter*
%{perl_privlib}/English*
%{_mandir}/man3/English*
%{perl_privlib}/Getopt*
%{_mandir}/man3/Getopt*
%{perl_privlib}/IPC
%{_mandir}/man3/IPC::Open*

# arch-dependent modules
%{perl_archlib}/Config*
%{_mandir}/man3/Config*
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
%{perl_archlib}/auto/Cwd/*.bs
%{_mandir}/man3/Cwd.*

%{perl_archlib}/Fcntl.*
%dir %{perl_archlib}/auto/Fcntl
%attr(755,root,root) %{perl_archlib}/auto/Fcntl/*.so
%{perl_archlib}/auto/Fcntl/*.bs
%{_mandir}/man3/Fcntl.*

%{perl_privlib}/File*
%{perl_archlib}/File
%dir %{perl_archlib}/auto/File
%dir %{perl_archlib}/auto/File/*/
%attr(755,root,root) %{perl_archlib}/auto/File/*/*.so
%{perl_archlib}/auto/File/*/*.bs
%{_mandir}/man3/File*

%{perl_archlib}/Opcode.*
%dir %{perl_archlib}/auto/Opcode
%attr(755,root,root) %{perl_archlib}/auto/Opcode/*.so
%{perl_archlib}/auto/Opcode/*.bs
%{_mandir}/man3/Opcode.*

%{perl_privlib}/PerlIO.*
%{perl_archlib}/PerlIO
%dir %{perl_archlib}/auto/PerlIO
%dir %{perl_archlib}/auto/PerlIO/*/
%attr(755,root,root) %{perl_archlib}/auto/PerlIO/*/*.so
%{perl_archlib}/auto/PerlIO/*/*.bs
%{_mandir}/man3/PerlIO.*
%{_mandir}/man3/PerlIO::[es]*
%{_mandir}/man3/PerlIO::via.*

%{perl_archlib}/POSIX*
%dir %{perl_archlib}/auto/POSIX
%attr(755,root,root) %{perl_archlib}/auto/POSIX/*.so
%{perl_archlib}/auto/POSIX/*.al
%{perl_archlib}/auto/POSIX/*.bs
%{perl_archlib}/auto/POSIX/*.ix
%{_mandir}/man3/POSIX.*

%attr(755,root,root) %{_libdir}/lib*.so.%{version}


%files devel
%defattr(644,root,root,755)
%{_mandir}/man1/perldebguts.*

%attr(755,root,root) %{_libdir}/lib*.so
%{perl_archlib}/CORE

# FIXME: Changes file to _docdir (and rm MANIFEST.SKIP?)
%{perl_privlib}/ExtUtils
%{_mandir}/man3/ExtUtils*
%{perl_privlib}/CPAN*
%{_mandir}/man3/CPAN*
%{perl_privlib}/DB.*
%{_mandir}/man3/DB.*
%{perl_archlib}/O.*
%{_mandir}/man3/O.*

%{perl_privlib}/B
%{perl_archlib}/B
%{perl_archlib}/B.pm
%dir %{perl_archlib}/auto/B
%dir %{perl_archlib}/auto/B/C
%attr(755,root,root) %{perl_archlib}/auto/B/*.so
%attr(755,root,root) %{perl_archlib}/auto/B/C/*.so
%{perl_archlib}/auto/B/*.bs
%{perl_archlib}/auto/B/C/*.bs
%{_mandir}/man3/B[.:]*

%{perl_archlib}/ByteLoader.*
%dir %{perl_archlib}/auto/ByteLoader
%attr(755,root,root) %{perl_archlib}/auto/ByteLoader/*.so
%{perl_archlib}/auto/ByteLoader/*.bs
%{_mandir}/man3/ByteLoader.*

%{perl_privlib}/Devel
%{perl_archlib}/Devel
%dir %{perl_archlib}/auto/Devel
%dir %{perl_archlib}/auto/Devel/*/
%attr(755,root,root) %{perl_archlib}/auto/Devel/*/*.so
%{perl_archlib}/auto/Devel/*/*.bs
%{_mandir}/man3/Devel::*

%{perl_archlib}/XS
%dir %{perl_archlib}/auto/XS
%dir %{perl_archlib}/auto/XS/*/
%attr(755,root,root) %{perl_archlib}/auto/XS/*/*.so
%{perl_archlib}/auto/XS/*/*.bs
%{_mandir}/man3/XS::*


%files doc-pod
%defattr(644,root,root,755)
%{perl_privlib}/pod/perl.pod
%{perl_privlib}/pod/perl[5abceghijklmnopqrstuvwx]*.pod
%{perl_privlib}/pod/perld[^i]*.pod
%{perl_privlib}/pod/perlf[^au]*.pod


%files doc-reference
%defattr(644,root,root,755)
%{_mandir}/man1/perl[5adefghilmnoprstuvwx]*
%{_mandir}/man1/perlbo*
%{_mandir}/man1/perlcall.*
%{_mandir}/man1/perlclib.*
%{_mandir}/man1/perlcompile.*
%lang(cn) %{_mandir}/man1/perlcn.*
%lang(jp) %{_mandir}/man1/perljp.*
%lang(ko) %{_mandir}/man1/perlko.*


%files modules
%defattr(644,root,root,755)
# XXX: should it really be in this package?
%{perl_privlib}/unicore

# *.ph files (could be made a separate package, but an autohelper's support is needed)
%{perl_archlib}/*.ph
%{perl_archlib}/asm
%{perl_archlib}/bits
%{perl_archlib}/gnu
%{perl_archlib}/linux
%{perl_archlib}/sys

%{perl_archlib}/Data
%dir %{perl_archlib}/auto/Data
%dir %{perl_archlib}/auto/Data/Dumper
%attr(755,root,root) %{perl_archlib}/auto/Data/Dumper/*.so
%{perl_archlib}/auto/Data/Dumper/*.bs
%{_mandir}/man3/Data*

%{perl_privlib}/Digest.pm
%{perl_archlib}/Digest
%dir %{perl_archlib}/auto/Digest
%dir %{perl_archlib}/auto/Digest/MD5
%attr(755,root,root) %{perl_archlib}/auto/Digest/MD5/*.so
%{perl_archlib}/auto/Digest/MD5/*.bs
%{_mandir}/man3/Digest*

## FIXME: *.h to devel(?), check out the use for *.e2x files
%{perl_privlib}/Encode
%{perl_archlib}/Encode*
%dir %{perl_archlib}/auto/Encode
%dir %{perl_archlib}/auto/Encode/*/
%attr(755,root,root) %{perl_archlib}/auto/Encode/*/*.so
%{perl_archlib}/auto/Encode/*/*.bs
%{_mandir}/man3/Encode*

# FIXME: README and Changes files
%{perl_privlib}/Filter
%{perl_archlib}/Filter
%dir %{perl_archlib}/auto/Filter
%dir %{perl_archlib}/auto/Filter/Util
%dir %{perl_archlib}/auto/Filter/Util/Call
%attr(755,root,root) %{perl_archlib}/auto/Filter/Util/Call/*.so
%{perl_archlib}/auto/Filter/Util/Call/*.bs
%{_mandir}/man3/Filter*

%{perl_privlib}/I18N
%{perl_archlib}/I18N
%dir %{perl_archlib}/auto/I18N
%dir %{perl_archlib}/auto/I18N/*/
%attr(755,root,root) %{perl_archlib}/auto/I18N/*/*.so
%{perl_archlib}/auto/I18N/*/*.bs
%{perl_archlib}/auto/I18N/*/*.ix
%{_mandir}/man3/I18N::*

%{perl_privlib}/IO
%{perl_archlib}/IO*
%dir %{perl_archlib}/auto/IO
%attr(755,root,root) %{perl_archlib}/auto/IO/*.so
%{perl_archlib}/auto/IO/*.bs
%{_mandir}/man3/IO*

%{perl_archlib}/IPC
%dir %{perl_archlib}/auto/IPC
%dir %{perl_archlib}/auto/IPC/*/
%attr(755,root,root) %{perl_archlib}/auto/IPC/*/*.so
%{perl_archlib}/auto/IPC/*/*.bs
%{_mandir}/man3/IPC::[MS]*

# FIXME: List/Util.pm should be archlib; patch needed
%{perl_privlib}/List
%dir %{perl_archlib}/auto/List
%dir %{perl_archlib}/auto/List/*/
%attr(755,root,root) %{perl_archlib}/auto/List/*/*.so
%{perl_archlib}/auto/List/*/*.bs
%{_mandir}/man3/List::*

%{perl_archlib}/MIME
%dir %{perl_archlib}/auto/MIME
%dir %{perl_archlib}/auto/MIME/Base64
%attr(755,root,root) %{perl_archlib}/auto/MIME/Base64/*.so
%{perl_archlib}/auto/MIME/Base64/*.bs
%{_mandir}/man3/MIME::*

%{perl_archlib}/SDBM_File.*
%dir %{perl_archlib}/auto/SDBM_File
%attr(755,root,root) %{perl_archlib}/auto/SDBM_File/*.so
%{perl_archlib}/auto/SDBM_File/*.bs
%{_mandir}/man3/SDBM_File.*

%{perl_archlib}/Socket.*
%dir %{perl_archlib}/auto/Socket
%attr(755,root,root) %{perl_archlib}/auto/Socket/*.so
%{perl_archlib}/auto/Socket/*.bs
%{_mandir}/man3/Socket.*

%{perl_archlib}/Storable.*
%dir %{perl_archlib}/auto/Storable
%attr(755,root,root) %{perl_archlib}/auto/Storable/*.so
%{perl_archlib}/auto/Storable/*.al
%{perl_archlib}/auto/Storable/*.bs
%{perl_archlib}/auto/Storable/*.ix
%{_mandir}/man3/Storable.*

%{perl_archlib}/Sys
%dir %{perl_archlib}/auto/Sys
%dir %{perl_archlib}/auto/Sys/*/
%attr(755,root,root) %{perl_archlib}/auto/Sys/*/*.so
%{perl_archlib}/auto/Sys/*/*.bs
%{perl_archlib}/auto/Sys/*/*.ix
%{_mandir}/man3/Sys::*

%{perl_archlib}/Time
%dir %{perl_archlib}/auto/Time
%dir %{perl_archlib}/auto/Time/HiRes
%attr(755,root,root) %{perl_archlib}/auto/Time/HiRes/*.so
%{perl_archlib}/auto/Time/HiRes/*.bs
%{_mandir}/man3/Time::HiRes*

%{perl_privlib}/Unicode
%{perl_archlib}/Unicode
%dir %{perl_archlib}/auto/Unicode
%dir %{perl_archlib}/auto/Unicode/*/
%attr(755,root,root) %{perl_archlib}/auto/Unicode/*/*.so
%{perl_archlib}/auto/Unicode/*/*.bs
%{perl_archlib}/auto/Unicode/*/*.ix
%{_mandir}/man3/Unicode::*

%{perl_privlib}/AnyDBM*
%{_mandir}/man3/AnyDBM*
# FIXME: move */demo to %_exapmlesdir or /dev/null
%{perl_privlib}/Attribute
%{_mandir}/man3/Attribute*
%{perl_privlib}/Benchmark*
%{_mandir}/man3/Benchmark*
# FIXME: move */eg to %_examplesdir or /dev/null
%{perl_privlib}/CGI*
%{_mandir}/man3/CGI*
# FIXME: move test.pl to %_examplesdir or /dev/null
%{perl_privlib}/Class
%{_mandir}/man3/Class::*
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
%{perl_privlib}/Hash
%{_mandir}/man3/Hash::*
# FIXME: README and Changes files
%{perl_privlib}/Locale
%{_mandir}/man3/Locale::*
%{perl_privlib}/Math
%{_mandir}/man3/Math::*
%{perl_privlib}/Memoize*
%{_mandir}/man3/Memoize*
%{perl_privlib}/NEXT*
%{_mandir}/man3/NEXT*
# FIXME: README and Changes files, */demos to %_examplesdir or /dev/null
%{perl_privlib}/Net
%{_mandir}/man3/Net::*
%{perl_privlib}/PerlIO
%{_mandir}/man3/PerlIO::via::*
%{perl_privlib}/Pod
%{_mandir}/man3/Pod::*
%{perl_privlib}/Scalar
%{_mandir}/man3/Scalar::*
%{perl_privlib}/Search
%{_mandir}/man3/Search::*
%{perl_privlib}/SelectSaver.*
%{_mandir}/man3/SelectSaver.*
%{perl_privlib}/SelfLoader.*
%{_mandir}/man3/SelfLoader.*
%{perl_privlib}/Shell.*
%{_mandir}/man3/Shell.*
# FIXME: README and Changes files
%{perl_privlib}/Switch.*
%{_mandir}/man3/Switch.*
%{perl_privlib}/Symbol.*
%{_mandir}/man3/Symbol.*
# FIXME: README and Changes files
%{perl_privlib}/Term
%{_mandir}/man3/Term::*
# FIXME: README and Changes files
%{perl_privlib}/Test*
%{_mandir}/man3/Test*
%{perl_privlib}/Text
%{_mandir}/man3/Text::*
# XXX: to perl-base?
%{perl_privlib}/Thread*
%{_mandir}/man3/Thread*
%{perl_privlib}/Tie
%{_mandir}/man3/Tie::*
%{perl_privlib}/Time
%{_mandir}/man3/Time::[La-z]*
# XXX: to perl-base?
%{perl_privlib}/UNIVERSAL.*
%{_mandir}/man3/UNIVERSAL.*
# FIXME: README and Changes files
%{perl_privlib}/User
%{_mandir}/man3/User::*


%files perldoc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perldoc
%{perl_privlib}/pod/perldiag.pod
%{perl_privlib}/pod/perlfaq*.pod
%{perl_privlib}/pod/perlfunc.pod
%{_mandir}/man1/perldoc.*


%files -n sperl
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/sperl%{version}
%attr(4755,root,root) %{_bindir}/suidperl

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/a2p
%{_mandir}/man1/a2p.*
%attr(755,root,root) %{_bindir}/find2perl
%{_mandir}/man1/find2perl.*
%attr(755,root,root) %{_bindir}/libnetcfg
%{_mandir}/man1/libnetcfg.*
%attr(755,root,root) %{_bindir}/piconv
%{_mandir}/man1/piconv.*
%attr(755,root,root) %{_bindir}/psed
%attr(755,root,root) %{_bindir}/s2p
%{_mandir}/man1/psed.*
%{_mandir}/man1/s2p.*

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
%attr(755,root,root) %{_bindir}/perlcc
%{_mandir}/man1/perlcc.*
%attr(755,root,root) %{_bindir}/perlivp
%{_mandir}/man1/perlivp.*
%attr(755,root,root) %{_bindir}/pl2pm
%{_mandir}/man1/pl2pm.*
%attr(755,root,root) %{_bindir}/splain
%{_mandir}/man1/splain.*
%attr(755,root,root) %{_bindir}/xsubpp
%{_mandir}/man1/xsubpp.*

%files tools-pod
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pod*
%{_mandir}/man1/pod*

%files -n microperl
%defattr(644,root,root,755)
%doc README.micro Todo.micro
%attr(755,root,root) %{_bindir}/microperl
