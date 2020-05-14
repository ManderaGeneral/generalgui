"""Random testing"""

from generalgui import Page, Button, Entry, LabelEntry


page = Page()


labelEntry = LabelEntry(page, "Name:", "Mandera", 10)

Button(page, "Click me", lambda: labelEntry.label.setValue(labelEntry.entry.getValue()))

labelEntry.show()


# Have to decide if we show everything when created or hide everything when created.
# Not intuitive whether labelEntry should be shown or hidden by default
# Maybe create a class called PageElement, which inherits from Page but is packed by default?
# I don't want to pack pages by default because with big GUIs it would cause lag I think having to create then hide most pages
