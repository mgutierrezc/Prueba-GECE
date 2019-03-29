from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
)
import random


class Constants(BaseConstants):
    name_in_url = 'survey_sr'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_id = models.PositiveIntegerField()
    question = models.CharField()
    submitted_answer = models.CharField(widget=widgets.RadioSelect())

    def current_question(self):
        return self.session.vars['questions'][self.round_number - 1]

    age = models.PositiveIntegerField(
        verbose_name='¿Cuál es tu edad?',
        min=13, max=125)

    gender = models.CharField(
        choices=['Masculino', 'Femenino', 'Otro'],
        verbose_name='¿Cuál es tu género?',
        widget=widgets.RadioSelect())

    carrera_padres= models.CharField(
        verbose_name='¿Alguno de tus padres estudió la misma carrera que tú?',
        choices=['Si', 'No'],
        widget=widgets.RadioSelect)

    escala = models.PositiveIntegerField(
        choices=[
            [0, 'Escala 1 (antigua)'],
            [1, 'Escala 2 (antigua)'],
            [2, 'Escala 3 (antigua)'],
            [3, 'Escala 4 (antigua)'],
            [4, 'Escala 5 (antigua)'],
            [5, 'Escala 1 (nueva)'],
            [6, 'Escala 2 (nueva)'],
            [7, 'Escala 3 (nueva)'],
            [8, 'Escala 4 (nueva)'],
            [9, 'Escala 5 (nueva)'],
            [10, 'Escala 6 (nueva)'],
            [11, 'Escala 7 (nueva)'],
            [12, 'Escala 8 (nueva)'],
            [13, 'Escala 9 (nueva)'],
        ],
        verbose_name='¿En qué escala de pago te encuentras',
    )

    field_studies = models.PositiveIntegerField(
        choices=[
            [1, 'Administración de Negocios'],
            [2, 'Economía'],
            [3, 'Biología'],
            [4, 'Química'],
            [5, 'Ingeniería'],
            [6, 'Filisofía'],
            [7, 'Psicología'],
            [8, 'Física'],
            [9, 'Derecho'],
            [10, 'Historia'],
            [11, 'Lengua y Literatura Inglesa'],
            [12, 'Arqueología'],
            [13, 'Lengua y Literatura Alemana'],
            [14, 'Bioquímica'],
            [15, 'Bioinformática'],
            [16, 'Ciencias de la Nutrición'],
            [17, 'Ciencias de la Educación'],
            [18, 'Teología'],
            [19, 'Geografía'],
            [20, 'Lengua y Literatura Romana'],
            [21, 'Geología'],
            [22, 'Filología'],
            [23, 'Ciencias de la Computación'],
            [24, 'Tecnología de la información comercial'],
            [25, 'Lenguas Indo Germánicas'],
            [26, 'Historia del Arte'],
            [27, 'Matemáticas'],
            [28, 'Ciencia de los Medios'],
            [29, 'Musicología'],
            [30, 'Idiomas y Literatura Eslava'],
            [31, 'Farmacia'],
            [32, 'Ciencias Políticas'],
            [33, 'Sociología'],
            [34, 'Ciencias del Deporte'],
            [35, 'Prehistoria e Historia temprana'],
            [36, 'Odontología'],
            [37, 'Tecnología Médica'],
            [38, 'Antropología'],
            [99, 'Otro / No Aplica']
        ],
        verbose_name='¿Qué carrera estudias?',
    )

    ciclo = models.PositiveIntegerField(
        choices=[
            [1, '1'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9'],
            [10, '10'],
            [11, '11'],
        ],
        verbose_name='¿En qué ciclo de la carrera te encuentras?',
    )

    preg11 = models.CharField(
        choices=['Si', 'No'],
        verbose_name='¿Cree que el dueño notificaría el error?',
        widget=widgets.RadioSelect())

    preg12 = models.CharField(
        choices=['Si', 'No'],
        verbose_name='¿Usted notificaría el error?',
        widget=widgets.RadioSelect())

    preg21 = models.CharField(
        choices=['Si', 'No'],
        verbose_name='¿Cree que si un extraño encontrara el sobre se lo devolvería?',
        widget=widgets.RadioSelect())

    preg22 = models.CharField(
        choices=['Si', 'No'],
        verbose_name='¿Si usted encontrara el sobre que se le cayó a otra persona, se lo devolvería?',
        widget=widgets.RadioSelect())
    # crt_bat = models.PositiveIntegerField(
    #     verbose_name='''
    #     Un bate y una pelota cuesta 22 soles en total.
    #     El bate cuesta 20 soles mas que la pelota.
    #     ¿Cuántos soles cuesta la pelota?'''
    # )
    #
    # crt_widget = models.PositiveIntegerField(
    #     verbose_name='''
    #     "If it takes 5 machines 5 minutes to make 5 widgets,
    #     how many minutes would it take 100 machines to make 100 widgets?"
    #     '''
    # )
    #
    # crt_lake = models.PositiveIntegerField(
    #     verbose_name='''
    #     In a lake, there is a patch of lily pads.
    #     Every day, the patch doubles in size.
    #     If it takes 48 days for the patch to cover the entire lake,
    #     how many days would it take for the patch to cover half of the lake?
    #     '''
    # )
