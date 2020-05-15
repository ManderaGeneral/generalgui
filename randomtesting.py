"""Random testing"""

from generalgui import Page, Button, Entry, LabelEntry


page = Page()


labelEntry = LabelEntry(page, "Name:", "Mandera", 10)

Button(page, "Click me", lambda: labelEntry.label.setValue(labelEntry.entry.getValue()))

page.show()

