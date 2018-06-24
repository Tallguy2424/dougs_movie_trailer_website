import webbrowser
from os import startfile

class Movie():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def movie_image(self):
        startfile(self.poster_image_url)

    def show_trailer_file(self):
        startfile(self.trailer_youtube_url)
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
