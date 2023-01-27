from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hola mundo Flask"


@app.route('/menu')
def hola():
    return "<h1>Hola desde menu </h1>"


@app.route('/user/<string:user>')
def user(user):
    return "Hola " + user


@app.route('/user/<int:n>')
def numero(n):
    return "Numero: {}".format(n)


@app.route('/user/<int:id>/<string:name>')
def fun(id, name):
    return "ID: {} nombre: {}".format(id, name)


@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return "La suma es {}".format(n1+n2)


@app.route('/suma2', methods=["GET","POST"])
def sumar():
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        return "<h2> La suma es: {}".format(str(int(num1)+int(num2)))
    else:
        return '''
        <form action="/suma2 method="POST">
        <label>N1: </label>
        <input type="text" name="num1"/><br><br>
        <label>N2: </label>
        <input type="text" name="num2"/><br><br>
        <input type="submit" value="calcular"/>
        </form>
        '''


if __name__ == '__main__':
    app.run(debug=True, port=3000)
