class States:
    def __init__(self):
        """ :param generalgui.MethodGrouper self: """
        self._shown = True

    @property
    def shown(self):
        """ :param generalgui.MethodGrouper self: """
        return self._shown

    @shown.setter
    def shown(self, shown):
        """ :param generalgui.MethodGrouper self: """
        self._shown = shown
        self.draw_show()

    def is_hidden_by_parent(self):
        """ :param generalgui.MethodGrouper self: """
        for parent in self.get_parents(depth=-1, gen=True):
            if parent and not parent.shown:
                return True
        return False

    def is_app(self):
        """ :param generalgui.MethodGrouper self: """
        return self.__class__.__name__ == "App"

    def is_page(self):
        """ :param generalgui.MethodGrouper self: """
        return self.__class__.__name__ == "Page"