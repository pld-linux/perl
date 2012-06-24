
%define		__find_provides	%{_builddir}/%{name}-%{version}/find-perl-provides
%define		perlthread %{?_with_perl_threads:-thread-multi}

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
Version:	5.6.1
Release:	43
Epoch:		1
License:	GPL on Artistic
Group:		Applications/Text
Source0:	ftp://ftp.cpan.org/pub/CPAN/src/%{name}-%{version}.tar.gz
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
Patch9:		%{name}-use-LD_PRELOAD-for-lib%{name}.so.patch
Patch10:	%{name}-sitearch.patch
Patch11:	%{name}-soname.patch
Patch12:	%{name}-db3.patch
URL:		http://www.perl.org/
BuildRequires:	db3-devel
BuildRequires:	gdbm-devel
Provides:	perl(DynaLoader)
Provides:	perl-File-Spec = 0.82
Obsoletes:	perl-File-Spec
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

%description -l cs
Perl je vy��� programovac� jazyk s ko�eny v jazyce C, sed, awk a
shellov�ch skriptech. Perl je vhodn� pro manipulace s procesy a
soubory, ale obzvl�t� se hod� ke zpracov�v�n� text�. Perl vynik�
prakti�nost� ��innost�. I kdy� se pou��v� prakticky na cokoli,
v�t�ina Perlov�ch program� slou�� jako spr�vcovsk� utility nebo
programy pro WWW. V Perlu je naps�no velmi mnoho CGI skript�
pro WWW servery na cel�m sv�t�.

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
C, sed, awk, og skeljar forritunar. Perl er g�� � a� me�h�ndla processa
og skr�r og er s�rstaklega g�� � a� me�h�ndla texta. Perls kostir eru
nytsamleiki og virkni. � me�an �a� er nota� til a� gera marga mismunandi
hluti, Perl mest notu�u forrit eru krefisstj�rnunar t�l og vef forritun
St�r hluti af CGI forritum � vefnum eru skrifa�ar � Perl. �� �arft
perl pakkann settan upp � ��nu krefi svo �itt kerfi geti nota� Perl
scriptur.

%description -l it
Perl � un linguaggio di programmazione di alto livello derivato
dal linguaggio C, da sed, da awk e dallo scripting delle shell. E' adatto
per la gestione di processi, di file e in particolare di file di testo.
Perl � un linguaggio semplice ed efficiente. Viene utilizzato per
numerosi scopi, ma le sue applicazioni pi� diffuse sono le
utility di amministrazione del sistema e la programmazione Web. Una grossa
parte degli script CGI nel Web sono scritti in Perl. � consigliabile installare
il pacchetto perl in modo che il sistema sia in grado di gestire gli script di Perl.

%description -l ja
Perl �� C���졢sed, awk���ڤ� �����륹����ץƥ��󥰤˺�����
���ĥϥ���٥�� �ץ�������Ǥ���Perl �ϥץ�����ե�����ν�����
Ŭ�ڤ� ���ä� �ƥ����Ƚ����ˤϺ�Ŭ�Ǥ������ޤ��ޤʺ�Ȥ�
���Ѥ���ޤ����� Perl�κǤ����ˤʳ��Ѥϥ����ƥॢ�ɥߥ˥��ȥ졼�����
�桼�ƥ���ƥ��� web�ץ���ߥ󥰤Ǥ���web��� ����ʬ��CGI"
������ץȤ�Perl�ǽ񤫤�Ƥ��ޤ��� �����ƥबPerl������ץȤ�
���������褦�ˤ��뤿��ˤ�  perl�ѥå������� ���󥹥ȡ��뤹��
ɬ�פ�����ޤ���

%description -l pl
Perl jest j�zykiem przeznaczonym do skanowania plik�w tekstowych,
wyci�gania z nich informacji i drukowania raportu bazuj�cego na tych
informacjach. Jest r�wnie� doskona�ym j�zykiem do wielu prac
zwi�zanych z nadzorem systemu. J�zyk ten jest w zamierzeniu bardziej
praktyczny (�atwy w u�yciu, wydajny, kompletny) ni� pi�kny (skromny,
elegancki, minimalny).

