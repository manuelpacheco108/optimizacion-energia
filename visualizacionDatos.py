import matplotlib.pyplot as plt

def graficar_consumo(consumos, nombres, filename='grafica.png'):
    plt.bar(nombres, consumos)
    plt.xlabel('Dispositivos')
    plt.ylabel('Consumo Energético (kWh)')
    plt.title('Consumo Energético de Dispositivos')
    plt.savefig(filename)  # Guardar la gráfica como imagen
    plt.close()
