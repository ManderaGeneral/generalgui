"""Random testing"""

import generalgui


from generalgui import Label, Page, App, _Value
# from generalgui.cartridge.tkinter import Label, Page, App


app = App()
# app.bgcolor = "green"
#
# page = Page(app)
# page.bgcolor = "yellow"
#
# label = Label("hello!", page)
# label.bgcolor = "red"
#
# label2 = Label("bar", page)
# label2.bgcolor = "blue"







# label = Label()
# label.value = 5

# copy = label.copy_to(label.get_parent())



# Label(parent=label.get_parent())

# print(App.load(label.app().save()).save())





# app = App()

# print(app.App)








# Save / Load
# part = Part(None, "Label")
# Part(part, "Button")
# Part(part, "Dropdown")
# saved = part.save()
# print(part)
# print(saved)
# part_loaded = Part.load(saved)
# print(part_loaded)
# print(part_loaded.save())



# pprint(label.app.storage)



# print(label, label.all_parents())

# print(label.get_parent().storages)

# print(label.app.store_get_dict())


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