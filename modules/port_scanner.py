import nmap
from utils.colors import Colors

def port_scanner():
    target = input(f"{Colors.BOLD}{Colors.WARNING}Introduce la dirección IP o el hostname: {Colors.ENDC}")
    scanner = nmap.PortScanner()
    print(f"{Colors.OKBLUE}Escaneando {target}...{Colors.ENDC}")
    scanner.scan(target, '1-1024')
    for host in scanner.all_hosts():
        print(f"{Colors.BOLD}{Colors.OKGREEN}Host: {host} ({scanner[host].hostname()}){Colors.ENDC}")
        for proto in scanner[host].all_protocols():
            print(f"{Colors.BOLD}{Colors.OKBLUE}Protocolo: {proto}{Colors.ENDC}")
            ports = scanner[host][proto].keys()
            for port in ports:
                print(f"{Colors.BOLD}{Colors.WARNING}Puerto: {port}\tEstado: {scanner[host][proto][port]['state']}{Colors.ENDC}")