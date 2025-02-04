# Ethical Hacking Tool - Documentación Completa

## Descargo de Responsabilidad

Esta herramienta está diseñada únicamente para fines educativos y de prueba en entornos controlados. El uso de esta herramienta para actividades ilegales o no autorizadas está estrictamente prohibido. El autor y los colaboradores de este proyecto no se hacen responsables de ningún mal uso o daño causado por el uso de esta herramienta.

### Advertencias Importantes:
1. **Uso Ético**: Asegúrate de tener el consentimiento explícito del propietario del sistema antes de realizar cualquier prueba.
2. **Legalidad**: El uso de esta herramienta en sistemas sin autorización es ilegal y puede resultar en consecuencias legales.
3. **Sin Garantías**: Esta herramienta se proporciona "tal cual", sin garantías de ningún tipo. El autor no es responsable de ningún daño o problema que pueda surgir del uso del software.
4. **Responsabilidad del Usuario**: El usuario es el único responsable de sus acciones y del uso que le dé a esta herramienta.

Al utilizar esta herramienta, aceptas estos términos y condiciones. Si no estás de acuerdo, no debes usar esta herramienta.

## Descripción
Esta es una herramienta de hacking ético diseñada para realizar pruebas de seguridad en redes y sistemas. La herramienta es modular y está escrita en Python, con una interfaz de terminal fácil de usar. Incluye funcionalidades como escaneo de puertos, escaneo de vulnerabilidades, fuerza bruta, sniffing de red, phishing Wi-Fi y más.

## Estructura del Proyecto
```
ethical_hacking_tool/
│
├── main.py
├── requirements.txt
├── manual.txt
├── LICENSE
├── bin/
│   ├── hostapd           # Binario de hostapd para Linux
│   └── dnsmasq           # Binario de dnsmasq para Linux
├── config/
│   ├── hostapd.conf      # Configuración de hostapd
│   └── dnsmasq.conf      # Configuración de dnsmasq
├── templates/
│   ├── default/
│   │   ├── index.html
│   │   ├── style.css
│   │   └── script.js
│   └── custom_template/
│       ├── index.html
│       ├── style.css
│       └── script.js
├── modules/
│   ├── __init__.py
│   ├── port_scanner.py
│   ├── vulnerability_scanner.py
│   ├── password_cracker.py
│   ├── network_sniffer.py
│   ├── phishing.py
│   ├── wifi_phishing.py
│   ├── automated_scan.py
│   └── report_generator.py
└── utils/
    ├── __init__.py
    ├── colors.py
    ├── helpers.py
    └── system.py            # Módulo para detectar el sistema operativo
```

## Requisitos del Sistema
### Linux
- Python 3.x
- `hostapd`
- `dnsmasq`
- `nmap`
- `scapy`
- `paramiko`

### Windows
**Nota**: Esta herramienta está diseñada principalmente para Linux. Algunas funcionalidades, como el phishing Wi-Fi, no están disponibles en Windows.

## Instalación de Dependencias
### En Linux
1. Instala Python 3.x:
   ```bash
   sudo apt update
   sudo apt install python3
   ```

2. Instala las dependencias del sistema:
   ```bash
   sudo apt install hostapd dnsmasq nmap python3-pip
   ```

3. Instala las dependencias de Python:
   ```bash
   pip install -r requirements.txt
   ```

### En Windows
1. Instala Python 3.x desde [python.org](https://www.python.org/).
2. Instala las dependencias de Python:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
### Ejecutar la Herramienta
```bash
sudo python main.py
```

### Menú Principal
```
1. Escaneo de Puertos
2. Escaneo de Vulnerabilidades
3. Fuerza Bruta (Password Cracker)
4. Sniffer de Red
5. Phishing Web
6. Phishing Wi-Fi (solo Linux)
7. Escaneo Automático
8. Generar Reporte
9. Ver Manual
10. Salir
```

### Ejemplos de Uso
1. **Escaneo de Puertos**:
   - Selecciona la opción 1 en el menú.
   - Introduce la dirección IP o el hostname del objetivo.
   - Observa los puertos abiertos en el objetivo.

2. **Phishing Wi-Fi**:
   - Selecciona la opción 6 en el menú (solo Linux).
   - Introduce el nombre del SSID.
   - Selecciona una plantilla de la carpeta `templates`.
   - Los usuarios que se conecten al SSID serán redirigidos a la página de autenticación.
   - Las credenciales capturadas se mostrarán en tiempo real.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contribuciones
Si deseas contribuir a este proyecto, por favor sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un pull request.

## Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme:
- Correo: [francoortizastudillo8@gmail.com](mailto:francoortizastudillo8@gmail.com)
- GitHub: [DaFt-Oni](https://github.com/DaFt-Oni)