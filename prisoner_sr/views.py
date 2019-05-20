from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from prisoner_sr import models


class Introduction(Page):
    timeout_seconds = 60

    def is_displayed(self):
        return self.round_number == 1


class Decision(Page):
    form_model = models.Player
    form_fields = ['decision']
#creo que debo definir aquí los valores con un IF que dependa de las rondas


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    def is_displayed(self):
        return self.group.round_number != 15

    def vars_for_template(self):
        return {
            'my_decision': self.player.decision.lower(),
            'other_player_decision': self.player.other_player().decision.lower(),
            'same_choice': self.player.decision == self.player.other_player().decision,
        }


class Resultsfinales(Page):
    def is_displayed(self):
        return self.group.round_number == 15

    def vars_for_template(self):
        return {
            'round_payoff1': self.player.in_round(1).payoff,
            'round_payoff2': self.player.in_round(2).payoff,
            'round_payoff3': self.player.in_round(3).payoff,
            'round_payoff4': self.player.in_round(4).payoff,
            'round_payoff5': self.player.in_round(5).payoff,
            'round_payoff6': self.player.in_round(6).payoff,
            'round_payoff7': self.player.in_round(7).payoff,
            'round_payoff8': self.player.in_round(8).payoff,
            'round_payoff9': self.player.in_round(9).payoff,
            'round_payoff10': self.player.in_round(10).payoff,
            'round_payoff11': self.player.in_round(11).payoff,
            'round_payoff12': self.player.in_round(12).payoff,
            'round_payoff13': self.player.in_round(13).payoff,
            'round_payoff14': self.player.in_round(14).payoff,
            'round_payoff15': self.player.in_round(15).payoff,
        }


page_sequence = [
    Introduction,
    Decision,
    ResultsWaitPage,
    Results,
    Resultsfinales,

]
