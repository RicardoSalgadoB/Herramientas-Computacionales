# Modificación al Juego de la Serpiente/Víbora/Culebra

El juego usado para la evidencia de está semana TEC fue el juego de la serpiente. Como se explica en el vídeo, existen distintas versiones del juego, por ejemplo, la versión de [Google](https://www.google.com/search?q=snake&sourceid=chrome&ie=UTF-8) y la versión de [FreeGames](https://grantjenks.com/docs/freegames/snake.html) en Python. Claramente, la segunda es mucho más simplona que la primera lo que significa que se puede tomar inspiración de la primera para mejorar la segunda, esto es justo lo que se hace en este proyecto.

Las siguientes son algunas de las características que se agregaron a la versión de *Freegames* (para los detalles de implementación veáse el código), en general, los cambios de Interfaz y cambios de Experiencia de Usario:

**Cambios de Interfaz de Usario (UI)**
* Se añadio un *tablero cuadrículado*
* El *color de la serpiente* y el *color del tablero* son distintos en cada partida

**Cambios de Experiencia de Usuario (UX)**
* *Tamaño del mapa variable* a partir de input del jugador.
* *Modificar velocidad de la serpiente* hasta un máximo de 2 celdas por segundos
* *Distintos tipos de frutas* que
    * *Aumentan el crecimiento* de la serpiente
    * *Otorgan invulnerabilidad* a los choques por un tiempo
    * *Dan mayor velocidad*
    * *Agregan óbstaculos*
    * *Agregan enemigos* o los *detienen*
    * *Agregan paredes*

Todos estos cambios resultan en que el juego se más visualmente atractivo y más retador para el jugador. Pese a esto, se recomienda discreción respecto a posibles jugadores que sufran de epilepsia o de daltonismo, ya que hay ciertas combinaciones de colores y de parámetros que podrían resultar no del todo placenteras.