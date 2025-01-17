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
  * [Usage](#usage)
* [Author(s)](#authors)
* [Version History](#version-history)
  * [Release Notes](#release-notes)
  * [Initial Release](#initial-release)
* [Future Work](#future-work)
* [License](#license)
* [Acknowledgments](#acknowledgments)
* [Screenshots](#screenshots)

## Features

* Dynamic web application built with Flask and SQLite
* Modern development tools integration (VS Code, Git)
* Historical archive of a student-led film series website from the early 2000s
* Recreated film database preserving information about past screenings
* Google Maps integration for historical location reference
* Mobile-responsive design preserving original color blocking aesthetic

## Project Structure

TODO

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

2. **Navigate into the project directory:**

    ```bash
    cd film-series # For example
    ```

3. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Create an `.env` file and set the environment variables:**

    Create a file named `.env` in the `app` directory of the project and add the following variables:

    ```properties
    SECRET_KEY=your_secret_key
    MAP_API_KEY=your_map_api_key
    DATABASE_NAME="lafs.db"
    ```

    Replace `your_secret_key` (see #6 below) and `your_map_api_key` (see # 7 below) with your actual secret key and API key.

6. **Notes on Flask Secret Keys:**

    TODO

7. **Notes on Google Maps API Keys:**

    For the embedded map to work, you need to set up your own API Key. Before you can create one, you will need to create a Google Cloud project, for which you need a Google Cloud account.

    * [Set up a Google Cloud account](https://cloud.google.com)
    * [Set up your Google Cloud project](https://developers.google.com/maps/documentation/javascript/cloud-setup)
    * [Using API Keys](https://developers.google.com/maps/documentation/javascript/get-api-key)

### Usage

1. **Go into the app directory and run the command:**

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

## Acknowledgments

* The distribution code for CS50's [Finance pset](https://cs50.harvard.edu/x/2023/psets/9/finance/) served as a template for the app.

## Screenshots

![Film Series](/docs/images/film-series0_2.png "Landscape Architecture Film Series")_Image created using [Portfoliofy](https://github.com/ggeerraarrdd/portfoliofy)._

![Film Series](/docs/images/film-series2_2.jpg "Landscape Architecture Film Series")
![Film Series](/docs/images/film-series3_2.jpg "Landscape Architecture Film Series")
![Film Series](/docs/images/film-series4_2.png "Landscape Architecture Film Series")
![Film Series](/docs/images/film-series5_2.png "Landscape Architecture Film Series")
