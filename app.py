import os
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
import pprint 

# SQL
import queries 


# Configure application
app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set SQLite database variable
db = "lafs.db"

# Make sure Google Maps API key is set
if not os.environ.get("MAP_API_KEY"):
    print("INFO: MAP_API_KEY not set")
    print("INFO: Get a Google Maps API Key")
    print("INFO: On terminal, excecute: 'export MAP_API_KEY=value'")

    raise RuntimeError("MAP_API_KEY not set")
else:
    print("MAP_API_KEY set")
    map_api_key = os.environ.get("MAP_API_KEY")
    

@app.route("/", methods=["GET", "POST"])
def index():

    # Populate Bottom Container
    # Website opens with list of films and their scheduled showtimes for current series

    if request.method == "POST":
        return redirect("/")

    else:

        # Get info of [current] series id
        query_result = queries.get_id_current_series(db)
        
        # Update session
        session["active_series_id"] = session["current_series_id"] = query_result[0]

        # NOTE: For development purposes, change current_series_id to first series, not actual current
        session["active_series_id"] = session["current_series_id"] = 1

        # Update function variable series_id
        series_id = session["active_series_id"]

        # Get info on [past] (1) series, (2) schedules, and (3) series ids
        series = queries.get_info_series(db, series_id)
        schedules = queries.get_info_schedules(db, series_id)
        series_ids = queries.get_info_series_ids(db)

        # Print to debug
        # pp = pprint.PrettyPrinter(depth=4)
        # pp.pprint(schedules[0])

        return render_template("index.html", series=series, schedules=schedules, series_ids=series_ids)


@app.route("/series", methods=["GET", "POST"])
def series():

    # Populate Bottom Container
    # List of films and their scheduled showtimes for selected past series

    # Temporary bypass to session timeouts
    try:
        current_series_id = session["current_series_id"]
    except KeyError:
        current_series_id = 1

    if request.method == "POST":

        # Get info of clicked series id 
        series_id = int(request.form.get("series-id"))

        if series_id == current_series_id:
            return redirect("/")
        else:
            # Update session variable active_series_id 
            session["active_series_id"] = series_id

            # Get info on [past] (1) series, (2) schedules, and (3) series ids
            series = queries.get_info_series(db, series_id)
            schedules = queries.get_info_schedules(db, series_id)
            series_ids = queries.get_info_series_ids(db)

        return render_template("index.html", series=series, schedules=schedules, series_ids=series_ids)

    else:
        return redirect("/")


@app.route("/film", methods=["GET", "POST"])
def film():

    # Populate Middle Container - Right
    # Individual film info for any series, current or past

    if request.method == "POST":
        # Get info of [active] series id
        series_id = request.form.get("series-id")
        series_id = int(series_id)

        # Get film_id of requested film
        film_id = request.form.get("film-id")

        # Get info on [past] (1) series, (2) schedules, and (3) series ids
        series = queries.get_info_series(db, series_id)
        schedules = queries.get_info_schedules(db, series_id)
        series_ids = queries.get_info_series_ids(db)

        # Get info of requested film
        film = queries.get_info_film(db, film_id)

        return render_template("film.html", series=series, schedules=schedules, series_ids=series_ids, film=film)

    else:
        return redirect("/")


@app.route("/map")
def map():

    # Populate Middle Container - Right
    # Map of Plym Auditorium

    # Set map_api_key
    global map_api_key

    # Get info of [active] series id
    series_id = session["active_series_id"]

    # Get info on [active] (1) series, (2) schedules, and (3) series ids
    series = queries.get_info_series(db, series_id)
    schedules = queries.get_info_schedules(db, series_id)
    series_ids = queries.get_info_series_ids(db)

    return render_template("map.html", series=series, schedules=schedules, series_ids=series_ids, map_api_key=map_api_key)


@app.route("/org")
def org():

    # Populate Middle Container - Right
    # Info on ORG

    # Get info of [active] series id
    series_id = session["active_series_id"]

    # Get info on [active] (1) series, (2) schedules, and (3) series ids
    series = queries.get_info_series(db, series_id)
    schedules = queries.get_info_schedules(db, series_id)
    series_ids = queries.get_info_series_ids(db)

    return render_template("org.html", series=series, schedules=schedules, series_ids=series_ids)

