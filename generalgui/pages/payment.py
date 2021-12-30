
from generalgui import Page, Label, Entry, Password, Button

# from generalbrowser import


class PaymentPage(Page):
    """ General payment Page. """
    def __init__(self, parent=None):
        self.label = Label(self, "Payment")
