#
# Conditional build:
# _without_tests   - do not perform "make test"
# _without_threads - build with support for threads
# _with_largefiles - build with large file support (think before turning it on)
#

#%define		__find_provides	%{_builddir}/%{name}-%{version}/find-perl-provides
%define		perlthread %{?!_without_threads:-thread-multi}

%define		perl_privlib	%{_libdir}/perl5/%{version}
%define		perl_archlib	%{perl_privlib}/%{_target_platform}%{perlthread}
%define		perl_sitelib	%{_libdir}/perl5/site_perl/%{version}
%define		perl_sitearch	%{perl_sitelib}/%{_target_platform}%{perlthread}
%define		perl_vendorlib	%{_libdir}/perl5/pld_perl/%{version}
%define		perl_vendorarch	%{perl_vendorlib}/%{_target_platform}%{perlthread}

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
Release:	0.04%{?_without_threads:_nothr}
Epoch:		1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/src/%{name}-%{version}.tar.gz
Source1:	%{name}-non-english-man-pages.tar.bz2
Source2:	%{name}.prov
Patch0:		%{name}_580-noroot_install.patch
# mostly obsolete and i just don't like it
#Patch1:		%{name}-nodb.patch
# weird one...
#Patch2:	%{name}-DESTDIR.patch
Patch3:		%{name}_580-find_provides.patch
# applied in a similar way
#Patch4:	%{name}-prereq.patch
# failed
#Patch5:	%{name}-syslog.patch
# failed
#Patch6:	%{name}-CGI-upload-tmpdir.patch
# what is this f* one for?!
#Patch7:	%{name}-LD_RUN_PATH.patch
Patch8:		%{name}_580-errno_h-parsing.patch
Patch9:		%{name}_580-use-LD_PRELOAD-for-lib%{name}.so.patch
# *weird*
#Patch10:	%{name}-sitearch.patch
Patch11:	%{name}_580-soname.patch
# is this one really needed?
#Patch12:	%{name}-db4.patch
# failed; is it still necessary?
#Patch13:	%{name}-gcc3.patch
Patch14:	%{name}_580-perluniintro.patch
URL:		http://www.perl.com/
#BuildRequires:	db-devel > 4.1
#Provides:	perl(DynaLoader)
Provides:	perl-File-Spec = 0.82
#Provides:	perl-IO = 1.20
#Obsoletes:	perl-File-Spec
Obsoletes:	perl-IO
Obsoletes:	perl-lib
Obsoletes:	perl-mod-skel
Obsoletes:	perl-base
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

%description -l no

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
Summary:	Base Perl components
# summaries needs fixup of course...
Group:		Text/Applications

%description base
Base Perl components, files, core modules, etc.

%package devel
Summary:	Perl development files
Summary(es):	Development and include files for perl
Summary(pl):	Pliki potrzebne przy tworzeniu w³asnych aplikacji w perlu
Summary(pt_BR):	Arquivos de desenvolvimento e cabeçalhos para o perl
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	%{name}-modules = %{version}
Obsoletes:	perl-lib-devel

%description devel
Files for developing applications which embed a Perl interpreter.

%description devel -l es
Development and include files for perl.

%description devel -l pl
Pliki potrzebne przy tworzeniu w³asnych aplikacji w perlu.

%description devel -l pt_BR
Arquivos de desenvolvimento e cabeçalhos para o perl.

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
Group:		Applications/Text
Requires:	%{name} = %{version}
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

%package modules
Summary:	Practical Extraction and Report Language - modules
Summary(es):	Perl's base modules
Summary(pl):	Practical Extraction and Report Language - modu³y
Summary(pt_BR):	Módulos do perl básicos
Group:		Applications/Text
#Requires:	perl-Test-Harness
Prereq:		%{name} = %{version}
#Provides:	perl-ANSIColor
#Provides:	perl-DProf
#Provides:	perl-Devel-Peek
#Provides:	perl-PodParser
#Obsoletes:	perl-ANSIColor
#Obsoletes:	perl-DProf
#Obsoletes:	perl-Devel-Peek
#Obsoletes:	perl-PodParser

%description modules
Practical Extraction and Report Language - modules.

%description modules -l es
This package contains standard perl modules needed by some
application/scripts.

%description modules -l pl
Practical Extraction and Report Language - modu³y.

%description modules -l pt_BR
Este pacote contém módulos perl básicos necessários por alguns
programas/ scripts.

