import media
import fishs_fav_films


thor_ragnarok = media.Movie("Thor: Ragnarok",
                            "Thor races to save Asgard from his evil sister Hela",
                            r"F:\Udacity\RefMaterials\Pictures\ThorRagMoviePoster1.jpg",
                            "https://www.youtube.com/watch?v=v7MGUNV8MxU")

star_wars = media.Movie("Star Wars",
                        "A boy and a girl fight to save a universe",
                        "StarWarsMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=vP_1T4ilm8M")

empire_strikes_back = media.Movie("The Empire Strikes Back",
                                  "The Empire has the Rebels and our heros on the run",
                                  "EmpireStrikesBackMoviePoster.jpg",
                                  "https://www.youtube.com/watch?v=-LuGkTtITQE")

a_good_year = media.Movie("A Good Year",
                          "A man discovers about himself, his past, and his future at his uncles French vinyard",
                          "AGoodYearMoviePoster.jpg",
                          "https://www.youtube.com/watch?v=pebd1DN8nok")

gladiator = media.Movie("Gladiator",
                        "A Roman general becomes a slave, becomes a gladiator, and becomes a legend",
                        "GladiatorMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=Q-b7B8tOAQU")

casablanca = media.Movie("Casablanca",
                       "An man must choose between his love for a woman and helping her husband escape the Nazis",
                       "CasablancaMoviePoster.jpg",
                       "https://www.youtube.com/watch?v=BZtWRRa_8I0")

movies = [thor_ragnarok, star_wars, empire_strikes_back, a_good_year,
          gladiator, casablanca]

fishs_fav_films.open_movies_page(movies)




#The following are code lines from the lessons but not relevant to the web page.
        #I have included these in case they need to be documented:


#toy_story = media.Movie("Toy Story",
#                        "A story of a boy and his toys that come to life",
#                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
#                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#avatar = media.Movie("Avatar",
#                     "A marine on an alien planet",
#                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
#                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(toy_story.storyline)
#print(avatar.storyline)
#avatar.show_trailer()
#print(thor_ragnarok.title)
#print(thor_ragnarok.storyline)
#print(thor_ragnarok.poster_image)
#print(thor_ragnarok.trailer_youtube_url)
#thor_ragnarok.movie_image()
#thor_ragnarok.show_trailer_file()
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
