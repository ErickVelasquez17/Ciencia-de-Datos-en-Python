# Introducción a GIT

## Origen de  GIT

Git es un proyecto de código abierto desarrollado por Linus Torvalds en el 2005 y actualmente es uno de los VCS (*Sistema de control de versiones*) mas populares del mercado, según estimaciones cerca del 87% de los desarrolladores utilizan Git para sus proyectos, lo que la hace una de las herramientas mas importantes para el control de versiones. Para explicar un poco la utilidad de Git, anteriormente al trabajar en un proyecto alcanzábamos una versión "Final" a la cual le colocábamos como nombre, por ejemplo *"Entregable Final"*, pero resulta que el cliente nos pide una modificaciones y luego de esto terminábamos llamando al archivo *"Entregable Final Final"* y así sucesivamente. Otro ejemplo para nombrar estas versiones es colocarle las fechas al inicio pero si no se hace correctamente el orden de las versiones no suele ser el correcto, y esto se complica mucho mas cuando colaboramos con otros programadores. Una de las plataformas mas conocidas para alojar los repositorios Git es **GitHub** alojando mas de **100 millones** de repositorios.

![Esta es una imagen](https://global-uploads.webflow.com/5f5a53e153805db840dae2db/6073fbf151fa4565d48572dc_GitHub_aprender-programaci%25C3%25B3n.jpeg)

Git se ha diseñado teniendo en cuenta el rendimiento, la flexibilidad y la seguridad, permitiendo colaborador facilmente entre varios programadores y trabajando en distintas versiones que en Git se denominan *Ramas* hasta tener una versión original y combinar esta con la última versión trabajada, a esto se le conoce como **Ramificación** y **Fusión**. 

## Seguridad

Con Git se puede tener la certeza de contar con un autentico historial de contenido del código fuente. El contenido de los archivos, relaciones entre estos y las direcciones y versiones estan protegidos con un algoritmo de *Hash Criptográficamente seguro* llamado **SHA1**, lo que garantiza que que todo el historial sea totalmente trazable y de esta manera salvaguarda el código y el historial de cambios frente a modificaciones accidentales y maliciosas. 

## Control de Versiones
Este es un sistema que permite rastrear y gestionar cambios realizados en un archivo o conjunto de archivos, con el objetivo de dar seguimiento de las modificaciones realizadas en el código fuente. El sistema de control de versiones permite analizar todos los cambios y revertirlos sin repercusiones si se llegará a cometer un error. En pocas palabras, el control de versiones permite hacer todos los cambios que se necesiten sin infringir o retrasar el trabajo de los demas colaboradores. 

## Actualidad

Git es la herramienta de mayor uso de su clase por lo que es muy atractiva por diferentes razones:
*	La mayoria de proyectos de gestionan en Git
*	Un gran número de desarrolladores tienen experiencia en Git. 
*	Es la herramienta mas popular que se enseñan en las universidades. 
*	Muchos servicios y herramientas de software de terceros ya estan integrados con Git. 
*	Git es un proyecto de Código Abierto de gran fiabilidad. 

# Tutorial
A continuación se mostrará un pequeño tutorial utilizando la herramienta **GitHub** para crear la cuenta y crear un repositorio para empezar a trabajar: 

### 1. Logearse en GitHub

Lo primero es buscar **GitHub** en google y acceder por el primer link:

![Prueba](https://pouch.jumpshare.com/preview/Wsolh2Yi6JKrTla-m5P7vzoXT00BdBkdvuK60_mtU2-lh9KmvctPtDE9vh2bP_PFfgrWk09xqAsd8ui6Gts_SBA1jQB_zmxltR5bgJ1-nls)

### 2. Registro

En la parte superior derecha nos aparece la opción para registrarnos:

![Imagen2](https://pouch.jumpshare.com/preview/DlHk1vm9R0Py0yj6Q6BPCcTS4kpuvejUoW1u6IJ1stI2xzA_Ya62C7OqPLGuqv5J3Tam47cfQV49xlpdSirJQxA1jQB_zmxltR5bgJ1-nls)
 y debemos de completar los datos para completar el registro: 
![magen 3](https://pouch.jumpshare.com/preview/NG95ggz-_4F7b9ZzFReRugaHKXWRpvKFT5RPTLRgA1G08QN0Pfrls9NBQEZgr1DrxdH6bHAO51uZdLq00ErxGhA1jQB_zmxltR5bgJ1-nls)

### 3. Crear Repositorio

Un repositorio es el eje central de todo proyecto, este será el lugar donde alojaremos los archivos que pueden contener código, imágenes, texto, etc.  Para esto podemos seleccionar en nuestro perfil el botón de "+" que esta en la parte superior derecha de la pantalla y luego seleccionar **New Repository**

![Imagen 4](https://pouch.jumpshare.com/preview/zZbxzODVYyFwsDa_GInWPsP5D5DOuOBXRX8-JClVkhBLKe0MGHAFXHlq09GyK6TLxVcrbDEblRlzHVescjVt6xA1jQB_zmxltR5bgJ1-nls)

Y luego debemos de seleccionar si nuestro repositorio será público o privado y seleccionar la opción de *Add a Readme file*

![Imagen 5](https://pouch.jumpshare.com/preview/CBeg036x3KVsW0Cw8D_lxJSVfjAlfUPdC7YFnC6L4mIgXj-pWi4-dtpOEpmQQSpdczDDYFsUQMOCH2hMu7nHnBA1jQB_zmxltR5bgJ1-nls)

### 4. Crear Ramas

Con la creación de ramas, se generarán diferentes versiones en nuestro proyecto y de esta manera cualquier colaborador podrá ver como afectará al proyecto maestro cuando se integre. Para esto debemos de ir a nuestro repositorio y en el botón **main** indicar el nombre que deseamos colocarle a nuestra rama y luego dar clic en **Create Branch**:

![Imagen 6](https://pouch.jumpshare.com/preview/8sl4Tyxp-VzepY4Ch60Wcj6hyoe0rP7ze2OyU666-6gt9rUqKxUjxlsHWQsvykFmo278twf0r1BWlZQBmjVHhRA1jQB_zmxltR5bgJ1-nls)

### 5. Versiones

Como se menciono al inicio, una de las cualidades de trabajar con Git es el control de versiones, este lo podemos consultar en cualquier momento donde van quedando registro de todos las modificaciones que se realicen en nuestro proyecto:

![Imagen 7](https://pouch.jumpshare.com/preview/g1oI_x17GB1arv7IZuPr70dwjMRqIBX6KofSvGE6dH0iEeSDKWmiVR30aKFNgP648QgaSshijBkOi-eo26dJbRA1jQB_zmxltR5bgJ1-nls)

### 6. Carga y Creación de Archivos

Ya en nuestro repositorio, podemos colaborar cargando o crear archivos según nuestra necesidad.
![Imagen 8](https://pouch.jumpshare.com/preview/-yzJmoogQpBmYJ_axS1BYLgO_u8DOmYUrO-VLrxTKZEBCc9Z_aHAT50Z0Bk_VKr-7xWCs0jTmfBoWdXE-i122RA1jQB_zmxltR5bgJ1-nls)

##### Referencias:

> Guía de Inicio de GitHub. Disponible en: 
> https://docs.github.com/en/get-started/quickstart/hello-world
> Tutorial de Github. Disponible en: 
> https://www.hostinger.es/tutoriales/que-es-github
> ¿Que es Git? Disponible en:
> https://www.atlassian.com/es/git/tutorials/what-is-git
> 


