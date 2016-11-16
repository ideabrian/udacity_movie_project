
import fresh_tomatoes
import media

gangster = media.Movie("American Gangster",
                       "70s Drug Lords",
                       "http://images.moviepostershop.com/american-gangster-movie-poster-2007-1020403604.jpg",  #noqa
                       "https://www.youtube.com/watch?v=BV_nssS6Zkg")

beauty_and_beast = media.Movie("Beauty and the Beast",
                               "Spells turn the prince into a beast.",
                               "http://cdn.collider.com/wp-content/uploads/2016/11/beauty-and-the-beast-poster-405x600.jpg",  #noqa
                               "https://www.youtube.com/watch?v=OvW_L8sTu5E")

the_martian = media.Movie("The Martian",
                          "Mars mission gone wrong.",
                          "http://static.hd-trailers.net/images/the-martian-104112-poster-xlarge.jpg",  #noqa
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

dragon_tatoo = media.Movie("The Girl with The Dragon Tatoo",
                            "Abused girl seeks revenge.",
                            "https://vinnieh.files.wordpress.com/2012/12/the-girl-with-the-dragon-tattoo-poster.jpg",  #noqa
                            "https://www.youtube.com/watch?v=WHphEoLl5S8")

amadeus = media.Movie("Amadeus",
                      "The Making of Mozart",
                      "http://www.hotel-r.net/im/hotel/es/amadeus-22.jpg",
                      "https://www.youtube.com/watch?v=yIzhAKtEzY0")

doctor_strange = media.Movie("Doctor Strange",
                             "Medical Doctor turned Super Hero",
                             "http://static.srcdn.com/slir/w691-h1023-q90-c691:1023/wp-content/uploads/Doctor-Strange-Comic-Con-Poster.jpg", #noqa
                             "https://www.youtube.com/watch?v=HSzx-zryEgM")


movies = [gangster, beauty_and_beast, the_martian, dragon_tatoo,
          amadeus, doctor_strange]

fresh_tomatoes.open_movies_page(movies)
