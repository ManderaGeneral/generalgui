"""Random testing"""

from generalgui import Page, Button, Entry


page = Page()


entry = Entry(page, "hello")
Button(page, "Change default", lambda: entry.setDefault("testing"))


entry.show()




