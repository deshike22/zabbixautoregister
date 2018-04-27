$a=((netstat -na | findstr TCP| %{$_.split(' ')[6];}) | %{ '{"{#TCPPORT}":"'+$_.split(':')[-1]+'"},';} | sort -u)
$b = -join $a
$c = $b.Substring(0,$b.Length-1)
write-output '{"data" : [' $c ']}'
