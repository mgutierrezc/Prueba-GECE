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
    betray_payoff = c(20)
    betrayed_payoff = c(2)

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = c(12)
    both_defect_payoff = c(6)

    list_betray_payoff = [10, 10.1, 10.2, 9.9, 10.3, 9.7, 10.2, 10, 9.9, 10.1, 9.8, 9.7, 10.3, 10, 9.8]
    list_betrayed_payoff = [1, 1.1, 1.2, 0.9, 1.3, 0.7, 1.2, 1, 0.9, 1.1, 0.8, 0.7, 1.3, 1, 0.8]
    list_both_cooperate_payoff = [6, 6.1, 6.2, 5.9, 6.3, 5.7, 6.2, 6, 5.9, 6.1, 5.8, 5.7, 6.3, 6, 5.8]
    list_both_defect_payoff = [3, 3.1, 3.2, 2.9, 3.3, 2.7, 3.2, 3, 2.9, 3.1, 2.8, 2.7, 3.3, 3, 2.8]


class Subsession(BaseSubsession):
    def constant_sum(self):
        c_sum = (self.round_number - 1)*0.1
        return c_sum

    def creating_session(self):
        self.group_randomly()
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.CharField(
        choices=['Cooperate', 'Defect'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect()
    )

    #betray_payoff = float(12)
    #betrayed_payoff = float(3)

    # payoff if both players cooperate or both defect
    #both_cooperate_payoff = float(9)
    #both_defect_payoff = float(6)

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):

        display_both_cooperate_payoff = Constants.list_both_cooperate_payoff[self.round_number - 1]

        display_betrayed_payoff = Constants.list_betrayed_payoff[self.round_number - 1]

        display_betray_payoff = Constants.list_betray_payoff[self.round_number - 1]

        display_both_defect_payoff = Constants.list_both_defect_payoff[self.round_number-1]

        payoff_matrix = {
            'Cooperate':
                {
                    'Cooperate': display_both_cooperate_payoff,
                    'Defect': display_betrayed_payoff
                },
            'Defect':
                {
                    'Cooperate': display_betray_payoff,
                    'Defect': display_both_defect_payoff
                }
        }

        self.payoff = payoff_matrix[self.decision][self.other_player().decision]
    pass
