# Landscape Architecture Film Series Website

An early aughts basic website recreated using modern tools

## Description

> [!NOTE]
> ALL CONTENTS IN THIS REPO ARE FOR EDUCATIONAL PURPOSES ONLY.

In the early aughts, I co-founded the _Landscape Architecture Film Series_ for the Department of Landscape Architecture at the University of Illinois Urbana/Champaign and for which I designed a website.

In need of a website to use as a vehicle to play around with a few AWS services (see [Future Work](#future-work)) but not wanting to spend anytime to ideate and design a new one from scratch, I turned to my [old website](https://web.archive.org/web/20040827234527/http://www.rehearsal.uiuc.edu/projects/filmseries/). Its look and feel has aged well, I think, and indeed looks remarkably contemporary. For instance, if the current version of MoMA's [film series](https://www.moma.org/calendar/film/) is anything to go by, bold color blocking isn't a dated design choice.

This, then, is that 20-year-old static website resurrected as a dynamic web application with a data model to speak of, using modern tools such as Flask, SQLite, VS Code and Git.

_*Note* A custom-made Content Management System (CMS) for the website is in development. Check it out in its own [repo](https://github.com/ggeerraarrdd/lafs-cms)._

![Film Series](/docs/images/film-series1_2.jpg "Landscape Architecture Film Series")

More screenshots below.

## Table of Contents

* [Description](#description)
* [Features](#features)
* [Project Structure](#project-structure)
* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)
  * [Dependencies](#dependencies)
  * [Installation](#installation)
  * [Configuration](#configuration)
  * [Usage](#usage)
* [Author(s)](#authors)
* [Version History](#version-history)
  * [Release Notes](#release-notes)
  * [Initial Release](#initial-release)
* [Future Work](#future-work)
* [License](#license)
* [Contributing](#contributing)
* [Acknowledgments](#acknowledgments)
* [Screenshots](#screenshots)

## Features

* Dynamic web application built with Flask and SQLite
* Modern development tools integration
* Historical archive of a student-led film series website from the early 2000s
* Recreated film database preserving information about past screenings
* Google Maps integration for historical location reference
* Mobile-responsive design preserving original color blocking aesthetic

## Project Structure

```text
film-series/
│
├── app/
│   │
│   ├── blueprints/
│   │   │
│   │   └── main/
│   │       ├── __init__.py
│   │       ├── routes.py
│   │       ├── static/
│   │       └── templates/
│   │
│   ├── config/
│   │   └── __init__.py
│   │
│   ├── crud/
│   │   └── __init__.py
│   │
│   ├── data/
│   │   └── lafs.db
│   │
│   ├── infra/
│   │   └── __init__.py
│   │
│   ├── utils/
│   │   └── __init__.py
│   │
│   └── app.py
│
├── docs/
├── logs/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Prerequisites

TODO

## Getting Started

### Dependencies

* See `requirements.txt`

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ggeerraarrdd/film-series.git
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. **Create an `.env` file:**

    Place the file in the root directory and add the following as default:

    ```python
    # Database Path
    DATABASE_NAME='data/lafs.db'

    # Database Connection Pool
    POOL_SIZE=15
    MAX_OVERFLOW=5
    POOL_TIMEOUT=30
    POOL_RECYCLE=1800
    ECHO=False

    # Database Retry Settings
    MAX_RETRIES=3
    BASE_DELAY=1
    MAX_DELAY=10

    # Flask Secret Key
    SECRET_KEY='your_flask_secret_key'

    # Google Maps API Key
    MAP_API_KEY='your_map_api_key'
    ```

2. **Database**

    ```python
    # Database Path
    DATABASE_NAME='data/lafs.db'  # Path to SQLite database file

    # Database Connection Pool
    POOL_SIZE=15   # Max number of persistent connections
    MAX_OVERFLOW=5  # Max number of connections above POOL_SIZE
    POOL_TIMEOUT=30  # Seconds to wait for available connection
    POOL_RECYCLE=1800  # Seconds before connection is recycled
    ECHO=False  # Enable SQLAlchemy engine logging

    # Database Retry Settings
    MAX_RETRIES=3  #  Max retry attempts for failed operations
    BASE_DELAY=1  # Initial delay between retries in seconds
    MAX_DELAY=10  # Max delay between retries in seconds
    ```

3. **Flask Secret Key**

    ```python
    # Flask Secret Key
    SECRET_KEY='your_flask_secret_key'
    ```

4. **Google Maps API Key**

    ```python
    # Google Maps API Key
    MAP_API_KEY='your_map_api_key'
    ```

    An API Key is needed for the embedded map to work. Before you can create one, you will need to create a Google Cloud project, for which you need a Google Cloud account.

    * [Set up a Google Cloud account](https://cloud.google.com)
    * [Set up your Google Cloud project](https://developers.google.com/maps/documentation/javascript/cloud-setup)
    * [Using API Keys](https://developers.google.com/maps/documentation/javascript/get-api-key)

### Usage

1. **Go into the `app` directory and run the command:**

    ```bash
    flask run
    ```

2. **Open the film series website:**

    Copy and open the URL displayed after 'Running on' in the terminal.

## Author(s)

* [@ggeerraarrdd](https://github.com/ggeerraarrdd/)

## Version History

### Release Notes

* See [https://github.com/ggeerraarrdd/film-series/releases](https://github.com/ggeerraarrdd/film-series/releases)

### Initial Release

The [original website](https://web.archive.org/web/20040827234527/http://www.rehearsal.uiuc.edu/projects/filmseries/) is archived on the Internet Archive.

## Future Work

Improvements and new features development are ongoing.

* Create CMS for user management and content creation and editing _(currently in alpha - see [repo](https://github.com/ggeerraarrdd/lafs-cms))_

## License

* [MIT License](https://github.com/ggeerraarrdd/film-series/blob/main/LICENSE)

## Contributing

* TBD

## Acknowledgments

* The distribution code for CS50's [Finance pset](https://cs50.harvard.edu/x/2023/psets/9/finance/) served as a template for the app.

## Screenshots

![Film Series](/docs/images/film-series0_2.png "Landscape Architecture Film Series")
_(Image created using [Portfoliofy](https://github.com/ggeerraarrdd/portfoliofy).)_

![Film Series](/docs/images/film-series2_2.jpg "Landscape Architecture Film Series")
![Film Series](/docs/images/film-series3_2.jpg "Landscape Architecture Film Series")
![Film Series](/docs/images/film-series4_2.png "Landscape Architecture Film Series")
![Film Series](/docs/images/film-series5_2.png "Landscape Architecture Film Series")

## Frontispiece

* TBD
