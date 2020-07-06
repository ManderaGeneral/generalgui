# generalgui
Makes tkinter easy to use.
Three main parts: App, Page and Element.

## App
Tk is 'widget' attribute.  
'mainPart' attribute is None.

## Page
Frame or ScrollableFrame is 'widget' attribute.  
Contains any amount of Elements and Pages.  
Can be subclassed to create pre-built pages easily.  
Has to be packed manually.  

## Element
Tkinter widget is 'widget' attribute.  
Packed instantly because it always has to be inside a page.  

## Guiderules
 * An Element always controls one widget.
 * A tkinter widget only has .element attribute.
 * Always use an Element's method if you can, otherwise you can always access element.widget to use tkinter directly.
 * .parentPage attribute in Label goes to Page.
 * .parentPart attribute in Label goes to Page's Frame.
 * Every part has a .parentPage and .parentPart attribute.
 * Element can only be put inside a Page, not Frame, so create subpages if needed.
 * Elements are packed directly because they need a parent page.
 
 * Only have one method with the same name, even if it's shared.

## Terms
Term | Meaning
---|---
Widget | A tkinter widget such as Label and Button.
Part | An App, Page or Element from generalgui

## Attributes
Attributes  | .parentPage   | .parentPart   | .widget   | .topElement   | .baseElement  | .element
---|---|---|---|---|---
App         | -             | -             | tk.Tk     | -             | -             | -
Page        | Page or App   | Frame or App  | -         | Frame         | Canvas        | -
Element     | Page          | Frame         | tk.Label  | -             | -             | -
Widget      | -             | -             | -         | -             | -             | Element

## Todo
 * Menu should probably inherit page so it becomes reuseable
 * getElement(s)By* inspired by js

## Features
 * App.widget.after can handle **kwargs and App.afters contains all queued "after" functions
