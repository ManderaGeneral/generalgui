# generalgui
Extends and simplifies tkinter functionality with built-in QoL improvements.

This package and 6 other make up [ManderaGeneral](https://github.com/ManderaGeneral).

## Information
| Package                                                    | Ver                                           | Latest Release       | Python                                                                                                                   | Platform        |   Lvl | Todo                                                   | Tests   |
|:-----------------------------------------------------------|:----------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------|:----------------|------:|:-------------------------------------------------------|:--------|
| [generalgui](https://github.com/ManderaGeneral/generalgui) | [2.0.3](https://pypi.org/project/generalgui/) | 2021-12-10 18:59 CET | [3.8](https://www.python.org/downloads/release/python-380/), [3.9](https://www.python.org/downloads/release/python-390/) | Windows, Ubuntu |     2 | [9](https://github.com/ManderaGeneral/generalgui#Todo) | 66.6 %  |

## Contents
<pre>
<a href='#generalgui'>generalgui</a>
├─ <a href='#Information'>Information</a>
├─ <a href='#Contents'>Contents</a>
├─ <a href='#Installation'>Installation</a>
├─ <a href='#Attributes'>Attributes</a>
└─ <a href='#Todo'>Todo</a>
</pre>

## Installation
| Command                  | <a href='https://pypi.org/project/generalvector'>generalvector</a>   | <a href='https://pypi.org/project/generallibrary'>generallibrary</a>   | <a href='https://pypi.org/project/generalfile'>generalfile</a>   | <a href='https://pypi.org/project/pandas'>pandas</a>   | <a href='https://pypi.org/project/numpy'>numpy</a>   |
|:-------------------------|:---------------------------------------------------------------------|:-----------------------------------------------------------------------|:-----------------------------------------------------------------|:-------------------------------------------------------|:-----------------------------------------------------|
| `pip install generalgui` | Yes                                                                  | Yes                                                                    | Yes                                                              | Yes                                                    | Yes                                                  |

## Attributes
<pre>
<a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/__init__.py#L1'>Module: generalgui</a>
├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/elements/button.py#L1'>Class: Button</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/text.py#L1'>Method: draw_text</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/text.py#L1'>Property: text</a>
├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/elements/checkbutton.py#L1'>Class: Checkbutton</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/text.py#L1'>Method: draw_text</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/text.py#L1'>Property: text</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/toggle.py#L1'>Method: toggle</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/toggle.py#L1'>Method: toggled</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/elements/entry.py#L1'>Class: Entry</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/text.py#L1'>Method: draw_text</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/text.py#L1'>Property: text</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/toggle.py#L1'>Method: toggle</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/toggle.py#L1'>Method: toggled</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/elements/label.py#L1'>Class: Label</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/text.py#L1'>Method: draw_text</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/text.py#L1'>Property: text</a>
├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/__init__.py#L1'>Class: MethodGrouper</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/text.py#L1'>Method: draw_text</a> <b>(Untested)</b>
│  ├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/text.py#L1'>Property: text</a>
│  ├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/toggle.py#L1'>Method: toggle</a> <b>(Untested)</b>
│  └─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/properties/toggle.py#L1'>Method: toggled</a> <b>(Untested)</b>
├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/elements/page.py#L1'>Class: Page</a>
├─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/elements/subelements/password.py#L1'>Class: Password</a> <b>(Untested)</b>
└─ <a href='https://github.com/ManderaGeneral/generalgui/blob/7d7f6e2/generalgui/pages/plot.py#L1'>Class: Plot</a> <b>(Untested)</b>
</pre>

## Todo
| Module                                                                                                                            | Message                                                                                                                                              |
|:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/properties/editable.py#L1'>editable.py</a>           | <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/properties/editable.py#L5'>Move trace to generallibrary.</a>            |
| <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/properties/text.py#L1'>text.py</a>                   | <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/properties/text.py#L30'>[UnitTest] for Method: draw_text</a>            |
| <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/elements/checkbutton.py#L1'>checkbutton.py</a>       | <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/elements/checkbutton.py#L10'>[UnitTest] for Class: Checkbutton</a>      |
| <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/properties/toggle.py#L1'>toggle.py</a>               | <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/properties/toggle.py#L23'>[UnitTest] for Method: toggle</a>             |
| <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/properties/toggle.py#L1'>toggle.py</a>               | <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/properties/toggle.py#L20'>[UnitTest] for Method: toggled</a>            |
| <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/elements/entry.py#L1'>entry.py</a>                   | <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/elements/entry.py#L10'>[UnitTest] for Class: Entry</a>                  |
| <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/__init__.py#L1'>__init__.py</a>                      | <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/__init__.py#L10'>[UnitTest] for Class: MethodGrouper</a>                |
| <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/elements/subelements/password.py#L1'>password.py</a> | <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/elements/subelements/password.py#L5'>[UnitTest] for Class: Password</a> |
| <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/pages/plot.py#L1'>plot.py</a>                        | <a href='https://github.com/ManderaGeneral/generalgui/blob/master/generalgui/pages/plot.py#L5'>[UnitTest] for Class: Plot</a>                        |

<sup>
Generated 2021-12-10 18:59 CET for commit <a href='https://github.com/ManderaGeneral/generalgui/commit/7d7f6e2'>7d7f6e2</a>.
</sup>
