<h1 align="center"> Microscopio Confocal: Una adaptación del microscopio de Openflexure V7 </h1>

<p>
  <img src="https://img.shields.io/github/languages/top/SebasM2000/Confocal_microscope_Openflexure_adaptation?style=flat&logo=python&color=green&logoColor=yellow&link=https%3A%2F%2Fwww.python.org" alt="GitHub top language">
  <img src="https://img.shields.io/github/license/SebasM2000/Confocal_microscope_Openflexure_adaptation?label=Licencia&labelColor=gray&color=yellow" alt="GitHub License" >
  <img src="https://img.shields.io/badge/Estado-En%20Desarrollo-blue" alt="Status: In Development">
</p>

<p> En este proyecto se adaptó la versión 7 del microscopio de alta resolución de <a href="https://build.openflexure.org/openflexure-microscope/v7.0.0-beta2/">Openflexure</a> a un microscopio confocal, el cual se controla desde una interfaz desarrollada en Python. Este microscopio tiene la capacidad de formar imágenes bidimensionales y volumétricas, gracias a que el código realiza un procesamiento de imágenes que las almacena en una carpeta especificada por el usuario. Este proyecto se realizó como una tesis de pregrado/licenciatura de Física en el Instituto Interdisciplicario de las Ciencias (IIC) de la Universidad del Quindío, por lo que toda la documentación y el mismo escrito de la tesis (en español) se proporcionan en este repositorio. </p>

<h2> Descripción del proyecto </h2>
<p> El enfoque de este proyecto es crear una interfaz de usuario para el Laboratorio de Acusto-óptica y Radiometría del Instituto Interdisciplinario de las Ciencias, el cual hace parte de la Universidad del Quindío (Colombia). Por lo anterior, pese a que el README principal esté en inglés, todos los documentos en este repositorio, así como las entradas, texto y etiquetas de la interfaz, están en español. No se descarta añadir otros idiomas para una mejor accesibilidad a nivel globar, no obstante, ¡se invita a los usuarios que clonen este repositorio a adaptarlo a su lengua materna! :D. </p>

<h2> Características </h2>

<p> Aunque se haya utilizado el microscopio de Openflexure como referencia, este microscopio funciona de manera completamente diferente. A continuación, se listan los cambios más significativos: </p>

<ul>
    <li> Medición de imagen automática. </li>
    <li> Creación de imágenes 2D y 3D. </li>
    <li> Utiliza un láser como fuente de iluminación puntual. </li>
    <li> Utiliza el modo de reflexión para la toma de imágenes. </li>
    <li> Se invirtió completamente la estructura del microscopio. </li>
    <li> Se añadió una lente adicional y dos estenopos al montaje. </li>
    <li> Se controla desde una interfaz diferente, desarrollada en Python. </li>
</ul>

<h2> Tecnologías utilizadas </h2>
<p> El código del proyecto está construido principalmente en Python y una pequeña parte en lenguaje C para el control de los componentes conectados al Arduino. A continuación, se describen las librerías de Python y su versión correspondiente utilizadas: </p>

<ul>
  <li> Numpy 1.23.2 </li>
  <li> Tkinter 1.3.3 </li>
  <li> OpenCV 4.6.0.66 </li>
  <li> Pyserial 3.5 </li>
</ul>

<h2> Funcionalidades </h2>
<p> En esta sección se explican, de manera detallada, las características de la interfaz de usuario y del procesamiento de imágenes. Considerando el estado actual del proyecto, esta sección se irá actualizando a medida que se vayan añadiendo, modificando o eliminando características.</p>

<h3> Interfaz de Usuario </h3>
<p> La interfaz de usuario consta de dos ventanas: la ventana de bienvenida, en la cual el usuario ingresa sus datos básicos; la ventana de control, cuya función es controlar el estado del láser, la posición de los motores y la medición del microscopio para producir imágenes. Por lo tanto, en esta subsección se mostrará cada ventana junto con varias marcas en las que se explicará su función. </p>

<h4> Ventana de Bienvenida </h4>
<h4> Ventana de Control </h4>
<p> Descripción más detallada cuando se haga la optimización del código. </p>