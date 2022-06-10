from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class TestMobile(Page):
    def is_displayed(self):
        # Here, we'll obtain the type of user we've
        user_agent = self.request.META['HTTP_USER_AGENT']
        # Default value
        self.participant.vars['MobilePhones'] = False
        # The default is changed if the player is mobile
        for substring in ['Mobi', 'Android']:
            if substring in user_agent:
                self.participant.vars['MobilePhones'] = True
        return self.participant.vars['MobilePhones']


class Results(Page):
    pass


page_sequence = [
    TestMobile
]
