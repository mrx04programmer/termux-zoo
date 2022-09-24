#! /bin/python
import os, sys , wget, random
W = '\033[37m'
R = '\033[1;31m'  # red
G = '\033[1;32m'  # green
O = '\033[0;33m'  # orange
B = '\033[1;34m'  # blue
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan
sh = os.system
def clear():
    sh("clear")

def banner():
    print(f"""{O}
                                ___   __   __
                               [_  | /  \ /  \ 
                                / /_| () | () |
                              _|____]\__/ \__/_
                          _.-"|   |   |   |   |"-._
                      _.-"|   |   |   |   |   |   |"-._
                  _.-"|   |   |   |   |   |   |   |   |"-._
             _.-"`|   |   |   |   |   |   |   |   |   |   |`"-._
         _.-"_|__~|.__|.__|.-~|~-.|__.|_..|.__|_._|___|.__|~__|_"-._ By Mrx04programmer
{G}""")

def main():
    module = sys.argv[1]
    #host = sys.argv[2]
    if "list" in module:
        print(f"""
    {P}nmap : {W}Escanea las vulnerabilidades y/o puertos abiertos
    {R}exploit : {W}Intenta vulnerar el sistema por medio de exploits ya creados
    {G}create-vuln : {W}Crea una vulnerabilidad por medio de un puerto
    {C}server : {W}Ejecuta el servidor simplificado de python3
    """)
    elif "nmap" in module:
        host = sys.argv[2]
        clear()
        banner()
        print(f"{O}[o] {W}Escaneando con nmap a {host}...")
        sh(f"./.s {host}")
        print(f"{G}[x] {W}{host} ha sido escaneado exitosamente.")
    elif "exploit" in module:
        host = sys.argv[2]
        port = int(input(f"{G}Puerto a atacar >> {W}"))
        clear()
        banner()
        cve = str(input(f"{O}CVE Basado {C}(ej: wordpress, 2022, windows, etc){O}>> {W}"))
        clear()
        banner()
        print(f"{B}[*] {W}Buscando {O}CVE {cve} {W} en {R}exploitdb{W}...")
        print(W+"-"*80+G)
        sh(f"w3m https://nvd.nist.gov/vuln/search/results\?form_type\=Advanced\&results_type\=overview\&query\={cve}\&search_type\=all\&isCpeNameSearch\=false | grep 'CVE'")
        print(W+"-"*80)
        used = str(input(f"{W}CVE a utilizar para {host}> {O}"))
        method = str(input(f"{W}Metodo (http/https) >> {G}"))
        if method == "http":
            url = f"http://{host}:{port}"
        else:
            url = f"https://{host}:{port}"
        clear()
        banner()
        print(f"{R}[+] {W}Explotando {host}:{port} con {used}")
        sh("ip tunnel show prl-default")
        sh("ip tunnel show {host}")
        try:
            wget.download(url, out="output")
            while True:
                print(f"\n{G}[x] {W} Conectado exitosamente a {host}")
                cmd = input(f"{R}{host}:{port}>> {W}")
                print(wget.download(url+"?"+cmd))
                print(f"{G}[x] {W}Comando enviado exitosamente ")
        except Exception:
            print(f"{R}ERR {W}la conexión no se pudo lograr a {host}")
    elif "create-vuln" in module:
        s = ['dhfmcl0', '019xMalfW4', 'wcC1k98', '00wrlcdoa', 'Pwdor569', 'adLdfj.10', 'Pwqjch125']
        passkeys = random.choice(s)+random.choice(s)
        passkey = random.choice(passkeys)
        host = sys.argv[2]
        port = int(input(f"{G}Puerto a atacar >> {W}"))
        clear()
        banner()
        based = str(input(f"{O}CVE basado >> {W}"))
        cve = str(input(f"{C}Nombre de CVE a crear (ej: wordpress-killer)>> {W}"))
        clear()
        banner()
        print(f"{O}[o] {W}Creando vulnerabilidad...")
        sh(f"ping -c30 {host} >> /dev/null")
        print(f"{G}[x] {W}Vulnerabilidad {O}{cve} ha sido creada exitosamente en el puerto {port}")
        print(f"{B}[*] {W}Clave de seguridad: {G}{passkey}")
    elif "server" in module:
        port = int(input(f"{G}Puerto a escuchar >> {W}"))
        clear()
        banner()
        print()
        sh(f"python3 -m http.server {port} > traffic.lst")

if __name__ == '__main__':
    try:
        main()
    except IndexError:
        clear()
        banner()
        print(f"\n{R}Utiliza el comando: {G}termux-zoo <modulo> <host/ip>\n")