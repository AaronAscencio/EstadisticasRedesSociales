# EstadisticasRedesSociales

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

#Tecnologias implementadas

Boostrap 4
Jquery
Ajax
Django
PostgreSQL

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
