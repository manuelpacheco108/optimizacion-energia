# Desarrollo de interfaz gráfica
import tkinter as tk
from tkinter import ttk
import moduloCalculo
import visualizacionDatos
from fpdf import FPDF
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Consumo Energético 💡")

        # Configuración de dispositivos
        self.dispositivos = [
            moduloCalculo.Dispositivo("Lámpara LED", 10, "Luz"),
            moduloCalculo.Dispositivo("Refrigerador", 300, "Luz"),
            moduloCalculo.Dispositivo("Televisor", 200, "Luz"),
            moduloCalculo.Dispositivo("Aire Acondicionado", 2000, "Climatización"),
            moduloCalculo.Dispositivo("Microondas", 850, "Calentador"),
            moduloCalculo.Dispositivo("Portátil", 190, "Dispositivo Electrónico"),
            moduloCalculo.Dispositivo("Celular", 15, "Dispositivo Electrónico")
        ]

        # Widgets de la interfaz
        self.create_widgets()

    def exportar_a_pdf(self, consumos, nombres, filename='reporteDatos.pdf'):
        pdf = FPDF()
        pdf.add_page()

        # Título
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Reporte de Consumo Energético", ln=True, align='C')

        # Agregar el contenido
        pdf.ln(10)
        for nombre, consumo in zip(nombres, consumos):
            pdf.cell(200, 10, txt=f"{nombre}: {consumo:.2f} kWh", ln=True)

        # Agregar la gráfica
        pdf.image('grafica.png', x=10, y=None, w=pdf.w - 20)

        # Guardar el PDF
        pdf.output(filename)

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
        self.label_resultadoTotal = tk.Label(self.root, text="")
        self.label_resultadoTotal.pack()

    def calcular_consumo(self):
        dispositivo_seleccionado = self.combo_dispositivo.get()
        horas_uso = float(self.entry_horas.get())
    
        consumos = []
        nombres = []
        consumoTotal = 0
        costoTotal = 0
    
        for dispositivo in self.dispositivos:
            if dispositivo.nombre == dispositivo_seleccionado:
                consumo = dispositivo.consumo_energia(horas_uso)
                costo = dispositivo.costo_energia(horas_uso)
                self.label_resultado.config(text=f"Consumo: {dispositivo_seleccionado}  {consumo:.2f} kWh\nCosto: ${costo:.2f}")
        
        # Acumular los consumos y nombres para el total
            consumos.append(dispositivo.consumo_energia(horas_uso))
            nombres.append(dispositivo.nombre)
            consumoTotal += dispositivo.consumo_energia(horas_uso)
            costoTotal += dispositivo.costo_energia(horas_uso)

    # Mostrar el resultado total
        self.label_resultadoTotal.config(text=f"Consumo Total: {consumoTotal:.2f} kWh\nCosto Total: ${costoTotal:.2f}")

    # Actualizar la gráfica y guardarla
        self.actualizar_grafica()

    # Exportar los resultados y la gráfica a un PDF
        self.exportar_a_pdf(consumos, nombres)
    
    def actualizar_grafica(self):
        consumos = [d.consumo_energia(float(self.entry_horas.get())) for d in self.dispositivos]
        nombres = [d.nombre for d in self.dispositivos]
        visualizacionDatos.graficar_consumo(consumos, nombres, 'grafica.png')

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()