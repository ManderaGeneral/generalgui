
from generallibrary import initBases
from generalgui.decorators import deco_group_top
from generalgui.properties_private.create import Create_Tkinter


class Create_Construct:
    """ Should contain all data necessary to encode."""
    def __init__(self, parent=None):
        """ :param generalgui.MethodGrouper self: """
        self._created = False
        self._parent = None
        
        self.set_parent(parent)
        self.set_created(True)

    @deco_group_top
    def get_created(self):
        """ Get whether this part is created.
            
            :param generalgui.MethodGrouper self: """
        return self._created

    @deco_group_top
    def set_created(self, created):
        """ Create or remove this part.

            :param generalgui.MethodGrouper self:
            :param bool created: """
        if self.get_created():
            self._destroy()
        
        if created:
            self._create()
        
        self._created = created

    @deco_group_top
    def get_parent(self):
        """ Get this part's parent.

            :param generalgui.MethodGrouper self: """
        return self._parent

    @deco_group_top
    def set_parent(self, parent):
        """ Set this part's parent.

            :param generalgui.MethodGrouper self:
            :param generalgui.MethodGrouper parent: """
        self._change_args(_master=parent._widget)
        self._parent = parent


class Create_Relations:
    """ . """
    pass


class Create_Store:
    """ . """
    pass


@initBases
class Create(Create_Construct, Create_Relations, Create_Store, Create_Tkinter):
    """ Contains all methods having to do with creating a GUI part. """
    
    @property
    def app(self):
        """ :param generalgui.MethodGrouper self: """
        while True:
            return self if self.__class__ == self.App else self.parent().app



class Value:
    def __init__(self, value=None):
        self._value = None

        self.set_value(value)

    def get_value(self):
        """ Get this part's value.

            :param generalgui.MethodGrouper self: """
        return self._value

    def set_value(self, value):
        """ Set this part's parent.

            :param generalgui.MethodGrouper self:
            :param value: """
        self._value = value




































