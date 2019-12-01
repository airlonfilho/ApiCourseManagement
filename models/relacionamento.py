from db.db import db
from models.topico import TopicoModel

class RelacionamentoModel(db.Model):
    
    __tablename__ = 'relacionamentotopicos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    topico1_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'topicos.id'
        )
    )
    topico2_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'topicos.id'
        )
    )

    topico1 = db.relationship(
        "TopicoModel",
        primaryjoin=TopicoModel.id == topico1_id,
    )
    topico2 = db.relationship(
        "TopicoModel",
        primaryjoin=TopicoModel.id == topico2_id,
    )

    def __init__(self, nome, topico1_id, topico2_id):
        self.nome = nome
        self.topico1_id = topico1_id
        self.topico2_id = topico2_id
    
    def json(self):
        return {'id': self.id, 'Descrição' : self.nome, 'id_topico1' : self.topico1_id, 'id_topico2' : self.topico2_id }

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

    