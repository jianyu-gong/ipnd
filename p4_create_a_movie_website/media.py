import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
    	'''
    	Behavior: Open web browser to play the trailer
    	Input: trailer_youtube_url
    	Output: none
    	'''
        webbrowser.open(self.trailer_youtube_url)
