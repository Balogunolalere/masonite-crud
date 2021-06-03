"""A BlogController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Post import Post

class BlogController(Controller):
	"""BlogController Controller Class."""

	def __init__(self, request: Request):
		"""BlogController Initializer

		Arguments:
			request {masonite.request.Request} -- The Masonite Request class.
		"""
		self.request = request

	def show(self, view: View):
		posts = Post.all()
		return view.render('posts', {'posts':posts})

	def update(self, view: View, request: Request):
			post = Post.find(request.param('id'))

			return view.render('article', {'post': post})

	def store(self, request:Request):
		post = Post.find(request.param('id'))
		post.body = request.input('body')
		post.save()
		return request.redirect('/articles')

	def remove(self,view:View,request:Request):
		post = Post.find(request.param('id'))

		return view.render('delete',{'post':post})

	def delete(self, request:Request):
		post = Post.find(request.param('id'))

		post.delete()

		return request.redirect('/articles')