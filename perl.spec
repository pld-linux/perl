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
Summary(cs):	Programovac� jazyk Perl
Summary(da):	Programmeringssproget Perl
Summary(de):	Praktische Extraktions- und Berichtsprache
Summary(es):	Lenguaje pr�ctica de extracci�n y listado
Summary(fr):	Langage de programmation Perl
Summary(id):	Bahasa pemrograman Perl
Summary(is):	Forritunarm�li� Perl
Summary(it):	Perl: linguaggio di programmazione
Summary(ja):	Perl �ץ���ߥ󥰸���
Summary(ko):	�� ���α׷��� ���
Summary(no):	Programmeringsspr�ket Perl
Summary(pl):	Interpreter j�zyka Perl (Practical Extraction and Report Language)
Summary(pt):	A linguagem de programa��o Perl
Summary(pt_BR):	Linguagem pr�tica de extra��o e relat�rio
Summary(ru):	���� ���������������� Perl
Summary(sk):	Programovac� jazyk Perl
Summary(sl):	Programski jezik Perl
Summary(sv):	Programmeringsspr�ket Perl
Summary(tr):	Kabuk yorumlama dili
Summary(zh_CN):	Perl ������ԡ�
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
Perl je vy��� programovac� jazyk s ko�eny v jazyce C, sed, awk a
shellov�ch skriptech. Perl je vhodn� pro manipulace s procesy a
soubory, ale obzvl�t� se hod� ke zpracov�v�n� text�. Perl vynik�
prakti�nost� ��innost�. I kdy� se pou��v� prakticky na cokoli, v�t�ina
Perlov�ch program� slou�� jako spr�vcovsk� utility nebo programy pro
WWW. V Perlu je naps�no velmi mnoho CGI skript� pro WWW servery na
cel�m sv�t�.

%description -l da
Perl er et h�gniveauprogramsprog med r�tter i C, sed, awk og
skalskript. Perl er godt p� at behandle processer og filer, og er
s�rskilt godt p� at behandle text. Utm�rkende for Perl er at det er
praktisk og effektivt. Det bruges for at g�re en m�ngd forskellige
saker, men de almindeligeste programmerne er systemadministration og
webbprogrammering. En stor andel af CGI-skripten p� webben er skrivna
i Perl. Du beh�ver installere pakken perl p� dit system s� at ditt
system kan behandle Perlskript.

%description -l de
Perl ist eine Interpreter-Sprache, die zum Durchsuchen beliebiger
Text- dateien, Extrahieren von Informationen aus diesen Dateien und
Drucken von auf diesen Informationen basierenden Berichten optimiert
ist. Die Sprache eignet sich au�erdem f�r viele
Systemverwaltungsaufgaben. Sie ist eher praktisch (einfache
Anwendung,effizient, vollst�ndig) als sch�n (winzig, elegant,
minimal).

%description -l es
Perl es un lenguaje interpretado, optimizado para manejar archivos
texto, extrayendo informaci�n de estos archivos y mostrando listados
basados en esta informaci�n. Tambi�n es un buen lenguaje para varias
tareas de administraci�n de sistema. El lenguaje busca ser m�s
pr�ctico (f�cil de usar, eficiente, completo) que bonito (min�sculo,
elegante, m�nimo).

%description -l fr
Perl est un langage interpr�t�, optimis� pour filtrer des fichiers
texte, extraire des informations de ces fichiers, et imprimer des
rapports bas�s sur ces informations. C'est aussi un bon langage pour
de nombreuses proc�dures de gestion syst�me. Ce langage se veut
pratique (simple � utiliser, efficace, complet) autant qu'agr�able
(conscrit, �l�gant, minimal).

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
Perl er h�s stigs forritunar tungum�l sem � r�tur s�nar a� rekja til
C, sed, awk, og skeljar forritunar. Perl er g�� � a� me�h�ndla
processa og skr�r og er s�rstaklega g�� � a� me�h�ndla texta. Perls
kostir eru nytsamleiki og virkni. � me�an �a� er nota� til a� gera
marga mismunandi hluti, Perl mest notu�u forrit eru krefisstj�rnunar
t�l og vef forritun St�r hluti af CGI forritum � vefnum eru skrifa�ar
� Perl. �� �arft perl pakkann settan upp � ��nu krefi svo �itt kerfi
geti nota� Perl scriptur.

%description -l it
Perl � un linguaggio di programmazione di alto livello derivato dal
linguaggio C, da sed, da awk e dallo scripting delle shell. E' adatto
per la gestione di processi, di file e in particolare di file di
testo. Perl � un linguaggio semplice ed efficiente. Viene utilizzato
per numerosi scopi, ma le sue applicazioni pi� diffuse sono le utility
di amministrazione del sistema e la programmazione Web. Una grossa
parte degli script CGI nel Web sono scritti in Perl. � consigliabile
installare il pacchetto perl in modo che il sistema sia in grado di
gestire gli script di Perl.

