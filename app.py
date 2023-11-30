from flask import Flask,render_template, request,redirect

app = Flask(__name__)

class cadInfluencer:
    def __init__(self,nome,social,seguidor,area):
        self.nome = nome
        self.social = social
        self.seguidor = seguidor
        self.area = area

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
lista = []

@app.route('/Influencer')
def Influencer():
    return render_template('Influencer.html',Titulo = "Influencers Iniciais:",ListaInfluencer = lista)

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo = "Cadastro de Influencer")

@app.route("/criar", methods= ["POST"])
def criar():
    nome = request.form["nome"]
    social = request.form["social"]
    seguidor = request.form["seguidor"]
    area = request.form["area"]
    obj = cadInfluencer(nome, social, seguidor, area)
    lista.append(obj)
    return redirect('/Influencer')

@app.route('/excluir/<nomeinflu>', methods=['GET','DELETE'])
def excluir(nomeinflu):
    for i, influ in enumerate(lista):
        if influ.nome == nomeinflu:
            lista.pop(i)
            break
    return redirect('/Influencer')

@app.route('/editar/<nomeinflu>', methods=['GET'])
def editar(nomeinflu):
    for i, influ in enumerate(lista):
        if influ.nome == nomeinflu:
            return render_template('Editar.html', influencer = influ, titulo="Alterar influencer")

@app.route('/alterar', methods=['POST', "PUT"])
def alterar():
    nome = request.form['nome']
    for i, influ in enumerate(lista): # o request acessa as informações do formulário
        if influ.nome == nome:
            influ.nome = request.form['nome']
            influ.social = request.form['social']
            influ.seguidor = request.form['seguidor']
            influ.area = request.form['area']
    return  redirect('/Influencer')

if __name__ == '__main__':
    app.run()