%description -l pt
O perl � uma linguagem de programa��o de alto n�vel que tem como raizes o
C, sed, awk, e 'shell scripting'. O perl � bom a manipular processos e
ficheiros, e � especialmente bom para manipular texto. Caracter�sticas do
Perl s�o a efici�ncia e o uso pr�tico. As aplica��es mais comuns do Perl
s�o utilit�rios de administra��o de sistema e programa��o Web. Uma grande
parte dos 'scripts' CGI na Web s�o escritos em Perl. Voc� precisa do pacote
perl instalado no seu sistema de maneira a que este possa tratar de
'scripts' de Perl.

%description -l no

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
Perl je programovac� jazyk vy��ej �rovne s kore�mi v C, sed, awk,
a shell skriptoch. Perl m� vhodn� vlastnosti pre spracovanie procesov
a s�borov a je zvlṻ vhodn� pre spracovanie textu. Jeho cie�mi s�
prakti�nos� a efektivita. Aj ke� je pou��van� pre mno�stvo rozli�n�ch
�innost�, jeho naj�astej��m pou�it�m (a kde vynik� najviac) s�
pravdepodobne n�stroje pre spr�vu syst�mu a programovanie na Webe.
Ve�k� �as� CGI skriptov na Webe je nap�san� v Perle. Bal�k perl
potrebujete ma� nain�talovan�, aby bol v� syst�m schopn� spracova�
Perl skripty.

%description -l sv
Perl �r ett h�gniv�programspr�k med r�tter i C, sed, awk och
skalskript.  Perl �r bra p� att hantera processer och filer, och �r
s�rskilt bra p� att hantera text.  Utm�rkande f�r Perl �r att det �r
praktiskt och effektivt.  Det anv�nds f�r att g�ra en m�ngd olika
saker, men de vanligaste till�mpningarna �r systemadministration och
webbprogrammering.  En stor andel av CGI-skripten p� webben �r skrivna
i Perl.  Du beh�ver installera paketet perl p� ditt system s� att ditt

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
�����ڴ�����̺��ļ��������Ǵ����ı���Perl ���ص�������ʵ���Ժ���Ч�ԡ�
������������ִ����಻ͬ�����񣬵���ͨ����Ӧ����ϵͳ����ʵ�ó���� Web
��̡�\n Web �ϵĴ󲿷� CGI �ű���ʹ�� Perl
���Խ��б�д����������ϵͳ�а�װ perl  ������� �Ա㴦�� Perl �ű���

%package devel
Summary:	Perl development files
Summary(es):	Development and include files for perl
Summary(pl):	Pliki potrzebne przy tworzeniu w�asnych aplikacji w perlu
Summary(pt_BR):	Arquivos de desenvolvimento e cabe�alhos para o perl
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	%{name}-modules = %{version}
Obsoletes:	perl-lib-devel

%description devel
Files for developing applications which embed a Perl interpreter.

%description devel -l es
Development and include files for perl.

%description devel -l pl
Pliki potrzebne przy tworzeniu w�asnych aplikacji w perlu.

%description devel -l pt_BR
Arquivos de desenvolvimento e cabe�alhos para o perl.

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
Group:		Applications/Text
Requires:	%{name} = %{version}
Obsoletes:	perl-suidperl

%description -n sperl
sperl is a setuid root binary copy of perl that allows for (hopefully)
more secure running of setuid Perl scripts.

%description -n sperl -l de
sperl ist eine bin�re setuid Kopie von Perl, mit der (hoffentlich)
setuid-Skripts sicherer ausgef�hrt werden k�nnen.

