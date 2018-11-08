from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import floppyforms as forms
import config_leex_1

doc = """
Primer juego Leex 2018 - 2: En este juego, cada jugador recibe una dotación inicial de fichas
entre 0 y 100 (M = 100) de acuerdo a una determinada distribución de probabilidad. Cada jugador
puede transferir una cantidad de fichas al otro jugador y pueden observar la decisión del otro
en cada momento. El pago final de cada jugador es la dotacion inicial - la cantidad que
decidió otorgar al otro jugador + la cantidad que el otro jugador decidió otorgar.
"""

class Constants(BaseConstants):
    name_in_url = 'segundo_encargo_mg'
    players_per_group = 2
    num_rounds = config_leex_1.PEMG_number_rounds #10

    instructions_template = 'sec_enc_mg/Instructions.html'

class Subsession(BaseSubsession):
        def creating_session(self):
            if self.round_number == 1:
                self.group_randomly()
            else:
                self.group_like_round(1)

            for p in self.get_players():
                p.sent_amount = 0
                #Assigning a zero value to avoid None values in the game
                p.endowment = c(random.randint(1, 100))
                #Random creation of endowments for every round


class Group(BaseGroup):
    #
    #
    def set_payoffs(self):

        pA = self.get_player_by_role('A') # o player 1
        pB = self.get_player_by_role('B') # o player 2

        pA.payoff = pA.endowment - pA.sent_amount
        pB.payoff = pB.endowment + pA.sent_amount

        pA.afterloss = pA.endowment - pA.sent_amount
        pB.afterloss = pB.endowment - pB.sent_amount
        pA.afterearn = pA.endowment + pB.sent_amount
        pB.afterearn = pB.endowment + pA.sent_amount

    def get_endowment_A(self):
            pA = self.get_player_by_role('A') # o player 1
            return pA.endowment

    def get_endowment_B(self):
            pB = self.get_player_by_role('B') # o player 2
            return pB.endowment

    def get_sent_amount_A(self):
            pA = self.get_player_by_role('A') # o player 1
            return pA.sent_amount

    def get_sent_amount_B(self):
            pB = self.get_player_by_role('B') # o player 2
            return pB.sent_amount

    def get_afterloss_A(self):
            pA = self.get_player_by_role('A') # o player 1
            return pA.afterloss

    def get_afterloss_B(self):
            pB = self.get_player_by_role('B') # o player 2
            return pB.afterloss

    def get_afterearn_A(self):
            pA = self.get_player_by_role('A') # o player 1
            return pA.afterearn

    def get_afterearn_B(self):
            pB = self.get_player_by_role('B') # o player 2
            return pB.afterearn

class Player(BasePlayer):

    endowment = models.CurrencyField()
    sent_amount = models.IntegerField(verbose_name='Deslice hasta escoger la cantidad a enviar deseada',
                                        min=0, max=100,
                                        initial=0,
                                        widget=widgets.SliderInput())
    afterloss = models.CurrencyField()
    afterearn = models.CurrencyField()

    def role(self):
        if self.id_in_group == 1:
            return 'A'
        else:
            return 'B'
