from utils.colors import Colors

def generate_report():
    report_content = "Reporte de Escaneo\n"
    report_content += "==================\n"
    report_content += "Detalles del escaneo...\n"
    
    with open("report.txt", "w") as report_file:
        report_file.write(report_content)
    
    print(f"{Colors.OKGREEN}Reporte generado en report.txt{Colors.ENDC}")