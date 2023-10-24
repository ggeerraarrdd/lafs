import sqlite3


def get_id_current_series(db):
    """Get id of current film series."""

    # Create connection and cursor
    connection = sqlite3.connect(db, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Query db
    query = "SELECT series_id FROM series ORDER BY series_id DESC LIMIT 1;"
    cursor.execute(query)
    current_series_id = cursor.fetchone()
    
    # Close cursor and connection
    cursor.close()
    connection.close()

    return(current_series_id)


def get_info_series(db, series_id):
    """Get info of series."""

    # Create connection and cursor
    connection = sqlite3.connect(db, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Query db
    query = "SELECT s.series_id, "
    query = query + "series_semester || series_year AS semester, "
    query = query + "series_semester, "
    query = query + "series_year, "
    query = query + "series_title, "
    query = query + "series_brief, "
    query = query + "series_poster, "
    query = query + "series_poster_url, "
    query = query + "series_display, "
    query = query + "color1, "
    query = query + "color2, "
    query = query + "color3 "
    query = query + "FROM series s "
    query = query + "JOIN colors AS c ON s.series_id = c.series_id "
    query = query + "WHERE s.series_id = ?; "
    cursor.execute(query, (series_id,))
    results = cursor.fetchone()

    # Close cursor and connection
    cursor.close()
    connection.close()

    return(dict(results))


def get_info_schedules(db, series_id):
    """Get info of series schedules."""

    # Create connection and cursor
    connection = sqlite3.connect(db, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Query db
    query = "SELECT strftime('%d', schedule) AS day, "
    query = query + "f.id, "
    query = query + "rtrim (substr ('January  February March    April    May      June     July     August   SeptemberOctober  November December', strftime ('%m', schedule) * 9 - 8, 9)) AS month, "
    query = query + "film_title, film_director, film_year, film_runtime "
    query = query + "FROM series AS se "
    query = query + "JOIN schedules AS sc ON se.series_id = sc.series_id "
    query = query + "JOIN films AS f ON sc.film_id = f.id "
    query = query + "WHERE se.series_id = ?; "
    cursor.execute(query, (series_id,))

    # Get rows
    rows = cursor.fetchall()

    # Get the column names from cursor.description
    columns = [column[0] for column in cursor.description]

    # Convert each row into a dictionary using zip
    result = [dict(zip(columns, row)) for row in rows]

    # Close cursor and connection
    cursor.close()
    connection.close()

    return(result)


def get_info_series_ids(db):
    """Get info of series ids."""

    # Create connection and cursor
    connection = sqlite3.connect(db, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Query db
    query = "SELECT DISTINCT(series_id), series_semester, series_year, series_display FROM series; "
    cursor.execute(query)

    # Get rows
    rows = cursor.fetchall()

    # Get the column names from cursor.description
    columns = [column[0] for column in cursor.description]

    # Convert each row into a dictionary using zip
    result = [dict(zip(columns, row)) for row in rows]

    return(result)


def get_info_serieses(db):
    """Get info of series ids."""

    # Create connection and cursor
    connection = sqlite3.connect(db, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Query db
    query = "SELECT DISTINCT(series_id), "
    query = query + "series_semester, "
    query = query + "series_year, "
    query = query + "series_display " 
    query = query + "FROM series; "
    cursor.execute(query)

    # Get rows
    rows = cursor.fetchall()

    # Get the column names from cursor.description
    columns = [column[0] for column in cursor.description]

    # Convert each row into a dictionary using zip
    result = [dict(zip(columns, row)) for row in rows]

    return(result)


def get_info_film(db, film_id):
    """Get info of film."""

    # Create connection and cursor
    connection = sqlite3.connect(db, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Query db
    query = "SELECT * "
    query = query + "FROM films "
    query = query + "WHERE id = ?; "
    cursor.execute(query, (film_id,))

    # Get row
    row = cursor.fetchone()

    # Convert row into a dictionary
    result = dict(row)

    return(result)



