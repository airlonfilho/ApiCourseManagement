from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.disciplina import DisciplinaModel

class Disciplina(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('nome',
                        type=str,
                        required=True,
                        help="Nome da Disciplina é obrigatória."
                        )
    @jwt_required()
    def post(self):
        dado = Disciplina.parser.parse_args()
        if DisciplinaModel.buscar_por_nome(dado['nome']):
            return {"mensagem": "Uma disciplona com esse nome já existe."}, 400
        disciplina = DisciplinaModel(**dado)
        disciplina.salvar_no_banco()

        return {"mensagem": "Disciplina criado com sucesso"}

    
class DeleteDisciplina(Resource):
    def delete(self, id):
        disciplina = DisciplinaModel.buscar_por_id(id)
        if disciplina:
            disciplina.remover_no_banco()
        return {'mensagem': 'Disciplina removida com sucesso.'},200

class DisciplinaId(Resource):
    def get(self, id):
        disciplina = DisciplinaModel.buscar_por_id(id)
        if disciplina:
            return disciplina.json()
        return {'mensagem': 'Disciplina não encontrada'}, 404

class EditDisciplina(Resource):
    @jwt_required()
    def put(self, id):
        dado = Disciplina.parser.parse_args()
        disciplina = DisciplinaModel.buscar_por_id(id)
        if not disciplina:
            return {'message': 'Disciplina não encontrada'}, 400
        disciplina.nome = dado['nome']
        disciplina.salvar_no_banco()

        return disciplina.json()
    
class ListaDisciplinas(Resource):
    def get(self):
        return {'disciplinas': [disciplina.json() for disciplina in DisciplinaModel.query.all()]}
    
    