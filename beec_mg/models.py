from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import config_leex_1

author = 'Your name here'

doc = """
Simple public goods game
"""


class Constants(BaseConstants):
    name_in_url = 'tiebout_incertidumbre'
    players_per_group = 8
    num_rounds = 5 #config_leex_1.PEMG_number_rounds #10
    instructions_template = 'beec_mg/Instructions.html'
    multiplier1 = 1.5
    multiplier2 = 2
    multiplier3 = 2.5
    i = 1
    j = 1
    k = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        gamma = random.randint(1, 100)
        for p in self.get_players():
            p.endowment = random.randint(1, 15)
            p.prob = gamma
            # Random creation of endowments for every round

class Group(BaseGroup):

    total_contribution1 = models.CurrencyField(initial=0)
    total_contribution2 = models.CurrencyField(initial=0)
    total_contribution3 = models.CurrencyField(initial=0)
    mean_contribution1 = models.CurrencyField(initial=0)
    mean_contribution2 = models.CurrencyField(initial=0)
    mean_contribution3 = models.CurrencyField(initial=0)
    totalp1 = models.IntegerField(initial=0)
    totalp2 = models.IntegerField(initial=0)
    totalp3 = models.IntegerField(initial=0)
    individual_share1 = models.CurrencyField(initial=0)
    individual_share2 = models.CurrencyField(initial=0)
    individual_share3 = models.CurrencyField(initial=0)

    def set_payoffs(self):
        # NOTA 1: LAS SUMAS CON FOR NO ESTÁN FUNCIONANDO, YA QUE DAN DE VALOR 0
        # NOTA 2: Los sums con if botan un error de invalid operation
        # NOTA 3: Segun SO, se deberia incluir parentesis después de p.role
        # if p.role== 'A':
        # self.total_contribution1 = sum(
            # [p.contribution for p in self.get_players() if p.role() == 'A'])
        for p in self.get_players():
            if p.role() == 'A':
                self.total_contribution1 += p.contribution

        for p in self.get_players():
            if p.role() == 'B':
                self.total_contribution2 += p.contribution

        for p in self.get_players():
            if p.role() == 'C':
                self.total_contribution3 += p.contribution

        # if p.role== 'B'
        # self.total_contribution2 = sum(
            # [p.contribution for p in self.get_players()])
        # if p.role== 'C'
        # self.total_contribution3 = sum(
            # [p.contribution for p in self.get_players()])

        # if p.role== 'A'
        # self.totalp1 = sum(
            # [p.counter for p in self.get_players() if p.role() == 'A'])
        for p in self.get_players():
            if p.role() == 'A':
                self.totalp1 += 1

        for p in self.get_players():
            if p.role() == 'B':
                self.totalp2 += 1

        for p in self.get_players():
            if p.role() == 'C':
                self.totalp3 += 1

        # if p.role == 'B'
        # self.totalp2 = sum(
            # [p.counter for p in self.get_players() if p.role() == 'B'])
        # if p.role == 'C'
        # self.totalp3 = sum(
            # [p.counter for p in self.get_players() if p.role() == 'C'])

        self.mean_contribution1 = self.total_contribution1/self.totalp1 if self.totalp1!=0 else 0
        self.mean_contribution2 = self.total_contribution2 /self.totalp2 if self.totalp2!=0 else 0
        self.mean_contribution3 = self.total_contribution3 /self.totalp3 if self.totalp3!=0 else 0
        self.individual_share1 = self.mean_contribution1 * Constants.multiplier1 if self.totalp1!=0 else 0
        self.individual_share2 = self.mean_contribution2 * Constants.multiplier2 if self.totalp2!=0 else 0
        self.individual_share3 = self.mean_contribution3 * Constants.multiplier3 if self.totalp3!=0 else 0
        #if self.totalp1!=0 else 0

        for p in self.get_players():
            if p.prob<=50:
                if p.roller == 3:
                    p.payoff = p.endowment - p.contribution + self.mean_contribution3 * Constants.multiplier3
                elif p.roller == 2:
                    p.payoff = p.endowment - p.contribution + self.mean_contribution2 * Constants.multiplier2
                elif p.roller == 1:
                    p.payoff = p.endowment - p.contribution + self.mean_contribution1 * Constants.multiplier1
            elif 50 < p.prob <= 75:
                if p.roller == 3:
                    p.payoff = p.endowment - p.contribution
                elif p.roller == 2:
                    p.payoff = p.endowment - p.contribution + self.mean_contribution2 * Constants.multiplier2
                elif p.roller == 1:
                    p.payoff = p.endowment - p.contribution + self.mean_contribution1 * Constants.multiplier1
            else:
                if p.roller == 3:
                    p.payoff = p.endowment - p.contribution
                elif p.roller == 2:
                    p.payoff = p.endowment - p.contribution
                elif p.roller == 1:
                    p.payoff = p.endowment - p.contribution + self.mean_contribution1 * Constants.multiplier1

class Player(BasePlayer):
    prob =models.IntegerField(min=0, max=100)
    endowment = models.CurrencyField(min=0, max=100, initial=0)
    contribution = models.CurrencyField(verbose_name='Deslice hasta seleccionar la cantidad a enviar deseada',
                                        min=0,max=100,
                                        initial=0,widget=widgets.SliderInput())
    roller = models.IntegerField(verbose_name='Deslice hasta seleccionar el número de la opción deseada',
                                 min=1, max=3,
                                 widget=widgets.SliderInput())
    # Se está usando un slider para esta opción pues permite evitar confusiones en caso se use un grupo de botones
    # los cuales se podrían clickear en cualquier momento sin que el jugador entienda si ya se registró o no su decisión

    def role(self):
        if self.roller == 1:
            return 'A'
        elif self.roller == 2:
            return 'B'
        else:
            return 'C'
