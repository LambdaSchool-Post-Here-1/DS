from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

# Create home route
@home_routes.route("/")
def index():
    return "HAKUNA MATADA!!!" # Return basic string to ensure things are working

    # return render_template() --- To connect to frontend?