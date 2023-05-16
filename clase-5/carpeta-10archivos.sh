#! /bin/bash
#! /bin/sh

dir='d:/Code\ Projects/github-test-clouding/clase-5'
filename="File_Lab1_$RANDOM" 
find $dir -type d -name $filename -delete
dir="$dir/$filename"
mkdir $dir
if [[ $? -eq 0 ]]
then
    for (( i=1;1<=10;i++ ))
    do
        file="File$i.txt"
        cat "$dir/$file"
        datetime=`date +"%d/%m/%Y %H:%M"`
        echo datetime >> $file 
    done
else
    echo "Error! Ha fallado la creación de la carpeta"
fi
