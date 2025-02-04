from utils.helpers import clear_screen, display_banner
from utils.colors import Colors


def nfc_tools_menu():
    clear_screen()
    display_banner()
    print(f"{Colors.BOLD}{Colors.OKBLUE}Herramientas NFC{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[1]. Modo PC con dispositivo NFC{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[2]. Modo Teléfono conectado al PC{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[3]. Modo Termux (ejecución en móvil){Colors.ENDC}")
    print(f"{Colors.OKGREEN}[4]. Volver al menú principal{Colors.ENDC}")
    modo = input(f"{Colors.BOLD}{Colors.WARNING}Selecciona un modo: {Colors.ENDC}")
    return modo

def nfc_functionality_menu():
    clear_screen()
    display_banner()
    print(f"{Colors.BOLD}{Colors.OKBLUE}Funcionalidades NFC{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[1]. Leer Tag NFC{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[2]. Escribir en Tag NFC{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[3]. Clonar Tag NFC{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[4]. Emular Tag NFC{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[5]. Volver al menú anterior{Colors.ENDC}")
    opcion = input(f"{Colors.BOLD}{Colors.WARNING}Selecciona una opción: {Colors.ENDC}")
    return opcion