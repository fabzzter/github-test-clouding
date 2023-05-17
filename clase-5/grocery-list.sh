#! /bin/bash
#! /bin/sh

ind=0
dir='d:/Lab_Bash/Grocery_List'
grocery_list[0]='GROCERY LIST'
file="Grocery_List_$RANDOM.txt"

while [ $ind -ne 2 ]
do
    echo "Por favor digita el item a ingresar a la lista de compras"
    read item
    grocery_list=("${grocery_list[@]}" $item)
    echo "Desea seguir ingresando mas items? (s/n)"
    read ans
    if [[ $ans == 'n' ]] then
        ind=2
    fi
done

cat "$dir/$file"
for i in "${grocery_list[@]}"
do
    echo $i >> "$dir/$file"
done