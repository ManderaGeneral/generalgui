from generalgui.properties.generic.generic import Generic
from generalgui.properties.generic.create.create import Create
from generalgui.properties.generic.create.contain.contain import Contain
from generalgui.properties.generic.create.value.value import Value

from generalgui.app import App
from generalgui.page import Page
from generalgui.elements import Label, Button


class MethodGrouper(App, Page, Label, Button, Value, Contain, Create, Generic):
    """ For code auto completion through reST docs. """
