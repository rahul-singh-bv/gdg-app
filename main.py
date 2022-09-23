import requests
from flask import Flask, render_template, request

from utils import get_secret

app = Flask(__name__)
api_key = get_secret("TMDB_API")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    query = request.args.get("q", "")
    page = request.args.get("page", 1)
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&query={query}&page={page}&include_adult=false"
    movies = requests.get(url).json()
    return render_template("search.html", query=query, movies=movies)


@app.route("/movie-detail/<movie_id>")
def movie_detail(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    movie = requests.get(url).json()
    return render_template("movie_detail.html", movie=movie)


if __name__ == "__main__":
    app.run(host="localhost", port=8888, debug=True, threaded=True)
