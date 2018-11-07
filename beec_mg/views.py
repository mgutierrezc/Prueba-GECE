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

class Contribution(Page):

    form_model = models.Player
    form_fields = ['contribution']
    def contribution_max(self):
        return self.player.endowment


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
