python-mvc-lite
===============

Autor: Leonardo López
Twitter @HijinLópez


El proyecto trata de lo siguiente:

    Crear aplicaciones web con arquitectura MVC
    Crear aplicaciones web o sistemas con Programación Orientada a Objetos.
    Separar las vistas HTML de la programación.
    Separar por módulos la aplicación.

IMPORTANTE:

Mi intención no es re-inventariar la rueda, sino aplicar conceptos puros 
de arquitectura de software valiéndonos de un lenguaje de programación y 
sobre todo practicar para entender su aplicación.



VIRTUAL HOST PARA LA APLICACION

<VirtualHost*:80>
	ServerName myapp.local
   	DocumentRoot /var/www/html/myapp.local/public_html/
	WSGIScriptAlias / /var/www/html/myapp .local/application/frontcontroller.py
	Alias /public_html/ /var/www/html/myapp.local/public_html/
	ErrorLog /var/log/myapp_errors.log
	CustomLog /var/log/myapp_access.log combined
	<Directory />
		Options FollowSymLinks
		AllowOverride All
	</Directory>
</VirtualHost>
