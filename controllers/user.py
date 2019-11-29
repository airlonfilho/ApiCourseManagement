from flask_restful import Resource, reqparse
from models.user import UserModel

class Usuario(Resource): 
    def get(self, nome):
        usuario = UserModel.buscar_por_nome(nome)
        if usuario:
            return usuario.json()
        return {'mensagem': 'Usuário não encontrado'}, 404

class ListarUsuario(Resource):
    def get(self):
        return {'usuarios': [usuario.json() for usuario in UserModel.query.all()]}

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="Usuário obrigatório."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Senha obrigatória."
                        )

    def post(self):
        dado = UserRegister.parser.parse_args()
        if UserModel.buscar_por_nome(dado['username']):
            return {"mensagem": "Usuário existente."}, 400
        usuario = UserModel(**dado)
        usuario.salvar_no_banco()

        return {"mensagem": "Usuário criado com sucesso"}

class DeleteUsuario(Resource):
    def delete(self, id):
        usuario = UserModel.buscar_por_id(id)
        usuario.remover_no_banco()
        return {'mensagem': 'Usuário removido com sucesso'},200

class EditUsuario(Resource):
    def put(self, id):
        dado = UserRegister.parser.parse_args()
        usuario = UserModel.buscar_por_id(id)
        if not usuario:
            return {'message': 'Usuário não encontrado'}, 400
        usuario.username = dado['username']
        usuario.salvar_no_banco()

        return usuario.json()