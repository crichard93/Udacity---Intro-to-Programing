"""
Creator: Cory Richard
Last Updated: 3/25/3018
"""

import webbrowser
class Movie():
	"""
	Class to be used for each movie on web page
	"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		"""
		Initialize Movie class

		"""
		self.title=movie_title
		self.storyline=movie_storyline
		self.poster_image_url=poster_image
		self.trailer_youtube_url=trailer_youtube
	def show_trailer(self):
		"""
		Instance method of class Movie that opens trailer in youtube. 
		"""
		webbrowser.open(self.trailer_youtube_url)