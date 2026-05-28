from flask import Flask, request, render_template_string

app = Flask(__name__)

def show_the_login_form():
    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
    """)

def do_the_login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    login = [
        {"nome": "luiza", "senha": 22403396}, {"nome": "janaina", "senha": "cotemig2026"}, {"nome": "antonio", "senha": "cotemig2026"}]

    for pessoa in login:
        if usuario == pessoa["nome"] and str(senha) == str(pessoa["senha"]):
            return f"Bem vindo, {usuario}!"

    return "Acesso negado"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)