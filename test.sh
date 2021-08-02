#!usr/bin/bash
file="test.sh"
i=1
while read line;
do
	echo "Line No. $i : $line"
	((i++))
done 
< $file
