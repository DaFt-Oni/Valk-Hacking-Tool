from modules.port_scanner import port_scanner
from modules.vulnerability_scanner import vulnerability_scanner
from utils.colors import Colors

def automated_scan():
    target = input(f"{Colors.BOLD}{Colors.WARNING}Introduce la dirección IP o el hostname: {Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKBLUE}Iniciando escaneo automático en {target}...{Colors.ENDC}")
    port_scanner(target)
    vulnerability_scanner(target)