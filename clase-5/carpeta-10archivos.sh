#! /bin/bash
#! /bin/sh

dir='d:/Lab_Bash'
foldername="Folder_Lab1_$RANDOM" 
find $dir -type d -name $foldername -delete
dir="$dir/$foldername"
mkdir $dir
if [[ $? -eq 0 ]]
then
    for (( i=1;i<=10;i++ ))
    do
        file="File$i.txt"
        cat "$dir/$file"
        datetime=`date +"%d/%m/%Y %H:%M:%S"`
        echo $datetime >> "$dir/$file"
    done
else
    echo "Error! Ha fallado la creación de la carpeta"
fi
