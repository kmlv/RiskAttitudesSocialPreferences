# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree import widgets
from otree.common import Currency as c, currency_range
import random
# </standard imports>




class Constants(BaseConstants):
    name_in_url = 'demograp'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time_Demographics = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_CognitiveReflectionTest = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0

    q_country = models.CharField(verbose_name='What country are you from?')

    q_major = models.CharField(verbose_name='What is your major?')

    q_age = models.PositiveIntegerField(verbose_name='What is your age?',
                                        min=18,
                                        max=120)

    q_school_year = models.CharField(initial=None,
                                 verbose_name='What is your school year?',
                                 choices=['Freshman', 'Sophomore','Junior','Senior','Postgraduate','Other'],
                                 widget=widgets.RadioSelect())

    q_station = models.PositiveIntegerField(verbose_name='What is your computer station number? (see white sticker on computer or ask experimenter)',
                                        choices=range(1, 24),
                                        initial=None)

    q_gender = models.CharField(verbose_name='What do you identify as?')

    q_income = models.PositiveIntegerField(verbose_name='What is the approximate annual income of your family?',
                                           choices=[
                                               [1, 'less than $15,000'],
                                               [2, '$15,000 - $29,999'],
                                               [3, '$30,000 - $59,999'],
                                               [4, '$60,000 - $99,999'],
                                               [5, '$100,000 - $199,999'],
                                               [6, '$200,000 or more'],
                                               [7, 'I rather not answer this question'],
                                           ]
                                           )

    q_zipcode = models.PositiveIntegerField(verbose_name='What is the zip code where you grew up?')

    q_opinion = models.CharField(initial=None,
                                 verbose_name='Were the instructions provided in this experiment clear and useful?',
                                 choices=['Yes', 'No'],
                                 widget=widgets.RadioSelect())

    q_linda = models.CharField(initial=None,
                                 verbose_name='Linda is 31 years old, single, outspoken, and very bright. She majored in philosophy. As a student, she was deeply concerned with issues of discrimination and social justice, and also participated in anti-nuclear demonstrations.\n\n Which of the following two alternatives is more probable?',
                                 choices=['Linda is a bank teller.', 'Linda is a bank teller and active in the feminist movement.'],
                                 widget=widgets.RadioSelect())

    q_monty = models.CharField(initial=None,
                                 verbose_name='Assume that a room is equipped with three doors. Behind two are goats, and behind the third is a shiny new car. You are asked to pick a door, and will win whatever is behind it. Someone who knows what is behind the doors opens one of the other two, revealing a goat and asks you if you wish to change your selection, you:',
                                 choices=['change the door.', 'do not change the door.'],
                                 widget=widgets.RadioSelect())

    q_how = models.CharField(verbose_name='How did you make your choices?')

    q_rule = models.CharField(verbose_name='Did you have any rule you applied to your choices?')

    q_number = models.PositiveIntegerField(verbose_name='How many studies have you participated in?')

    crt_bat = models.PositiveIntegerField()

    crt_widget = models.PositiveIntegerField()

    crt_lake = models.PositiveIntegerField()
