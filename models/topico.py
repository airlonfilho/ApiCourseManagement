from db.db import db

class TopicoModel(db.Model):
    
    __tablename__ = 'topicos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    id_disciplinas = db.Column(db.Integer, db.ForeignKey('disciplinas.id'))
    
    disciplina = db.relationship('DisciplinaModel')

    def __init__(self, nome, id_disciplinas):
        self.nome = nome
        self.id_disciplinas = id_disciplinas

    
    def json(self):
        return {'id': self.id, 'nome' : self.nome, 'id_disciplina': self.id_disciplinas}

    @classmethod
    def buscar_por_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()
    
    @classmethod
    def buscar_por_id(cls, id):
        return cls.query.filter_by(id=id).first()


    def salvar_no_banco(self):
        db.session.add(self)
        db.session.commit()
    
    def remover_no_banco(self):
        db.session.delete(self)
        db.session.commit()

    