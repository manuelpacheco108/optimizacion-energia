# Módulos de cálculos de energía

class Dispositivo:
    def __init__(self, nombre, potencia, tipo, descripcion=""):
        self.nombre = nombre
        self.potencia = potencia  # W
        self.tipo = tipo  # Tipo de dispositivo
        self.descripcion = descripcion
        self.tarifa_energia = 739 
    
    def consumo_energia(self, horas_uso):
        consumo = (self.potencia / 1000) * horas_uso
        return consumo  # kWh
    
    def costo_energia(self, horas_uso):
        consumo = self.consumo_energia(horas_uso)
        return consumo * self.tarifa_energia # Costo

