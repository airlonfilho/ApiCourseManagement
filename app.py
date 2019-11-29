from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from secure.security import authenticate, identity
from controllers.user import UserRegister, Usuario, ListarUsuario, DeleteUsuario, EditUsuario
from controllers.disciplina import DisciplinaId, DeleteDisciplina, Disciplina, ListaDisciplinas, EditDisciplina
from controllers.topico import Topico, TopicoList, DeleteTopico, TopicoId, EditTopico
from controllers.relacionamento import Relacionamento, RelacionamentoList 
from db.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../dado.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'segredo'
api = Api(app)
db.init_app(app)

@app.before_first_request
def criar_banco():
    db.create_all()
    
#cria o endpoint /auth por onde são enviados
#usuario e senha
jwt = JWT(app, authenticate, identity) 


#Rotas de Usuário
api.add_resource(UserRegister, '/register')
api.add_resource(ListarUsuario, '/usuarios')
api.add_resource(Usuario, '/usuario/<string:nome>')
api.add_resource(DeleteUsuario, '/usuario/<string:id>')
api.add_resource(EditUsuario, '/usuario/edit/<string:id>')

#Rotas de Disciplinas
api.add_resource(Disciplina, '/disciplina')
api.add_resource(EditDisciplina, '/disciplina/edit/<string:id>')
api.add_resource(ListaDisciplinas, '/disciplinas')
api.add_resource(DisciplinaId, '/disciplina/<string:id>')
api.add_resource(DeleteDisciplina, '/disciplina/<string:id>')

#Rotas de Tópicos
api.add_resource(Topico, '/topico')
api.add_resource(TopicoList, '/topicos')
api.add_resource(TopicoId, '/topico/<string:id>')
api.add_resource(EditTopico, '/topico/edit/<string:id>')
api.add_resource(DeleteTopico, '/topico/<string:id>')

#Rotas de Rela
api.add_resource(Relacionamento, '/rel')
api.add_resource(RelacionamentoList, '/rels')