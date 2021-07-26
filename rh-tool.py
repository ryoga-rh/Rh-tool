import colorama 
import os 
import sys
import time 
import pytube 
import socket 
import webbrowser 
import signal 
from colorama import * 


def ctrlc(signal, freame):
    limpiar()
    logo()
    print(Fore.RED+"Precionaste ctrl c, el proceso termino, saliendo...")
    time.sleep(2)
    salida()

signal.signal(signal.SIGINT, ctrlc)


def limpiar():
    os.system("cls || clear") 
    
def logo():
    print(f'''
{Fore.GREEN}██                  {Fore.CYAN} 
{Fore.GREEN}████████╗{Fore.CYAN}░███╗░░███╗ {Fore.YELLOW} █████████╗{Fore.LIGHTMAGENTA_EX}░█████╗{Fore.WHITE}░░█████╗{Fore.RED}░███╗░░░░░
{Fore.GREEN} ██╔══██╗  {Fore.CYAN}██║░░██║   {Fore.YELLOW} ╚══██╔══╝{Fore.LIGHTMAGENTA_EX}██╔══██╗{Fore.WHITE}██╔══██╗{Fore.RED}░██║░░░░░ 
{Fore.GREEN} ██████╔╝  {Fore.CYAN}███████║   {Fore.YELLOW} ░░░██║{Fore.LIGHTMAGENTA_EX}░░░██║░░██║{Fore.WHITE}██║░░██║{Fore.RED}░██║░░░░░
{Fore.GREEN} ██╔══██╗  {Fore.CYAN}██╔══██║   {Fore.YELLOW} ░░░██║{Fore.LIGHTMAGENTA_EX}░░░██║░░██║{Fore.WHITE}██║░░██║{Fore.RED}░██║░░░░░
{Fore.GREEN}██║░░░██║ {Fore.CYAN} ██║░░██║   {Fore.YELLOW} ░░░██║{Fore.LIGHTMAGENTA_EX}░░░╚█████╔╝{Fore.WHITE}╚█████╔╝{Fore.RED}░███████╗ 
{Fore.GREEN}╚═╝░░░╚═╝  {Fore.CYAN}╚═╝░░╚═╝   {Fore.YELLOW} ░░░╚═╝{Fore.LIGHTMAGENTA_EX}░░░░╚════╝{Fore.WHITE}░░╚════╝{Fore.RED}░░╚══════╝
        ''') 

def menu():
    os.system("mode con: cols=120 lines=50")
    limpiar()
    logo()
    print(f'''{Fore.BLUE}
Bienvenido a esta pequeña herramienta, estas son las opciones que tengo{Fore.GREEN}
╔════════╦══════════╦════════════════════════════════════════════╗
║ Numero ║ Opciones ║ Descripción                                ║
╠════════╬══════════╬════════════════════════════════════════════╣
║ 1      ║ Sistema  ║ Muestra algunas configuraciones de sistema ║
║ 2      ║ IP       ║ Muestra la información de una IP           ║
║ 3      ║ Youtube  ║ Descargar videos de Youtube                ║
║ 4      ║ Salir    ║ Salir de esta pequeña herramienta          ║
╚════════╩══════════╩════════════════════════════════════════════╝
         {Fore.RESET} ''')
    selccion = input(f'{Fore.CYAN} Selecciona una opcion: {Fore.RESET}')
    if selccion == "1":
        print(f'{Fore.BLUE}En un momento se cargara la opcion{Fore.RESET}')
        time.sleep(2)
        sistema()
    elif selccion == "2":
        print(f'{Fore.BLUE}En un momento se cargara la opcion{Fore.RESET}')
        time.sleep(2)
        ip()
    elif selccion == "3":
        print(f'{Fore.BLUE}En un momento se cargara la opcion{Fore.RESET}')
        time.sleep(2)
        yt()
    elif selccion == "4":
        print(f'{Fore.BLACK} Saliendo...{Fore.RESET}')
        time.sleep(2)
        salida()  

def salida():
    limpiar()
    logo()
    print(f'{Fore.YELLOW} Gracias por usar la herramienta, saliendo...{Fore.RESET}')
    time.sleep(3)
    limpiar()
    sys.exit()

