"""A Home Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class Home(Controller):
    """Home Controller Class."""

    def __init__(self, request: Request):
        """Home Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render('home')
