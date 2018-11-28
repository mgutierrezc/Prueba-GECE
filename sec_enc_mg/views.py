from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants
import config_leex_1

class Introduction(Page):
    #wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number == 1

class Offer(Page):
    form_model = 'player'
    form_fields = ['sent_amount']

    def sent_amount_max(self):
        return self.player.endowment

    def is_displayed(self):
        if self.group.get_endowment_A() <= self.group.get_endowment_B():
            return self.player.id_in_group == 2
        elif self.group.get_endowment_A() > self.group.get_endowment_B():
            return self.player.id_in_group == 1

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def vars_for_template(self):

        if self.player.id_in_group == 2:
            a = str(self.group.get_endowment_A())
            b = str(self.group.get_endowment_B())
            #a = str(self.pB.endowment)
            body_text = 'Tu dotación es de ' + b + '. La dotación del otro jugador es ' + a + '. \n Por favor, espere'
            return {'body_text': body_text}
        elif self.player.id_in_group == 1:
            a = str(self.group.get_endowment_A())
            b = str(self.group.get_endowment_B())
            body_text = 'Tu dotación es de ' + a + '. La dotación del otro jugador es ' + b + '. \n Por favor, espere'
            return {'body_text': body_text}

class Results(Page):
    """This page displays the earnings of each player"""

    def vars_for_template(self):
        if self.group.get_endowment_A() <= self.group.get_endowment_B():
            text_A1 = ''
            text_A2 = ''
            text_B1 = '+' + str(self.group.get_sent_amount_B())
            text_B2 = '-' + str(self.group.get_sent_amount_B())
            return {'text_A1': text_A1, 'text_A2': text_A2, 'text_B1': text_B1, 'text_B2': text_B2}
        elif self.group.get_endowment_A() > self.group.get_endowment_B():
            text_A1 = '+' + str(self.group.get_sent_amount_A())
            text_A2 = '-' + str(self.group.get_sent_amount_A())
            text_B1 = ''
            text_B2 = ''
            return {'text_A1': text_A1, 'text_A2': text_A2, 'text_B1': text_B1, 'text_B2': text_B2}


#    def vars_for_template(self):
#        if self.group.get_endowment_A() <= self.group.get_endowment_B():
#            text_A = '. \nEl otro participante te ha enviado ' + str(self.group.get_sent_amount_B())+ ' de un total de '+ str(self.group.get_endowment_B()) +'.'
#            text_B = ', de los cuales tu enviaste ' + str(self.group.get_sent_amount_B()) +' al otro participante.\nEl monto inicial del otro jugador fue ' + str(self.group.get_endowment_A()) + ' .'
#            return {'text_A':text_A, 'text_B':text_B}
#        elif self.group.get_endowment_A() > self.group.get_endowment_B():
#            text_A = ', de los cuales tu enviaste ' + str(self.group.get_sent_amount_A()) +' al otro participante.\nEl monto inicial del otro jugador fue ' + str(self.group.get_endowment_B()) + ' .'
#            text_B = '. \nEl otro participante te ha enviado ' + str(self.group.get_sent_amount_A())+ ' de un total de '+ str(self.group.get_endowment_A()) +'.'
#            return {'text_A':text_A, 'text_B':text_B}

page_sequence = [
    Introduction,
    Offer,
    ResultsWaitPage,
    Results,
]

