# TelcoAudit-Hardener 🔒
### Suite Portátil de Auditoría Perimetral CPE y Hardening FTTH/GPON (Termux Edition)

---

## 🛠️ Descripción del Proyecto
**TelcoAudit-Hardener** es una herramienta defensiva avanzada desarrollada en Python y optimizada específicamente para entornos móviles CLI (**Termux / Android Linux Subsystem**). Su objetivo principal es automatizar la auditoría de interfaces locales y el descubrimiento de fallos de configuración en dispositivos locales de usuario (CPE), tales como routers comerciales y terminales ópticas (ONT) proveídas por ISPs.

La suite permite a analistas SecOps y de infraestructura diagnosticar de manera ágil el nivel de exposición de los puertos de gestión remota (legados y TR-069) y exportar reportes técnicos detallados directamente al almacenamiento local del smartphone en formato Markdown.

---

## 🎯 Módulos Implementados

### 1. Escaneo de Puertos Críticos CPE / ISP (Capa 4 - OSI)
*   Usa la librería nativa `socket` para realizar un sondeo ligero y de bajo impacto, determinando el nivel de exposición en el segmento local.
*   Audita servicios esenciales de administración: **SSH (22)**, **Telnet (23)**, **HTTP (80)**, **HTTPS (443)** y el protocolo de gestión remota de proveedores **TR-069 (7547)**.

### 2. Marco de Auditoría FTTH / Clonación ONT (Capa 2 - OSI)
*   Despliega la matriz metodológica empírica para la auditoría de redes de fibra óptica estructurada.
*   Documenta las fases esenciales de control: extracción segura de archivos de configuración XML, aislamiento de identificadores de VLAN y extracción de credenciales críticas (PPPoE / PLOAM Passwords) para pruebas controladas de resiliencia del enlace.

### 3. Generación Automatizada de Reportes Técnicos
*   Exporta los hallazgos en formato estructurado **Markdown (.md)**.
*   Genera de forma autónoma tablas de estado y aplica una línea base de hardening recomendada para mitigar vectores de movimiento lateral y accesos WAN/LAN no autorizados.
*   Escribe de forma redundante tanto en el entorno aislado de Termux como en la carpeta nativa de `/Descargas (Download)` del dispositivo móvil para facilitar su lectura.

---

## 🚀 Requisitos e Instalación

Al estar construido sobre la librería estándar de Python, el script consume menos de **15 MB de RAM** en su ejecución y no requiere dependencias de terceros.

1. **Instalar dependencias necesarias en Termux:**
   ```bash
   pkg update && pkg upgrade
   pkg install python
   ```
2. **Otorgar permisos de almacenamiento a Termux (Esencial para exportar reportes):**
   ```bash
   termux-setup-storage
   ```
3. **Clonar y ejecutar:**
   ```bash
   git clone https://github.com
   cd TelcoAudit-Hardener
   python telco_audit.py
   ```

---

## 🛡️ Enfoque Filosófico: Zero Trust
Este desarrollo se rige bajo la filosofía de **Confianza Cero (Zero Trust)**: toda interfaz de red es hostil por defecto. La herramienta ayuda a los administradores de infraestructura a verificar el estado real de sus defensas perimetrales y a aplicar políticas estrictas de control de acceso antes de que ocurra una brecha de seguridad.

---
**Desarrollado de forma independiente por Alejandro Buitrago**  
*Junior Cybersecurity Analyst | SecOps & Infrastructure Defense*
