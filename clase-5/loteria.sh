#! /bin/bash

echo "Por favor ingresa un numero del 1 al 100"
read numero
if [[ $numero -ge 1 ]] && [[ $numero -le 100 ]]
then
    echo "Bingo! tu numero es el siguiente ${numero}"
else
    echo "El numero no esta dentro del rango indicado."
fi