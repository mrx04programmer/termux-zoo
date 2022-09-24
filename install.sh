echo "[+] Instalando dependencia w3m..."
apt update && apt install w3m -y
echo "[+] Instalando dependencia nmap..."
apt install nmap -y
echo "[+] Instalando dependencia wget..."
python3 -m pip install wget
echo "[o] Creando ejecutable de termux-zoo..."
cp ./termux-zoo.py $PREFIX/bin/termux-zoo
mv ./s $PREFIX/bin/s
chmod 777 $PREFIX/bin/termux-zoo
chmod 777 $PREFIX/bin/s
echo "[x] Instalación terminada exitosamente."
echo "[x] Ejecuta el comando : termux-zoo <modulo> <host/ip>"