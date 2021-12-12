
from generalgui import Page, Label, Entry, Password, Button


class SigninPage(Page):
    """ General sign in Page. """
    client = ...

    def __init__(self, parent=None):
        self.label = Label(self, "Welcome")

        self.email = Entry(self)
        self.password = Password(self, hidden=True)

        self.email.text = "tests@gmail.com"
        self.password.text = "hellothere"

        buttons = Page(self)
        self.button_signin = Button(buttons, "Sign in", self.signin)
        self.button_register = Button(buttons, "Register", self.register)

    def hook_signin_success(self, response): ...

    def signin(self):
        email = self.email.text
        password = self.password.text
        response = self.client.signin(email=email, password=password)
        if response.status_code == 200:
            self.hook_signin_success(response=response)
        else:
            self.label.text = response.text
        return response

    def register(self):
        email = self.email.text
        password = self.password.text
        response = self.client.register(email=email, password=password)
        self.label.text = response.text
        return response

