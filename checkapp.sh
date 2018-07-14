#!/bin/sh
SSH_USER=''
SSH_PASS=''
CMD='which perl'
for server in $(cat unix.csv)
do
   result=`sshpass -p $SSH_PASS ssh -o ConnectTimeout=3 -o BatchMode=no -o StrictHostKeyChecking=no $SSH_USER@$server '$CMD' 2>/dev/null`
   echo $server,$result
done
