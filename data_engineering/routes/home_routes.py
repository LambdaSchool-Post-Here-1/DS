from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

# Create home route


@home_routes.route("/")
def index():

    return "HAKUNA MATADA!!!"  # Return basic string for testing
