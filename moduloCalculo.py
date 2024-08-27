# Módulos de cálculos de energía

class Dispositivo:
    def __init__(self, nombre, potencia, tipo):
        self.nombre = nombre
        self.potencia = potencia  # W
        self.tipo = tipo  # Tipo de dispositivo
    
    def consumo_energia(self, horas_uso):
        return (self.potencia / 1000) * horas_uso  # kWh
