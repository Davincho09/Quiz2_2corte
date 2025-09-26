# Quiz2_2corte
Se pidió que a partir de unos drones, se encontrara la posición optima para hallar la mayor probabilidad de sobrevientes de un tsunami en un área de 5x5km.

Cada partícula del PSO es una configuración distinta de 10 drones distribuidos en el área de búsqueda, es decirsus coordenadas. En cada iteración, el algoritmo mide qué tan buena es esa configuración usando la función fitness qué tanto cubren los drones las zonas del mapa con mayor probabilidad de sobrevivientes. El PSO va ajustando las posiciones de los drones (como si fueran un “enjambre” que busca la mejor estrategia) durante las 50 iteraciones:

Iteración 1/50 -> Mejor resultado: 73.30793861540394
Iteración 2/50 -> Mejor resultado: 73.30793861540394
Iteración 3/50 -> Mejor resultado: 73.30793861540394
Iteración 4/50 -> Mejor resultado: 73.45744184971652
Iteración 5/50 -> Mejor resultado: 73.45744184971652
Iteración 6/50 -> Mejor resultado: 74.37020982737594
Iteración 7/50 -> Mejor resultado: 74.37020982737594
Iteración 8/50 -> Mejor resultado: 74.80751094249696
Iteración 9/50 -> Mejor resultado: 74.80751094249696
Iteración 10/50 -> Mejor resultado: 74.80751094249696
Iteración 11/50 -> Mejor resultado: 74.80751094249696
Iteración 12/50 -> Mejor resultado: 74.80751094249696
Iteración 13/50 -> Mejor resultado: 74.80751094249696
Iteración 14/50 -> Mejor resultado: 74.80751094249696
Iteración 15/50 -> Mejor resultado: 74.80751094249696
Iteración 16/50 -> Mejor resultado: 74.80751094249696
Iteración 17/50 -> Mejor resultado: 74.80751094249696
Iteración 18/50 -> Mejor resultado: 74.80751094249696
Iteración 19/50 -> Mejor resultado: 75.46069428142525
Iteración 20/50 -> Mejor resultado: 75.48643464091569
Iteración 21/50 -> Mejor resultado: 75.48643464091569
Iteración 22/50 -> Mejor resultado: 75.48643464091569
Iteración 23/50 -> Mejor resultado: 75.58815412996908
Iteración 24/50 -> Mejor resultado: 75.59529608438338
Iteración 25/50 -> Mejor resultado: 75.64452153406557
Iteración 26/50 -> Mejor resultado: 75.64452153406557
Iteración 27/50 -> Mejor resultado: 76.17310293364312
Iteración 28/50 -> Mejor resultado: 76.45292832346368
Iteración 29/50 -> Mejor resultado: 76.45292832346368
Iteración 30/50 -> Mejor resultado: 76.45292832346368
Iteración 31/50 -> Mejor resultado: 76.45292832346368
Iteración 32/50 -> Mejor resultado: 76.45292832346368
Iteración 33/50 -> Mejor resultado: 76.45292832346368
Iteración 34/50 -> Mejor resultado: 76.45292832346368
Iteración 35/50 -> Mejor resultado: 76.45292832346368
Iteración 36/50 -> Mejor resultado: 76.51154060319084
Iteración 37/50 -> Mejor resultado: 76.51154060319084
Iteración 38/50 -> Mejor resultado: 76.51154060319084
Iteración 39/50 -> Mejor resultado: 76.6646004287914
Iteración 40/50 -> Mejor resultado: 76.6646004287914
Iteración 41/50 -> Mejor resultado: 76.6646004287914
Iteración 42/50 -> Mejor resultado: 76.6646004287914
Iteración 43/50 -> Mejor resultado: 77.99066485325878
Iteración 44/50 -> Mejor resultado: 77.99066485325878
Iteración 45/50 -> Mejor resultado: 77.99066485325878
Iteración 46/50 -> Mejor resultado: 77.99066485325878
Iteración 47/50 -> Mejor resultado: 77.99066485325878
Iteración 48/50 -> Mejor resultado: 77.99066485325878
Iteración 49/50 -> Mejor resultado: 77.99066485325878
Iteración 50/50 -> Mejor resultado: 77.99066485325878

Al final, se obtiene una distribución óptima de los drones que maximiza la probabilidad de encontrar sobrevivientes en el menor tiempo posible. Dicha optimización se grafica en el área de 5 x 5 km para visualizar la posición final y óptima de los drones en función a la probabilidad encontrada en las 50 iteraciones.

En otras palabras, lo desarrollado para encontrar las mejores posiciones de los drones, se aplicaron varias condiciones acorde al ejercicio:

-Se define un cuadrado de 5 km × 5 km  es decir 5000 × 5000 metros. Ese espacio se divide en una grilla de 50 × 50 y cada celda representa una parte del terreno.

-en la misma área creada, no todas las zonas tienen la misma probabilidad de sobrevivientes por lo que el código genera un mapa aleatorio (np.random.rand), pero en la realidad se puede basar ya sean lugares donde había población, zonas altas o con refugios, reportes de emergencia. Entre otros ejemplos.

-Se tienen 10 drones que se pueden ubicar en cualquier coordenada del área, cada uno tiene un radio de detección de 200 metros, simulando su sensor para encontrar señales de vida. En la función fitness, cada dron cubre un “círculo” de detección en parte de su área.

-El algoritmo arranca con varias configuraciones aleatorias, es decir un total de 30 partículas. En cada iteración calcula qué tan buena es la configuración (fitness), guarda la mejor posición personal de cada partícula (pbest), la mejor posición global del enjambre (gbest). También ajusta las posiciones con base en inercia, atracción hacia su mejor posición **personal y global**.

-El algoritmo maximiza la **probabilidad** de sobrevivientes gracias a la función fitness. Es decir, suma todas las probabilidades de las zonas que quedaron dentro del rango de detección de algún dron, Cuanto más zonas de alta probabilidad cubren los drones, mejor es el fitness, esto es aplicado en las 50 iteraciones mostradas anteriormente.

-Finalmente se muestra el plano del área a buscar, con las posiciones más óptimas de los drones y la probabilidad de sobrevivientes representado en colores rojizos, cuanto más claro sea el cuadro, mayor probabilidad hay de que haya sobrevivientes en esa zona.

### Qué pasaria si las iteraciones tuvieran el total de 120 minutos?

Si en cada iteración los drones escanean más terreno, la función fitness podría mejorar porque cada dron tiene chance de cubrir más celdas. No obstante, el objetivo de encontrar la mayor probabilidad de sobrevivientes en el menor tiempo posible, quedaría afectado, dado que si se toman 50 iteraciones dentro de esas 2 horas, pueden terminar afectando la probabilidad final dado un tiempo pasado.

Eso sí, la maximización de la función fitness **se mantendría* ya que siempre busca el mejor resultado de esta, más si no llega a encontrar un mejor resultado que el anterior un tiempo después, la probabilidad nunca aumentaría con el pasar del tiempo.


