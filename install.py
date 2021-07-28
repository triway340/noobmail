import os
import time
print("\n\n")
print("Instalando paquetes necesarios...")
time.sleep(2)
os.system("pip install -r requirements.txt")
os.system("chmod +x noobmail.py")
time.sleep(2)
print("\n\n¡Instalacion completada!")
time.sleep(1)
print("Escriba en su terminal: 'python noobmail.py' para continuar.")
exit()