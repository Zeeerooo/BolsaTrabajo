DataBase (van en el archivo setup)
    name: bolsadetrabajo
    user: datosbolsa
    pass: losdatosestanseguros

WIKI:

MySQL:
Instale primero mysql: sudo apt-get install mysql-server
Luego, setear password de usuario root de mysql.
Entrar a mysql como root; mysql -u root -p<password> (junto!)
Aquí, crear base de datos: CREATE DATABASE bolsadetrabajo;
Crear usuario para la bd: CREATE USER datosbolsa;
Darle privilegios a ese usuario sobre la bd de la bolsa: grant all on bolsadetrabajo.* to 'datosbolsa'@'localhost' identified by 'losdatosestanseguros';

Django:
Instalar primero pip : sudo apt-get install python-pip
Luego instalar django: sudo pip install django
Pueden probar la versión con: python -c "import django; print(django.get_version())" (yo estoy usando la 1.6.2, ojo que son super distintos algunos comandos!)
Por último instalar la aplicación que relaciona python con mysql: sudo apt-get install python-mysqldb

Ahora, hacer syncdb con: pyhton manage.py syncdb
Al crear el super usuario, usar los siguientes valores:
Username: cadcc2014
Email: directiva@cadcc.cl
password: cumpliendopromesas2014

Comandos utiles django:
- python manage.py runserver
Corre un servidor local con al aplicación. Si le agregan 0.0.0.0.0:8000, corre visible para la red LAN donde se encuentren en el puerto 8000 de su pc.
