import nfc
from ndef import TextRecord
from utils.colors import Colors
from utils.helpers import clear_screen, display_banner
from .utils_nfc import guardar_tag, cargar_tag, listar_tags

def leer_tag(tag):
    print(f"\n{Colors.OKGREEN}[+] Tag detectado:{Colors.ENDC}")
    print(f"ID: {tag.identifier.hex()}")
    print(f"Tipo: {tag.type}")
    if tag.ndef:
        print("Datos NDEF:")
        for record in tag.ndef.records:
            print(f"  {record.type}: {record.text}")
        # Guardar el tag
        nombre_archivo = input(f"{Colors.BOLD}{Colors.WARNING}Ingresa un nombre para guardar este tag: {Colors.ENDC}")
        tag_data = {
            "id": tag.identifier.hex(),
            "type": tag.type,
            "records": [{"type": record.type, "text": record.text} for record in tag.ndef.records]
        }
        guardar_tag(tag_data, nombre_archivo)
    else:
        print(f"{Colors.WARNING}Este tag no contiene datos NDEF.{Colors.ENDC}")
    return True

def escribir_tag(tag, mensaje):
    if tag.ndef:
        record = TextRecord(mensaje)
        tag.ndef.records = [record]
        print(f"\n{Colors.OKGREEN}[+] Mensaje escrito en el tag NFC.{Colors.ENDC}")
    else:
        print(f"\n{Colors.FAIL}[-] Este tag no soporta NDEF.{Colors.ENDC}")
    return True

def clonar_tag(tag_origen, tag_destino):
    if tag_origen.ndef:
        tag_destino.ndef.records = tag_origen.ndef.records
        print(f"\n{Colors.OKGREEN}[+] Tag clonado exitosamente.{Colors.ENDC}")
        # Guardar el tag clonado
        nombre_archivo = input(f"{Colors.BOLD}{Colors.WARNING}Ingresa un nombre para guardar este tag: {Colors.ENDC}")
        tag_data = {
            "id": tag_origen.identifier.hex(),
            "type": tag_origen.type,
            "records": [{"type": record.type, "text": record.text} for record in tag_origen.ndef.records]
        }
        guardar_tag(tag_data, nombre_archivo)
    else:
        print(f"\n{Colors.FAIL}[-] El tag origen no contiene datos NDEF.{Colors.ENDC}")
    return True

def emular_tag():
    tags = listar_tags()
    if not tags:
        return
    seleccion = input(f"{Colors.BOLD}{Colors.WARNING}Selecciona el número del tag a emular: {Colors.ENDC}")
    try:
        seleccion = int(seleccion) - 1
        tag_data = cargar_tag(tags[seleccion])
        if tag_data:
            record = TextRecord(tag_data["records"][0]["text"])
            print(f"\n{Colors.OKGREEN}[+] Emulando tag: {tags[seleccion]}{Colors.ENDC}")

            def on_startup(targets):
                return targets[0], record

            with nfc.ContactlessFrontend('tty') as clf:
                print(f"\n{Colors.OKGREEN}[+] Esperando a que otro dispositivo NFC se conecte...{Colors.ENDC}")
                clf.connect(llcp={'on-startup': on_startup})
                print(f"\n{Colors.OKGREEN}[+] Emulación completada.{Colors.ENDC}")
    except (ValueError, IndexError):
        print(f"{Colors.FAIL}[-] Selección no válida.{Colors.ENDC}")

def nfc_termux_tools():
    while True:
        clear_screen()
        display_banner()
        print(f"{Colors.BOLD}{Colors.OKBLUE}Modo Termux (ejecución en móvil){Colors.ENDC}")
        print(f"{Colors.OKGREEN}[1]. Leer Tag NFC{Colors.ENDC}")
        print(f"{Colors.OKGREEN}[2]. Escribir en Tag NFC{Colors.ENDC}")
        print(f"{Colors.OKGREEN}[3]. Clonar Tag NFC{Colors.ENDC}")
        print(f"{Colors.OKGREEN}[4]. Emular Tag NFC{Colors.ENDC}")
        print(f"{Colors.OKGREEN}[5]. Volver al menú anterior{Colors.ENDC}")
        opcion = input(f"{Colors.BOLD}{Colors.WARNING}Selecciona una opción: {Colors.ENDC}")

        if opcion == '1':
            with nfc.ContactlessFrontend('tty') as clf:
                print(f"\n{Colors.OKGREEN}[+] Acerca un tag NFC al teléfono...{Colors.ENDC}")
                clf.connect(rdwr={'on-connect': leer_tag})
                input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")
        elif opcion == '2':
            mensaje = input("Ingresa el mensaje a escribir: ")
            with nfc.ContactlessFrontend('tty') as clf:
                print(f"\n{Colors.OKGREEN}[+] Acerca un tag NFC al teléfono...{Colors.ENDC}")
                clf.connect(rdwr={'on-connect': lambda tag: escribir_tag(tag, mensaje)})
                input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")
        elif opcion == '3':
            with nfc.ContactlessFrontend('tty') as clf:
                print(f"\n{Colors.OKGREEN}[+] Acerca el tag origen al teléfono...{Colors.ENDC}")
                clf.connect(rdwr={'on-connect': lambda tag: clonar_tag(tag, None)})
                print(f"\n{Colors.OKGREEN}[+] Acerca el tag destino al teléfono...{Colors.ENDC}")
                clf.connect(rdwr={'on-connect': lambda tag: clonar_tag(None, tag)})
                input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")
        elif opcion == '4':
            emular_tag()
            input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")
        elif opcion == '5':
            break
        else:
            print(f"{Colors.FAIL}[-] Opción no válida.{Colors.ENDC}")
            input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para continuar...{Colors.ENDC}")