def sistema():
    limpiar()
    logo()
    print(f'''
{Fore.GREEN}Estas son las opciones para ver configuraciones de sistema de tu pc{Fore.RESET}
{Fore.CYAN}
┌──────────────────────────────────┬───────────────────────┬───────────────────────┬───────────┐
│          1.-Ip config            │  2.-Hora del sistema  │      3.-Netstat       │    3      │
├──────────────────────────────────┼───────────────────────┼───────────────────────┼───────────│ 
│  Muestra la configuracion de     │  Muestra la hora      │Muestra las conexiones │  Todas    │
│          de tu ip                │    del sistema        │    activas en tu      │   las     │
│                                  │  puedes modificarla   │      dispositivo      │ anteriores│
└──────────────────────────────────┴───────────────────────┴───────────────────────┴───────────┘
         {Fore.RESET} ''')
    seleccion = input("Selecciona una opcion: ")
    if seleccion == "1":
        limpiar()
        logo()
        nombre = socket.gethostname()
        print(f'Esta es la configuracion de ip de la maquina {nombre}')
        time.sleep(2)
        os.system("ipconfig /all")
        time.sleep(3)
        y = input(Fore.YELLOW+"El proceso termino, que es lo que quieres hacer?\n1.-Volver al menu \n2.-Salir: "+Fore.RESET)
        if y == "1":
            print(f'{Fore.GREEN} Volviendo al menu... {Fore.RESET}')
            time.sleep(3)
            menu()
        elif y == "2":
            print(f'{Fore.GREEN} Saliendo... {Fore.RESET}')
            time.sleep(3)
            salida()
        else: 
            print(Fore.RED+"Opcion no valida, volviendo al menu..."+Fore.RESET)
            time.sleep(3)
            menu()
    elif seleccion == "2":
        limpiar()
        logo()
        time.sleep(2)
        os.system("echo La hora actual del sistema es %time% \n Quieres modificarla?")
        x = input(f'{Fore.BLUE}Si/No: {Fore.RESET}')
        if x == "Si":
            os.system("time")
            time.sleep(2)
            e = input(f'{Fore.YELLOW} El proceso termino, que deseas hacer?\n 1.-Volver al menu\n 2.-Salir: {Fore.RESET}')
            if e == "1":
                print(f'{Fore.GREEN} Volviendo al menu... {Fore.RESET}')
                time.sleep(3)
                menu()
            elif e == "2":
                print(f'{Fore.GREEN} Saliendo... {Fore.RESET}')
                time.sleep(3)
                salida()
            else: 
                print(Fore.RED+"Opcion no valida, volviendo al menu..."+Fore.RESET)
                time.sleep(3)
                menu()
        elif x == "No":
            print(f'{Fore.GREEN} Volviendo al menu...{Fore.RESET}')
            time.sleep(3)
            menu()
        else:
            print(f'{Fore.CYAN}Opcion no valida, volviendo al menu...{Fore.RESET}')
            time.sleep(2)
            menu()
    elif seleccion == "3":
        limpiar()
        logo()
        print(f''' {Fore.LIGHTGREEN_EX} Como quieres ver tu conexion?{Fore.RESET}
              {Fore.BLUE}
┌───────────────────────────────────────────────────────────────────────────────┐
│ 1.-Estadisticas de interfaz  │ 2.-Estado de descarga │ 3.-Conexiones activas  │
└───────────────────────────────────────────────────────────────────────────────┘
              {Fore.RESET}''')
        eleccion = input(f'Selecciona una opcion: ')
        if eleccion == "1":
            limpiar()
            logo()
            print(f'{Fore.YELLOW}Estas es la estadisticas de interfaz{Fore.RESET}')
            os.system("netstat -e -s")
            time.sleep(3)
            y = input(Fore.YELLOW+"El proceso termino, que es lo que quieres hacer?\n1.-Volver al menu \n2.-Salir: "+Fore.RESET)
            if y == "1":
                print(f'{Fore.GREEN} Volviendo al menu... {Fore.RESET}')
                time.sleep(3)
                menu()
            elif y == "2":
                print(f'{Fore.GREEN} Saliendo... {Fore.RESET}')
                time.sleep(3)
                salida()
            else: 
                print(Fore.RED+"Opcion no valida, volviendo al menu..."+Fore.RESET)
                time.sleep(3)
                menu()
        elif eleccion == "2":
            print(f'{Fore.YELLOW}Estado de descarga{Fore.RESET}')
            os.system("netstat -t")
            y = input(Fore.YELLOW+"El proceso termino, que es lo que quieres hacer?\n1.-Volver al menu \n2.-Salir: "+Fore.RESET)
            if y == "1":
                print(f'{Fore.GREEN} Volviendo al menu... {Fore.RESET}')
                time.sleep(3)
                menu()
            elif y == "2":
                print(f'{Fore.GREEN} Saliendo... {Fore.RESET}')
                time.sleep(3)
                salida()
            else: 
                print(Fore.RED+"Opcion no valida, volviendo al menu..."+Fore.RESET)
                time.sleep(3)
                menu()
        elif eleccion == "3":
            print(f'{Fore.YELLOW}Tus conexiones activas{Fore.RESET}')
            os.system("netstat -a")
            y = input(Fore.YELLOW+"El proceso termino, que es lo que quieres hacer?\n1.-Volver al menu \n2.-Salir: "+Fore.RESET)
            if y == "1":
                print(f'{Fore.GREEN} Volviendo al menu... {Fore.RESET}')
                time.sleep(3)
                menu()
            elif y == "2":
                print(f'{Fore.GREEN} Saliendo... {Fore.RESET}')
                time.sleep(3)
                salida()
            else: 
                print(Fore.RED+"Opcion no valida, volviendo al menu..."+Fore.RESET)
                time.sleep(3)
                menu()
        else: 
            print(f'{Fore.RED} Opcion no valida, volviendo al menu...{Fore.RESET}')
            time.sleep(2)
            menu()
        
