from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.relacionamento import RelacionamentoModel

class RelacionamentoCad(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('nome',
                        type=str,
                        required=True,
                        help="Nome do tópico é obrigatório."
                        )
    
    parser.add_argument('topico1_id',
                        type=int,
                        required=True,
                        help="topico1_id obrigatória.")
                
    parser.add_argument('topico2_id',
                        type=int,
                        required=True,
                        help="topico2_id obrigatória.")
    
    def post(self):
        dado = RelacionamentoCad.parser.parse_args()
        relacionamento = RelacionamentoModel(**dado)
        relacionamento.salvar_no_banco()

        return {"mensagem": "Relacionamento criado com sucesso"},201

class Relacionamento(Resource):
    def get(self):
        return {'relacionamentos': [relacionamento.json() for relacionamento in RelacionamentoModel.query.all()]}

class DeleteRel(Resource):
    def delete(self, id):
        relacionamento = RelacionamentoModel.buscar_por_id(id)
        relacionamento.remover_no_banco()
        return {'mensagem': 'Relacionamento removido com sucesso'},200

class EditRel(Resource):
    def put(self, id):
        dado = RelacionamentoCad.parser.parse_args()
        relacionamento = RelacionamentoModel.buscar_por_id(id)
        if not relacionamento:
            return {'message': 'Relacionamento não encontrado'}, 400
        relacionamento.nome = dado['nome']
        relacionamento.salvar_no_banco()

        return relacionamento.json()
