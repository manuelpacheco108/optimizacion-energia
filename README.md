# optimizacion-energia
Proyecto de física para la universidad del Tecnológico de Antioquia, Medellín
# Autores
Manuel Pacheco, Juliana Torres, Juan Arce, Kelly Salgado

La aplicación es una herramienta interactiva diseñada para calcular el consumo energético de dispositivos eléctricos, basado en la energía cinética generada por una persona al correr o andar en bicicleta.

Ingreso de datos: El usuario ingresa su masa, el tiempo en horas que ha estado corriendo o andando en bicicleta, y la velocidad en km/h.
Cálculos automáticos: Basado en los datos ingresados, la aplicación calcula la energía cinética generada y estima cuántas horas se podría utilizar un dispositivo eléctrico específico con esa energía.
Visualización: Muestra una gráfica del tiempo de uso estimado para el dispositivo seleccionado. Adicionalmente, se pueden generar múltiples gráficas con distintos dispositivos a lo largo de la sesión, y al final se puede visualizar una comparativa de todos los dispositivos seleccionados.
Exportación: Permite exportar las gráficas generadas, junto con los cálculos de energía y costo, en un archivo PDF. En la última página del PDF, se incluye una comparativa final y el costo promedio estimado de uso de los dispositivos.

# Energía Cinética
La energía cinética es la energía que un objeto tiene debido a su movimiento. La fórmula que se utiliza para calcularla es:

              Energía Cinética = (1/2) * m * v^2

Donde:

- Energía Cinética es la energía cinética en Joules.
- m es la masa del objeto en kilogramos.
- v es la velocidad en metros por segundo.

# Conversión a Energía Eléctrica:
En el caso de una bicicleta o correr, parte de la energía cinética del cuerpo podría ser convertida en energía eléctrica, por ejemplo, mediante un generador. Sin embargo, la eficiencia de esta conversión no es del 100%, ya que siempre se pierde energía debido a la fricción, el calor, y las limitaciones de los sistemas de conversión. Por lo general, la eficiencia en sistemas pequeños como bicicletas generadoras puede estar alrededor del 25-30%.

Por lo tanto, la energía eléctrica resultante será una fracción de la energía cinética generada:

              Ee =  Eficiencia * Energía Cinética

Si tomamos una eficiencia del 25% (0.25):

              Ee = 0.25 * Energía Cinética

En el caso del proyecto, la eficiencia es la misma constante del ejemplo anterior, 25% o 0.25, pues esta normalmente se encuentra entre el 20 al 30 porciento. Este valor será la energía eléctrica disponible que podrá usarse para alimentar dispositivos electrónicos.

Una vez que tenemos la energía cinética, se puede convertir a energía eléctrica en kWh utilizando la siguiente relación:

              1 kwh = 3.6 * 10^6 J

# Posibles Mejoras:

1. Ampliar la Base de Dispositivos: Agregar más dispositivos eléctricos con diferentes características, como electrodomésticos, dispositivos de entretenimiento, etc., para hacer la aplicación más completa y relevante.
2. Incluir Datos Reales y Comparaciones: Incorporar datos reales de costos de energía para que los usuarios puedan ver no solo el consumo en kWh, sino también el costo monetario de usar diferentes dispositivos durante un periodo de tiempo.
3. Agregar Funcionalidades Educativas: Incluir explicaciones sobre por qué ciertos dispositivos consumen más energía que otros, o cómo se puede reducir el consumo energético en el hogar.
4. Guardado y Exportación de Resultados: Añadir la capacidad de guardar los resultados de consumo y exportar los datos y gráficos en formatos como PDF o CSV para su análisis posterior.
# Librerías

1. Matplotlib

       pip install matplotlib
2. FPDF (Creación de archivos pdf)
   
       pip install fpdf
       pip install reportlab
4. API XM

       pip install pydataxm


* Error en el costo de la energia (Se debe calcular el costo de la energia electrica para calcular lo que costaria dadas las horas obtenidas por el usuario)
