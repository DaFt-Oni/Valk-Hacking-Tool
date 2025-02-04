import os
import sys
import signal
from utils.colors import Colors
from utils.helpers import clear_screen, display_banner

# Función para manejar la señal SIGINT (Ctrl+C)
def signal_handler(sig, frame):
    print(f"\n{Colors.FAIL}Saliendo...{Colors.ENDC}")
    sys.exit(0)

# Registrar el manejador de la señal SIGINT
signal.signal(signal.SIGINT, signal_handler)

def main_menu():
    clear_screen()  # Limpia la pantalla antes de mostrar el menú
    display_banner()
    print(f"{Colors.BOLD}{Colors.OKBLUE}Menú Principal{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[1]. Escaneo de Puertos{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[2]. Escaneo de Vulnerabilidades{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[3]. Fuerza Bruta (Password Cracker){Colors.ENDC}")
    print(f"{Colors.OKGREEN}[4]. Sniffer de Red{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[5]. Phishing Web{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[6]. Phishing Wi-Fi{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[7]. Escaneo Automático{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[8]. Generar Reporte{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[9]. Executables4victims{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[10]. Montar Servidor C&C{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[11]. Ver Manual{Colors.ENDC}")
    print(f"{Colors.OKGREEN}[12]. Herramientas NFC{Colors.ENDC}")  # Nueva opción
    print(f"{Colors.OKGREEN}[13]. Salir{Colors.ENDC}")  # Ajusta el número de salida
    choice = input(f"{Colors.BOLD}{Colors.WARNING}Selecciona una opción: {Colors.ENDC}")
    return choice

def main():
    if os.name == 'nt':
        print(f"{Colors.WARNING}¡Atención! Para una mejor experiencia, usa Windows Terminal o PowerShell.{Colors.ENDC}")

    # Verifica si el módulo nmap está instalado
    try:
        import nmap
    except ModuleNotFoundError:
        print(f"{Colors.FAIL}Error: El módulo 'nmap' no está instalado.{Colors.ENDC}")
        print(f"{Colors.WARNING}Instálalo con: pip install python-nmap{Colors.ENDC}")
        sys.exit(1)

    while True:
        choice = main_menu()
        if choice == '1':
            from modules.port_scanner import port_scanner
            port_scanner()
            input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")  # Pausa
        elif choice == '2':
            from modules.vulnerability_scanner import vulnerability_scanner
            vulnerability_scanner()
            input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")  # Pausa
        elif choice == '3':
            from modules.password_cracker import password_cracker
            password_cracker()
            input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")  # Pausa
        elif choice == '4':
            try:
                from modules.network_sniffer import network_sniffer
                network_sniffer()
            except ModuleNotFoundError as e:
                print(f"{Colors.FAIL}Error: {e}{Colors.ENDC}")
                print(f"{Colors.WARNING}Asegúrate de instalar las dependencias necesarias.{Colors.ENDC}")
            input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")  # Pausa
        elif choice == '5':
            from modules.phishing import phishing
            phishing()
            input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")  # Pausa
        elif choice == '6':
            from modules.wifi_phishing import wifi_phishing
            wifi_phishing()
            input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")  # Pausa
        elif choice == '7':
            from modules.automated_scan import automated_scan
            automated_scan()
            input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")  # Pausa
        elif choice == '8':
            from modules.report_generator import generate_report
            generate_report()
            input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")  # Pausa
        elif choice == '9':
            from modules.executables4victims import executables4victims
            executables4victims()
            input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")  # Pausa
        elif choice == '10':
            from cnc_server.app import app
            print(f"{Colors.OKBLUE}Servidor C&C iniciado en http://0.0.0.0:5000{Colors.ENDC}")
            app.run(host="0.0.0.0", port=5000)
        elif choice == '11':
            with open("manual.txt", "r") as file:
                print(file.read())
            input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")  # Pausa
        elif choice == '12':  # Nueva opción: Herramientas NFC
            from modules.NFC.menus_nfc import nfc_tools_menu
            while True:
                modo = nfc_tools_menu()
                if modo == '1':
                    from modules.NFC.nfc_pc import nfc_pc_tools
                    nfc_pc_tools()
                elif modo == '2':
                    from modules.NFC.nfc_phone_pc import nfc_phone_pc_tools
                    nfc_phone_pc_tools()
                elif modo == '3':
                    from modules.NFC.nfc_termux import nfc_termux_tools
                    nfc_termux_tools()
                elif modo == '4':
                    break  # Volver al menú principal
                else:
                    print(f"{Colors.FAIL}Opción no válida. Inténtalo de nuevo.{Colors.ENDC}")
                    input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")  # Pausa
        elif choice == '13' or choice.lower() in ["exit", "quit"]:
            print(f"{Colors.FAIL}Saliendo...{Colors.ENDC}")
            break
        else:
            print(f"{Colors.FAIL}Opción no válida. Inténtalo de nuevo.{Colors.ENDC}")
            input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")  # Pausa

if __name__ == "__main__":
    main()