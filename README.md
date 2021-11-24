# generalgui
Extends and simplifies tkinter functionality with built-in QoL improvements.

* Makes tkinter easy to use with some built-in QoL improvements.
* Built on top of tkinter, intended to extend features.
* Three main parts: App, Frame and Element.
* Cannot partially use generalgui, everything has to be from here or nothing.

## Installation
```
pip install generalgui
```

## Usage example
Simple Button
```python
from generalgui import App, Frame, Button

btn = Button(Frame(App(), pack=True), "Click me", lambda: btn.setValue("Changed value"))
btn.show()
```

Spreadsheet
```python
from generalgui import App, Frame, Spreadsheet
import pandas as pd
import random

df = pd.DataFrame([[random.randint(-100, 100) for _ in range(20)] for _ in range(20)])
page = Frame(App())
Spreadsheet(page, cellVSB=True).loadDataFrame(df)
page.show()
```


## Parts
#### App
Main part.
Controls everything.
Tk is 'widget' attribute.  

#### Frame
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
 * .parentPage attribute in Label goes to Frame.
 * .parentPart attribute in Label goes to Frame's Frame.
 * Every part has a .parentPage and .parentPart attribute.
 * Element can only be put inside a Frame, not Frame, so create subpages if needed.
 * Elements are packed directly because they need a parent page.
 
 * Only have one method with the same name, even if it's shared. So no overriding.

## Terms
Term | Meaning
---|---
Widget | A tkinter widget such as Label and Button.
Part | An App, Frame or Element from generalgui

## Attributes
.  | .parentPage   | .parentPart   | .widget   | .element
---|---|---|---|---
App         | -             | -             | tk.Tk     | -
Frame        | Frame or App   | Frame or App  | -         | -
Element     | Frame          | Frame         | tk.Label  | -
Widget      | -             | -             | -         | Element

## Todo
 * Menu should probably inherit page so it becomes reuseable
 * getElement(s)By* inspired by js
 * Unique default style to distinguish my package from generic tkinter
 * Automatic app and page creation
 * Scale element / element.setSize()
 * nan in spreadsheet becomes <NA> after saving then loading
 * UnitTest for spreadsheet size syncs
 * UnitTest for label hiding
 * Make all parts visible by default

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
 * Propagating stackable binds through entire app, allows creating one bind for entire Frame or App.
 * Bind propagation options to stop propagation anywhere.
 
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
 * Grid(Frame)
 * Spreadsheet(Frame: Grids)
 * ElementList(Grid)
 * InputList(ElementList)
 * LabelCheckbutton(Frame: Label and Checkbutton)
 * LabelEntry(Frame: Label and Entry)

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

## What's new
#### 1.3.0
 * Made all binds go through App.
 * Which allows us to propagate events through parts.
 * Letting us for example bind an entire page.
 * Changed bindPropagation to just prevent propagating after part.
 * We can do that because we changed Button to use a tk.Label.
 * Silenced error for calling events on removed parts.
 * Made remove() iterate all children to set their 'removed' attribute to True.
 * Made hover and click style enable even if bound after init.


 * Silenced error for hiding resize element.


 * Tried fixing scroll page out of view, but failed so commented.


 * Made hideMultiline skip first spaces in line when hiding.


 * Made hideMultiline skip first empty lines.


 * Fixed multiline hiding for Label.
 * Also made it work in grid, although it doesn't preserve states, but it's probably fine.
 * Fixed issue with Styler where enabling an enabled style caused styles to stack. (Added to test)


 * Overrode Frame.toggleMultilines() in Spreadsheet.toggleMultilines() to only call syncSizes() once.


 * Added toggleMultilines to Label and Frame.
 * Added style for hiddenMultiline Labels.


 * Added 'recurrent' parameter to children methods.


 * Added 'add' parameter for menu().
 * Middle of toggleMultilines() for Frame.


 * Solution for syncing spreadsheet sizes automatically.
 * Added spreadsheetSyncSizesWrappers for Element_Page.
 * Added hideMultiline to Frame, which affects all Labels inside it.
 * Changed Label's hideMultiline parameter to default to it's parentPage.


 * Added a 'hideMultiline' option to Label.
 * Enabled this for all Labels in MainGrid in Spreadsheet.
 * Put all _sync functions in _syncSizes() and bound them to '<Configure>' of MainGrid when df has been loaded.


 * Made spreadsheet prettier.


 * Changed default font to Consolas which is fixed-length and has no kerning. Aka monospace.

#### 1.2.0
 * Alternating bg color in grid by default.
 * Left-align grid by default.
 * Enabled hover color for grid by default.
 
 
 * Added maximize().
 * Added setSize().
 * Added _syncRowKeysHeight to allow linebreak in a cell.
 * Added all getFirstPatternPos parameters to ElementList.
 
 
 * Fixed pixel alignments for spreadsheet.
 * Allowed Float for setSize().
