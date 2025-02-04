import os
import json
from utils.colors import Colors

# Ruta de la carpeta de tags NFC
NFC_TAGS_DIR = os.path.join(os.path.dirname(__file__), "tags")

# Crear la carpeta de tags si no existe
if not os.path.exists(NFC_TAGS_DIR):
    os.makedirs(NFC_TAGS_DIR)

def guardar_tag(tag_data, nombre_archivo):
    """
    Guarda los datos de un tag NFC en un archivo JSON.
    """
    ruta_archivo = os.path.join(NFC_TAGS_DIR, f"{nombre_archivo}.json")
    with open(ruta_archivo, "w") as archivo:
        json.dump(tag_data, archivo, indent=4)
    print(f"{Colors.OKGREEN}[+] Tag guardado en {ruta_archivo}{Colors.ENDC}")

def cargar_tag(nombre_archivo):
    """
    Carga los datos de un tag NFC desde un archivo JSON.
    """
    ruta_archivo = os.path.join(NFC_TAGS_DIR, f"{nombre_archivo}.json")
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r") as archivo:
            return json.load(archivo)
    else:
        print(f"{Colors.FAIL}[-] El archivo {ruta_archivo} no existe.{Colors.ENDC}")
        return None

def listar_tags():
    """
    Lista todos los tags NFC guardados.
    """
    tags = [f.replace(".json", "") for f in os.listdir(NFC_TAGS_DIR) if f.endswith(".json")]
    if tags:
        print(f"{Colors.OKGREEN}[+] Tags NFC guardados:{Colors.ENDC}")
        for i, tag in enumerate(tags, 1):
            print(f"{Colors.OKBLUE}{i}. {tag}{Colors.ENDC}")
    else:
        print(f"{Colors.WARNING}[-] No hay tags NFC guardados.{Colors.ENDC}")
    return tags