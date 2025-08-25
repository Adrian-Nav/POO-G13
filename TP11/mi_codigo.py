import qrcode
from PIL import Image
import os

def crear_carpeta_salida():
    """Crear carpeta para guardar los códigos QR"""
    if not os.path.exists("mis_qr"):
        os.makedirs("mis_qr")

def generar_qr(texto, nombre_archivo):
    """
    Genera un código QR básico
    texto: El contenido del QR
    nombre_archivo: Nombre para guardar el archivo
    """
    # Crear el código QR
    qr = qrcode.QRCode(
        version=1,              # Tamaño del QR
        box_size=10,           # Tamaño de cada cuadrito
        border=4               # Borde blanco alrededor
    )
    
    # Agregar los datos
    qr.add_data(texto)
    qr.make()
    
    # Crear la imagen
    imagen_qr = qr.make_image(fill_color="black", back_color="white")
    
    # Guardar el QR
    imagen_qr.save(f"mis_qr/{nombre_archivo}.png")
    print(f"✅ QR guardado como: {nombre_archivo}.png")

def generar_qr_color(texto, nombre_archivo, color="blue"):
    """
    Genera un QR con color
    texto: El contenido del QR
    nombre_archivo: Nombre para guardar el archivo
    color: Color para el QR (blue, red, green)
    """
    # Diccionario de colores
    colores = {
        "blue": "#0000FF",
        "red": "#FF0000",
        "green": "#00FF00"
    }
    
    # Crear el código QR
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    
    qr.add_data(texto)
    qr.make()
    
    # Crear imagen con color
    imagen_qr = qr.make_image(
        fill_color=colores.get(color, "black"),
        back_color="white"
    )
    
    # Guardar
    imagen_qr.save(f"mis_qr/{nombre_archivo}.png")
    print(f"✅ QR de color guardado como: {nombre_archivo}.png")

def menu():
    """Menú principal del programa"""
    while True:
        print("\n== GENERADOR DE CÓDIGOS QR ==")
        print("1. Crear QR simple")
        print("2. Crear QR con color")
        print("3. Salir")
        
        opcion = input("\nElige una opción (1-3): ")
        
        if opcion == "1":
            texto = input("Escribe el texto para el QR: ")
            nombre = input("Nombre para guardar el archivo: ")
            generar_qr(texto, nombre)
            
        elif opcion == "2":
            texto = input("Escribe el texto para el QR: ")
            nombre = input("Nombre para guardar el archivo: ")
            print("\nColores disponibles:")
            print("- blue (azul)")
            print("- red (rojo)")
            print("- green (verde)")
            color = input("Elige un color: ")
            generar_qr_color(texto, nombre, color)
            
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida")

if __name__ == "__main__":
    # Crear carpeta para los QR
    crear_carpeta_salida()
    # Iniciar el programa
    menu()