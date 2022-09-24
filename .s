#!/bin/bash
#count=1
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
grayColour="\e[0;37m\033[1m"


if [ -n "$1" ];
then
   nmap -v -p0-9999 $1 -d2 | grep 'open' | while read line; do
      echo -e "${blueColour}[*] ${grayColour}$line"
   done
else
   echo "[*] ERROR"
fi