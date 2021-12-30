from generalgui.elements.page import Page
from generalgui.elements.label import Label
from generalgui.elements.button import Button
from generalgui.elements.checkbutton import Checkbutton
from generalgui.elements.entry import Entry
from generalgui.elements.subelements.password import Password

from generalgui.pages.plot import PlotPage
from generalgui.pages.signin import SigninPage
from generalgui.pages.payment import PaymentPage

class MethodGrouper(SigninPage, PlotPage, Page, Label, Button, Checkbutton, Password, Entry):
    pass
