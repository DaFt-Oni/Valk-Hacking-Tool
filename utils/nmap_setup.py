import os
import platform
import subprocess
import sys
import requests
import tarfile

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIN_DIR = os.path.join(BASE_DIR, "bin")

# URLs de descarga de Nmap
NMAP_LINUX_URL = "https://nmap.org/dist/nmap-7.94.tar.bz2"

def is_windows():
    return platform.system() == "Windows"

def is_linux():
    return platform.system() == "Linux"

def get_system():
    if is_windows():
        return "windows"
    elif is_linux():
        return "linux"
    else:
        raise Exception("Sistema operativo no soportado.")

def download_file(url, destination):
    """Descarga un archivo desde una URL y lo guarda en la ruta especificada."""
    print(f"Descargando {url}...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(destination, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Descarga completada: {destination}")
    else:
        raise Exception(f"No se pudo descargar el archivo desde {url}")

def extract_tar(tar_path, extract_to):
    """Extrae un archivo TAR en la ruta especificada."""
    print(f"Extrayendo {tar_path}...")
    with tarfile.open(tar_path, "r:bz2") as tar_ref:
        tar_ref.extractall(extract_to)
    print(f"Extracción completada: {extract_to}")

def install_nmap_system():
    """Intenta instalar Nmap en el sistema usando el gestor de paquetes."""
    try:
        if is_linux():
            print("Instalando Nmap en el sistema (requiere permisos de administrador)...")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "nmap"], check=True)
            print("Nmap instalado en el sistema.")
            return True
        elif is_windows():
            print("Instalando Nmap en el sistema usando Chocolatey...")
            subprocess.run(["choco", "install", "nmap", "-y"], check=True)
            print("Nmap instalado en el sistema.")
            return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("No se pudo instalar Nmap en el sistema.")
        return False

def install_nmap_local():
    """Descarga, compila e instala Nmap localmente en el entorno del proyecto."""
    system = get_system()
    nmap_dir = os.path.join(BIN_DIR, system)

    # Crear la carpeta bin si no existe
    os.makedirs(nmap_dir, exist_ok=True)

    if is_linux():
        # Descargar Nmap para Linux
        tar_path = os.path.join(nmap_dir, "nmap.tar.bz2")
        download_file(NMAP_LINUX_URL, tar_path)
        extract_tar(tar_path, nmap_dir)
        os.remove(tar_path)  # Eliminar el archivo TAR después de extraer

        # Compilar Nmap
        nmap_source_dir = os.path.join(nmap_dir, "nmap-7.94")
        print(f"Compilando Nmap en {nmap_source_dir}...")
        subprocess.run(["./configure"], cwd=nmap_source_dir, check=True)
        subprocess.run(["make"], cwd=nmap_source_dir, check=True)
        subprocess.run(["make", "install"], cwd=nmap_source_dir, check=True)
        print("Nmap compilado e instalado localmente.")

        # Ruta del binario de Nmap
        nmap_path = os.path.join(nmap_source_dir, "nmap")
    else:
        raise Exception("No se puede instalar Nmap localmente en Windows.")

    print(f"Nmap instalado localmente en: {nmap_path}")
    return nmap_path

def add_to_path(nmap_path):
    """Agrega la ruta de Nmap al PATH temporalmente."""
    nmap_dir = os.path.dirname(nmap_path)
    os.environ["PATH"] += os.pathsep + nmap_dir
    print(f"Ruta de Nmap agregada al PATH: {nmap_dir}")

def check_nmap_installed():
    """Verifica si Nmap está instalado en el sistema."""
    try:
        subprocess.run(["nmap", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print("Nmap ya está instalado en el sistema.")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Nmap no está instalado en el sistema.")
        return False

def setup_nmap():
    """Configura Nmap para su uso en el script."""
    if not check_nmap_installed():
        print("Intentando instalar Nmap en el sistema...")
        if not install_nmap_system():
            print("No se pudo instalar Nmap en el sistema. Intentando instalarlo localmente...")
            nmap_path = install_nmap_local()
            add_to_path(nmap_path)