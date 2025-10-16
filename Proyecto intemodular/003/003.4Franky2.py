
from flask import Flask

#Importamos el archivo json
import json

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    #Esto es el archivo 003.3.html
    #Esto es el primer trozo
    cadena = '''
    <!DOCTYPE html>
<html lang="esp">
    <head>
        <litle>RODRIGOMMblog</litle>
        <meta charset="utf-8">
        <style>
            body{background-color: ghostwhite;color:black;font-family: sans-serif;}
            header,main,footer{background-color: white;padding: 20px;margin: auto;width: 600px;}
            main{color: slateblue;}
        </style>
    </head>

    <body>
        <header><h1>RODRIGOMMblog</h1></header>
        <main>
        '''
        #Esto es otro bloque
    #Este codigo proviene del 003.2LeerJson
    archivo = open("003.2.json","r")
    contenido = json.load(archivo)
    for linea in contenido:
        cadena += '''
            <article>
                <h3>'''+linea["titulo"]+'''</h3>
                <time>'''+linea["fecha"]+'''</time>
                <p>'''+linea["autor"]+'''</p>
                <p>'''+linea["contenido"]+'''</p>
            </article>
            '''
            #Esto es otro bloque
    cadena += '''
        </main>
        <footer>(c) 2025 Rodrigo Menendez Molina</footer>
    </body>
</html>
'''
    #No olvidarse del return y de la sangria, el return y las cadenas  a la misma altura
    return cadena

#Dividir en trozos el articulo permite reutilizar partes

if __name__ == "__main__":
    aplicacion.run(debug=True)


