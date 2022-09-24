<div align="center">
<img src="https://user-images.githubusercontent.com/46001898/192107602-73c673e5-0e11-4e82-963f-a44dbbdd3111.png" width="200">

</div>
<h6>Pack de herramientas de pentesting para termux </h6>

## Instalación
Para su instalación , se debe seguir los siguientes pasos:
1. Descargar y entrar a la carpeta de la herramienta
> git clone https://github.com/mrx04programmer/termux-zoo.git

> cd termux-zoo
2. Darle permiso de ejecución al instalador
> chmod +x install.sh
3. Ejecutar el instalador
> ./install.sh

## Ejecución
> termux-zoo <modulo> <host>
* Modulo -> El modulo a utilizar:
    * list -> Modulo para listar los modulos
    * nmap -> Escanea las vulnerabilidades y/o puertos abiertos
    * exploit -> Intenta vulnerar el sistema por medio de exploits ya creados
    * create-vuln -> Crea una vulnerabilidad por medio de un puerto
    * server -> Ejecuta el servidor simplificado de python3 y obtener shell (beta)
* Host -> Dispositivo a realizar testing , solo es usada cuando se necesita

<img src="https://img.shields.io/badge/version-1.0.2-t?style=for-the-badge&logo=python&color=darkgreen&logoColor=green&labelColor=black">
<img src="https://img.shields.io/badge/status-finishing-t?style=for-the-badge&color=white&logoColor=darkgreen&labelColor=black">
