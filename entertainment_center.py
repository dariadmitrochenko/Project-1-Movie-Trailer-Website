import fresh_tomatoes
import media

# creating "Amelie" instance with name, storyline, poster art, trailer url
amelie = media.Movie("Amelie",
                      "Amelie is an innocent and naive girl in Paris with her own sense of justice. She decides to help those around her and, along the way, discovers love.",
                      "http://www.impawards.com/2001/posters/amelie_ver1.jpg",
                      "https://www.youtube.com/watch?v=2UT5xaAfxWU")

# creating "Night On Earth" instance with name, storyline, poster art, trailer url
night_on_earth = media.Movie("Night On Earth",
                             "It is a collection of five vignettes, taking place during the same night, concerning the temporary bond formed between taxi driver and passenger in five cities: Los Angeles, New York, Paris, Rome, and Helsinki. ",
                             "http://t3.gstatic.com/images?q=tbn:ANd9GcRAqGirU1EOol_i43FAuhZB5czgTrYSx7eEwWCeVOHQ7BtcA8eP",
                             "https://www.youtube.com/watch?v=o_ESHkySoJs")

# creating "My Neighbor Totoro" instance with name, storyline, poster art, trailer url
my_neighbor_totoro = media.Movie("My Neighbor Totoro",
                                 "The film tells the story of the two young daughters (Satsuki and Mei) of a professor and their interactions with friendly wood spirits in postwar rural Japan.",
                                 "https://upload.wikimedia.org/wikipedia/en/0/02/My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg",
                                 "https://www.youtube.com/watch?v=92a7Hj0ijLs")

# creating "WALL-E" instance with name, storyline, poster art, trailer url
walle = media.Movie("WALL-E",
                     "In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.",
                     "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
                     "https://www.youtube.com/watch?v=8_X8N_SaU90")

# creating "Casablanca" instance with name, storyline, poster art, trailer url
casablanca = media.Movie ("Casablanca",
                          "In Casablanca in December 1941, a cynical American expatriate encounters a former lover, with unforeseen complications.",
                          "https://upload.wikimedia.org/wikipedia/commons/b/b3/CasablancaPoster-Gold.jpg",
                          "https://www.youtube.com/watch?v=S9ID5DHsX8g")

# creating "Mad Max: Fury Road" instance with name, storyline, poster art, trailer url
mad_max = media.Movie("Mad Max: Fury Road", 
                       " A woman rebels against a tyrannical ruler in postapocalyptic Australia in search for her home-land with the help of a group of female prisoners, a psychotic worshipper, and a drifter named Max.",
                       "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
                       "https://www.youtube.com/watch?v=hEJnMQG9ev8")


#creating a list with all the instances of class Movie
movies = [amelie, night_on_earth, my_neighbor_totoro, walle, casablanca, mad_max]

fresh_tomatoes.open_movies_page(movies)


