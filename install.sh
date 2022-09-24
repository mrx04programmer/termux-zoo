greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
grayColour="\e[0;37m\033[1m"

echo "${greenColour}[+] Instalando dependencia w3m...${endColour}"
apt update && apt install w3m -y
echo "${greenColour}[+] Instalando dependencia nmap...${endColour}"
apt install nmap -y
echo "${greenColour}[+] Instalando dependencia wget...${endColour}"
python3 -m pip install wget
echo "${yellowColour}[o] Creando ejecutable de termux-zoo...${endColour}"
cp ./termux-zoo.py $PREFIX/bin/termux-zoo
chmod 777 $PREFIX/bin/termux-zoo
chmod 777 ./.s
echo "${greenColour}[x] Instalación terminada"
echo "${greenColour}[x] Ejecuta el comando : ${grayColour}termux-zoo <modulo> <host/ip>${endColour}"