import tkinter as tk
from tkinter import ttk
import moduloCalculo
import visualizacionDatos
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from io import BytesIO

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Consumo Energético 💡")
        
        # Listas para guardar las figuras y datos
        self.figuras = []
        self.datos_registrados = []
        
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

    def exportar_pdf(self):
        c = canvas.Canvas("reporte_consumo.pdf", pagesize=letter)
        width, height = letter

        for figura, datos in zip(self.figuras, self.datos_registrados):
            # Guardar la figura en un objeto BytesIO en formato PNG
            buf = BytesIO()
            figura.savefig(buf, format='png')
            buf.seek(0)  # Mover al inicio del objeto BytesIO
            
            # Convertir el objeto BytesIO a ImageReader
            image = ImageReader(buf)
            
            # Ajustar la posición y tamaño de la imagen en el PDF
            c.drawImage(image, 0, height - 400, width=width, height=300)
            
            # Añadir los datos correspondientes debajo de la gráfica
            c.drawString(100, 400, f"Dispositivo: {datos['dispositivo']}")
            c.drawString(100, 380, f"Horas de uso: {datos['horas']}")
            c.drawString(100, 360, f"Consumo: {datos['consumo']:.2f} kWh")
            c.drawString(100, 340, f"Costo: ${datos['costo']:.2f}")
            
            # Añadir nueva página si hay más gráficas
            c.showPage()
        
        # Guardar el PDF
        c.save()

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

        # Botón para exportar el PDF
        self.button_exportar_pdf = tk.Button(self.root, text="Exportar a PDF 📄", command=self.exportar_pdf)
        self.button_exportar_pdf.pack()

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
                
                # Registro de datos
                self.datos_registrados.append({
                    "dispositivo": dispositivo_seleccionado,
                    "horas": horas_uso,
                    "consumo": consumo,
                    "costo": costo
                })
                
                self.label_resultado.config(text=f"Consumo: {dispositivo_seleccionado}  {consumo:.2f} kWh\nCosto: ${costo:.2f}")
                self.actualizar_grafica()
                break 
               
        
    def actualizar_grafica(self):
        consumos = [d.consumo_energia(float(self.entry_horas.get())) for d in self.dispositivos]
        nombres = [d.nombre for d in self.dispositivos]

        # Obtener la figura desde visualizacionDatos y almacenarla en self.figuras
        figura = visualizacionDatos.graficar_consumo(consumos, nombres)
        self.figuras.append(figura)

        # Mostrar la gráfica generada
        figura.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
