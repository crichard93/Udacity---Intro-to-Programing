"""
Creator: Cory Richard
Last Updated: 3/25/3018
"""

import media
import fresh_tomatoes
lotr_fellowship=media.Movie('Fellowship of The Ring',
	'The story of an unexpected alliance to destroy the One Ring and overcome the rise of the evil lord Sauron',
	"https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
	'https://www.youtube.com/watch?v=V75dMMIW2B4')
bladerunner=media.Movie('Blade Runner',
	'In a future where synthetic humans are nearly identical to their creators, a career assassin of replicants and a replicant himself, finds his own humanity during a routine assignment,',
	'https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg',
	'https://www.youtube.com/watch?v=eogpIG53Cis')
pulpfiction=media.Movie("Pulp Fiction",
	"""Two hitmen are ordered to retrieve their boss's stolen suitcase while a rising boxing star 
	is on the run after betraying him.""",
	"https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
	"https://www.youtube.com/watch?v=s7EdQ4FqbhY")
prometheus=media.Movie("Prometheus",
	"""A team of scientists accidentally uncover the origins of humaninity... And something more sinister""",
	"https://upload.wikimedia.org/wikipedia/en/a/a3/Prometheusposterfixed.jpg",
	"https://www.youtube.com/watch?v=sftuxbvGwiU")
let_the_right_one_in=media.Movie("Let the Right One In",
	"A young, outcast boy unknowlingly befriends an Anti-Twilight vampire when she becomes his new neighbor",
	"https://upload.wikimedia.org/wikipedia/en/c/c9/Let_the_Right_One_In_%28Swedish%29.jpg",
	"https://www.youtube.com/watch?v=ICp4g9p_rgo")
the_godfather=media.Movie('The Godfather',
	'An epic drama plays out as the son of the don has to take over the family business as gang war erupts in the Mafia',
	'https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg',
	'https://www.youtube.com/watch?v=sY1S34973zA')
movies=[lotr_fellowship,bladerunner,pulpfiction,prometheus,let_the_right_one_in,the_godfather]
fresh_tomatoes.open_movies_page(movies)

