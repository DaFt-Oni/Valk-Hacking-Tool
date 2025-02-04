import os
import sys
import io
import subprocess
from utils.system import VERSION
from utils.colors import Colors

# Configurar la salida estándar para usar UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def clear_screen():
    """
    Limpia la pantalla de la terminal de manera compatible con cualquier entorno.
    Funciona en Windows (cmd, PowerShell, Git Bash), Linux y macOS.
    """
    try:
        # Intenta usar el comando 'clear' (funciona en Linux, macOS y Git Bash)
        subprocess.run('clear', shell=True, check=True)
    except:
        try:
            # Si falla, intenta usar 'cls' (funciona en cmd y PowerShell)
            subprocess.run('cls', shell=True, check=True)
        except:
            # Si todo falla, imprime un mensaje de error
            print(f"{Colors.FAIL}No se pudo limpiar la pantalla.{Colors.ENDC}")
    
def supports_ansi():
    # Verificar si la terminal soporta ANSI
    return os.name != 'nt' or 'ANSICON' in os.environ or 'WT_SESSION' in os.environ

def display_banner():
    banner = """
    
 ██▒   █▓ ▄▄▄       ██▓     ██ ▄█▀▓██   ██▓ ██▀███   ██▓▓█████     ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀ ██▓ ███▄    █   ▄████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓██░   █▒▒████▄    ▓██▒     ██▄█▒  ▒██  ██▒▓██ ▒ ██▒▓██▒▓█   ▀    ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██▒ ██ ▀█   █  ██▒ ▀█▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
 ▓██  █▒░▒██  ▀█▄  ▒██░    ▓███▄░   ▒██ ██░▓██ ░▄█ ▒▒██▒▒███      ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
  ▒██ █░░░██▄▄▄▄██ ▒██░    ▓██ █▄   ░ ▐██▓░▒██▀▀█▄  ░██░▒▓█  ▄    ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░██░▓██▒  ▐▌██▒░▓█  ██▓   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
   ▒▀█░   ▓█   ▓██▒░██████▒▒██▒ █▄  ░ ██▒▓░░██▓ ▒██▒░██░░▒████▒   ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░██░▒██░   ▓██░░▒▓███▀▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
   ░ ▐░   ▒▒   ▓▒█░░ ▒░▓  ░▒ ▒▒ ▓▒   ██▒▒▒ ░ ▒▓ ░▒▓░░▓  ░░ ▒░ ░    ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░▓  ░ ▒░   ▒ ▒  ░▒   ▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
   ░ ░░    ▒   ▒▒ ░░ ░ ▒  ░░ ░▒ ▒░ ▓██ ░▒░   ░▒ ░ ▒░ ▒ ░ ░ ░  ░    ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ▒ ░░ ░░   ░ ▒░  ░   ░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
     ░░    ░   ▒     ░ ░   ░ ░░ ░  ▒ ▒ ░░    ░░   ░  ▒ ░   ░       ░  ░░ ░  ░   ▒   ░        ░ ░░ ░  ▒ ░   ░   ░ ░ ░ ░   ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
      ░        ░  ░    ░  ░░  ░    ░ ░        ░      ░     ░  ░    ░  ░  ░      ░  ░░ ░      ░  ░    ░           ░       ░                 ░ ░      ░ ░      ░  ░
     ░                             ░ ░                                              ░                                                                            

    """
    
    subtitle = f"""
    ════════════════════════════════════════════════════════════════════════════════════════════════════
     [*] Creado por DaFt | GitHub: https://github.com/DaFt-Oni | Versión: {VERSION} [*]
    ────────────────────────────────────────────────────────────────────────────────────────────────────
     [!] ¡ADVERTENCIA! Este software es únicamente para fines educativos y de investigación. [!]
     [X] No me hago responsable del uso indebido de esta herramienta. ¡Haz el bien, no el mal! [X]
    ════════════════════════════════════════════════════════════════════════════════════════════════════
    """
    if supports_ansi():
        # Mostrar el banner con colores
        print(banner)
        print(subtitle)
    else:
        # Mostrar el banner sin colores
        print(banner.replace(Colors.OKBLUE, "").replace(Colors.ENDC, ""))
        print(subtitle.replace(Colors.OKBLUE, "").replace(Colors.ENDC, ""))
    sys.stdout.flush()  # Forzar el vaciado del buffer