class Dispositivo:
    def __init__(self, nombre, potencia, categoria):
        self.nombre = nombre
        self.potencia = potencia  # Potencia en vatios (W)
        self.categoria = categoria
    
    def costo_energia(self, horas_uso, precio_kWh=622.33):
        """
        Calcula el costo de energía para usar el dispositivo durante las horas indicadas.
        Asume un costo promedio por kWh (kilovatio-hora).
        """
        consumo_kWh = (self.potencia / 1000) * horas_uso  # Conversión de vatios a kilovatios y multiplicación por horas
        costo = consumo_kWh * precio_kWh  # Costo total según el precio por kWh
        return costo
