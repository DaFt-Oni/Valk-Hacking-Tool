from scapy.all import sniff
from utils.colors import Colors

def packet_callback(packet):
    print(f"{Colors.BOLD}{Colors.OKBLUE}Paquete capturado: {packet.summary()}{Colors.ENDC}")

def network_sniffer():
    interface = input(f"{Colors.BOLD}{Colors.WARNING}Introduce la interfaz de red: {Colors.ENDC}")
    print(f"{Colors.OKBLUE}Iniciando captura de paquetes en {interface}...{Colors.ENDC}")
    sniff(iface=interface, prn=packet_callback, count=10)