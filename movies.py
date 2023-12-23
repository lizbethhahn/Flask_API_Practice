# movie.py

from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

MOVIES = {
    "It's A Wonderful Life": {
        "movieName": "It's a Wonderful Life",
        "genre": "Christmas",
        "yearReleased": 1947,
        "timestamp": get_timestamp(),
    },
    "Dogma": {
        "movieName": "Dogma",
        "genre": "comedy",
        "yearReleased": 1999,
        "timestamp": get_timestamp(),
    },
    "Sense and Sensibility": {
        "movieName": "Sense and Sensibility",
        "genre": "period drama",
        "yearReleased": 1995,
        "timestamp": get_timestamp(),
    }
}

def read_all():
    return list(MOVIES.values())

def create(movie):
    movieName = movie.get("movieName")
    genre = movie.get("genre")
    yearReleased = movie.get("yearReleased")
    
    if movieName and genre and yearReleased not in MOVIES:
        MOVIES[movieName] = {
            "movieName": movieName,
            "genre": genre,
            "yearReleased": yearReleased,
            "timestamp": get_timestamp(),
		}
        return MOVIES[movieName], 201
    else:
        abort(
            406, 
            f"Movie with the name {movieName} already exists",     
        )

def read_one(movieName):
    if movieName in MOVIES:
        return MOVIES[movieName]
    else:
        abort(
            404, f"Movie with the name {movieName} not found"
        )

def update(movieName, movie):
    if movieName in MOVIES:
        MOVIES[movieName]['movieName'] = movie.get("movieName", MOVIES[movieName]["movieName"])
        MOVIES[movieName]["timestamp"] = get_timestamp()
        return MOVIES[movieName]
    else:
        abort(
            400,
            f"Movie the the name {movieName} not found"
        )

def delete(movieName):
    if movieName in MOVIES:
        del MOVIES[movieName]
        return make_response(
            f"{movieName} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with last name {movieName} not found"
        )