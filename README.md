# Landscape Architecture Film Series Website

An early aughts basic website recreated using modern tools

## Description

_**NOTE:** The website now has a custom-made content management system (CMS) in alpha. Check it out in its own [repo](https://github.com/ggeerraarrdd/lafs-cms)._

In the early aughts, I co-founded the _Landscape Architecture Film Series_ for the Department of Landscape Architecture at the University of Illinois Urbana/Champaign and for which I designed a website.

In need of a website to use as a vehicle to play around with a few AWS services (see [Future Work](#future-work)) but not wanting to spend anytime to ideate and design a new one from scratch, I turned to my [old website](https://web.archive.org/web/20040827234527/http://www.rehearsal.uiuc.edu/projects/filmseries/). Its look and feel has aged well, I think, and indeed looks remarkably contemporary. For instance, if the current version of MoMA's [film series](https://www.moma.org/calendar/film/) is anything to go by, bold color blocking isn't a dated design choice.

This, then, is that 20-year-old static website ressurrected as a dynamic web application with a data model to speak of, using modern tools such Flask, SQLite, VS Code and Git.

![Film Series](/static/images/film-series1.png)

More screenshots below.

## Disclaimer

ALL CONTENTS IN THIS REPO ARE FOR EDUCATIONAL PURPOSES ONLY.

## Getting Started

### Dependencies

* Flask==3.0.0
* Werkzeug==3.0.1

### Usage

Clone it!

```bash
git clone https://github.com/ggeerraarrdd/film-series.git
```

Go into the project directory and run the command:

```bash
flask run
```

Open the URL after 'Running on'.

### Notes on Google Maps

For the embedded maps to work, you need to use your own API Key. Before you can create one, you will need to create a Google Cloud project, for which you need a Google Cloud account.

* [Set up a Google Cloud account](https://cloud.google.com)
* [Set up your Google Cloud project](https://developers.google.com/maps/documentation/javascript/cloud-setup)
* [Using API Keys](https://developers.google.com/maps/documentation/javascript/get-api-key)

Create an `.env` file in the root directory and then add:

```text
MAP_API_KEY=value
```

where `value` is your API key.

## Author(s)

* [@ggeerraarrdd](https://github.com/ggeerraarrdd/)

## Version History

### Release Notes

* See [https://github.com/ggeerraarrdd/film-series/releases](https://github.com/ggeerraarrdd/film-series/releases)

### Future Work

Improvements and new features development are ongoing.

* Create CMS for user management and content creation and editing _(currently in alpha - see [repo](https://github.com/ggeerraarrdd/lafs-cms))_

## License

* [MIT License](https://github.com/ggeerraarrdd/film-series/blob/main/LICENSE)

## Acknowledgments

* The distribution code for CS50's [Finance pset](https://cs50.harvard.edu/x/2023/psets/9/finance/) served as a template for the app.

## Screenshots

![Film Series](/static/images/film-series0.png "Landscape Architecture Film Series")*Image created using [Portfoliofy](https://github.com/ggeerraarrdd/portfoliofy).*

![Film Series](/static/images/film-series2.png "Landscape Architecture Film Series")
![Film Series](/static/images/film-series3.png "Landscape Architecture Film Series")
![Film Series](/static/images/film-series4.png "Landscape Architecture Film Series")
![Film Series](/static/images/film-series5.png "Landscape Architecture Film Series")
