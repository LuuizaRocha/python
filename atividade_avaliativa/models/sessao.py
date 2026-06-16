from . import db
from .base import ModeloBase


class Sessao(ModeloBase):
    __tablename__ = "sessoes"

    filme_id = db.Column(
        db.Integer,
        db.ForeignKey("filmes.id")
    )

    sala_id = db.Column(
        db.Integer,
        db.ForeignKey("salas.id")
    )

    data_hora = db.Column(db.DateTime, nullable=False)
    preco = db.Column(db.Float, nullable=False)

    filme = db.relationship("Filme")
    sala = db.relationship("Sala")
    ingressos = db.relationship("Ingresso")

    @classmethod
    def listar_com_detalhes(cls):
        return cls.query.order_by(cls.data_hora.desc()).all()