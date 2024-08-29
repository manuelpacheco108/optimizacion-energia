import matplotlib.pyplot as plt

def graficar_consumo(consumos, nombres):
    fig, ax = plt.subplots()  # Crear una figura y un eje
    ax.bar(nombres, consumos)
    ax.set_xlabel('Dispositivos')
    ax.set_ylabel('Consumo Energético (kWh)')
    ax.set_title('Consumo Energético de Dispositivos')
    return fig  # Devolver la figura en lugar de guardarla en un archivo
