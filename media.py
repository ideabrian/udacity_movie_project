import webbrowser

class Movie():
    """A class to hold movie related information."""

    def __init__(self, title, storyline, poster_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Play the movie trailer from YouTube in a new window."""
        webbrowser.open(self.youtube_url)