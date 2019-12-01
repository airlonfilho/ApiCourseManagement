from db.db import db

class UserModel(db.Model):

    __tablename__ = 'usuers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(15))
    nivel = db.Column(db.Integer, default="1")
    

    def __init__(self, username, password, nivel):
        self.username = username
        self.password = password
        self.nivel = nivel

    def json(self):
        return {'id' : self.id, 'nome' : self.username, 'nivel': self.nivel}

    @classmethod
    def buscar_por_nome(cls, username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def buscar_por_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def salvar_no_banco(self):
        db.session.add(self)
        db.session.commit()
    
    def remover_no_banco(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

