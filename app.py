import os
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from helpers import get_series_data
import queries


# Configure application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# Set constants
MAP_API_KEY = os.environ.get("MAP_API_KEY")
DATABASE_NAME = os.environ.get("DATABASE_NAME")


@app.route("/", methods=["GET", "POST"])
def index():
    """TODO: function docstring """

    if request.method == "POST":
        return redirect("/")

    # Get info of [current] series id
    query_result = queries.get_id_current_series(DATABASE_NAME)

    # Update session
    session["active_series_id"] = session["current_series_id"] = query_result[0]

    # NOTE: For development purposes, change current_series_id to first series, not actual current
    session["active_series_id"] = session["current_series_id"] = 1

    # Update function variable series_id
    series_id = session["active_series_id"]

    # Get info on [past] (1) series, (2) schedules, and (3) series ids
    series, schedules, series_ids = get_series_data(DATABASE_NAME, series_id)

    return render_template("index.html",
                            series=series,
                            schedules=schedules,
                            series_ids=series_ids)


@app.route("/series", methods=["GET", "POST"])
def series_view():
    """TODO: function docstring """

    current_series_id = session["current_series_id"]

    if request.method == "POST":

        # Get info of clicked series id
        series_id = int(request.form.get("series-id"))

        if series_id == current_series_id:
            return redirect("/")

        # Update session variable active_series_id
        session["active_series_id"] = series_id

        # Get info on [past] (1) series, (2) schedules, and (3) series ids
        series, schedules, series_ids = get_series_data(DATABASE_NAME, series_id)

        return render_template("index.html",
                               series=series,
                               schedules=schedules,
                               series_ids=series_ids)

    return redirect("/")


@app.route("/film", methods=["GET", "POST"])
def film_view():
    """TODO: function docstring """

    if request.method == "POST":
        # Get info of [active] series id
        series_id = request.form.get("series-id")
        series_id = int(series_id)

        # Get film_id of requested film
        film_id = request.form.get("film-id")

        # Get info on [past] (1) series, (2) schedules, and (3) series ids
        series, schedules, series_ids = get_series_data(DATABASE_NAME, series_id)

        # Get info of requested film
        film = queries.get_info_film(DATABASE_NAME, film_id)

        return render_template("film.html",
                               series=series,
                               schedules=schedules,
                               series_ids=series_ids,
                               film=film)

    return redirect("/")


@app.route("/location")
def location_view():
    """TODO: function docstring """

    # Get info of [active] series id
    series_id = session["active_series_id"]

    # Get info on [past] (1) series, (2) schedules, and (3) series ids
    series, schedules, series_ids = get_series_data(DATABASE_NAME, series_id)

    return render_template("location.html",
                           series=series,
                           schedules=schedules,
                           series_ids=series_ids,
                           map_api_key=MAP_API_KEY)


@app.route("/org")
def org_view():
    """TODO: function docstring """

    # Get info of [active] series id
    series_id = session["active_series_id"]

    # Get info on [past] (1) series, (2) schedules, and (3) series ids
    series, schedules, series_ids = get_series_data(DATABASE_NAME, series_id)

    return render_template("org.html",
                           series=series,
                           schedules=schedules,
                           series_ids=series_ids)
