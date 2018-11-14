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

    def checkslider_error_message(self, value):
            if not value:
                return 'Please make your decision using slider'

   # def is_displayed(self):
    #    return self.player.id_in_group == 1



class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    """This page displays the earnings of each player"""

page_sequence = [
    Introduction,
    Offer,
    ResultsWaitPage,
    Results,
]

