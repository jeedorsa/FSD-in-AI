# Feature selection of dataset for Deep Learning and applications in computer vision.
### Jesus Eduardo Ortiz Sandoval
### Ferran Cancio Pujols
### Ph.D Student
### Universidad Tecnica Federico Santa Maria
---
En este trabajo se pretende establecer unas bases teóricas para el estudio de los datasets sinteticos en aplicaciones de deep learning, el dataset sintetico es generado a partir de un software de renderizado 3D (Adobe MAX 3DS con licencia estudiantil). A continuación podemos observar una imágen generada desde el software de renderizado 3D.
![Papas pringles cebolla)](01.jpg)
Esta imágen guarda una relación muy parecida con una foto real, ya que se hace una composición del modelamiento 3D del producto con una serie de 3000 fondos de supermercados.  
En total se obtienen 25.000 imagenes desde el software antes de comenzar a hacer el pre-procesamiento de la información.
Lo primero que vamos a realizar es la extracción de caracteristicas de estas imagenes, cada imagen con fondo controlado tiene su misma imagen (ubicación, rotación, iluminación) con fondo blanco, esto para poder realizar la segmentación para generar el dataset de entrenamiento para la aplicación de visión por computador.

Una vez que se tienen todas las bibliotecas que se pueden utilizar en nuestro programa el siguiente paso es extraer las caracteristicas de nuestra imagen respectiva, pero con fondo blanco.
![Papas pringles clasicas)](02.jpg)
