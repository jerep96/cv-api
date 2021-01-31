#!flask/bin/python
#-*- coding: UTF-8 -*-

from flask import Flask, jsonify, request, abort

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR']=True
@app.route('/')
def index():
    info = {
        "mensaje" : "Bienvenido a la API de curriculum vitae de Jeremias Palacios.",
        "acciones": [
            "GET /curriculum",
            "POST /mensajes"
        ]
    }
    return jsonify(info)

@app.route('/curriculum', methods=['GET'])
def cv():
    url_imagen = request.host_url + "static/FotoJeremias.png"
    cv = {
        "nombre" : "Jeremias",
        "apellido" : "Palacios Toconas",
        "residencia" : "Argentina",
        "experiencia" : [{
            "posicion" : "Front-End Developer",
            "empresa" : "MPSoft",
            "desde" : "28/11/2020",
            "hasta" : "Actualmente",
            "descripcion" : "<detalles>"
        },
        {
            "posicion" : "Big Data Analyst",
            "empresa" : "Ministerio de educacion de la Prov. de Jujuy",
            "desde" : "16/03/2018",
            "hasta" : "Actualmente",
            "descripcion" : "<detalles>"
        }],
        "educacíon" : {
            "nivel" : "Terciario - Completo",
            "titulo" : "Tec. Superior en Desarrollo de Software",
            "institucion" : "IES N° 7 Populorum Progressio Intela"
        },
        "intereses" : ["Python", "API", "Node.js", "React.js", "Angular"],
        "redes" :{
            "github" : "link",
            "linkedin" : "link",
            "instagram" : "link"
        },
        "foto": url_imagen,
    }
    return jsonify(cv)

@app.route('/mensaje', methods=['POST'])
def contacto():
    mensaje = request.get_data()
    if not mensaje:
        abort(400, description="Debe enviar un mensaje en le body del POST.")
    print("MENSAJE DE CONTACTO:" + str(mensaje))
    return "Gracias por su mensaje."


if __name__ == '__main__':
    app.run()