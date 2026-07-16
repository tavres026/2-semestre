from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

usuario_cadastrado = ""
senha_hash = ""


@app.route("/", methods=["GET", "POST"])
def cadastro():
    global usuario_cadastrado, senha_hash

    if request.method == "POST":
        usuario_cadastrado = request.form["nome"]
        senha = request.form["senha"]

        # Gera o hash da senha
        senha_hash = generate_password_hash(senha)

        return redirect(url_for("login"))

    return render_template("cadastro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    mensagem = ""

    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]

        if nome != usuario_cadastrado:
            mensagem = "Usuário não encontrado."

        elif not check_password_hash(senha_hash, senha):
            mensagem = "Senha inválida."

        else:
            return redirect(url_for("inicio"))

    return render_template("login.html", mensagem=mensagem)


@app.route("/inicio")
def inicio():
    return render_template("inicio.html", nome=usuario_cadastrado)


if __name__ == "__main__":
    app.run(debug=True)