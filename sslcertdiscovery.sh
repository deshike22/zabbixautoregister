#!/usr/bin/sh
host=$1
macro=$2

#for ports in $(`./zext_ssl_cert.sh -i $1
#do ;
#done;

for ports in $(echo $macro | tr , "\n");do
        issuer=$(./externalscripts/zext_ssl_cert.sh -i $1 $ports)
        if [ -n "$issuer"  ];then
                portlist="$portlist,"'{"{#TCPPORT}":"'$ports'"}';
        fi
done;
echo '{"data":['${portlist#,}']}'
