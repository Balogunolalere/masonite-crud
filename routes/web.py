"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    #Get("/", "WelcomeController@show").name("welcome"),
    Get('/', 'Home@show').name("welcome"),
    Get('/post', 'PostController@show'),
    Post('/post/create', 'PostController@store'),
    Get('/articles', 'BlogController@show'),
    Get('/articles/@id/update', 'BlogController@update').name('update'),
    Post('/articles/@id/update', 'BlogController@store').name('edit'),
    Get('/articles/@id/delete', 'BlogController@remove').name('remove'),
    Post('/articles/@id/deleted', 'BlogController@delete').name('delete'),
]
