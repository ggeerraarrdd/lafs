# LAFS

A digital archive of the Landscape Architecture Film Series website from the early aughts

## Table of Contents

* [Description](#description)
* [Target Users](#target-users)
* [Features](#features)
* [Project Structure](#project-structure)
* [Quick Start](#quick-start)
* [Local Setup](#local-setup)
  * [Prerequisites](#prerequisites)
  * [Dependencies](#dependencies)
  * [Installation](#installation)
  * [Configuration](#configuration)
* [Usage](#usage)
* [Production Setup](#production-setup)
* [System Administration](#system-administration)
* [Author(s)](#authors)
* [Version History](#version-history)
  * [Release Notes](#release-notes)
  * [Initial Release](#initial-release)
* [Future Work](#future-work)
* [License](#license)
* [Contributing](#contributing)
* [Acknowledgments](#acknowledgments)
* [Screenshots](#screenshots)

## Description

> [!NOTE]
> ALL CONTENTS IN THIS REPO ARE FOR EDUCATIONAL PURPOSES ONLY.

_LAFS_ serves as a digital archive for the website of the _Landscape Architecture Film Series_, a student-led initiative which I co-founded and co-curated for the [Department of Landscape Architecture](https://landarch.illinois.edu/) at the University of Illinois Urbana-Champaign in the early 2000s.

This repository preserves a sentimental piece of personal digital history. What would otherwise exist only as slowly disintegrating bits on a forgotten CD in a remote storage facility, as [fragmented snapshots](https://web.archive.org/web/20040827234527/http://www.rehearsal.uiuc.edu/projects/filmseries/) somewhere in the depths of the Internet Archive, or as a vaselined landscape in some province of collective memory has—here and at [l-a-f-s.org](https://l-a-f-s.org/)—been meticulously restored and recreated.

To learn how this project came about, check out [_LAFS-DEV_](https://github.com/ggeerraarrdd/lafs-dev).

![LAFS](/assets/images/film-series1_2.jpg "Landscape Architecture Film Series")

## Target Users

_LAFS_ is intended for:

* **Self-guided learners** seeking a reference implementation of modern backend web architecture powering a straightforward content website with simple navigation patterns.
* **Landscape architecture students and faculty** interested in the intersection of film and landscape studies.
* **Cinema enthusiasts** looking for a good film to watch.

## Features

* 📚 **Historical Preservation** - Faithful recreation of website from the early 2000s
* 🌐 **Modern Dev Tooling** - Implementation of a modern web architecture and software development practices
* 📱 **Dynamic Responsiveness** - Mobile-adjustable layout for today's wide range of devices
* 🎬 **Curated Film Database** - Recreated collection preserving information about past screenings
* 🗺️ **Location Context** - Google Maps integration for historical site reference

## Project Structure

```text
lafs/
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
├── logs/
│
├── docs/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Quick Start

For those who want to get up and running quickly with default settings:

```bash
# Clone the repo
git clone https://github.com/ggeerraarrdd/lafs.git
cd lafs

# Set up environment and install dependencies
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
pip install -r requirements.txt

# Run the application
flask run

# Navigate to the URL specified in the terminal output
```

## Local Setup

### Prerequisites

* TBD

### Dependencies

* See `requirements.txt`

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/ggeerraarrdd/lafs.git
    cd lafs
    ```

2. **Create and activate a Python virtual environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**

    ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

### Configuration

1. **Create an `.env` file**

    Place the file in the root directory and add the following as default:

    ```python
    # Database Path
    DATABASE_NAME='data/lafs.db'

    # Database Connection Pool
    POOL_SIZE=5
    MAX_OVERFLOW=10
    POOL_TIMEOUT=30
    POOL_RECYCLE=-1
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

## Usage

1. **Go into the `app` directory and run the command:**

    ```bash
    flask run
    ```

2. **Open the film series website**

    Copy and open the URL displayed after 'Running on' in the terminal.

## Production Setup

* TBD

## System Administration

* TBD

## Author(s)

* [@ggeerraarrdd](https://github.com/ggeerraarrdd/)

## Version History

### Release Notes

* See [https://github.com/ggeerraarrdd/lafs/releases](https://github.com/ggeerraarrdd/lafs/releases)

### Initial Release

The [original website](https://web.archive.org/web/20040827234527/http://www.rehearsal.uiuc.edu/projects/filmseries/) is archived on the Internet Archive.

## Future Work

* TBD

## License

* [MIT License](https://github.com/ggeerraarrdd/lafs/blob/main/LICENSE)

## Contributing

This project is not accepting contributions at this time. It is intended solely for personal learning and exploration. However, feel free to clone the repository and use it as a learning resource.

## Acknowledgments

* The distribution code for CS50's [Finance pset](https://cs50.harvard.edu/x/2023/psets/9/finance/) served as a template for the app.

## Screenshots

![LAFS](/docs/images/film-series0_2.png "Landscape Architecture Film Series")
_(Image created using [Portfoliofy](https://github.com/ggeerraarrdd/portfoliofy).)_

![LAFS](/assets/images/film-series2_2.jpg "Landscape Architecture Film Series")
![LAFS](/assets/images/film-series3_2.jpg "Landscape Architecture Film Series")
![LAFS](/assets/images/film-series4_2.png "Landscape Architecture Film Series")
![LAFS](/assets/images/film-series5_2.png "Landscape Architecture Film Series")

## Frontispiece

* TBD
