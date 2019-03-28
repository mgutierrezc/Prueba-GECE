from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range



class Introduction(Page):
    timeout_seconds = 100


class Decision(Page):
    form_model = models.Player
    form_fields = ['decision']
#creo que debo definir aquí los valores con un IF que dependa de las rondas

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    def vars_for_template(self):
        return {
            'my_decision': self.player.decision.lower(),
            'other_player_decision': self.player.other_player().decision.lower(),
            'same_choice': self.player.decision == self.player.other_player().decision,
        }

page_sequence = [
    Introduction,
    Decision,
    ResultsWaitPage,
    Results
]
