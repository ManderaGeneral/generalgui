"""Random testing"""

from generallibrary.time import sleep

from generalgui import App, Grid, Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

from generalvector import Vec2



app = App()

page = Page(app)
Label(page, "test", onClick=lambda: print(4))

page2 = Page(app)

page2a = Page(page2)
page2b = Page(page2)
Button(page2a, "hello").onClick(lambda: print(3))

Label(page2b, "hi\nthere\nyo").setBindPropagation("<Button-1>", False)

LabelEntry(page, "testing", "hello")
Entry(page, "testing")

page2.onClick(lambda: print(2))

app.showChildren(recurrent=True)




# Label(page, "hello\nthere", hideMultiline=True).show()