%description -n sperl -l pl
sperl es una copia binaria de setuid para perl que le permite\n"
una ejecuci�n m�s segura de los scripts de Perl setuid."

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
sperl jest to kopia setuid root programu binarnego perl
umo�liwiaj�ca bezpieczniejsze (miejmy nadziej�) uruchamianie
setuidowych skrypt�w Perla.

%description -n sperl -l pt
O suidperl � uma c�pia do perl com 'setuid' que permite uma execu��o mais
segura dos 'scripts' de Perl 'setuid'.

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
suidperl �� perl �� setuid �����Ƹ�����������ϣ����ˣ�
����ȫ������ setuid perl �ű���

%package modules
Summary:	Practical Extraction and Report Language - modules
Summary(es):	Perl's base modules
Summary(pl):	Practical Extraction and Report Language - modu�y
Summary(pt_BR):	M�dulos do perl b�sicos
Group:		Applications/Text
Requires:	perl-Test-Harness
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

%description modules -l es
This package contains standard perl modules needed by some
application/scripts.

%description modules -l pl
Practical Extraction and Report Language - modu�y.

%description modules -l pt_BR
Este pacote cont�m m�dulos perl b�sicos necess�rios por alguns
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
STDH	= \$(filter %{_includedir}/%%, \$(shell rpm -q --queryformat '[%%{FILENAMES}\n]' \$(PKGS)))
STDH	+= \$(wildcard %{_includedir}/linux/*.h) \$(wildcard %{_includedir}/asm/*.h) \$(wildcard %{_includedir}/scsi/*.h)
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
	cd %{_includedir} && \$(H2PH) \$(STDH:%{_includedir}/%%=%%)

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

## Fix lib
rm -f $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/*/CORE/libperl.so*
install libperl.so.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -sf libperl.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libperl.so

## Fix installed man pages list
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/perl{5004delta,5005delta,aix,amiga,bs2000}* \
	$RPM_BUILD_ROOT%{_mandir}/man1/perl{cygwin,dos,hpux,machten,macos}* \
	$RPM_BUILD_ROOT%{_mandir}/man1/perl{mpeix,os2,os390,solaris,vmesa,vms,vos,win32}*

# dir tree for other perl modules
(cd $RPM_BUILD_ROOT%{_libdir}/perl5/site_perl
install -d Apache Archive Authen B Bundle Business CGI Class Convert Crypt \
	DBD Data Date Devel ExtUtils File Filesys Font Games Getopt Graph \
	HTML HTTP I18N IO/Socket IPC Image Inline Language Lingua/EN \
	Locale Log MIME Mail Math Module Net NetServer Netscape News \
	Number Parse Pod PostScript Proc RADIUS RPC Regexp Set Sort \
	Statistics String Sys TeX Test Text/Query Tie Time Tree XML \
	auto/{Net,Statistics,Text,WWW}

cd %{_target_platform}*/%{version}
install -d Authen BSD Bit Compress Crypt Data Devel Digest File IPC \
	Locale Math Net String Term Text Unicode XML \
	auto/{Authen,BSD,Bit,Compress,Crypt,Data,Devel,Digest,File,IPC} \
	auto/{Locale,Math,Net,String,Term,Text,Unicode,XML}
)

# These File::Spec submodules are for non-Unix systems
rm -f $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/File/Spec/[EFMOVW]*.pm
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/File::Spec::{Epoc,Functions,Mac,OS2,VMS,Win32}.3pm*
#
# Newer Test::Harness is available as a separate package
rm -f $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/Test/Harness.pm
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/Test::Harness.3pm*
#
# Newer DB_File is available as a separate package 
rm -rf $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DB_File
rm -f $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/%{_target_platform}*/DB_File.pm
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/DB_File.3pm*
#
# Newer CGI is available as a separate package 
rm -rf $RPM_BUILD_ROOT%{_libdir}/perl5/%{version}/CGI*
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/CGI*.3pm*

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

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
%{_libdir}/perl5/site_perl/Apache
%{_libdir}/perl5/site_perl/Archive
%{_libdir}/perl5/site_perl/Authen
%{_libdir}/perl5/site_perl/Bundle
%{_libdir}/perl5/site_perl/Business
%{_libdir}/perl5/site_perl/CGI
%{_libdir}/perl5/site_perl/Class
%{_libdir}/perl5/site_perl/Convert
%{_libdir}/perl5/site_perl/Crypt
%{_libdir}/perl5/site_perl/DBD
%{_libdir}/perl5/site_perl/Data
%{_libdir}/perl5/site_perl/Date
%{_libdir}/perl5/site_perl/Devel
%{_libdir}/perl5/site_perl/ExtUtils
%{_libdir}/perl5/site_perl/File
%{_libdir}/perl5/site_perl/Filesys 
%{_libdir}/perl5/site_perl/Font
%{_libdir}/perl5/site_perl/Games
%{_libdir}/perl5/site_perl/Getopt
%{_libdir}/perl5/site_perl/Graph
%{_libdir}/perl5/site_perl/HTML
%{_libdir}/perl5/site_perl/HTTP
%{_libdir}/perl5/site_perl/I18N
%{_libdir}/perl5/site_perl/IO
%{_libdir}/perl5/site_perl/IPC
%{_libdir}/perl5/site_perl/Image
%{_libdir}/perl5/site_perl/Inline
%{_libdir}/perl5/site_perl/Language
%{_libdir}/perl5/site_perl/Lingua
%{_libdir}/perl5/site_perl/Locale
%{_libdir}/perl5/site_perl/Log
%{_libdir}/perl5/site_perl/MIME
%{_libdir}/perl5/site_perl/Mail
%{_libdir}/perl5/site_perl/Math
%{_libdir}/perl5/site_perl/Module
%{_libdir}/perl5/site_perl/News
%{_libdir}/perl5/site_perl/Net
%{_libdir}/perl5/site_perl/Number
%{_libdir}/perl5/site_perl/Parse
%{_libdir}/perl5/site_perl/Pod
%{_libdir}/perl5/site_perl/PostScript
%{_libdir}/perl5/site_perl/Proc
%{_libdir}/perl5/site_perl/RADIUS
%{_libdir}/perl5/site_perl/RPC
%{_libdir}/perl5/site_perl/Regexp
%{_libdir}/perl5/site_perl/Set
%{_libdir}/perl5/site_perl/Sort
%{_libdir}/perl5/site_perl/Statistics
%{_libdir}/perl5/site_perl/String
%{_libdir}/perl5/site_perl/Sys
%{_libdir}/perl5/site_perl/TeX
%{_libdir}/perl5/site_perl/Test
%{_libdir}/perl5/site_perl/Text
%{_libdir}/perl5/site_perl/Tie
%{_libdir}/perl5/site_perl/Time
%{_libdir}/perl5/site_perl/Tree
%{_libdir}/perl5/site_perl/XML
%{_libdir}/perl5/site_perl/auto
%dir %{_libdir}/perl5/site_perl/%{_target_platform}*
%dir %{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Authen
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/BSD
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Bit
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Compress
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Crypt
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Data
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Devel
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Digest
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/File
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/IPC
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Locale
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Math
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Net
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/String
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Term
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Text
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/Unicode
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/XML
%dir %{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Authen
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/BSD
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Bit
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Compress
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Crypt
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Data
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Devel
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Digest
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/File
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/IPC
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Locale
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Math
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Net
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/String
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Term
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Text
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/Unicode
%{_libdir}/perl5/site_perl/%{_target_platform}*/%{version}/auto/XML

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
%{_mandir}/man3/AutoL*
%{_mandir}/man3/C[aow]*
%{_mandir}/man3/D[iy]*
%{_mandir}/man3/Exp*
%{_mandir}/man3/File::[BFPSs]*
%{_mandir}/man3/FileH*
%{_mandir}/man3/IO*
%{_mandir}/man3/IPC::O*
%{_mandir}/man3/PO*
%{_mandir}/man3/Sele*
%{_mandir}/man3/So*
%{_mandir}/man3/Sym*
%{_mandir}/man3/Text::[TW]*
%{_mandir}/man3/Time::L*
%{_mandir}/man3/[Xivw]*
%{_mandir}/man3/attri*
%{_mandir}/man3/au*
%{_mandir}/man3/bas*
%{_mandir}/man3/ch*
%{_mandir}/man3/fie*
%{_mandir}/man3/l[io]*
%{_mandir}/man3/ov*
%{_mandir}/man3/st*

%files devel
%defattr(644,root,root,755)
%doc README Changes
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
%lang(fi) %{_mandir}/fi/man1/perl[a-z]*.1*
%lang(pl) %{_mandir}/pl/man1/perl[a-z]*.1*
#unknown
%{_mandir}/man3/W*


%{_libdir}/perl5/%{version}/%{_target_platform}*/CORE

%files -n sperl
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/sperl%{version}
%attr(4755,root,root) %{_bindir}/suidperl

%files modules
%defattr(644,root,root,755)
%{_libdir}/perl5/site_perl/B
%{_libdir}/perl5/site_perl/NetServer
%{_libdir}/perl5/site_perl/Netscape
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
#%{_libdir}/perl5/%{version}/File/Spec/[A-OV-Z]*.pm
%{_libdir}/perl5/%{version}/Getopt
%{_libdir}/perl5/%{version}/I18N
%{_libdir}/perl5/%{version}/Math
%{_libdir}/perl5/%{version}/Net
%{_libdir}/perl5/%{version}/Pod
%{_libdir}/perl5/%{version}/Search
%{_libdir}/perl5/%{version}/Term
#%{_libdir}/perl5/%{version}/Test
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
# we have newer DB_File in a separate package
#%dir %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DB_File
#%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DB_File/autosplit.ix
#%{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DB_File/DB_File.bs
#%attr(755,root,root) %{_libdir}/perl5/%{version}/%{_target_platform}*/auto/DB_File/DB_File.so
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
#%{_libdir}/perl5/%{version}/%{_target_platform}*/DB_File.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/attrs.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/GDBM_File.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/NDBM_File.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/Opcode.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/O.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/ops.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/re.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/Safe.pm
%{_libdir}/perl5/%{version}/%{_target_platform}*/SDBM_File.pm

%{_mandir}/man3/An*
%{_mandir}/man3/AutoS*
%{_mandir}/man3/[BMNOU]*
%{_mandir}/man3/C[Pl]*
%{_mandir}/man3/D[Beu]*
%{_mandir}/man3/E[nr]*
%{_mandir}/man3/Ext*
%{_mandir}/man3/Fa*
%{_mandir}/man3/File::[CDGT]*
%{_mandir}/man3/FileC*
%{_mandir}/man3/Fin*
%{_mandir}/man3/G[De]*
%{_mandir}/man3/I1*
%{_mandir}/man3/IPC::[MS]*
%{_mandir}/man3/Po*
%{_mandir}/man3/S[Dah]*
%{_mandir}/man3/Sea*
%{_mandir}/man3/Self*
%{_mandir}/man3/Sys*
%{_mandir}/man3/Te[rs]*
%{_mandir}/man3/Text::[APS]*
%{_mandir}/man3/Tie*
%{_mandir}/man3/Time::[glt]*
%{_mandir}/man3/attrs*
%{_mandir}/man3/b[ly]*
%{_mandir}/man3/ch*
%{_mandir}/man3/d*
%{_mandir}/man3/fil*
%{_mandir}/man3/le*
%{_mandir}/man3/op*
%{_mandir}/man3/re*
%{_mandir}/man3/s[iu]*
%{_mandir}/man3/u*

%files pod
%defattr(644,root,root,755)
%{_libdir}/perl5/%{version}/pod/perl[^d]*
%{_libdir}/perl5/%{version}/pod/perld[^i]*
