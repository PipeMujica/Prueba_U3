from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ejemplo1', methods=['GET', 'POST'])
def ejemplo1():
    if request.method == 'POST':
        resultado= ''
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        promedio = (nota1+nota2+nota3)/3
        asistencia = int(request.form['asistencia'])
        if promedio >= 40 and asistencia >= 75:
            resultado = "APROBADO"
        else:
            resultado="REPROBADO"
        return render_template('ejemplo1.html',promedio=promedio,resultado=resultado)
    return render_template('ejemplo1.html')

@app.route('/ejemplo2', methods=['GET', 'POST'])
def ejemplo2():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])
        lista = [nombre1,nombre2,nombre3]
        largo = max(lista, key=len)
        cantidad = len(largo)
        return render_template('ejemplo2.html',lista=lista, largo=largo, cantidad=cantidad)
    return render_template('ejemplo2.html')


if __name__ == '__main__':
    app.run()