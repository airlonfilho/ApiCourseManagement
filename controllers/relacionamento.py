from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.relacionamento import RelacionamentoModel

class Relacionamento(Resource):

    parser = reqparse.RequestParser()

    def post(self):
        dado = Relacionamento.parser.parse_args()
        if RelacionamentoModel.buscar_por_nome(dado['nome']):
            return {"mensagem": "Relacionamento já existe."}, 400
        relacionamento = RelacionamentoModel(**dado)
        relacionamento.salvar_no_banco()

        return {"mensagem": "Relacionamento criado com sucesso"}

class RelacionamentoList(Resource):
    def get(self):
        return {'itens': [relacionamento.json() for relacionamento in RelacionamentoModel.query.all()]}
