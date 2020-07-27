
from generallibrary.time import sleep
from generallibrary.iterables import combine

from generalgui import App, Grid, Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

from generalvector import Vec2

import pandas as pd

# combinations = combine(
#     cls=(Label, Button),
#     hideMultiline=(True, False),
#     maxLen=(3, 10, None),
#     onClick=(None, lambda: print(5)),
#     value=("testing\nmultilines", "   leading spaces", "normal")
# )

combinations = combine(
    cls=Label,
    hideMultiline=True,
    maxLen=(5, 2),
    onClick=lambda: print(2),
    value="normal"
)




app = App()
page = Page(app)

# Button(page, "Set to single line", lambda: [part.setValue("hello") for part in grid.getChildren()], side="left")
# Button(page, "Set to multiline", lambda: [part.setValue("hello\nthere") for part in grid.getChildren()], side="left")

spreadsheet = Spreadsheet(app)

for i, c in enumerate(combinations):
    c["part"] = c["cls"](spreadsheet.mainGrid, c["value"], pos=Vec2(1), hideMultiline=c["hideMultiline"], maxLen=c["maxLen"], onClick=c["onClick"])


df = pd.DataFrame(combinations)

print(df.to_string())

exit()


spreadsheet.loadDataFrame(combinations)

spreadsheet.maximize()

app.showChildren(recurrent=True)




# Label(page, "hello\nthere", hideMultiline=True).show()







