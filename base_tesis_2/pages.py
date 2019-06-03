from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instrucciones_1(Page):
    def is_displayed(self):
        return self.round_number == 1


class Instrucciones_2(Page):
    def is_displayed(self):
        return self.round_number == 1


class Instrucciones_3(Page):
    def is_displayed(self):
        return self.round_number == 1


class Instrucciones_4(Page):
    def is_displayed(self):
        return self.round_number == 1


class Grupoa (Page):
    def is_displayed(self):
        return self.round_number == 1 and self.group.tratamiento == 'a'


class Grupob (Page):
    def is_displayed(self):
        return self.round_number == 1 and self.group.tratamiento == 'b'


class MyPage(Page):
    form_model = 'player'
    form_fields = ['lanzamiento_1','lanzamiento_2','lanzamiento_3','lanzamiento_4','lanzamiento_5','lanzamiento_6',
                   'lanzamiento_7','lanzamiento_8','lanzamiento_9','lanzamiento_10','lanzamiento_11', 'lanzamiento_12']
    pass


class Intermedio(Page):
    def is_displayed(self):
        return self.round_number == 1
    form_model = 'player'
    form_fields = ['Seleccione_una_de_las_siguientes_opciones', 'Pago_en_soles']
    # def vars_for_template(self): aca va el codigo


class Results_1(Page):
    def is_displayed(self):
        return self.round_number == 1



class Results_2(Page):
    def is_displayed(self):
        return self.round_number == 2


class Final(Page):
    def is_displayed(self):
        return self.round_number == 2
    form_model = 'player'
    form_fields = ['Seleccione_una_entre_las_siguientes_opciones', 'Que_tan_religioso_te_consideras','Que_tanto_crees_en_dios','Hasta_que_punto_crees_en_un_dios_que_castiga', 'Pago_en_soles']


page_sequence = [
    Instrucciones_1,
    Instrucciones_2,
    Instrucciones_3,
    Instrucciones_4,
    MyPage,
    Results_1,
    Results_2,
    Intermedio,
    Final
]