%package pod
Summary:	Perl POD documentation
Summary(pl):	Dokumentacja Perla w formacie POD
Group:		Applications/Text
Prereq:		%{name} = %{version}

%description pod
Practical Extraction and Report Language - POD docs.

%description pod -l pl
Practical Extraction and Report Language - dokumentacja w formacie
POD.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1
#%patch2 -p1
%patch3 -p1
#%patch4 -p1
#%patch5 -p1
#%patch6 -p1
#%patch7 -p1
%patch8 -p1
%patch9 -p1
#%patch10 -p1
%patch11 -p1
#%patch12 -p1
#%patch13 -p1
%patch14 -p0

install -m 0755 %{SOURCE2} $PWD/find-perl.prov
chmod 0755 find-perl-provides

%build
sh Configure \
	-des \
	-Dcc=%{__cc} \
	-Darchname=%{_target_platform} \
	-Dcccdlflags='-fPIC' \
	-Dccdlflags='-rdynamic' \
	-Dcf_by=PLD -Dmyhostname=localhost -Dperladmin=root@localhost \
	-Dd_dosuid \
	-Dinstallprefix=$RPM_BUILD_ROOT%{_prefix} \
	-Dman1dir=%{_mandir}/man1 \
	-Dman3dir=%{_mandir}/man3 \
	-Dman3ext=3pm \
	-Doptimize="%{rpmcflags}" \
	-Dprefix=%{_prefix} \
	-Dprivlib=%{perl_privlib}     -Darchlib=%{perl_archlib} \
	-Dsitelib=%{perl_sitelib}     -Dsitearch=%{perl_sitearch} \
	-Dvendorlib=%{perl_vendorlib} -Dvendorarch=%{perl_vendorarch} \
	-Duseshrplib \
	-Ui_dbm -Ui_gdbm -Ui_ndbm -Ui_db \
	-Dlibswanted="nsl dl m c crypt util" \
	-%{?_without_threads:U}%{?!_without_threads:D}usethreads \
	-%{?_with_largefiles:D}%{?!_with_largefiles:U}uselargefiles

## why were these three undefined?
#	-Ud_setresgid \
#	-Ud_setresuid \
## what's the problem with this one?
# %ifarch sparc sparc64
#	-Ud_longdbl
# %endif

%{__make}

%{?!_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install

%{__ln_s} -f  perl%{version} $RPM_BUILD_ROOT%{_bindir}/perl
%{__ln_s} -f sperl%{version} $RPM_BUILD_ROOT%{_bindir}/suidperl

## Generate the *.ph files
(
LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}
PERL5LIB=$RPM_BUILD_ROOT%{perl_privlib}
PERL=$RPM_BUILD_ROOT%{_bindir}/perl
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

# just using the occasion, prepare scripts for finding provides
$PERL -pi -e 's|FPPATH|%{_builddir}/%{name}-%{version}|' find-perl-provides find-perl.prov

cd /usr/include
$PERL $H2PH -a -d $PHDIR $WANTED
)

## Fix lib
rm -f $RPM_BUILD_ROOT%{perl_archlib}/CORE/libperl.so*
install libperl.so.%{version} $RPM_BUILD_ROOT%{_libdir}
%{__ln_s} -f libperl.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libperl.so

## Fix installed man pages list
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/perl{aix,amiga,bs2000}* \
	$RPM_BUILD_ROOT%{_mandir}/man1/perl{cygwin,dos,hpux,machten,macos}* \
	$RPM_BUILD_ROOT%{_mandir}/man1/perl{mpeix,os2,os390,solaris,vmesa,vms,vos,win32}*

