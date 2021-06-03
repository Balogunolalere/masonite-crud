"""Post Model."""

from masoniteorm.models import Model


class Post(Model):
    """Post Model."""
    __table__ = 'posts'
    __fillable__ = ['title', 'author', 'body', 'description']