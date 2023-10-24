# Landscape Architecture Film Series Website
Early aughts basic website recreated using modern tools

## Description
In the early aughts, I co-founded the _Landscape Architecture Film Series_ for the Department of Landscape Architecture at the University of Illinois Urbana/Champaign and for which I designed a website.

In need of a website to use as a vehicle to play around with a few AWS services (see [Future Work](#future-work)) but not wanting to spend anytime to ideate and design from scratch, I turned to my [old website](https://web.archive.org/web/20040827234527/http://www.rehearsal.uiuc.edu/projects/filmseries/). Its look and feel has aged well, I think, and indeed looks remarkably contemporary. For instance, if the current version of MoMA's [film series](https://www.moma.org/calendar/film/5632) is anything to by, bold color blocking isn't a dated design choice.

This, then, is that 20-year-old static website ressurrected as a dynamic web application with a data model to speak of, using modern tools such Flask, SQLite, VS Code and Git.

<picture><img src="/static/images/film-series1_2.jpg"></picture>
More screenshots below.

## Disclaimer
ALL CONTENTS IN THIS REPO ARE FOR EDUCATIONAL PURPOSES ONLY.

## Learning Objectives

### Requirements
N/A

### Personal Goals
N/A

## Getting Started

### Dependencies

* Flask==2.2.5
* flask_session==0.5.0

### Usage

Clone it!
```
$ git clone https://github.com/ggeerraarrdd/geo50x.git
```

Go into the project directory and run the command:
```
$ flask run
```

Open the URL after 'Running on'.

### Notes on Google Maps

For the embedded maps to work, you need to use your own API Key. Before you can create one, you will need to create a Google Cloud project, for which you need a Google Cloud account.
* [Set up a Google Cloud account](https://cloud.google.com)
* [Set up your Google Cloud project](https://developers.google.com/maps/documentation/javascript/cloud-setup)
* [Using API Keys](https://developers.google.com/maps/documentation/javascript/get-api-key)

In your terminal window, execute:
```
$ export MAP_API_KEY=value
```
where `value` is your API key.

Check to confirm if environmental variable is saved by executing
```
$ echo $MAP_API_KEY
```

## Author(s)
* [@ggeerraarrdd](https://github.com/ggeerraarrdd/)

## Future Work

* Change database to PostgreSQL and migrate to AWS RDS
* Deploy Flask app with AWS Lightsail and/or AWS Elastic Beanstalk

## License
* [MIT License](https://github.com/ggeerraarrdd/large-parks/blob/main/LICENSE)

## Acknowledgments

* The distribution code for CS50's Finance problem served as a template for the app.

## Screenshots
<picture><img src="/static/images/film-series2_2.jpg"></picture>
<picture><img src="/static/images/film-series3_2.jpg"></picture>
<picture><img src="/static/images/film-series4_1.jpg"></picture>
<picture><img src="/static/images/film-series5_1.jpg"></picture>
