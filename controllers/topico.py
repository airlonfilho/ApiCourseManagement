from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.topico import TopicoModel

class Topico(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('nome',
                        type=str,
                        required=True,
                        help="Nome do tópico é obrigatório."
                        )
    
    parser.add_argument('id_disciplinas',
                        type=int,
                        required=True,
                        help="Disciplina obrigatória.")
                    

    def post(self):
        dado = Topico.parser.parse_args()
        if TopicoModel.buscar_por_nome(dado['nome']):
            return {"mensagem": "Tópico existente."}, 400
        topico = TopicoModel(**dado)
        topico.salvar_no_banco()

        return {"mensagem": "Tópico criado com sucesso"},201

class TopicoList(Resource):
    def get(self):
        return {'itens': [topico.json() for topico in TopicoModel.query.all()]}

class TopicoId(Resource):
    def get(self, id):
        topico = TopicoModel.buscar_por_id(id)
        if topico:
            return topico.json()
        return {'mensagem': 'Tópico não encontrado'}, 404

class DeleteTopico(Resource):
    def delete(self, id):
        topico = TopicoModel.buscar_por_id(id)
        topico.remover_no_banco()
        return {'mensagem': 'Tópico removido com sucesso'},200

class EditTopico(Resource):
    def put(self, id):
        dado = Topico.parser.parse_args()
        topico = TopicoModel.buscar_por_id(id)
        if not topico:
            return {'message': 'Tópico não encontrado'}, 400
        topico.nome = dado['nome']
        topico.salvar_no_banco()

        return topico.json()

