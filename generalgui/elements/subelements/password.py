
from generalgui.elements.entry import Entry


class Password(Entry):
    def draw_create_hook(self, kwargs):
        kwargs["show"] = "*"
        return kwargs
