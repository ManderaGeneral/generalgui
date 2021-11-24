from generalgui.properties.funcs import _deco_draw_queue


class App:
    @property
    def _tk(self):
        """ :param generalgui.MethodGrouper self: """
        return getattr(self.get_parent(index=-1, depth=-1, include_self=True).widget, "master", None)

    @_deco_draw_queue
    def app_close(self):
        """ :param generalgui.MethodGrouper self: """
        if self._tk:
            self._tk.destroy()

