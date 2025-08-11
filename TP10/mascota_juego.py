import pygame
import sys
import math
import random

# Inicializar Pygame
pygame.init()

# Constantes
ANCHO = 1000
ALTO = 700
FPS = 60

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (100, 150, 255)
VERDE = (100, 255, 100)
ROJO = (255, 100, 100)
AMARILLO = (255, 255, 100)
ROSA = (255, 150, 200)
MORADO = (150, 100, 255)
NARANJA = (255, 150, 100)

class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.especie = "Mascotita"
        self.energia = 80
        self.felicidad = 70
        self.hambre = 60
        self.aura = 0
        self.altitud = 0
        self.x = ANCHO // 2
        self.y = ALTO // 2 + 50
        self.animation_timer = 0
        self.estado = "normal"  # normal, jugando, comiendo, durmiendo, backflip, volando
        self.mensaje = ""
        self.mensaje_timer = 0
        
    def limitar_valores(self):
        self.energia = max(0, min(100, self.energia))
        self.felicidad = max(0, min(100, self.felicidad))
        self.hambre = max(0, min(100, self.hambre))
        
    def jugar(self):
        self.felicidad += 20
        self.energia -= 30
        self.hambre += 20
        self.limitar_valores()
        self.estado = "jugando"
        self.mensaje = "¡Que perro revoltoso!"
        self.mensaje_timer = 180
        
    def comer(self):
        self.felicidad += 10
        self.energia += 20
        self.hambre -= 60
        self.limitar_valores()
        self.estado = "comiendo"
        self.mensaje = "Cuanta hambre tenía..."
        self.mensaje_timer = 180
        
    def dormir(self):
        self.felicidad += 10
        self.energia += 60
        self.hambre += 50
        self.limitar_valores()
        self.estado = "durmiendo"
        self.mensaje = "Parece un ladrillo..."
        self.mensaje_timer = 180
        
    def backflip(self):
        self.aura += 1000000
        self.felicidad += 10000
        self.energia -= 100
        self.hambre += 100
        self.limitar_valores()
        self.estado = "backflip"
        self.mensaje = "¡No lo puedo creer, CUANTA AURA!"
        self.mensaje_timer = 180
        
    def volar(self):
        self.aura += 102120120
        self.felicidad += 12334234
        self.energia -= 80
        self.hambre += 30
        self.altitud += 1000000
        self.limitar_valores()
        self.estado = "volando"
        self.mensaje = "¡Aura, una mascota que vuela!"
        self.mensaje_timer = 180
        
    def update(self):
        self.animation_timer += 1
        if self.mensaje_timer > 0:
            self.mensaje_timer -= 1
        else:
            self.estado = "normal"
            self.mensaje = ""
            
    def dibujar_mascota(self, screen):
        # Dibujar la mascota según su estado
        if self.estado == "durmiendo":
            self.dibujar_durmiendo(screen)
        elif self.estado == "comiendo":
            self.dibujar_comiendo(screen)
        elif self.estado == "jugando":
            self.dibujar_jugando(screen)
        elif self.estado == "backflip":
            self.dibujar_backflip(screen)
        elif self.estado == "volando":
            self.dibujar_volando(screen)
        else:
            self.dibujar_normal(screen)
            
    def dibujar_normal(self, screen):
        # Cuerpo del dragón
        pygame.draw.ellipse(screen, AZUL, (self.x - 40, self.y - 30, 80, 60))
        # Cabeza
        pygame.draw.circle(screen, AZUL, (self.x, self.y - 40), 25)
        # Alas
        wing_offset = math.sin(self.animation_timer * 0.1) * 5
        pygame.draw.ellipse(screen, MORADO, (self.x - 60, self.y - 20 + wing_offset, 30, 40))
        pygame.draw.ellipse(screen, MORADO, (self.x + 30, self.y - 20 + wing_offset, 30, 40))
        # Ojos
        pygame.draw.circle(screen, BLANCO, (self.x - 10, self.y - 45), 5)
        pygame.draw.circle(screen, BLANCO, (self.x + 10, self.y - 45), 5)
        pygame.draw.circle(screen, NEGRO, (self.x - 10, self.y - 45), 3)
        pygame.draw.circle(screen, NEGRO, (self.x + 10, self.y - 45), 3)
        # Cola
        tail_wag = math.sin(self.animation_timer * 0.2) * 10
        pygame.draw.circle(screen, VERDE, (self.x + 50 + tail_wag, self.y), 15)
        
    def dibujar_durmiendo(self, screen):
        # Mascota acostada
        pygame.draw.ellipse(screen, AZUL, (self.x - 50, self.y - 10, 100, 40))
        pygame.draw.circle(screen, AZUL, (self.x - 30, self.y - 20), 20)
        # Ojos cerrados
        pygame.draw.line(screen, NEGRO, (self.x - 40, self.y - 25), (self.x - 30, self.y - 25), 3)
        pygame.draw.line(screen, NEGRO, (self.x - 20, self.y - 25), (self.x - 10, self.y - 25), 3)
        # Zzz
        font = pygame.font.Font(None, 36)
        z_text = font.render("Zzz", True, AZUL)
        screen.blit(z_text, (self.x + 20, self.y - 60))
        
    def dibujar_comiendo(self, screen):
        self.dibujar_normal(screen)
        # Comida
        pygame.draw.circle(screen, NARANJA, (self.x - 30, self.y + 20), 8)
        pygame.draw.circle(screen, ROJO, (self.x - 15, self.y + 25), 6)
        pygame.draw.circle(screen, VERDE, (self.x + 5, self.y + 22), 7)
        
    def dibujar_jugando(self, screen):
        # Mascota saltando
        bounce = abs(math.sin(self.animation_timer * 0.3)) * 20
        temp_y = self.y - bounce
        # Cuerpo
        pygame.draw.ellipse(screen, ROSA, (self.x - 40, temp_y - 30, 80, 60))
        pygame.draw.circle(screen, ROSA, (self.x, temp_y - 40), 25)
        # Alas extendidas
        pygame.draw.ellipse(screen, AMARILLO, (self.x - 70, temp_y - 30, 40, 50))
        pygame.draw.ellipse(screen, AMARILLO, (self.x + 30, temp_y - 30, 40, 50))
        # Ojos felices
        pygame.draw.arc(screen, NEGRO, (self.x - 15, temp_y - 50, 10, 10), 0, math.pi, 3)
        pygame.draw.arc(screen, NEGRO, (self.x + 5, temp_y - 50, 10, 10), 0, math.pi, 3)
        
    def dibujar_backflip(self, screen):
        # Mascota girando
        rotation = self.animation_timer * 0.5
        size = 30 + math.sin(rotation) * 10
        # Efecto de giro con colores cambiantes
        color = (int(128 + 127 * math.sin(rotation)), 
                int(128 + 127 * math.sin(rotation + 2)), 
                int(128 + 127 * math.sin(rotation + 4)))
        pygame.draw.circle(screen, color, (self.x, self.y - 30), int(size))
        # Estrellas de aura
        for i in range(5):
            angle = rotation + i * (2 * math.pi / 5)
            star_x = self.x + math.cos(angle) * 60
            star_y = self.y - 30 + math.sin(angle) * 60
            pygame.draw.circle(screen, AMARILLO, (int(star_x), int(star_y)), 5)
            
    def dibujar_volando(self, screen):
        # Mascota volando alto
        fly_height = math.sin(self.animation_timer * 0.1) * 30
        temp_y = self.y - 100 + fly_height
        # Cuerpo brillante
        pygame.draw.ellipse(screen, AMARILLO, (self.x - 45, temp_y - 35, 90, 70))
        pygame.draw.circle(screen, AMARILLO, (self.x, temp_y - 50), 30)
        # Alas grandes
        wing_flap = math.sin(self.animation_timer * 0.2) * 15
        pygame.draw.ellipse(screen, BLANCO, (self.x - 80, temp_y - 40 + wing_flap, 50, 60))
        pygame.draw.ellipse(screen, BLANCO, (self.x + 30, temp_y - 40 + wing_flap, 50, 60))
        # Nubes
        for i in range(3):
            cloud_x = (self.x + i * 100) % ANCHO
            pygame.draw.circle(screen, BLANCO, (cloud_x, temp_y + 80), 20)
            pygame.draw.circle(screen, BLANCO, (cloud_x + 15, temp_y + 85), 15)
            pygame.draw.circle(screen, BLANCO, (cloud_x - 15, temp_y + 85), 15)

