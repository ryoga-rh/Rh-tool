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
    limpiar()
    logo()
    print(f'''{Fore.BLUE}
Bienvenido a esta pequeña herramienta, estas son las opciones que tengo{Fore.GREEN}
╔════════╦══════════╦════════════════════════════════════════════╗
║ Numero ║ Opciones ║ Descripción                                ║
╠════════╬══════════╬════════════════════════════════════════════╣
║ 1      ║ Sistema  ║ Muestra algunas configuraciones de sistema ║
║ 2      ║ IP       ║ Muestra la información de una IP           ║
║ 3      ║ Youtube  ║ Descargar videos de Yutube                 ║
║ 4      ║ Salir    ║ Salir de esta pequeña herramienta          ║
╚════════╩══════════╩════════════════════════════════════════════╝
         {Fore.RESET} ''')
    selccion = input(f'{Fore.CYAN} Selecciona una opcion: {Fore.RESET}')
    if selccion == "1":
        print(f'{Fore.BLUE}Estoy trabajando en esa opcion xD')
        time.sleep(2)
        menu()
    elif selccion == "2":
        print(f'{Fore.BLUE}En un momento se cargara la opcion{Fore.RESET}')
        time.sleep(2)
        ip()
    elif selccion == "3":
        print(f'{Fore.BLUE}Estoy trabajando en esa opcion xD')
        time.sleep(2)
        menu()
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

def ip():
    limpiar()
    logo()
    ip1 = input(Fore.YELLOW+"Introduce una ip: "+Fore.RESET)
    time.sleep(2)
    print(f'''{Fore.CYAN}
┌──────────────────────────────────┬───────────────────────────────────┐
│          1.-CheckHost            │   2.-Infobyip         │    3      │
├──────────────────────────────────┼───────────────────────┼───────────│
│  Muestra localización            │  Muestra localización │  Todas    │
│  proveedor, rango, código postal │       proveedor       │   las     │
│  organización y horario          │      código postal    │ anteriores│
└──────────────────────────────────┴───────────────────────────────────┘
          {Fore.RESET}''')
    x = input(Fore.RED+"Selecciona una opcion: "+Fore.RESET)
    if x == "1":
        print(Fore.GREEN+"En un momento se abrira en tu naegador la pagina"+Fore.RESET)
        webbrowser.open(f'https://check-host.net/ip-info?host={ip1}')
        time.sleep(3)
        y = init()(Fore.YELLOW+"El proceso termino, que es lo que quieres hacer?\n1.-Volver al menu \n2.-Salir"+Fore.RESET)
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
        y = init()(Fore.YELLOW+"El proceso termino, que es lo que quieres hacer?\n1.-Volver al menu \n2.-Salir"+Fore.RESET)
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
        print(Fore.GREEN+"En un momento se abriran en tu navegador las pagins"+Fore.RESET)
        webbrowser.open(f'https://check-host.net/ip-info?host={ip1}')   
        webbrowser.open(f'https://es.infobyip.com/ip-{ip1}.html')
        time.sleep(3)
        y = init()(Fore.YELLOW+"El proceso termino, que es lo que quieres hacer?\n1.-Volver al menu \n2.-Salir"+Fore.RESET)
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