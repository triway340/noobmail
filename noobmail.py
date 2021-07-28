#Code by Triway
try:
	from guerrillamail import *
	import os
	from colorama import init, Fore
	import platform
	import time
except ModuleNotFoundError:
	print("No has instalado los requerimientos, por favor ingrese en su terminal: 'pip install -r requirements.txt'")
init(autoreset=True)
YELLOW = Fore.YELLOW
RED = Fore.RED
CYAN = Fore.CYAN
BLUE = Fore.BLUE
RESET = Fore.WHITE
GREEN = Fore.GREEN
PURPLE = Fore.MAGENTA
banner = RED+'''
────────▄▄▄▄▄▄▄▄▄
────────▌▐░▀░▀░▀▐
────────▌░▌░░░░░▐
────────▌░░░░░░░▐
────────▄▄▄▄▄▄▄▄▄
──▄▀▀▀▀▀▌▄█▄░▄█▄▐▀▀▀▀▀▄
─█▒▒▒▒▒▐░░░░▄░░░░▌▒▒▒▒▒█
▐▒▒▒▒▒▒▒▌░░░░░░░▐▒▒▒▒▒▒▒▌
▐▒▒▒▒▒▒▒█░▀▀▀▀▀░█▒▒▒▒▒▒▒▌
▐▒▒▒▒▒▒▒▒█▄▄▄▄▄█▒▒▒▒▒▒▒▒▌
▐▒▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▌
▐▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▌
▐▒▒▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒▌
▐▒▒▒▒▒▒▌▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▌
▐▒▒▒▒▒▒▌▄▄▄▄▄▄▄▄▄▐▒▒▒▒▒▒▌
▐▄▄▄▄▄▄▌▌███████▌▐▄▄▄▄▄▄▌
─█▀▀▀▀█─▌███▌███▌─█▀▀▀▀█
─▐░░░░▌─▌███▌███▌─▐░░░░▌
──▀▀▀▀──▌███▌███▌──▀▀▀▀
────────▌███▌███▌
────────▌███▌███▌
──────▐▀▀▀██▌█▀▀▀▌
▒▒▒▒▒▒▐▄▄▄▄▄▄▄▄▄▄▌▒▒▒▒▒▒▒

'''
def clear():
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")
def emailtemp():
	session = GuerrillaMailSession()
	print(f"\n{YELLOW}=====================")
	print(session.get_session_state()["email_address"])
def home():
	while True:
		try:
			clear()
			print(f"\n\n{YELLOW}===========================")
			print(f"{banner}")
			print(f"{BLUE}<> Tool Created by Triway <>")
			print(f"{YELLOW}===========================\n\n")
			print(f"{GREEN}¿Como usar?:")
			time.sleep(1)
			print(f"{GREEN}\nIngresa en tu terminal: {PURPLE}'mail'{GREEN} cada vez que quieras obtener un Email\nTambien puede ingresar {PURPLE}'exit' {GREEN}para salir del script.{RESET}")
			try:
				email_peticion = input("\n---> ")
			except KeyboardInterrupt:
				print(RED+"\n(EXIT) Detectado, saliendo...")
				time.sleep(1)
				print(RESET+"")
				exit()
			print()	
			if email_peticion=="mail" or email_peticion=="Mail" or email_peticion=="EMAIL":
				print(GREEN+"Generando correo.")
				print(GREEN+"Por favor sea paciente...")
				emailtemp()
				print(f"{YELLOW}=====================")
				print(GREEN+"\n¡Email hecho!")
				time.sleep(1)
				print(f"\n\n{RED}AVISO: {BLUE}SERA BORRADO TODO LO ANTERIOR (INCLUSO EL CORREO){RESET}")
				try:
					extra1 = input("Presione enter para continuar...")
				except KeyboardInterrupt:
				print(RED+"\n(EXIT) Detectado, saliendo...")
				time.sleep(1)
				print(RESET+"")
				exit()
			elif email_peticion=="Exit" or email_peticion=="exit" or email_peticion=="EXIT":
				clear()
				print(YELLOW+"\n\n===========================")
				print(banner)
				print(BLUE+"<> Tool Created by Triway <>")
				print(YELLOW+"===========================\n\n")
				print(GREEN+"Okey, saliendo...")
				time.sleep(2)
				print(RESET+"\n¡ADIOS VUELVE PRONTO!\n")
				exit()
			else:
				print(RED+"No he reconocido lo que ha que querido decir, por favor, vuelta a intentarlo.")
				time.sleep(2)
				try:
					extra2 = input("\n\nPresione enter para continuar...")
				except KeyboardInterrupt:
				print(RED+"\n(EXIT) Detectado, saliendo...")
				time.sleep(1)
				print(RESET+"")
				exit()
		except (KeyboardInterrupt, TypeError):
			print(f"{RED}Ha ocurrido un error, vuelva a intentarlo...{RESET}")
			time.sleep(3)
			try:
				extra3 = input("\n\nPresione enter para continuar...")
			except KeyboardInterrupt:
				print(RED+"\n(EXIT) Detectado, saliendo...")
				time.sleep(1)
				print(RESET+"")
				exit()
home()
#Code by Triway