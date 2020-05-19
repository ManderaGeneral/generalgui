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
 * Never use a widget directly, always go through an Element subclass.
 * .parentPage attribute in Label goes to Page.
 * .parentPart attribute in Label goes to Page's Frame.
 * Every part has a .parentPage and .parentPart attribute.
 * An Element can never have more than one widget.
 * A widget only has .element attribute.
 * Element can only be put inside a Page, so create subpages if needed.

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
Split page

