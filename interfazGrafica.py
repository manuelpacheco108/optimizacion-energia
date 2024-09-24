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
        self.root.title("Consumo Energético con Energía Cinética ⚡")

        # Listas para guardar las figuras y datos
        self.figuras = []
        self.datos_registrados = []

        # Variables para almacenar el costo total y costo promedio
        self.costo_total = 0
        self.consumo_total_horas = 0

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
            c.drawImage(image, 25, height - 400, width=width, height=300)
            
            # Añadir los datos correspondientes debajo de la gráfica
            c.drawString(100, 380, f"Energia Cinetica en kwh: {datos['energia_cinetica']} kwh")
            c.drawString(100, 360, f"Dispositivo: {datos['dispositivo']}")
            c.drawString(100, 340, f"Velocidad: {datos['velocidad']} km/h")
            c.drawString(100, 320, f"Masa: {datos['masa']} kg")
            c.drawString(100, 300, f"Horas de ejercicio: {datos['horas_ejercicio']}")
            c.drawString(100, 280, f"Horas de uso: {datos['horas_uso']:.2f}")
            c.drawString(100, 260, f"Costo: ${datos['costo']:.2f}")
            
            # Añadir nueva página si hay más gráficas
            c.showPage()

        # Comparativa final
        comparativa = visualizacionDatos.graficar_comparativa(self.datos_registrados)
        buf = BytesIO()
        comparativa.savefig(buf, format='png')
        buf.seek(0)
        image = ImageReader(buf)
        c.drawImage(image, 0, height - 400, width=width, height=300)
        
        # Calcular y mostrar el costo promedio
        
        costo_promedio = self.costo_total / len(self.datos_registrados)
        
        c.drawString(100, 350, f"\nCosto promedio de energía: ${costo_promedio:.2f}")

        c.save()

    def create_widgets(self):
        # Entrada de masa
        self.label_masa = tk.Label(self.root, text="Ingrese la masa (kg):")
        self.label_masa.pack()

        self.entry_masa = tk.Entry(self.root)
        self.entry_masa.pack()

        # Entrada de velocidad
        self.label_velocidad = tk.Label(self.root, text="Ingrese la velocidad (km/h):")
        self.label_velocidad.pack()

        self.entry_velocidad = tk.Entry(self.root)
        self.entry_velocidad.pack()

        # Selección de dispositivo
        self.label_dispositivo = tk.Label(self.root, text="Seleccione el dispositivo:")
        self.label_dispositivo.pack()
        
        self.combo_dispositivo = ttk.Combobox(self.root, values=[d.nombre for d in self.dispositivos])
        self.combo_dispositivo.pack()

        # Entrada de horas de ejercicio
        self.label_horas = tk.Label(self.root, text="Horas de ejercicio (correr/bicicleta):")
        self.label_horas.pack()
        
        self.entry_horas = tk.Entry(self.root)
        self.entry_horas.pack()

        # Botón para calcular energía cinética y consumo
        self.button_calcular = tk.Button(self.root, text="Calcular Consumo 🌩", command=self.calcular_consumo)
        self.button_calcular.pack()

        # Label para mostrar el resultado
        self.label_resultado = tk.Label(self.root, text="")
        self.label_resultado.pack()

        # Botón para exportar el PDF
        self.button_exportar_pdf = tk.Button(self.root, text="Exportar a PDF 📄", command=self.exportar_pdf)
        self.button_exportar_pdf.pack()

    def calcular_consumo(self):
        masa = float(self.entry_masa.get())
        velocidad_kmh = float(self.entry_velocidad.get())
        velocidad_ms = velocidad_kmh / 3.6  # Convertir a m/s
        horas_ejercicio = float(self.entry_horas.get())
        energia_cinetica = 0.5 * masa * (velocidad_ms ** 2) * horas_ejercicio

    # Conversión de energía cinética a kWh
        energia_kWh = energia_cinetica / (3.6e6)

        dispositivo_seleccionado = self.combo_dispositivo.get()
        for dispositivo in self.dispositivos:
            if dispositivo.nombre == dispositivo_seleccionado:
                # Calcular las horas que puede usar el dispositivo con la energía cinética
                horas_uso = energia_kWh / (dispositivo.potencia / 1000)
                
                # Usamos el método 'costo_energia' del dispositivo
                costo = dispositivo.costo_energia(horas_uso)
                
                # Registro de datos
                self.datos_registrados.append({
                    "energia_cinetica": energia_kWh ,
                    "dispositivo": dispositivo_seleccionado,
                    "velocidad": velocidad_kmh,
                    "masa": masa,
                    "horas_ejercicio": horas_ejercicio,
                    "horas_uso": horas_uso,
                    "costo": costo
                })

                self.costo_total += costo
                self.consumo_total_horas += horas_uso

                self.label_resultado.config(
                    text=f"Energía Cinética: {energia_kWh:.4f} kWh\n"
                        f"Horas de uso del {dispositivo_seleccionado}: {horas_uso:.2f}\nCosto: ${costo:.2f}")
                self.actualizar_grafica(dispositivo_seleccionado, horas_uso)
                break

    def actualizar_grafica(self, dispositivo, horas_uso):
        # Mostrar solo la gráfica del dispositivo seleccionado
        figura = visualizacionDatos.graficar_dispositivo(dispositivo, horas_uso)
        self.figuras.append(figura)
        figura.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
