# Desarrollo de interfaz gráfica
import tkinter as tk
from tkinter import ttk
import moduloCalculo
import visualizacionDatos

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Consumo Energético 💡")

        # Configuración de dispositivos
        self.dispositivos = [
            moduloCalculo.Dispositivo("Lámpara Tradicional", 60, "Luz"),
            moduloCalculo.Dispositivo("Lámpara LED", 10, "Luz")
        ]

        # Widgets de la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Selección de dispositivo
        self.label_dispositivo = tk.Label(self.root, text="Seleccione el dispositivo:")
        self.label_dispositivo.pack()
        
        self.combo_dispositivo = ttk.Combobox(self.root, values=[d.nombre for d in self.dispositivos])
        self.combo_dispositivo.pack()
        
        # Entrada de horas de uso
        self.label_horas = tk.Label(self.root, text="Horas de uso:")
        self.label_horas.pack()
        
        self.entry_horas = tk.Entry(self.root)
        self.entry_horas.pack()

        # Botón para calcular consumo
        self.button_calcular = tk.Button(self.root, text="Calcular Consumo 🌩", command=self.calcular_consumo)
        self.button_calcular.pack()
        
        # Label para mostrar el resultado
        self.label_resultado = tk.Label(self.root, text="")
        self.label_resultado.pack()

    def calcular_consumo(self):
        dispositivo_seleccionado = self.combo_dispositivo.get()
        horas_uso = float(self.entry_horas.get())
        
        for dispositivo in self.dispositivos:
            if dispositivo.nombre == dispositivo_seleccionado:
                consumo = dispositivo.consumo_energia(horas_uso)
                self.label_resultado.config(text=f"Consumo: {consumo} kWh")
                self.actualizar_grafica()
                break
    
    def actualizar_grafica(self):
        consumos = [d.consumo_energia(float(self.entry_horas.get())) for d in self.dispositivos]
        nombres = [d.nombre for d in self.dispositivos]
        visualizacionDatos.graficar_consumo(consumos, nombres)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
