
from tkinter import TclError


class States:
    def __init__(self):
        """ :param generalgui.MethodGrouper self: """
        self._shown = True
        self._exists = True


    # Possibly return False for these if hidden/deleted by parent?
    @property
    def shown(self):
        """ :param generalgui.MethodGrouper self: """
        return self._shown

    @property
    def exists(self):
        """ :param generalgui.MethodGrouper self: """
        return self._exists



    @shown.setter
    def shown(self, shown):
        """ :param generalgui.MethodGrouper self: """
        self._shown = shown
        self.draw_show()

    @exists.setter
    def exists(self, exists):
        """ :param generalgui.MethodGrouper self: """
        self._exists = exists
        self.draw_create()

        if exists:
            for child in self.get_children(depth=-1, gen=True):
                child.draw_create()



    def _shown_tk(self):
        """ :param generalgui.MethodGrouper self: """
        if not self.widget:
            return False
        try:
            return bool(self.widget.winfo_ismapped())
        except TclError:
            return False

    def _exists_tk(self):
        """ :param generalgui.MethodGrouper self: """
        if not self.widget:
            return False
        try:
            return bool(self.widget.winfo_exists())
        except TclError:
            return False



    def is_hidden_by_parent(self):
        """ :param generalgui.MethodGrouper self: """
        for parent in self.get_parents(depth=-1, gen=True):
            if parent and not parent.shown:
                return True
        return False

    def is_deleted_by_parent(self):
        """ :param generalgui.MethodGrouper self: """
        for parent in self.get_parents(depth=-1, gen=True):
            if parent and not parent.exists:
                return True
        return False



    def is_app(self):
        """ :param generalgui.MethodGrouper self: """
        return self.__class__.__name__ == "App"

    def is_page(self):
        """ :param generalgui.MethodGrouper self: """
        return self.__class__.__name__ == "Page"

