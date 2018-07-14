#!/usr/bin/ksh

secs(){

Date=$1
Month=$(echo "$@"|awk '{print $1}')
Day=$(echo "$@"|awk '{print $2}')
Hour=$(echo "$@"|awk '{print $3}'|cut -d':' -f1)
Minute=$(echo "$@"|awk '{print $3}'|cut -d':' -f2)
Seconds=$(echo "$@"|awk '{print $3}'|cut -d':' -f3)
Time=$(echo "$@"|awk '{print $3}')
Year=$(echo "$@"|awk '{print $4}')

case $Month in
        Jan )
                Month=01 ;;
        Feb )
                Month=02 ;;
        Mar )
                Month=03 ;;
        Apr )
                Month=04 ;;
        May )
                Month=05 ;;
        Jun )
                Month=06 ;;
        Jul )
                Month=07 ;;
        Aug )
                Month=08 ;;
        Sep )
                Month=09 ;;
        Oct )
                Month=10 ;;
        Nov )
                Month=11 ;;
        Dec )
                Month=12 ;;
esac



ty=$(( $Year + 10000 )) # handle negative year up to -9999
p=$(( $ty - 1 ))
set -A odm 0 0 31 59 90 120 151 181 212 243 273 304 334
rd=$(( $p * 365 + $p / 4 - $p / 100 + $p / 400 + ${odm[$Month]} + $Day + ( ( 1 - ( 14 - $Month ) / 12 ) * ( $ty / 4 - $ty / 100 + $ty / 400 - ( $p / 4 - $p / 100 + $p / 400
) ) ) - 3652425 ))
echo $(( $rd * 24 * 60 * 60 + $Hour * 60 * 60 + $Minute * 60 + $Seconds ))


}

certdate=$(secs "$@")
now=$(secs $(date +"%b %d %H:%M:%S %Y"))
diff=$(($certdate - $now))
echo $diff
