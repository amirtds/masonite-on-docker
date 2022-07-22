"""Web Routes."""

from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show").name("welcome"),
    Route.get("/sample", "WelcomeController@show").name("welcome"),
    Route.post("/", "WelcomeController@upload"),
]
