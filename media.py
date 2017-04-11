import webbrowser


class Movie():
     
     # create space for the instances of class Movie
     def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
          self.title = movie_title
          self.storyline = movie_storyline
          self.poster_image_url = poster_image
          self.trailer_youtube_url = trailer_youtube

     # open the the webbrowser with the correct url
     def show_trailer(self):
          webbrowser.open(self.trailer_youtube_url)
          
     
