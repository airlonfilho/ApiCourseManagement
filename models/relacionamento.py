from db.db import db
from models.topico import TopicoModel

class RelacionamentoModel(db.Model):
    
    __tablename__ = 'relacionamentos'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(500))

    id_topico1 = db.Column(db.Integer, db.ForeignKey('topicos.id'))
    id_topico2 = db.Column(db.Integer, db.ForeignKey('topicos.id'))

    #topico1 = db.relationship("TopicoModel", foreign_keys=[id_topico1])
    #topico2 = db.relationship("TopicoModel", foreign_keys=[id_topico2])

    topico1 = db.relationship("TopicoModel", primaryjoin=TopicoModel.id == id_topico1)
    topico2 = db.relationship("TopicoModel", primaryjoin=TopicoModel.id == id_topico2)

    def __init__(self, nome, id_topico1, id_topico2):
        self.nome = nome
        self.id_topico1 = id_topico1
        self.id_topico2 = id_topico2

    def json(self):
        return {'id': self.id, 'nome' : self.nome}

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

    