%description -l ja
Perl �� C���졢sed, awk���ڤ� �����륹����ץƥ��󥰤˺�����
���ĥϥ���٥�� �ץ�������Ǥ���Perl �ϥץ�����ե�����ν�����
Ŭ�ڤ� ���ä� �ƥ����Ƚ����ˤϺ�Ŭ�Ǥ������ޤ��ޤʺ�Ȥ�
���Ѥ���ޤ����� Perl�κǤ����ˤʳ��Ѥϥ����ƥॢ�ɥߥ˥��ȥ졼�����
�桼�ƥ���ƥ��� web�ץ���ߥ󥰤Ǥ���web��� ����ʬ��CGI"
������ץȤ�Perl�ǽ񤫤�Ƥ��ޤ��� �����ƥबPerl������ץȤ�
���������褦�ˤ��뤿��ˤ� perl�ѥå������� ���󥹥ȡ��뤹��
ɬ�פ�����ޤ���

%description -l pl
Perl jest j�zykiem przeznaczonym do skanowania plik�w tekstowych,
wyci�gania z nich informacji i drukowania raportu bazuj�cego na tych
informacjach. Jest r�wnie� doskona�ym j�zykiem do wielu prac
zwi�zanych z nadzorem systemu. J�zyk ten jest w zamierzeniu bardziej
praktyczny (�atwy w u�yciu, wydajny, kompletny) ni� pi�kny (skromny,
elegancki, minimalny).

%description -l pt
O perl � uma linguagem de programa��o de alto n�vel que tem como
raizes o C, sed, awk, e 'shell scripting'. O perl � bom a manipular
processos e ficheiros, e � especialmente bom para manipular texto.
Caracter�sticas do Perl s�o a efici�ncia e o uso pr�tico. As
aplica��es mais comuns do Perl s�o utilit�rios de administra��o de
sistema e programa��o Web. Uma grande parte dos 'scripts' CGI na Web
s�o escritos em Perl. Voc� precisa do pacote perl instalado no seu
sistema de maneira a que este possa tratar de 'scripts' de Perl.

%description -l pt_BR
Perl � uma linguagem interpretada, otimizada para tratar arquivos
texto, extraindo informa��o desses arquivos e mostrando relat�rios
baseados nessa informa��o. Tamb�m � uma boa linguagem para v�rias
tarefas de administra��o de sistema. A linguagem procura ser mais
pr�tica (f�cil de usar, eficiente, completa) do que bonita (min�scula,
elegante, m�nima).

%description -l ru
Perl - ��� ���������������� ���� ����������������, �������� ������� �
C, sed, awk � ����� ��������� �������� (shell). Perl ����� ��� ������
� ���������� � �������, � �������� ����� ��� ����� ��������� �������.
����������� Perl - ������������ � �������������. ���� �� �
������������ ��� ������� ����� ������ �����, �������� ����������������
���������� (� ��, � ��� �� �����) ���, ��������, ������� ����������
����������������� � web-����������������. ������� ����� CGI ��������
�������� �� Perl.

%description -l sk
Perl je programovac� jazyk vy��ej �rovne s kore�mi v C, sed, awk, a
shell skriptoch. Perl m� vhodn� vlastnosti pre spracovanie procesov a
s�borov a je zvlṻ vhodn� pre spracovanie textu. Jeho cie�mi s�
prakti�nos� a efektivita. Aj ke� je pou��van� pre mno�stvo rozli�n�ch
�innost�, jeho naj�astej��m pou�it�m (a kde vynik� najviac) s�
pravdepodobne n�stroje pre spr�vu syst�mu a programovanie na Webe.
Ve�k� �as� CGI skriptov na Webe je nap�san� v Perle. Bal�k perl
potrebujete ma� nain�talovan�, aby bol v� syst�m schopn� spracova�
Perl skripty.

%description -l sv
Perl �r ett h�gniv�programspr�k med r�tter i C, sed, awk och
skalskript. Perl �r bra p� att hantera processer och filer, och �r
s�rskilt bra p� att hantera text. Utm�rkande f�r Perl �r att det �r
praktiskt och effektivt. Det anv�nds f�r att g�ra en m�ngd olika
saker, men de vanligaste till�mpningarna �r systemadministration och
webbprogrammering. En stor andel av CGI-skripten p� webben �r skrivna
i Perl. Du beh�ver installera paketet perl p� ditt system s� att ditt

