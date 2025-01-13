from typing import Tuple, List, Dict
from flask import render_template
import queries


def get_series_data(db: str, series_id: int) -> Tuple[Dict, List, List]:
    """Helper function to get common series data"""

    series = queries.get_info_series(db, series_id)
    schedules = queries.get_info_schedules(db, series_id)
    series_ids = queries.get_info_series_ids(db)

    return series, schedules, series_ids


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

