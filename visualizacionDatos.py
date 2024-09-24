import matplotlib.pyplot as plt

# Gráfica para un solo dispositivo
def graficar_dispositivo(dispositivo, horas_uso):
    fig, ax = plt.subplots()
    ax.bar([dispositivo], [horas_uso])
    ax.set_xlabel('Dispositivo')
    ax.set_ylabel('Horas de uso')
    ax.set_title(f'Horas de uso del {dispositivo}')
    return fig

# Gráfica comparativa de todos los dispositivos
def graficar_comparativa(datos):
    fig, ax = plt.subplots()
    nombres = [d['dispositivo'] for d in datos]
    horas_uso = [d['horas_uso'] for d in datos]
    ax.bar(nombres, horas_uso)
    ax.set_xlabel('Dispositivos')
    ax.set_ylabel('Horas de uso')
    ax.set_title('Comparativa de Horas de Uso')
    return fig