%description -l tr
Perl, metin dosyalar�n� taramak, bu metin dosyalar�ndan bilgi ��karmak
ve bu bilgiye dayal� raporlar haz�rlamak icin geli�tirilmi� bir
yorumlamal� dildir. Ayr�ca pek �ok sistem y�netimi g�revleri i�in de
yararl� yetenekleri vard�r. Perl, g�zel (ufak, zarif, minimum)
olmaktan �ok, pratik olmaya y�nelik (kullan�m� kolay, verimli,
eksiksiz) olarak tasarlanm��t�r.

%description -l uk
Perl - �� �������������� ���� �������������, �� �������դ ��ŧ � C,
sed, awk �� ����� ��������� �������� (shell). Perl ����� Ц������� ���
������ � ��������� �� �������, � �������� - ��� ������� ����Ԧ�.
���������Ԧ Perl - �������Φ��� �� �������Φ���. ���� ����� ����
������������ ���� ������, ���¦��� �������� ���� ������������ (��
�������Φ�� �������) ��, ���צ���, ���̦�� ���������� ��ͦΦ���������
�� web-�������������. ����� ������� CGI �����Ԧ� �������� �� Perl.

%description -l zh_CN
Perl ��һ�ָ߼�������ԣ���Դ�� C��sed��awk �� shell �ű���
�����ڴ�����̺��ļ��������Ǵ����ı���Perl
���ص�������ʵ���Ժ���Ч�ԡ�
������������ִ����಻ͬ�����񣬵���ͨ����Ӧ����ϵͳ����ʵ�ó���� Web
��̡�\n Web �ϵĴ󲿷� CGI �ű���ʹ�� Perl
���Խ��б�д����������ϵͳ�а�װ perl ������� �Ա㴦�� Perl �ű���

%package base
Summary:	Base perl components for a minimal installation
Summary(pl):	Podstawowe sk�adniki potrzebne do minimalnej instalacji perla
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
Podstawowe sk�adniki, pliki, g��wne modu�y itp. - minimalna u�ywalna
instalacja Perla. Zaleca si� instalacj� pe�nego Perla (pakietu perl)
je�li to tylko mo�liwe.

%package devel
Summary:	Perl development files
Summary(pl):	Pliki potrzebne przy tworzeniu w�asnych aplikacji w perlu
Summary(pt_BR):	Arquivos de desenvolvimento e cabe�alhos para o perl
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
Sk�adniki potrzebne do tworzenia aplikacji osadzaj�cych interpreter
Perla oraz kompilowania modu��w Perla.

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
Dokumentacja referencyjna w formacie man do j�zyka Perl (Practical
Extraction and Report Language) i jego interpretera.

%package modules
Summary:	Modules from the core perl distribution
Summary(pl):	Modu�y z podstawowej dystrybucji perla
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
Practical Extraction and Report Language - modu�y z podstawowej
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
drzewie instalacji perla lub w skypcie perlowym i wy�wietla go przez
"pod2man | nroff -man | $PAGER". Program ten u�ywany jest g��wnie do
dokumentacji modu��w z bibliotek Perla.

%package -n sperl
Summary:	Perl setuid root binaries for use with setuid Perl scripts
Summary(de):	sperl zur Verwendung mit setuid Perl-Skripts
Summary(es):	sperl, para uso con los scrips de Perl setuid
Summary(fr):	sperl, � utiliser avec les scripts Perl setuid
Summary(it):	sperl, da usare con gli script di Perl setuid
Summary(ja):	Setuid Perl scripts �Ȱ��˻��Ѥ��뤿��� suidperl
Summary(ko):	Setuid �� ��ũ��Ʈ�� �Բ� ���Ǵ� suidperl
Summary(pl):	Binaria setuid root Perla dla setuid-owych skrypt�w Perla
Summary(pt):	O suidperl, para usar com os programas de Perl 'setuid'
Summary(ru):	SUID ������ ����� Perl
Summary(sv):	sperl, att anv�ndas med setuid perlskript
Summary(uk):	SUID-���Ӧ� ���� Perl
Summary(zh_CN):	sperl�������� setuid perl �ű�һ��ʹ��
Group:		Development/Languages/Perl
Requires:	%{name}-base = %{version}
Obsoletes:	perl-suidperl

%description -n sperl
sperl is a setuid root binary copy of perl that allows for (hopefully)
more secure running of setuid Perl scripts.

%description -n sperl -l de
sperl ist eine bin�re setuid Kopie von Perl, mit der (hoffentlich)
setuid-Skripts sicherer ausgef�hrt werden k�nnen.

%description -n sperl -l es
sperl es una copia binaria de setuid para perl que le permite una
ejecuci�n m�s segura de los scripts de Perl setuid.

%description -n sperl -l fr
sperl est une copie binaire setuid de perl qui permet une ex�cution
plus s�re de scripts Perl setuid.