# dir tree for other perl modules
(
cd $RPM_BUILD_ROOT%{perl_sitelib}
install -d AI/NeuralNet Algorithm Apache Archive Array Astro Attribute \
	Audio Authen B Bundle Business CGI Cache Chart Class Config \
	Convert Crypt DBD Data Date Devel Digest Error ExtUtils File \
	Filesys Font Games Getopt GnuPG Graph HTML HTTP I18N IO/Socket IPC \
	Image Inline Language Lingua/EN List Locale Log MIME Mail Math \
	Module Net/SMTP NetServer Netscape News Number OLE Parse Pod \
	PostScript Proc RADIUS RPC RPM Regexp SOAP/Transport SQL Schedule \
	Set Sort Speech Spreadsheet Statistics String Sub Sys TeX Test \
	Text/Query Tie Time Tree Unicode WWW XML/{Filter,Handler,Parser} \
	auto/{AI,Array,Crypt,Data,Mail,Net,Schedule,Statistics,Text,WWW}

cd $RPM_BUILD_ROOT%{perl_sitearch}
install -d Astro Audio Authen B BSD Bit Compress Crypt/OpenSSL Data Devel \
	Digest File IPC Inline Locale Math Net Speech/Recognizer String Term \
	Text Unicode XML \
	auto/{Astro,Audio,Authen,BSD,Bit,Compress,Crypt/OpenSSL,Data,Devel} \
	auto/{Digest,File,IPC,Inline,Locale,Math,Net,Speech/Recognizer,String} \
	auto/{Term,Text,Unicode,XML}
)

# These File::Spec submodules are for non-Unix systems
rm -f $RPM_BUILD_ROOT%{perl_privlib}/File/Spec/[EMOVW]*.pm
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/File::Spec::{Epoc,Mac,OS2,VMS,Win32}.3pm*

# # Test::Harness is available as a separate package
# rm -f $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/Test/Harness.pm
# rm -f $RPM_BUILD_ROOT%{_mandir}/man3/Test::Harness.3pm*
# #
# # DB_File is available as a separate package
# rm -rf $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/%{_target_platform}%{perlthread}/auto/DB_File
# rm -f $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/%{_target_platform}%{perlthread}/DB_File.pm
# rm -f $RPM_BUILD_ROOT%{_mandir}/man3/DB_File.3pm*
# #
# # CGI is available as a separate package
# rm -rf $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/CGI*
# rm -f $RPM_BUILD_ROOT%{_mandir}/man3/CGI*.3pm*
# #
# # Attribute::Handlers is available as a separate package
# rm -rf $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/Attribute/Handlers*
# #
# # Time::HiRes is available as a separate package
# rm -rf $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/%{_target_platform}%{perlthread}/auto/Time/HiRes
# rm $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/%{_target_platform}%{perlthread}/Time/HiRes.pm

%{__bzip2} -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS

%attr(755,root,root) %{_bindir}/libnetcfg
%{_mandir}/man1/libnetcfg.*

%attr(755,root,root) %{_bindir}/perlbug
%{_mandir}/man1/perlbug.*

%attr(755,root,root) %{_bindir}/piconv
%{_mandir}/man1/piconv.*

%attr(755,root,root) %{_bindir}/psed
%{_mandir}/man1/psed.*

%attr(755,root,root) %{_bindir}/perldoc
%{perl_privlib}/pod/perldiag.pod
%{perl_privlib}/pod/perlfaq*.pod
%{perl_privlib}/pod/perlfunc.pod
%{_mandir}/man1/perld[io]*
%{_mandir}/man1/perlfaq*.*
%{_mandir}/man1/perlfunc.*


%files base
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/perl
%attr(755,root,root) %{_bindir}/perl%{version}
%{_mandir}/man1/perl.*
%lang(fi) %{_mandir}/fi/man1/perl*
%lang(pl) %{_mandir}/pl/man1/perl*


%{_mandir}/man3/[a-z]*
%{_mandir}/man3/English.*

%attr(755,root,root) %{_libdir}/lib*.so.%{version}


%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/[acdefh]*
%attr(755,root,root) %{_bindir}/perlcc
%attr(755,root,root) %{_bindir}/pl2pm
%attr(755,root,root) %{_bindir}/pstruct
%attr(755,root,root) %{_bindir}/[sx]*
%{_mandir}/man1/[acefh]*
%{_mandir}/man1/perlcc.*
%{_mandir}/man1/perld[^io]*
%{_mandir}/man1/pl2pm.*
%{_mandir}/man1/pstruct.*
%{_mandir}/man1/[sx]*

%attr(755,root,root) %{_libdir}/lib*.so
%{perl_archlib}/CORE


%files -n sperl
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/sperl%{version}
%attr(4755,root,root) %{_bindir}/suidperl




%files pod
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pod2*
%{perl_privlib}/pod/perl.pod
%{perl_privlib}/pod/perl[5abceghijklmnopqrstuvwx]*.pod
%{perl_privlib}/pod/perld[^i]*.pod
%{perl_privlib}/pod/perlf[^au]*.pod
%{_mandir}/man1/pod*
