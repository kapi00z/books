#!/bin/sh

#https://www.gutenberg.org/files/65194/65194-0.txt

URLTEMP='https://www.gutenberg.org/files/'

download () {
    for id in $(shuf -i 1000-1999 -n 5)
    do
        echo $id
        link="${URLTEMP}${id}/${id}-0.txt"
        curl $link > book${id}.txt
    done
}

if [ -z $1 ]
then
    N=5
else
    N=$1
fi

#echo -n '' > url.txt

for id in $(shuf -i 1000-1999 -n ${N})
do
    link="${URLTEMP}${id}/${id}-0.txt"
    echo $link
done