# Python-Proyecto-Final
**Link al video**
https://www.youtube.com/watch?v=icxxvvRE870

Este proyecto tiene una app llamada blog, justamente se trata de mi propio blog en el cual las personas pueden agregar artículos.

La app cuenta con 7 modelos y 4 propios de esta entrega y que se implementan
* Usuario 
* Creador
* Espectador
* Avatar
* Article
* Profile_data
* Mensajes

Siguiendo la consigna arme todo para que se pueda acceder desde el home a las vistas. 
En el home hay acceso directo mediante links a los artículos, contacto, mensajes, agradecimientos, login y about.


**Pruebas-unitarias**
---------------------------------------
---------------------------------------

* **Nro Prueba:** 1
* **Acción:** Click en la foto de "articulos"
* **Resultados esperados:** Redireccione a la página con todos los artículos y en el caso de no ser usuario no mostrar el "añadir artículo"
* **Resultados actuales:** Redireccionado a la página y al no ser usuario no mostró el añadir artículo
* **Estado:** Aprobado
_____________________________________________________

* **Nro Prueba:** 2
* **Acción:** Iniciar sesión
* **Resultados esperados:** Muestre una página de bienvenida y donde antes estaba la palabra login ahora diga el nickname del usuario y al lado Logout
* **Resultados actuales:** Aparece una página de bienvenida que dice Bienvenido y el nickname del usuario y donde antes estaba la palabra login ahora aparece el nickname del usuario y al lado Logout
* **Estado:** Aprobado
_____________________________________________________

* **Nro Prueba:** 3
* **Acción:** Click en el "añadir artículo" en la pagína de los artículos
* **Resultados esperados:** Redireccione a la página con un formulario de artículos y que tenga un editor de texto enriquecido que permita poner en negrita, subrayar y etc.
* **Resultados actuales:** Redireccionado a la página con un forms y aparece el editor 
* **Estado:** Aprobado
_____________________________________________________
