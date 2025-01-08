from flask import Flask # Importamos Flask, que es como una caja de herramientas para crear aplicaciones web.
# Esto nos permite iniciar nuestra aplicación y manejar rutas (URLs).

from flask import render_template # Importamos render_template, una función que sirve para mostrar archivos HTML

app = Flask(__name__) # Creamos nuestra aplicación web usando Flask llamada "app", esta puede cambiar no necesariamente tiene que ser "app"
# "__name__" le dice a Flask que esta aplicación está basada en este archivo, ayudándole a encontrar recursos como plantillas HTML
#  y archivos estáticos. 

@app.route('/') # Esta función se llama cuando la URL es "/", app.route() es una decorador que nos permite definir rutas
#recordemos El .route() se utiliza para asociar las rutas de tu aplicación con funciones específicas. 
# #Si no lo usas, Flask no sabrá qué hacer cuando alguien intente acceder a una URL, porque no habrá una función vinculada a esa URL.
def home(): #creamos una ruta que apunta a la función home
    return "Welcome in my house シ!" #Esta función nos devuelve una cadena de texto que se mostrará en la pantalla

@app.errorhandler(404) # Esta función se llama cuando Flask no encuentra una ruta y nos devuelve un código de error 404 que significa "no encontrado"
def page_not_found(e): #creamos una función llamda page_not_found que lo llamamos cuando Flask no encuentra una ruta, la letra e representa el parametro del error
    return render_template('404.html'), 404 #Esta función nos devuelve una respuesta HTML y el codigo de estado 404 HTTP al navegador
# que se mostrará en la pantalla

if __name__ == '__main__': # Este bloque de código se ejecuta cuando el archivo principal se ejecuta directamente
    app.run() # Ejecutamos la aplicación web