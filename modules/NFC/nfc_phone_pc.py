import os
from utils.colors import Colors
from utils.helpers import clear_screen, display_banner
from .utils_nfc import guardar_tag, cargar_tag, listar_tags

def leer_tag():
    print(f"\n{Colors.OKGREEN}[+] Leyendo tag NFC desde el teléfono...{Colors.ENDC}")
    os.system("adb shell am start -n com.wakdev.nfctools/com.wakdev.nfctools.activities.MainActivity")
    os.system("adb shell input keyevent KEYCODE_NFC")
    nombre_archivo = input(f"{Colors.BOLD}{Colors.WARNING}Ingresa un nombre para guardar este tag: {Colors.ENDC}")
    # Simulación de datos del tag (debes adaptar esto según la aplicación NFC)
    tag_data = {
        "id": "simulated_id",
        "type": "simulated_type",
        "records": [{"type": "text/plain", "text": "Simulated NFC Tag"}]
    }
    guardar_tag(tag_data, nombre_archivo)
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
    nombre_archivo = input(f"{Colors.BOLD}{Colors.WARNING}Ingresa un nombre para guardar este tag: {Colors.ENDC}")
    # Simulación de datos del tag (debes adaptar esto según la aplicación NFC)
    tag_data = {
        "id": "simulated_id",
        "type": "simulated_type",
        "records": [{"type": "text/plain", "text": "Simulated NFC Tag"}]
    }
    guardar_tag(tag_data, nombre_archivo)
    input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")

def emular_tag():
    tags = listar_tags()
    if not tags:
        return
    seleccion = input(f"{Colors.BOLD}{Colors.WARNING}Selecciona el número del tag a emular: {Colors.ENDC}")
    try:
        seleccion = int(seleccion) - 1
        tag_data = cargar_tag(tags[seleccion])
        if tag_data:
            print(f"\n{Colors.OKGREEN}[+] Emulando tag: {tags[seleccion]}{Colors.ENDC}")
            # Simulación de emulación (debes adaptar esto según la aplicación NFC)
            os.system("adb shell am start -n com.wakdev.nfctools/com.wakdev.nfctools.activities.EmulateActivity")
            os.system(f"adb shell input text '{tag_data['records'][0]['text']}'")
            os.system("adb shell input keyevent KEYCODE_NFC")
            print(f"\n{Colors.OKGREEN}[+] Emulación completada.{Colors.ENDC}")
    except (ValueError, IndexError):
        print(f"{Colors.FAIL}[-] Selección no válida.{Colors.ENDC}")
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