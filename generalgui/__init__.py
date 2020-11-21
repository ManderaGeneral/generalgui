from generalgui.properties.generic.generic import _Generic
from generalgui.properties.generic.create.create import _Create
from generalgui.properties.generic.create.contain.contain import _Contain
from generalgui.properties.generic.create.value.value import _Value

from generalgui.app import App
from generalgui.page import Page
from generalgui.elements import Label, Button


class MethodGrouper(App, Page, Label, Button, _Value, _Contain, _Create, _Generic):
    """ For code auto completion through reST docs. """
