import colorama
import os
import sys
import time
import pytube
import socket
from colorama import *

def limpiar():
    os.system("cls || clear")
    
def logo():
    limpiar()
    print(Fore.RED)
    print(f'''
                                                                                   
{Fore.GREEN} 88888888ba  {Fore.CYAN} 88        88      {Fore.YELLOW}888888888888                           {Fore.RED} 88  
{Fore.GREEN} 88      "8b {Fore.CYAN} 88        88      {Fore.YELLOW}     88                                {Fore.RED} 88  
{Fore.GREEN} 88      ,8P {Fore.CYAN} 88        88      {Fore.YELLOW}     88                                {Fore.RED} 88  
{Fore.GREEN} 88aaaaaa8P' {Fore.CYAN} 88aaaaaaaa88      {Fore.YELLOW}     88   {Fore.LIGHTMAGENTA_EX}     ,adPPYba,  {Fore.WHITE}  ,adPPYba,  {Fore.RED} 88  
{Fore.GREEN} 88""""88'   {Fore.CYAN} 88""""""""88      {Fore.YELLOW}     88   {Fore.LIGHTMAGENTA_EX}    a8"     "8a {Fore.WHITE} a8"     "8a {Fore.RED} 88  
{Fore.GREEN} 88    `8b   {Fore.CYAN} 88        88      {Fore.YELLOW}     88   {Fore.LIGHTMAGENTA_EX}    8b       d8 {Fore.WHITE} 8b       d8 {Fore.RED} 88  
{Fore.GREEN} 88     `8b  {Fore.CYAN} 88        88      {Fore.YELLOW}     88   {Fore.LIGHTMAGENTA_EX}    "8a,   ,a8" {Fore.WHITE} "8a,   ,a8" {Fore.RED} 88  
{Fore.GREEN} 88      `8b {Fore.CYAN} 88        88      {Fore.YELLOW}     88   {Fore.LIGHTMAGENTA_EX}     `"YbbdP"'  {Fore.WHITE}  `"YbbdP"'  {Fore.RED} 88  
          ''')
    print(Fore.RESET)
    
logo(
    
)