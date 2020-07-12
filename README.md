# generalgui
Extends and simplifies tkinter functionality with built-in QoL improvements.

* Makes tkinter easy to use with some built-in QoL improvements.
* Built on top of tkinter, intended to extend features.
* Three main parts: App, Page and Element.
* Cannot partially use generalgui, everything has to be from here or nothing.

## Installation
```
pip install generalgui
```

## Usage example
Simple Button
```python
from generalgui import App, Page, Button

btn = Button(Page(App(), pack=True), "Click me", lambda: btn.setValue("Changed value"))
btn.show()
```

Spreadsheet
```python
from generalgui import App, Page, Spreadsheet
import pandas as pd
import random

df = pd.DataFrame([[random.randint(-100, 100) for _ in range(20)] for _ in range(20)])
page = Page(App())
Spreadsheet(page, cellVSB=True).loadDataFrame(df)
page.show()
```


## Parts
#### App
Main part.
Controls everything.
Tk is 'widget' attribute.  

#### Page
Middle part, controls Frame (and Canvas if scrollable).
Has no 'widget'. getBaseWidget() / getTopWidget().
Contains any amount of Elements and Pages.  
Can be subclassed to create pre-built pages easily.
Has to be packed manually.

#### Element
Smallest part, controls widget.
Tkinter widget is 'widget' attribute.  
Packed automatically because it always has to be inside a page.  

## Guidelines
 * An Element always controls one widget. It also has the same name as the tkinter widget it's controlling.
 * A tkinter widget only has .element attribute.
 * Always use an Element's method if you can, otherwise you can always access element.widget to use tkinter directly.
 * .parentPage attribute in Label goes to Page.
 * .parentPart attribute in Label goes to Page's Frame.
 * Every part has a .parentPage and .parentPart attribute.
 * Element can only be put inside a Page, not Frame, so create subpages if needed.
 * Elements are packed directly because they need a parent page.
 
 * Only have one method with the same name, even if it's shared. So no overriding.

## Terms
Term | Meaning
---|---
Widget | A tkinter widget such as Label and Button.
Part | An App, Page or Element from generalgui

## Attributes
.  | .parentPage   | .parentPart   | .widget   | .element
---|---|---|---|---
App         | -             | -             | tk.Tk     | -
Page        | Page or App   | Frame or App  | -         | -
Element     | Page          | Frame         | tk.Label  | -
Widget      | -             | -             | -         | Element

## Todo
 * Menu should probably inherit page so it becomes reuseable
 * getElement(s)By* inspired by js
 * Unique default style
 * Automatic app and page creation
 * Scale element / element.setSize()

## Features
 * Easily make pages resizeable or scrollable.
 * Styler which handles multiple stacked styles and automatically updates config.
 * Lists all queued "after" functions and allows **kwargs when creating one.
 * Entry: Ctrl+Del/Backspace to remove entire words.
 * Entry: Press enter to press the next Button.
 * Entry: Click outside Entry to remove selection.
 * Right click anywhere to show a menu, propagates through elements to combine menus.
 * Spreadsheet with optional locked headers and capable of loading and saving TSV files.
 * ElementList which nicely stacks groups of buttons for example in a certain pattern.
 * Combined Elements such as LabelEntry which easily allows you to get/set values.
 * Default menu option to 'Rainbow' which colors all widgets in a random color for debugging.
 
#### Elements
 * Button
 * Canvas
 * Checkbutton
 * Entry
 * Frame
 * Label
 * OptionMenu
 * Scrollbar

#### Combined Elements
 * Grid(Page)
 * Spreadsheet(Page: Grids)
 * ElementList(Grid)
 * InputList(ElementList)
 * LabelCheckbutton(Page: Label and Checkbutton)
 * LabelEntry(Page: Label and Entry)

#### Unsupported Elements
 * Radiobutton
 * Combobox
 * Listbox
 * SizeGrip
 * Text
 * Progressbar
 * Scale
 * Spinbox
 * -Probably missing some