from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

#import random
from django import forms
import itertools

author = 'Your name here'
doc = """
Your app description
"""
#
OPTIONS = (
    ("1", "Uno"),
    ("2", "Dos"),
    ("3", "Tres"),
    ("4", "Cuatro"),
    ("5", "Cinco"),
    ("6", "Seis"),
    ("7", "Todos los numeros fueron reportados por igual"),
)


class Constants(BaseConstants):
    name_in_url = 'base_tesis'
    players_per_group = 8 #El objetivo del juego es que la mitad de participantes sea control y la mitad tratamiento,
    #ponemos 8 partiendo de la idea de que tendremos un salón de 16 participantes. si son menos, este número se acomoda
    #de modo que haya la mitad del total de jugadores en cada grupo.
    num_rounds = 2


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        tratamientos = itertools.cycle(['a', 'b'])
        for g in self.get_groups():
            g.tratamiento = next(tratamientos)


class Group(BaseGroup):
    tratamiento = models.StringField()
    pass


class Player(BasePlayer):
    lanzamiento_1 = models.IntegerField(
        choices=[6, 1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal,
    )
    lanzamiento_2 = models.IntegerField(
        choices=[6, 1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal,
    )
    lanzamiento_3 = models.IntegerField(
        choices=[6, 1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal,
    )
    lanzamiento_4 = models.IntegerField(
        choices=[6, 1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal,
    )
    lanzamiento_5 = models.IntegerField(
        choices=[6, 1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal,
    )
    lanzamiento_6 = models.IntegerField(
        choices=[6, 1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal,
    )
    lanzamiento_7 = models.IntegerField(
        choices=[6, 1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal,
    )
    lanzamiento_8 = models.IntegerField(
        choices=[6, 1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal,
    )
    lanzamiento_9 = models.IntegerField(
        choices=[6, 1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal,
    )
    lanzamiento_10 = models.IntegerField(
        choices=[6, 1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal,
    )
    lanzamiento_11 = models.IntegerField(
        choices=[6, 1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal,
    )
    lanzamiento_12 = models.IntegerField(
        choices=[6, 1, 2, 3, 4, 5],
        widget=widgets.RadioSelectHorizontal,
    )
    otros = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5],
        widget=widgets.RadioSelect,
    )
    
    Seleccione_una_de_las_siguientes_opciones = models.StringField(
        widget=forms.CheckboxSelectMultiple(choices=OPTIONS),)


    Seleccione_una_entre_las_siguientes_opciones = models.StringField(
        widget=forms.CheckboxSelectMultiple(choices=OPTIONS),)

    
    Pago_en_soles = models.FloatField(min=0, max=5)

    Que_tan_religioso_te_consideras = models.StringField(choices=['Nada','Poco','Algo','Bastante', 'Mucho'],
                                                         widget=widgets.RadioSelectHorizontal,
                                                         )
    Que_tanto_crees_en_dios = models.StringField(choices=['Nada','Poco','Algo','Bastante', 'Mucho'],
                                                         widget=widgets.RadioSelectHorizontal,
                                                         )
    Hasta_que_punto_crees_en_un_dios_que_castiga = models.StringField(choices=['Nada','Poco','Algo','Bastante', 'Mucho'],
                                                         widget=widgets.RadioSelectHorizontal,
                                                         )

#currency