%description -n sperl -l it
sperl � una copia binaria setuid di perl che consente un'esecuzione
pi� sicura di script di Perl setuid.

%description -n sperl -l ja
sperl �� setuid Perl scripts.���äȰ�����ư��Ǥ���(���ԤΤ���)�٤�
perl ��setuid �Х��ʥ� ���ԡ��Ǥ���

%description -n sperl -l pl
sperl jest to kopia setuid root programu binarnego perl umo�liwiaj�ca
bezpieczniejsze (miejmy nadziej�) uruchamianie setuidowych skrypt�w
Perla.

%description -n sperl -l pt
O suidperl � uma c�pia do perl com 'setuid' que permite uma execu��o
mais segura dos 'scripts' de Perl 'setuid'.

%description -n sperl -l ru
Suid perl ����������� ��� ����, ����� ���� ����������� ���������
������� � ������������ ����� SUID. ���� � ���� �������� ����������
����� ��������, ��������� ���������� ������������ ��� �������������
suid perl ��� ����� ������������ ����� ������������ �������������
���������.

%description -n sperl -l sv
suidperl �r en setuid bin�rkopia av pers som till�ter
(f�rhoppningsvis) s�krare k�rning av setuid perlskript.

%description -n sperl -l zh_CN
suidperl �� perl �� setuid �����Ƹ�����������ϣ����ˣ� ����ȫ������
setuid perl �ű���

%package tools
Summary:	Various tools from the core perl distribution
Summary(pl):	R�ne narz�dzia z podstawowej dystrybucji perla
Group:		Applications
Requires:	%{name}-base = %{version}

%description tools
Various tools from the core perl distribution:

 a2p       - Awk to Perl translator
 find2perl - translate find command lines to Perl code
 piconv    - iconv(1), reinvented in perl
 psed, s2p - a stream editor

%description modules -l pl
R�ne narz�dzia z podstawowej dystrybucji Perla:

 a2p       - translator skrypt�w Awka do Perla
 find2perl - t�umaczenie linii polece� programu find na kod w Perlu
 piconv    - iconv(1) napisany w Perlu
 psed, s2p - edytor strumieniowy

%package tools-devel
Summary:	Developer's tools from the core perl distribution
Summary(pl):	Narz�dzia z podstawowej dystrybucji perla, przeznaczone dla programist�w
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
R�ne narz�dzia z podstawowej dystrybucji Perla:

 c2ph, pstruct - zrzucanie struktur C w postaci generowanej z tablic
                 symboli z cc -g -S
 dprofpp       - wy�wietlanie perlowych danych profiluj�cych
 enc2xs        - generator modu��w koduj�cych w Perlu
 h2ph          - konwerter plik�w nag��wkowych .h z C na perlowe pliki
                 nag��wkowe .ph
 h2xs          - konwerter plik�w nag��wkowych .h z C na rozszerzenia
                 Perla
 perlcc        - generator binarek z program�w w Perlu
 perlivp       - procedura weryfikacji instalacji Perla
 pl2pm         - zgrubne narz�dzie do t�umaczenia plik�w pl Perla 4 na
                 modu�y .pm Perla 5
 splain        - wymuszenie obszernych ostrze�e� diagnostycznych

%package tools-pod
Summary:	Tools for manipulating files in the POD format
Summary(pl):	Narz�dzia do przetwarzania plik�w w formacie POD
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
Narz�dzia do przetwarzania plik�w w formacie POD (Plain Old
Documentation):

 pod2html   - konwerter plik�w .pod do plik�w .html
 pod2latex  - konwerter dokumentacji pod do formatu LaTeX
 pod2man    - konwerter danych POD na wej�cie sformatowane dla *roffa
 pod2text   - konwerter danych POD na sformatowany tekst ASCII
 pod2usage  - wypisanie informacji o u�ywaniu programu z dokumentacji
              osadzonej w plikach
 podchecker - kontrola sk�adni dokumentacji w formacie POD
 podselect  - wypisanie wybranych sekcji z dokumentacji POD

%package -n microperl
Summary:	A really minimal perl, even more minimal than miniperl
Summary(pl):	Naprawd� minimalny Perl, nawet bardziej minimalny ni� miniperl
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
microperl ma by� naprawd� minimalnym Perlem, nawet bardziej minimalnym
od miniperla. Uruchamianie Configure nie jest potrzebne do zbudowania
microperla, z drugiej strony oznacza to, �e interfejs mi�dzy Perlem a
systemem operacyjnym pozostaje bardzo minimalny.

Ca�o�� jest eksperymentalna. Je�li nie wiesz co zrobi� z microperlem,
prawdopodobnie nie powiniene� tego robi�. Nie zg�aszaj b��d�w w
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
