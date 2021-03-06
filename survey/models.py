from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'survey'
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

    provincia= models.CharField(
        verbose_name='¿Indique la provincia en la que reside?',
        choices=['Lima', 'Callao', 'Otro'],
        widget=widgets.RadioSelect )
    ciclo_ingreso = models.PositiveIntegerField(
        choices=[
            [0, '2018 2'],
            [1, '2018 1'],
            [2, '2017 2'],
            [3, '2017 1'],
            [4, '2016 2'],
            [5, '2016 1'],
            [6, '2015 2'],
            [7, '2015 1'],
            [8, '2014 2'],
            [9, '2014 1'],
            [10, '2013 2'],
            [11, '2013 1'],
            [12, '2012 2'],
            [13, '2012 1'],
            [14, '2011 2'],
            [15, '2011 1'],
            [16, '2010 2'],
            [17, '2010 1'],
            [18, '2009 2'],
            [19, '2009 1'],
            [20, '2008 2'],
            [21, '2008 1'],
        ],
        verbose_name='¿En qué ciclo ingresaste a la universidad?',
    )
    escala_pago = models.PositiveIntegerField(
        choices=[
            [0, '1 - Escala antigua'],
            [1, '2 - Escala antigua'],
            [2, '3 - Escala antigua'],
            [3, '4 - Escala antigua'],
            [4, '5 - Escala antigua'],
            [5, '1 - Escala nueva'],
            [6, '2 - Escala nueva'],
            [7, '3 - Escala nueva'],
            [8, '4 - Escala nueva'],
            [9, '5 - Escala nueva'],
            [10, '6 - Escala nueva'],
            [11, '7 - Escala nueva'],
            [12, '8 - Escala nueva'],
            [13, '9 - Escala nueva'],
            [14, 'Becado/Crédito Educativo'],
            ],
        verbose_name='¿Cuál es tu escala de pago?',
    )
    ciclos_egreso = models.PositiveIntegerField(
        choices=[
            [0, '0'],
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
            [12, '12'],
            ],
        verbose_name='¿Cuántos ciclos te faltan para egresar?',
    )
    distrito = models.PositiveIntegerField(
        choices=[
            [0, 'Callao'],
            [1, 'Ancón'],
            [2, 'Ate'],
            [3, 'Barranco'],
            [4, 'Breña'],
            [5, 'Carabayllo'],
            [6, 'Chaclacayo'],
            [7, 'Chorrillos'],
            [8, 'Cieneguilla'],
            [9, 'Comas'],
            [10, 'El Agustino'],
            [11, 'Independencia'],
            [12, 'Jesús María'],
            [13, 'La Molina'],
            [14, 'La Victoria'],
            [15, 'Lima'],
            [16, 'Lince'],
            [17, 'Los Olivos'],
            [18, 'Lurigancho'],
            [19, 'Lurín'],
            [20, 'Magdalena del Mar'],
            [21, 'Miraflores'],
            [22, 'Pachacamac'],
            [23, 'Pucusana'],
            [24, 'Pueblo Libre'],
            [25, 'Puente Piedra'],
            [26, 'Punta Hermosa'],
            [27, 'Punta Negra'],
            [28, 'Rímac'],
            [29, 'San Bartolo'],
            [30, 'San Borja'],
            [31, 'San Isidro'],
            [32, 'San Juan de Lurigancho'],
            [33, 'San Juan de Miraflores'],
            [34, 'San Luis'],
            [35, 'San Martín de Porres'],
            [36, 'San Miguel'],
            [37, 'Santa Anita'],
            [38, 'Santa María del Mar'],
            [39, 'Santa Rosa'],
            [40, 'Santiago de Surco'],
            [41, 'Surquillo'],
            [42, 'Villa El Salvador'],
            [43, 'Villa María del Triunfo'],
            [99, 'Otro / No Aplica']
        ],
        verbose_name='¿Cuál es su distrito de residencia? (seleccione otro si su provincia de residencia no es Lima Metropolitana ni el Callao)',
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
        verbose_name='¿Cuál es su principal campo de estudios?',
    )

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
