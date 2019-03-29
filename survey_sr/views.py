from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Demographics(Page):
    form_model = models.Player
    form_fields = ['gender',
                   'field_studies',
                   'escala',
                   'ciclo',
                   'age',
                   'carrera_padres', ]


class CognitiveReflectionTest(Page):
    form_model = models.Player
    form_fields = ['preg11',
                   'preg12', ]


class SegundoCaso(Page):
    form_model = models.Player
    form_fields = ['preg21',
                   'preg22', ]


class gracias(Page):

    def vars_for_template(self):
        participant = self.participant
        return {
            'redemption_code': participant.label or participant.code,
        }


page_sequence = [
    CognitiveReflectionTest,
    SegundoCaso,
    Demographics,
    gracias,
]
