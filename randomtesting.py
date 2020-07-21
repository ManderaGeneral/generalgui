"""Random testing"""

from generallibrary.time import sleep

from generalgui import App, Grid, Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

from generalvector import Vec2



app = App()

page = Page(app)
Label(page, "test")

page2 = Page(app)

page2a = Page(page2)
page2b = Page(page2)
Button(page2a, "hello", lambda x: print(x.widget.element.app.getChildren(recurrent=True)))

Label(page2b, "hi")


app.showChildren(recurrent=True)




# Label(page, "hello\nthere", hideMultiline=True).show()




