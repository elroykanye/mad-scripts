#!/bin/bash

NOL=0
while read i;
do
	isFile=$(file -0 "$i" | cut -d $'\0' -f2)
	case "$isFile" in
   		(*text*)
   		echo "$i is a text file"
		LINES=`cat $i | wc -l` 
		NOL=$(($NOL+$LINES))
   		;;
	(*)
		echo "$i is not a text file, please use a different file"
		;;
	esac
done < <(find .)

echo $NOL
return $NOL
