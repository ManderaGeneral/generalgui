
import atexit

from generallibrary import initBases, SigInfo

from generalgui.properties import Generic, Create, Contain


@initBases
class App(Generic, Create, Contain):
    apps = []
    def __init__(self):
        self.widget_sig_info = SigInfo(self.tk.Tk)
        Create.widget(self.tk.Tk)

        self._add_app()

    def _add_app(self):
        if not self.apps:
            atexit.register(App._mainloop)

        self.apps.append(self)

    @classmethod
    def _mainloop(cls):
        for app in cls.apps:
            app.show()

        cls.tk.mainloop()

Generic.App = App


