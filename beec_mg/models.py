from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import floppyforms as forms
import config_leex_1

author = 'Your name here'

doc = """
Simple public goods game
"""


class Constants(BaseConstants):
    name_in_url = 'tiebout_incertidumbre'
    num_rounds = config_leex_1.PEMG_number_rounds #10
    instructions_template = 'beec_mg/Instructions.html'
    multiplier1 = 1
    multiplier2 = 1.5
    multiplier3 = 2
    i = 1
    j = 1
    k = 1

class Subsession(BaseSubsession):
    def creating_session(self):

        for p in self.get_players():
            p.endowment = c(random.randint(1, 100))
            p.prob = random.randint(0,100)
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
        self.total_contribution1 = sum(
            [p.contribution for p in self.get_players() if p.role== "A"])
        self.totalp1 = sum(
            [p.counter for p in self.get_players() if p.role== "A"])
        self.totalp2 = sum(
            [p.counter for p in self.get_players() if p.role == "B"])
        self.totalp3 = sum(
            [p.counter for p in self.get_players() if p.role == "C"])

        self.individual_share1 = self.total_contribution1 * Constants.multiplier1 / self.totalp1
        self.individual_share2 = self.total_contribution2 * Constants.multiplier2 / self.totalp2
        self.individual_share3 = self.total_contribution3 * Constants.multiplier3 / self.totalp3

        self.mean_contribution1 = self.total_contribution1/self.totalp1
        self.mean_contribution2 = self.total_contribution2 / self.totalp2
        self.mean_contribution3 = self.total_contribution3 / self.totalp3

        for p in self.get_players():
            if p.role == "A":
                p.payoff = p.endowment - p.contribution + self.individual_share1
            elif p.role == "B":
                if p.prob <= 75:
                    p.payoff = p.endowment - p.contribution + self.individual_share2
                else:
                    p.payoff = p.endowment - p.contribution
            else:
                if p.prob <= 50:
                    p.payoff = p.endowment - p.contribution + self.individual_share3
                else:
                    p.payoff = p.endowment - p.contribution

class Player(BasePlayer):
    contribution = models.CurrencyField(verbose_name='Deslice hasta seleccionar la cantidad a enviar deseada',
                                        min=0,max=100,
                                        initial=0,widget=widgets.SliderInput())
    counter = models.IntegerField(initial=1)
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