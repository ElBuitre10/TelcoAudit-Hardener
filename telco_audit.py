import os
import sys
import socket
import time

def clear_screen():
    os.system('clear')

def b_green(text): return f"\033[1;32m{text}\033[0m"
def b_cyan(text): return f"\033[1;36m{text}\033[0m"
def b_yellow(text): return f"\033[1;33m{text}\033[0m"
def b_red(text): return f"\033[1;31m{text}\033[0m"

def banner():
    print(b_green("="*55))
    print(b_green("     TELCOAUDIT-HARDENER v1.1 - Termux Edition"))
    print(b_green("   Auditoría de Redes Domésticas y Dispositivos CPE"))
    print(b_green("   Desarrollado por: Alejandro Buitrago"))
    print(b_green("="*55))

def cpe_port_scan():
    clear_screen()
    banner()
    print(b_cyan("\n[*] Módulo 1: Escaneo de Puertos Críticos CPE / ISP"))
    target = input("\nIntroduce la IP del Router/ONT (ej. 192.168.1.1): ")
    if not target:
        target = "192.168.1.1"
    
    ports = {22: "SSH", 23: "Telnet", 80: "HTTP", 443: "HTTPS", 7547: "TR-069 (Gestión Remota)"}
    scan_results = {}
    
    print(b_yellow(f"\n[+] Analizando vulnerabilidades de interfaz en {target}...\n"))
    
    for port, service in ports.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"  [!] Puerto {port} ({service}): " + b_red("ABIERTO / EXPUESTO"))
            scan_results[port] = (service, "ABIERTO (Riesgo potencial de administración no autorizada)")
        else:
            print(f"  [✓] Puerto {port} ({service}): Seguro / Cerrado")
            scan_results[port] = (service, "Cerrado / Seguro")
        s.close()
        
    print(b_green("\n[✓] Análisis perimetral completado."))
    input("\nPresiona Enter para avanzar a la generación del reporte técnico...")
    generate_markdown_report(target, scan_results)

def generate_markdown_report(target, results):
    clear_screen()
    banner()
    print(b_cyan("\n[*] Módulo 3: Exportando Reporte de Hardening..."))
    
    filename = f"auditoria_telco_{target.replace('.', '_')}.md"
    
    report_content = f"""# Reporte Técnico de Auditoría de Red Residencial / CPE
**Auditor de Seguridad:** Alejandro Buitrago (Analista de Ciberseguridad Junior)
**Entorno de Ejecución:** Termux (Android Linux Subsystem)
**Dispositivo Evaluado (IP):** {target}
**Fecha de Análisis:** {time.strftime('%Y-%m-%d %H:%M:%S')}

## 1. Resumen Ejecutivo
Este reporte técnico ha sido generado de manera automatizada utilizando la suite *TelcoAudit-Hardener* desde un dispositivo móvil. Se evaluaron los vectores de exposición perimetral estándar en routers comerciales y terminales ópticas (ONT) asignados por ISPs.

## 2. Resultados del Escaneo de Puertos de Gestión (CPE / TR-069)
A continuación se detallan los servicios de administración identificados en la interfaz del dispositivo:

| Puerto | Servicio | Estado / Hallazgo |
| :--- | :--- | :--- |
"""
    for port, (service, status) in results.items():
        report_content += f"| {port} | {service} | {status} |\n"
        
    report_content += """
## 3. Recomendaciones de Hardening y Mitigación (Línea Base GPON/FTTH)
Basado en los principios de auditoría empírica y resiliencia de infraestructuras:
* **Aislamiento de TR-069:** Si el puerto `7547` está expuesto a la LAN o WAN, se recomienda limitar su acceso únicamente a la VLAN de gestión interna del ISP mediante reglas de firewall ACL.
* **Cierre de Interfaces Legadas:** Deshabilitar por completo el protocolo `Telnet (23)` en el firmware del CPE, forzando el uso exclusivo de `SSH` con llaves criptográficas si se requiere acceso de soporte.
* **Protección de Credenciales:** Modificar las contraseñas por defecto del archivo de configuración XML del router para evitar la extracción local de identificadores PPPoE o PLOAM Passwords.
"""
    
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report_content)
        
        shared_path = "/sdcard/Download"
        if os.path.exists(shared_path):
            with open(f"{shared_path}/{filename}", "w", encoding="utf-8") as f:
                f.write(report_content)
            print(b_green(f"\n[✓] ¡Éxito! Copia exportada a tu carpeta de Descargas del celular."))
            
        print(b_green(f"[✓] Reporte local guardado en Termux como: {filename}"))
    except Exception as e:
        print(b_red(f"\n[X] Error al escribir el archivo: {e}"))
        
    input("\nPresiona Enter para volver al menú...")

def generate_markdown_report(target, results):
    pass
def ont_bypass_knowledge():
    clear_screen()
    banner()
    print(b_cyan("\n[*] Módulo 2: Marco de Auditoría FTTH / Clonación ONT"))
    print("\nEste módulo describe la metodología lógica de auditoría para verificar")
    print("el correcto aislamiento de credenciales en equipos de fibra óptica.")
    print("\nPasos metodológicos implementados de forma manual:")
    print(b_green("  1.") + " Extracción segura de la configuración XML del dispositivo original.")
    print(b_green("  2.") + " Identificación de parámetros críticos de conexión: VLAN IDs (Voz/Datos).")
    print(b_green("  3.") + " Extracción de credenciales de autenticación de red (PPPoE / PLOAM Password).")
    print(b_green("  4.") + " Replicación controlada de parámetros para validar resiliencia del ISP.")
    input("\nPresiona Enter para volver al menú...")

def main_menu():
    while True:
        clear_screen()
        banner()
        print(b_cyan("\n[ Menú de Opciones ]"))
        print("1. Escanear Puertos de Gestión Remota e Interfaz CPE")
        print("2. Ver Metodología de Auditoría FTTH e Ingesta de Datos")
        print("3. Salir")
        print(b_green("\n"+"="*55))
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            cpe_port_scan()
        elif opcion == '2':
            ont_bypass_knowledge()
        elif opcion == '3':
            sys.exit()

main_menu()
