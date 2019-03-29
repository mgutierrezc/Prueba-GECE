from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from . import config as config_py
import config_leex_1
import random
import math

doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


class Constants(BaseConstants):
    name_in_url = 'prisoner_sr'
    players_per_group = 2
    num_rounds = config_leex_1.PDsr_number_rounds  #esto estaba en 4, lo cambié

    instructions_template = 'prisoner_sr/Instructions.html'

    config = config_py

    one = 1

    # payoff if 1 player defects and the other cooperates""",
    #betray_payoff = float(12)
    #betrayed_payoff = float(3)

    # payoff if both players cooperate or both defect
    #both_cooperate_payoff = float(9)
    #both_defect_payoff = float(6)

#    data = [
#        [
#            {"betray_payoff": 12, "betrayed_payoff": 3, "both_cooperate_payoff": 9, "both_defect_payoff": 6},
#            {"betray_payoff": 12.1, "betrayed_payoff": 3.1, "both_cooperate_payoff": 9.1, "both_defect_payoff": 6.1},
#            {"betray_payoff": 12.2, "betrayed_payoff": 3.2, "both_cooperate_payoff": 9.2, "both_defect_payoff": 6.2},
#            {"betray_payoff": 12.3, "betrayed_payoff": 3.3, "both_cooperate_payoff": 9.3, "both_defect_payoff": 6.3},
#            {"betray_payoff": 12.4, "betrayed_payoff": 3.4, "both_cooperate_payoff": 9.4, "both_defect_payoff": 6.4},
#            {"betray_payoff": 12.5, "betrayed_payoff": 3.5, "both_cooperate_payoff": 9.5, "both_defect_payoff": 6.5},
#            {"betray_payoff": 12.6, "betrayed_payoff": 3.6, "both_cooperate_payoff": 9.6, "both_defect_payoff": 6.6},
#            {"betray_payoff": 12.7, "betrayed_payoff": 3.7, "both_cooperate_payoff": 9.7, "both_defect_payoff": 6.7},
#            {"betray_payoff": 12.8, "betrayed_payoff": 3.8, "both_cooperate_payoff": 9.8, "both_defect_payoff": 6.8},
#            {"betray_payoff": 12.9, "betrayed_payoff": 3.9, "both_cooperate_payoff": 9.9, "both_defect_payoff": 6.9},
#            {"betray_payoff": 13, "betrayed_payoff": 4, "both_cooperate_payoff": 10, "both_defect_payoff": 7},
#            {"betray_payoff": 13.1, "betrayed_payoff": 4.1, "both_cooperate_payoff": 10.1, "both_defect_payoff": 7.1},
#            {"betray_payoff": 13.2, "betrayed_payoff": 4.2, "both_cooperate_payoff": 10.2, "both_defect_payoff": 7.2},
#            {"betray_payoff": 13.3, "betrayed_payoff": 4.3, "both_cooperate_payoff": 10.3, "both_defect_payoff": 7.3},
#            {"betray_payoff": 13.4, "betrayed_payoff": 4.4, "both_cooperate_payoff": 10.4, "both_defect_payoff": 7.4}
#        ]
#    ]


class Subsession(BaseSubsession):
    def constant_sum(self):
        c_sum = (self.round_number - 1)*0.1
        return c_sum

    def creating_session(self):
        for p in self.get_players():
            p.betray_payoff = p.betray_payoff+(self.round_number - 1)*0.1

#problema actual, debo sumar un float con el resultado de la línea 59

#    def in_round(self, round_number):
#        if self.round_number == 1:
#            return 12
#        elif self.round_number == 2:
#            return 13


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.CharField(
        choices=['Cooperate', 'Defect'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect()
    )

    betray_payoff = models.FloatField(
        initial=12
    )

    betrayed_payoff = models.FloatField(
        initial=3
    )

    both_cooperate_payoff = models.FloatField(
        initial=9
    )

    both_defect_payoff = models.FloatField(
        initial=6
    )
    #betray_payoff = float(12)
    #betrayed_payoff = float(3)

    # payoff if both players cooperate or both defect
    #both_cooperate_payoff = float(9)
    #both_defect_payoff = float(6)

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):

        payoff_matrix = {
            'Cooperate':
                {
                    'Cooperate': self.both_cooperate_payoff,
                    'Defect': self.betrayed_payoff
                },
            'Defect':
                {
                    'Cooperate': self.betray_payoff,
                    'Defect': self.both_defect_payoff
                }
        }

        self.payoff = payoff_matrix[self.decision][self.other_player().decision]

#+ Subsession.constant_sum,
#+ Subsession.constant_sum
#+ Subsession.constant_sum,
#+ Subsession.constant_sum