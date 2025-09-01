import qrcode
from PIL import Image
import os
import json
from datetime import datetime

class ConfigQR:
    """Configuración por defecto para códigos QR"""
    VERSIONS = {
        "pequeño": 1,    # ~25 caracteres
        "mediano": 2,    # ~47 caracteres
        "grande": 3      # ~77 caracteres
    }
    
    COLORS = {
        "azul": "#0000FF",
        "rojo": "#FF0000",
        "verde": "#00FF00",
        "negro": "#000000",
        "morado": "#800080",
        "naranja": "#FFA500",
        "rosa": "#FF69B4",
        "amarillo": "#FFFF00",
        "cyan": "#00FFFF",
        "blanco": "#FFFFFF"
    }
    
    STYLES = {
        "normal": {"fill": "negro", "back": "blanco"},
        "neon": {"fill": "verde", "back": "negro"},
        "sunset": {"fill": "naranja", "back": "rosa"},
        "ocean": {"fill": "azul", "back": "cyan"},
        "royal": {"fill": "morado", "back": "amarillo"}
    }

def configurar_atributos():
    """Solicita al usuario configurar todos los atributos del QR"""
    print("\n== CONFIGURACIÓN DE ATRIBUTOS DEL QR ==")
    
    # Configurar versión
    print("\n1. VERSIÓN DEL QR:")
    print("La versión determina la capacidad de datos del código QR")
    print("- Versión 1 (~25 caracteres)")
    print("- Versión 2 (~47 caracteres)")
    print("- Versión 3 (~77 caracteres)")
    while True:
        version = input("¿Qué versión deseas usar? (1/2/3): ")
        if version in ['1', '2', '3']:
            break
        print("❌ Por favor, elige 1, 2 o 3")

    # Configurar tamaño de caja
    print("\n2. TAMAÑO DE CAJA:")
    print("Define qué tan grande será cada módulo del QR")
    print("Recomendado: 10 pixeles")
    while True:
        try:
            box_size = int(input("Ingresa el tamaño de caja (1-50): "))
            if 1 <= box_size <= 50:
                break
            print("❌ El tamaño debe estar entre 1 y 50")
        except ValueError:
            print("❌ Por favor, ingresa un número válido")

    # Configurar borde
    print("\n3. BORDE DEL QR:")
    print("Espacio en blanco alrededor del QR")
    print("Recomendado: 4 módulos")
    while True:
        try:
            border = int(input("Ingresa el tamaño del borde (0-10): "))
            if 0 <= border <= 10:
                break
            print("❌ El borde debe estar entre 0 y 10")
        except ValueError:
            print("❌ Por favor, ingresa un número válido")

    # Configurar estilo de color
    print("\n4. ESTILO DE COLOR:")
    print("Estilos disponibles:")
    for estilo, colores in ConfigQR.STYLES.items():
        print(f"- {estilo}: {colores['fill']} sobre {colores['back']}")
    print("- personalizado: elegir colores manualmente")
    
    while True:
        estilo = input("\nElige un estilo: ").lower()
        if estilo in ConfigQR.STYLES:
            fill_color = ConfigQR.STYLES[estilo]["fill"]
            back_color = ConfigQR.STYLES[estilo]["back"]
            break
        elif estilo == "personalizado":
            print("\nColores disponibles:", ", ".join(ConfigQR.COLORS.keys()))
            while True:
                fill_color = input("Color del QR: ").lower()
                if fill_color in ConfigQR.COLORS:
                    break
                print("❌ Color no válido")

            while True:
                back_color = input("Color del fondo: ").lower()
                if back_color in ConfigQR.COLORS and back_color != fill_color:
                    break
                print("❌ Color no válido o igual al del QR")
            break
        print("❌ Estilo no válido")

    return {
        "version": int(version),
        "box_size": box_size,
        "border": border,
        "fill_color": ConfigQR.COLORS[fill_color],
        "back_color": ConfigQR.COLORS[back_color]
    }

def crear_carpeta_salida():
    """Crear carpeta para guardar los códigos QR"""
    if not os.path.exists("mis_qr"):
        os.makedirs("mis_qr")

def generar_qr_personalizado(texto, nombre_archivo, version=1, box_size=10, 
                           border=4, fill_color="#000000", back_color="#FFFFFF"):
    """Genera un código QR personalizado"""
    try:
        qr = qrcode.QRCode(
            version=version,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border
        )
        
        qr.add_data(texto)
        qr.make(fit=True)
        
        imagen_qr = qr.make_image(fill_color=fill_color, back_color=back_color)
        ruta_archivo = f"mis_qr/{nombre_archivo}.png"
        imagen_qr.save(ruta_archivo)
        
        print(f"✅ QR guardado como: {nombre_archivo}.png")
        return True
        
    except Exception as e:
        print(f"❌ Error al generar QR: {str(e)}")
        return False

def menu():
    """Menú principal del programa"""
    while True:
        print("\n== GENERADOR DE CÓDIGOS QR ==")
        print("1. Crear nuevo QR")
        print("2. Salir")
        
        opcion = input("\nElige una opción (1-2): ")
        
        if opcion == "1":
            texto = input("\nEscribe el texto para el QR: ")
            nombre = input("Nombre para guardar el archivo: ")
            
            print("\n¿Cómo deseas configurar los parámetros del QR?")
            print("1. Configurar manualmente")
            print("2. Usar valores por defecto")
            
            config_opcion = input("\nElige una opción (1-2): ")
            
            if config_opcion == "1":
                config = configurar_atributos()
                generar_qr_personalizado(
                    texto, 
                    nombre, 
                    version=config["version"],
                    box_size=config["box_size"],
                    border=config["border"],
                    fill_color=config["fill_color"],
                    back_color=config["back_color"]
                )
            elif config_opcion == "2":
                print("\nUsando configuración por defecto:")
                print("- Versión: 1")
                print("- Tamaño de caja: 10")
                print("- Borde: 4")
                print("- Estilo: normal (negro sobre blanco)")
                generar_qr_personalizado(texto, nombre)
            else:
                print("❌ Opción no válida, usando configuración por defecto")
                generar_qr_personalizado(texto, nombre)
            
        elif opcion == "2":
            print("\n¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción no válida")

if __name__ == "__main__":
    crear_carpeta_salida()
    menu()