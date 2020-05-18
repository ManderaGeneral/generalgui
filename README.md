# generalgui
Makes tkinter easy.
Three main parts: App, Page and Element.

## App
Tk is 'widget' attribute.

## Page
Has to be packed manually.
Frame or ScrollableFrame is 'widget' attribute.
Contains any amount of Elements and Pages
Can be subclassed to create pre-built pages easily.

## Element
Packed instantly because it always has to be inside a page.
Tkinter widget is 'widget' attribute.

## Guiderules
 * Never use a widget directly, always go through an Element subclass.
 * parentPage attribute in Label goes to Page.
 * parentPart attribute in Label goes to Page's Frame.
 * Every widget and part has a parentPage and parentPart attribute.
 * An Element can never have more than one widget.

## Terms
Term | Meaning
--- | ---
Widget | A tkinter widget such as Label and Button.
Part | An App, Page or Element from generalgui

