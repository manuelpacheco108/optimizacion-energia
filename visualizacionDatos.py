import matplotlib.pyplot as plt

def graficar_consumo(consumos, nombres):
    plt.figure(figsize=(10, 6))
    plt.bar(nombres, consumos, color=['blue', 'green'])
    plt.xlabel('Dispositivos')
    plt.ylabel('Consumo Energético (kWh)')
    plt.title('Consumo Energético de Dispositivos')
    plt.ylim(0, max(consumos) + 1)
    plt.show()
