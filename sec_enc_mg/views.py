from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants
import config_leex_1

class Introduction(Page):
    #wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number == 1

class Offer(Page):
    form_model = 'player'
    form_fields = ['sent_amount']

    def sent_amount_max(self):
        return self.player.endowment

    def is_displayed(self):
        return self.player.id_in_group == 1

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def vars_for_template(self):
        if self.player.id_in_group == 2:
            a = str(self.player.endowment)
            body_text = 'Tu dotación es de ' + a + '. Espera la decisión del otro jugador'
        else:
            body_text = 'Por favor, espere.'
        return {'body_text': body_text}

class Results(Page):
    """This page displays the earnings of each player"""

page_sequence = [
    Introduction,
    Offer,
    ResultsWaitPage,
    Results,
]

