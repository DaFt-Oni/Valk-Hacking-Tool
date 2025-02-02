import platform

# Ruta del archivo de configuración
CONFIG_FILE = "config.json"

VERSION = "1.0.0"

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
    
    