class Juego:
    def __init__(self):
        self.screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Mi Mascotita")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.font_pequeña = pygame.font.Font(None, 24)
        self.mascota = None
        self.estado_juego = "inicio"  # inicio, jugando
        self.input_nombre = ""
        
    def manejar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            if event.type == pygame.KEYDOWN:
                if self.estado_juego == "inicio":
                    if event.key == pygame.K_RETURN and self.input_nombre:
                        self.mascota = Mascota(self.input_nombre)
                        self.estado_juego = "jugando"
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_nombre = self.input_nombre[:-1]
                    else:
                        if len(self.input_nombre) < 20:
                            self.input_nombre += event.unicode
                            
                elif self.estado_juego == "jugando":
                    if event.key == pygame.K_1:
                        self.mascota.jugar()
                    elif event.key == pygame.K_2:
                        self.mascota.comer()
                    elif event.key == pygame.K_3:
                        self.mascota.dormir()
                    elif event.key == pygame.K_4:
                        self.mascota.backflip()
                    elif event.key == pygame.K_5:
                        self.mascota.volar()
                    elif event.key == pygame.K_ESCAPE:
                        self.estado_juego = "inicio"
                        self.input_nombre = ""
                        
        return True
        
    def dibujar_interfaz_inicio(self):
        self.screen.fill(MORADO)
        
        # Título
        titulo = self.font.render("Mi Mascotita", True, AMARILLO)
        titulo_rect = titulo.get_rect(center=(ANCHO//2, 100))
        self.screen.blit(titulo, titulo_rect)
        
        # Instrucciones
        instruccion = self.font.render("Ingresa el nombre de tu mascota:", True, BLANCO)
        instruccion_rect = instruccion.get_rect(center=(ANCHO//2, 200))
        self.screen.blit(instruccion, instruccion_rect)
        
        # Campo de entrada
        pygame.draw.rect(self.screen, BLANCO, (ANCHO//2 - 150, 250, 300, 50))
        pygame.draw.rect(self.screen, NEGRO, (ANCHO//2 - 150, 250, 300, 50), 3)
        
        nombre_text = self.font.render(self.input_nombre, True, NEGRO)
        self.screen.blit(nombre_text, (ANCHO//2 - 140, 265))
        
        # Instrucción para continuar
        if self.input_nombre:
            continuar = self.font_pequeña.render("Presiona ENTER para continuar", True, AMARILLO)
            continuar_rect = continuar.get_rect(center=(ANCHO//2, 350))
            self.screen.blit(continuar, continuar_rect)
            
    def dibujar_barras_estado(self):
        # Fondo de las barras
        pygame.draw.rect(self.screen, NEGRO, (20, 20, 300, 120))
        pygame.draw.rect(self.screen, BLANCO, (20, 20, 300, 120), 3)
        
        # Nombre de la mascota
        nombre_text = self.font.render(f"{self.mascota.nombre} el {self.mascota.especie}", True, BLANCO)
        self.screen.blit(nombre_text, (30, 30))
        
        # Barras de estado
        barras = [
            ("Energía", self.mascota.energia, VERDE),
            ("Felicidad", self.mascota.felicidad, AMARILLO),
            ("Hambre", self.mascota.hambre, ROJO)
        ]
        
        for i, (nombre, valor, color) in enumerate(barras):
            y = 60 + i * 20
            # Barra de fondo
            pygame.draw.rect(self.screen, (50, 50, 50), (30, y, 200, 15))
            # Barra de valor
            pygame.draw.rect(self.screen, color, (30, y, valor * 2, 15))
            # Texto
            texto = self.font_pequeña.render(f"{nombre}: {valor}%", True, BLANCO)
            self.screen.blit(texto, (240, y))
            
    def dibujar_stats_especiales(self):
        if self.mascota.aura > 0 or self.mascota.altitud > 0:
            pygame.draw.rect(self.screen, NEGRO, (ANCHO - 320, 20, 300, 80))
            pygame.draw.rect(self.screen, AMARILLO, (ANCHO - 320, 20, 300, 80), 3)
            
            if self.mascota.aura > 0:
                aura_text = self.font_pequeña.render(f"AURA: {self.mascota.aura:,}", True, AMARILLO)
                self.screen.blit(aura_text, (ANCHO - 310, 30))
                
            if self.mascota.altitud > 0:
                altitud_text = self.font_pequeña.render(f"Altitud: {self.mascota.altitud:,}m", True, AMARILLO)
                self.screen.blit(altitud_text, (ANCHO - 310, 50))
                
    def dibujar_controles(self):
        controles = [
            "1 - Jugar", "2 - Comer", "3 - Dormir",
            "4 - Backflip", "5 - Volar", "ESC - Menú"
        ]
        
        pygame.draw.rect(self.screen, NEGRO, (20, ALTO - 120, 500, 100))
        pygame.draw.rect(self.screen, BLANCO, (20, ALTO - 120, 500, 100), 3)
        
        titulo_controles = self.font_pequeña.render("CONTROLES:", True, AMARILLO)
        self.screen.blit(titulo_controles, (30, ALTO - 110))
        
        for i, control in enumerate(controles):
            x = 30 + (i % 3) * 150
            y = ALTO - 85 + (i // 3) * 25
            control_text = self.font_pequeña.render(control, True, BLANCO)
            self.screen.blit(control_text, (x, y))
            
    def dibujar_mensaje(self):
        if self.mascota.mensaje and self.mascota.mensaje_timer > 0:
            # Fondo del mensaje
            pygame.draw.rect(self.screen, NEGRO, (ANCHO//2 - 200, 150, 400, 60))
            pygame.draw.rect(self.screen, AMARILLO, (ANCHO//2 - 200, 150, 400, 60), 3)
            
            # Texto del mensaje
            mensaje_text = self.font_pequeña.render(self.mascota.mensaje, True, BLANCO)
            mensaje_rect = mensaje_text.get_rect(center=(ANCHO//2, 180))
            self.screen.blit(mensaje_text, mensaje_rect)
            
    def dibujar_fondo(self):
        # Degradado del cielo
        for y in range(ALTO):
            color_ratio = y / ALTO
            r = int(135 * (1 - color_ratio) + 25 * color_ratio)
            g = int(206 * (1 - color_ratio) + 25 * color_ratio)
            b = int(235 * (1 - color_ratio) + 112 * color_ratio)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (ANCHO, y))
            
        # Suelo
        pygame.draw.rect(self.screen, VERDE, (0, ALTO - 50, ANCHO, 50))
        
    def ejecutar(self):
        ejecutando = True
        
        while ejecutando:
            ejecutando = self.manejar_eventos()
            
            if self.estado_juego == "inicio":
                self.dibujar_interfaz_inicio()
            else:
                self.dibujar_fondo()
                self.mascota.update()
                self.mascota.dibujar_mascota(self.screen)
                self.dibujar_barras_estado()
                self.dibujar_stats_especiales()
                self.dibujar_controles()
                self.dibujar_mensaje()
                
            pygame.display.flip()
            self.clock.tick(FPS)
            
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar()