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
label2 = Label(page, "hi")

print(page.get_children())
print(label, label2)

# for i in range(2):
#     btn = Button(page, str("hi"))
#     # btn = Button(page, str(random.randint(1, 1000)))
#     btn.bind(lambda x=btn: test2(x))

# page.view()
copy = page.copy_node()
assert page.view(print_out=False) == copy.view(print_out=False)
# copy.view()



# print(a.get_children(depth=-1, include_self=True, flat=False))


draw = page.draw()









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