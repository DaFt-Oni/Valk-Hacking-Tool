import os
from utils.colors import Colors
from utils.helpers import clear_screen, display_banner

def leer_tag():
    print(f"\n{Colors.OKGREEN}[+] Leyendo tag NFC desde el teléfono...{Colors.ENDC}")
    os.system("adb shell am start -n com.wakdev.nfctools/com.wakdev.nfctools.activities.MainActivity")
    os.system("adb shell input keyevent KEYCODE_NFC")
    input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")

def escribir_tag(mensaje):
    print(f"\n{Colors.OKGREEN}[+] Escribiendo mensaje en el tag NFC desde el teléfono...{Colors.ENDC}")
    os.system("adb shell am start -n com.wakdev.nfctools/com.wakdev.nfctools.activities.WriteActivity")
    os.system(f"adb shell input text '{mensaje}'")
    os.system("adb shell input keyevent KEYCODE_NFC")
    input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")

def clonar_tag():
    print(f"\n{Colors.OKGREEN}[+] Clonando tag NFC desde el teléfono...{Colors.ENDC}")
    print(f"{Colors.WARNING}[-] Esta funcionalidad requiere una aplicación avanzada de NFC en el teléfono.{Colors.ENDC}")
    input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")

def emular_tag():
    print(f"\n{Colors.OKGREEN}[+] Iniciando emulación de tag NFC en el teléfono...{Colors.ENDC}")
    print(f"{Colors.WARNING}[-] Asegúrate de tener una aplicación de emulación NFC instalada (ej: NFC Tools).{Colors.ENDC}")
    os.system("adb shell am start -n com.wakdev.nfctools/com.wakdev.nfctools.activities.EmulateActivity")
    os.system("adb shell input keyevent KEYCODE_NFC")
    input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")

def nfc_phone_pc_tools():
    while True:
        clear_screen()
        display_banner()
        print(f"{Colors.BOLD}{Colors.OKBLUE}Modo Teléfono conectado al PC{Colors.ENDC}")
        print(f"{Colors.OKGREEN}[1]. Leer Tag NFC{Colors.ENDC}")
        print(f"{Colors.OKGREEN}[2]. Escribir en Tag NFC{Colors.ENDC}")
        print(f"{Colors.OKGREEN}[3]. Clonar Tag NFC{Colors.ENDC}")
        print(f"{Colors.OKGREEN}[4]. Emular Tag NFC{Colors.ENDC}")
        print(f"{Colors.OKGREEN}[5]. Volver al menú anterior{Colors.ENDC}")
        opcion = input(f"{Colors.BOLD}{Colors.WARNING}Selecciona una opción: {Colors.ENDC}")

        if opcion == '1':
            leer_tag()
        elif opcion == '2':
            mensaje = input("Ingresa el mensaje a escribir: ")
            escribir_tag(mensaje)
        elif opcion == '3':
            clonar_tag()
        elif opcion == '4':
            emular_tag()
        elif opcion == '5':
            break
        else:
            print(f"{Colors.FAIL}[-] Opción no válida.{Colors.ENDC}")
            input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")