from tkinter import Tk, Label, Button, StringVar
from pet import Mascota

class VirtualPetApp:
    def __init__(self, master):
        self.master = master
        master.title("Virtual Pet")

        self.pet = Mascota("Fido", "Perro")

        self.status = StringVar()
        self.status.set(self.get_status())

        self.label = Label(master, textvariable=self.status)
        self.label.pack()

        self.play_button = Button(master, text="Jugar", command=self.play)
        self.play_button.pack()

        self.feed_button = Button(master, text="Comer", command=self.feed)
        self.feed_button.pack()

        self.sleep_button = Button(master, text="Dormir", command=self.sleep)
        self.sleep_button.pack()

        self.backflip_button = Button(master, text="Backflip", command=self.backflip)
        self.backflip_button.pack()

        self.fly_button = Button(master, text="Volar", command=self.fly)
        self.fly_button.pack()

        self.quit_button = Button(master, text="Salir", command=self.master.destroy, bg="red", fg="white")
        self.quit_button.pack(pady=10)

    def get_status(self):
        return (f"Nombre: {self.pet.nombre}\n"
                f"Especie: {self.pet.especie}\n"
                f"Felicidad: {self.pet.felicidad}%\n"
                f"Energia: {self.pet.energia}%\n"
                f"Hambre: {self.pet.hambre}%\n"
                f"Aura: {self.pet.aura}%\n"
                f"Altitud: {self.pet.altitud}m")

    def play(self):
        self.pet.jugar()
        self.update_status()

    def feed(self):
        self.pet.comer()
        self.update_status()

    def sleep(self):
        self.pet.dormir()
        self.update_status()

    def backflip(self):
        self.pet.backflip()
        self.update_status()

    def fly(self):
        self.pet.volar()
        self.update_status()

    def update_status(self):
        self.status.set(self.get_status())

if __name__ == "__main__":
    root = Tk()
    app = VirtualPetApp(root)
    root.mainloop()