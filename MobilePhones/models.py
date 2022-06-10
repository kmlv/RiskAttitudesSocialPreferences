from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Marco Gutierrez'

doc = """
Mobile devices blocker for oTree Experiments

Add it at the beginning of your project and it'll automatically work
"""


class Constants(BaseConstants):
    name_in_url = 'MobilePhones'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
