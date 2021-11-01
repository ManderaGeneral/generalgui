

class Toggle:
    """ Contains all methods having to do with containing a part. """
    def __init__(self, toggled):
        """ :param generalgui.MethodGrouper self:
            :param toggled: """
        self._toggled = toggled

        self.bind(self._sync_toggle)

    def _sync_toggle(self):


    def toggled(self):
        return self._toggled

    def toggle(self):
        self._toggled = not self._toggled

    def toggle_on(self):
        self._toggled = True

    def toggle_off(self):
        self._toggled = False



