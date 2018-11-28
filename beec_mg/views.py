from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction (Page):

        def is_displayed(self):
            return self.round_number == 1

class Decision (Page):

    form_model = models.Player
    form_fields = ['roller']
    def roller_error_message(self, value):
        print('value is', value)
        if self.player.endowment < 3 and (value == 2 or value == 3):
            return 'No tienes suficiente dinero para escoger este escenario'
        elif self.player.endowment < 6 and value == 3:
            return 'No tienes suficiente dinero para escoger este escenario'

class Contribution(Page):

    form_model = models.Player
    form_fields = ['contribution']
    def contribution_max(self):
        return self.player.endowment
    def contribution_min(self):
        if self.player.roller == 1:
            return 0
        elif self.player.roller == 2:
            return 3
        else:
            return 6

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    """This page displays the earnings of each player"""

page_sequence =[
    Introduction,
    Decision,
    Contribution,
    ResultsWaitPage,
    Results
]
