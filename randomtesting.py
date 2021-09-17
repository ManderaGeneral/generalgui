"""Random testing"""


from generalgui import Page, Label, Button
from generallibrary import getBaseClassNames

import random


def test():
    print(5)

def test2(part):
    # part.get_parent().copy_part()
    # part.copy_part()
    # part.copy_part(part.get_parent())
    # part.remove_node()
    # part.shown = False
    part.value = "hello"

page = Page()
# b = page.add_node()  # This doesnt work now for some reason
label = Label(page, "hi")

data = label.get_data_tuple()
label.bind(lambda: 5)
print(data)
# label2 = Label(page, "hi")
# label.copy_part(page)

for i in range(2):
    # btn = Button(page, str("hi"))
    btn = Button(page, str(random.randint(1, 1000)))
    btn.bind(lambda x=btn: test2(x))

page.view()
# copy = page.copy_node()
# assert page.view(print_out=False) == copy.view(print_out=False)
# copy.view()



# print(a.get_children(depth=-1, include_self=True, flat=False))


draw = page.draw()




"""
Divide all parts into batches to detect changes, in the future we could direct it somehow if it notices one part keeps updating
Instead of drawing all we should keep a different set of parts for drawn, that way we have a current tree and a target tree


---------

Trying to figure out a better way to detect change, previously I've compared reprs, too slow
Thinking to use one huge tuple, constructed of each part and it's attrs
Maybe this tuple could be deterministic (probably should be), if it is then we could draw the gui from the tuple purely, should be fast

We don't actually need to keep track of binds because we don't need to redraw anything if bind changes, simply store bool to create the bind or not
I don't think we're gonna need id either, now that we're moving away from sets

Maybe the attrs used can be dynamically made from pars required to init each part
    Instead of one big tuple we could have a big tuple containing tuples
    Because the number of slots would otherwise increase for every part, even if only one uses it

Not sure about using tuples instead of top part
    Aren't we going to have to iterate parts anyway to create the tuple?
    I think it would only make sense if changing a value would change the tuple directly, in which case it'd have to be a list
    Think I'll scratch this whole idea
"""






# WANT: Easy autocompletion for each arg
# WANT: Ability to configure multiple
# WANT: Automatic updating when changing a value
# WANT: Allowing adding to args lower in hierarchy (i.e. value for Label)

# DONT: Update after changing one of multiple values, only once
# DONT: Rely on manual updating as it's prone for de-sync issues

# IDEA: Remove config method, make them all attributes,
# IDEA: Convert old Styler to a config class for generallibrary, use that here
# Give combined lists to Config class, then add code for our purpose




# Create_Construct
    # @deco_group_top
    # def get_shown(self, propagate=True):
    #     """ Get whether this part and all its parents aren't is_hidden.
    #
    #         :param generalgui.MethodGrouper self:
    #         :param propagate: """
    #     if not propagate:
    #         return self._shown
    #
    #     for part in self.parents(include_self=True):
    #         if not part.get_shown(propagate=False):
    #             return False
    #     return True
    #
    # @deco_group_top
    # def set_shown(self, shown):
    #     """ Show this part.
    #         If this part doesn't have a widget then it's created.
    #         If widget is hidden then it's re-packed.
    #
    #
    #         :param generalgui.MethodGrouper self:
    #         :param shown: """
    #     if shown:
    #         self._shown = False
    #         if self.destroy_when_hidden:
    #             return self.remove()
    #         else:
    #             self.widget.hide()
    #     else:
    #         pass
    #
    # @deco_group_top
    # def get_removed(self):
    #     """ Remove this part from it's parent's children and destroys widget.
    #
    #         :param generalgui.MethodGrouper self: """
    #
    # @deco_group_top
    # def set_removed(self):
    #     """ Remove this part from it's parent's children and destroys widget.
    #
    #         :param generalgui.MethodGrouper self: """
    #     if self.parent():
    #         self.parent().children.remove(self)
    #
    #     self._parent = None
    #     self._destroy()