def yt():
    limpiar()
    logo()
    url = input(f'{Fore.GREEN}Da un link {Fore.RESET}')
    adescargar = pytube.YouTube(url)
    print(f'{Fore.GREEN}Nombre del video:{Fore.YELLOW}  {adescargar.title}')
    print(f'{Fore.GREEN}Duracion: {Fore.YELLOW} {adescargar.length}')
    x = input(Fore.RED+"Estas seguro que quieres descargar el video? si/no \n"+Fore.RESET)
    if x == "si":
        video = yt.streams.first()
        video.download()
    elif x == "no":
        print("Volviendo al menu")
        time.sleep(3)
        menu()
    else:
        print(Fore.RED+"Opcion no valida, volviendo al menu"+Fore.RESET)
        time.sleep(3)
        menu()
    time.sleep(4)
    termino = input(Fore.YELLOW+"El proceso termino que deseas hacer?"+ Fore.GREEN+"\n 1.- Volver al menu \n 2.- Salir: "+Fore.RESET)
    if termino == "1":
        print(Fore.GREEN+"Volviendo al menu..."+Fore.RESET)
        time.sleep(2)
        menu()
    elif termino == "2":
        print(Fore.RED+"Saliendo..."+Fore.RESET)
        time.sleep(2)
        salida()
    else:
        print(Fore.RED+"Eleccion no valida, volviendo al menu..."+Fore.RESET)
        time.sleep(2)    
        menu()
    


def ip():
    limpiar()
    logo()
    ip1 = input(Fore.YELLOW+"Introduce una ip: "+Fore.RESET)
    time.sleep(2)
    print(f'''
{Fore.GREEN} Estas son las opciones que tengo para ver la informacion de una ip
          {Fore.CYAN}
┌──────────────────────────────────┬───────────────────────┬───────────┐
│          1.-CheckHost            │   2.-Infobyip         │    3      │
├──────────────────────────────────┼───────────────────────┼───────────│
│  Muestra localización            │  Muestra localización │  Todas    │
│  proveedor, rango, código postal │       proveedor       │   las     │
│  organización y horario          │      código postal    │ anteriores│
└──────────────────────────────────┴───────────────────────┴───────────┘
          {Fore.RESET}''')
    x = input(Fore.RED+"Selecciona una opcion: "+Fore.RESET)
    if x == "1":
        print(Fore.GREEN+"En un momento se abrira en tu naegador la pagina"+Fore.RESET)
        webbrowser.open(f'https://check-host.net/ip-info?host={ip1}')
        time.sleep(3)
        y = input(Fore.YELLOW+"El proceso termino, que es lo que quieres hacer?\n1.-Volver al menu \n2.-Salir: "+Fore.RESET)
        if y == "1":
            print(f'{Fore.GREEN} Volviendo al menu... {Fore.RESET}')
            time.sleep(3)
            menu()
        elif y == "2":
            print(f'{Fore.GREEN} Saliendo... {Fore.RESET}')
            time.sleep(3)
            salida()
        else: 
            print(Fore.RED+"Opcion no valida, volviendo al menu..."+Fore.RESET)
            time.sleep(3)
            menu()
    elif x == "2":
        print(Fore.GREEN+"En un momento se abrira en tu navegador la pagina"+Fore.RESET)
        webbrowser.open(f'https://es.infobyip.com/ip-{ip1}.html')
        time.sleep(3)
        y = input(Fore.YELLOW+"El proceso termino, que es lo que quieres hacer?\n1.-Volver al menu \n2.-Salir"+Fore.RESET)
        if y == "1":
            print(f'{Fore.GREEN} Volviendo al menu... {Fore.RESET}')
            time.sleep(3)
            menu()
        elif y == "2":
            print(f'{Fore.GREEN} Saliendo... {Fore.RESET}')
            time.sleep(3)
            salida()
        else: 
            print(Fore.RED+"Opcion no valida, volviendo al menu..."+Fore.RESET)
            time.sleep(3)
            menu()
    elif x == "3":
        print(Fore.GREEN+"En un momento se abriran en tu navegador las paginas"+Fore.RESET)
        webbrowser.open(f'https://check-host.net/ip-info?host={ip1}')   
        webbrowser.open(f'https://es.infobyip.com/ip-{ip1}.html')
        time.sleep(3)
        y = input(Fore.YELLOW+"El proceso termino, que es lo que quieres hacer?\n1.-Volver al menu \n2.-Salir"+Fore.RESET)
        if y == "1":
            print(f'{Fore.GREEN} Volviendo al menu... {Fore.RESET}')
            time.sleep(3)
            menu()
        elif y == "2":
            print(f'{Fore.GREEN} Saliendo... {Fore.RESET}')
            time.sleep(3)
            salida()
        else: 
            print(Fore.RED+"Opcion no valida, volviendo al menu..."+Fore.RESET)
            time.sleep(3)
            menu() 
            
menu()