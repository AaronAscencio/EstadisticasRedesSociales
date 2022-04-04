# EstadisticasRedesSociales

Autor: Ascencio Mata Aaron 

Live Demo: https://redessocialesestadisticas.herokuapp.com/

# Problematica
Generar una web para llenado de una encuesta sobre uso de redes sociales, 
dicho cuestionario deberá tener mínimo las siguientes preguntas:

• Correo del participante

• Edad, seleccionable de 4 rangos, ejemplo: 18-25, 26-33, 34-40, 40+

• Sexo

• Red social favorita 

• Tiempo promedio al día en Facebook

• Tiempo promedio al día en WhatsApp

• Tiempo promedio al día en Twitter

• Tiempo promedio al día en Instagram

• Tiempo promedio al día en Tiktok


La aplicación web adicionalmente deberá contar con un apartado de estadísticas donde se pueda ver al 
menos:
• Cantidad de encuestas respondidas

• Tiempo promedio por red social

• Red social favorita

• Red social menos querida

• Rango de edad que más use cada red social (ejemplo: Facebook entre 18-25 e Instagram entre 
26-33)

# Tecnologias implementadas

-Boostrap 4

-Jquery

-Ajax

-Django

-PostgreSQL


Bibliotecas implementadas:

-Gunicorn

-dj-static

-Chartjs

-SweetAlert



# Guia  de Instalacion 

1. Descargar o clonar el repositorio
2. Instalar las bibliotecas (pip install -r requirements.txt)
3. Cambiar la configuracion de forma local (modificar los archivos manage.py y wsgi.py)
4. Adecuar la conexion de la base de datos (Entrar a la carpeta "Project", "Setting") en el archivo "base.py"
5. Correr el comandos en la consola:
   "python manage.py makemigrations"
   "python manage.py migrate"
   "python manage.py createsuperuser"
   **NOTA Ingresar los datos para crear un super usuario
   "python manage.py runserver"
6. Ingresar al administrador de Django http://localhost:8000/admin
7. Crear las siguientes Sociales:
  -Facebook
  -Whatsapp
  -Twitter
  -Instagram
  -Tiktok
  -Otra
8. Una vez creadas, podemos ingresar al dashboard localhost:8000/

# Consideraciones 
1. Solo se permite un correo por encuesta
2. La entrada del promedio por cada red social es en decimal por ejemplo 4.5 = 4 horas con 30 minutos

# Capturas de Pantalla

1. Pantalla principal
[![Index.jpg](https://i.postimg.cc/ZKk7Z8yQ/Index.jpg)](https://postimg.cc/K4NrDgf7)

2. Formulario para el llenado de la encuesta
[![Formulario.jpg](https://i.postimg.cc/RZvzC5n2/Formulario.jpg)](https://postimg.cc/Mv3LtL5Y)

3. Validaciones en el formulario 

3.1 Validacion si el usuario ha ingresado un texto en el campo de correo
[![validaciones1.jpg](https://i.postimg.cc/xdWxCM4q/validaciones1.jpg)](https://postimg.cc/rdNCZ0cL)

3.2 Validacion si el correo es valido
[![validaciones2.jpg](https://i.postimg.cc/mZSjxvBP/validaciones2.jpg)](https://postimg.cc/jCLPPkWT)

3.3 Validacion de tiempos mayores a 0 horas
[![validaciones3.jpg](https://i.postimg.cc/T2ZD4QWK/validaciones3.jpg)](https://postimg.cc/t7NJ13kb)

4 Mensaje de Exito al enviar una encuesta (Si el formulario es valido)
[![Mensaje-de-Exito.jpg](https://i.postimg.cc/FFcR7v7K/Mensaje-de-Exito.jpg)](https://postimg.cc/CdhYQWCy)

5 Alerta de error si el correo ya ha sido ingresado
[![Error-correo-duplicado.jpg](https://i.postimg.cc/VLL32BQc/Error-correo-duplicado.jpg)](https://postimg.cc/23McZWSH)
