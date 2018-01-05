import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Open a webpage displaying a movie's trailer

        Keyword arguments:
            - Takes in the trailer url from the instance of Movie in question
        Outputs:
            -Starts the trailer for that movie

        """

        webbrowser.open(self.trailer_youtube_url)

#class tvshow():
#    def __init__(self, title, duration, season, episode, poster_image, trailer_youtube_url):
#        video.__init__(self, title, duration):
#        self.poster_image_url = poster_image
#        self.trailer_youtube_url = trailer_youtube

#    def show_clip(self):
#        webbrowser.opent(self.trailer_youtube_url)
