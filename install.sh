greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
grayColour="\e[0;37m\033[1m"

echo -e "${greenColour}[+] Instalando dependencia w3m...${endColour}"
apt update && apt install w3m -y
echo -e "${greenColour}[+] Instalando dependencia nmap...${endColour}"
apt install nmap -y
echo -e "${greenColour}[+] Instalando dependencia wget...${endColour}"
python3 -m pip install wget
echo -e "${yellowColour}[o] Creando ejecutable de termux-zoo...${endColour}"
cp ./termux-zoo.py $PREFIX/bin/termux-zoo
chmod 777 $PREFIX/bin/termux-zoo
chmod 777 ./.s
echo -e "${greenColour}[x] Instalación terminada exitosamente."
echo -e "${greenColour}[x] Ejecuta el comando : ${grayColour}termux-zoo <modulo> <host/ip>${endColour}"