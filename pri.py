from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world(): 
    nombre = "Unai"
    sobrenombre = "'Ñupi'"
    hobbies = ["Leer", "Jugar a videojuegos", "Ver anime"]
    caps = ["Cogiendo datos", "Haciendo calculos"]
    return render_template('target.html', nombre=nombre, sobrenombre=sobrenombre, hobbies=hobbies, caps=caps)
@app.route('/nuevo', methods=['GET'])
def nuevo():
    return render_template('nuevo.html')
@app.route("/tarjeta", methods=['GET','POST'])
def tarjeta():
    nombre=request.form['nombre']
    sobrenombre=request.form["sobrenombre"]
    hobbies=request.form['hobbies'].split(',')
    caps=request.form['caps'].split(",")
    
    return render_template('target.html', nombre=nombre, sobrenombre=sobrenombre, hobbies=hobbies, caps=caps)
@app.route("/hija")
def enlace_am():
    return '<h1>A continación tendra un enlace</h1> <a href="/RUTA">enlace a nieto'
    
@app.route("/RUTA")
def actus_minecraft():
    return"<p>Número de actualizaciones de Minecraft: 25<p>"

app.run(debug=True)