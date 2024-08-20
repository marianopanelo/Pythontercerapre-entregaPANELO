Cabañas Altas Cumbres
Este proyecto es un sistema de reservas de cabañas desarrollado en Django. Permite a los usuarios realizar y gestionar reservas de cabañas en la montaña.

Características:
Búsqueda de Reservas: Los usuarios pueden buscar sus reservas utilizando un código 
Creación de Reservas: Posibilidad de realizar nuevas reservas, especificando detalles como la fecha de entrada y dias en los cuales se van a hospedar,visualizar el precio que les saldria 
Visualización de Detalles: Los usuarios pueden ver los detalles de sus reservas realizadas con el codigo generado.

Instalación:
Clona este repositorio:
git clone https://github.com/marianopanelo/Pythontercerapre-entregaPANELO.git

crea la carpeta entorno-virtual con 
python -m venv entorno-virtual

habrir una terminal de la nueva carpeta y activar el entorno virutal con source Scripts/activate
(en la terminal tendria que aparecer (entorno-virtual))

crea el archivo requirements.txt con
pip freeze > requirements.txt

en la carpeta , como minimo tiene que estar 
#Python 3.11.9 (esta es la version de Python en la que se creo el proyecto)
django==5.0.7 (la version de django utilizada)

ya estaria esta parte, ahora veamos la base de datos
si no se creo la base de datos correctamente (db.sqlite3), con
las tablas creadas en models.py ejecutar en la terminal donde esta el proyecto guardado usar
python manage.py migrate

ahora solamente falta correr el servidor , en la carpeta donde este el proyecto ejecuta
python manage.py runserver
al ejecutar este codigo se generada el http://127.0.0.1:8000/
y te permitira navegar en la aplicacion

una vez finalizado cierra el entorno virtual con deactivate

Navegación de la Aplicación
nicio: Contiene un pequeño comentario sobre los dueños del lugar.
Login: Permite almacenar los datos del usuario.
Nuestras Cabañas: Muestra una foto de la cabaña junto con el precio y los servicios ofrecidos.
Reservar: Permite almacenar una reserva en la base de datos, especificando la fecha de entrada y el número de días. Luego de un login exitoso, te redirige a una página con los detalles de la reserva y el precio a pagar.
Tus Reservas: Permite al usuario, utilizando el código generado, ver los detalles de su reserva. Esta es la misma página que se muestra después de realizar una reserva.
Coméntanos: Un espacio para que los huéspedes dejen comentarios sobre su estancia.

herramientras utilizadas
Django
Python
ChatGPT-4: Se utilizó para corregir algunas líneas de código y resolver dudas durante el desarrollo del proyecto.
Leonardo.ai: Se utilizó para las fotos de las cabañas y para la foto de los dueños en la página de inicio.

futuras lineas
Generar códigos de reserva únicos para evitar duplicados en la base de datos.
Implementar la funcionalidad para eliminar reservas.
Agregar más imágenes de las cabañas.
Permitir la actualización de reservas.
Incluir la capacidad de registrar cuántas personas se hospedarán en la cabaña.

