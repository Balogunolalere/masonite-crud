"""A PostController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Post import Post

class PostController(Controller):
	"""PostController Controller Class."""

	def __init__(self, request: Request):
		"""PostController Initializer

		Arguments:
			request {masonite.request.Request} -- The Masonite Request class.
		"""
		self.request = request

	def show(self, view: View):
		return view.render('post')

	def store(self,request:Request):
		Post.create(
			title=request.input('title'),
			author=request.input('author'),
			description=request.input('description'),
			body=request.input('body')
			)
		return request.redirect('/articles')
