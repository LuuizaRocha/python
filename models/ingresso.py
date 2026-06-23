from . import db
from .base import ModeloBase


class Ingresso(ModeloBase):
    __tablename__ = "ingressos"

    sessao_id = db.Column(
        db.Integer,
        db.ForeignKey("sessoes.id")
    )

    assento = db.Column(db.String(10), nullable=False)
    nome_comprador = db.Column(db.String(120), nullable=False)

    sessao = db.relationship("Sessao")