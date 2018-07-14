#!/usr/bin/sh

macro=$1
for ports in $(echo $macro | tr , "\n");
do portlist="$portlist,"'{"{#TCPPORT}":"'$ports'"}';
done;
echo '{"data":['${portlist#,}']}'
