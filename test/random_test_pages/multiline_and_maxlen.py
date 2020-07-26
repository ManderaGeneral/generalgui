
from generallibrary.time import sleep
from generallibrary.iterables import combine

from generalgui import App, Grid, Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

from generalvector import Vec2



combinations = combine(
    cls=(Label, Button),
    hideMultiline=(True, False),
    maxLen=(3, 10, None),
    onClick=(None, lambda: print(5)),
    value=("testing\nmultilines", "   leading spaces", "normal")
)


app = App()
page = Page(app)

# Button(page, "Set to single line", lambda: [part.setValue("hello") for part in grid.getChildren()], side="left")
# Button(page, "Set to multiline", lambda: [part.setValue("hello\nthere") for part in grid.getChildren()], side="left")

spreadsheet = Spreadsheet(app)

for i, c in enumerate(combinations):
    c["part"] = c["cls"](spreadsheet, c["value"], hideMultiline=c["hideMultiline"], maxLen=c["maxLen"], onClick=c["onClick"])


print(combinations)
spreadsheet.loadDataFrame(combinations)

spreadsheet.maximize()

app.showChildren(recurrent=True)




# Label(page, "hello\nthere", hideMultiline=True).show()







