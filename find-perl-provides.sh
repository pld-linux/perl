#!/bin/sh
# $Id$
ulimit -c 0

filelist=`sed "s/['\"]/\\\&/g"`
if [ -f __rpm_noautoprovfiles ] ; then
	for i in `cat __rpm_noautoprovfiles`; do
		filelist=`echo $filelist | sed "s![[:space:]]*$i[[:space:]]*!!g"`
	done
fi


echo $filelist|/usr/lib/rpm/find-provides
provides_perl=`@perl@ @perl_build_dir@/find-perl.prov $filelist`
if [ -f __rpm_noautoprov ] ; then
	for i in `cat __rpm_noautoprov`; do
		provides_perl=`echo $provides_perl | sed "s!\<$i[[:space:]]*!!g"`
	done
fi

echo "$provides_perl"

