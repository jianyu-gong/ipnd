import fresh_tomatoes
import media

la_la_land = media.Movie(
                         "La La Land",
                         "Mia, an aspiring actress, serves lattes to movie "
                         "stars in between auditions and Sebastian, a "
                         "jazz musician, scrapes by playing cocktail party "
                         "gigs in dingy bars, but as success mounts they "
                         "are faced with decisions that begin to fray the "
                         "fragile fabric of their love affair, and the "
                         "dreams they worked so hard to maintain in each "
                         "other threaten to rip them apart.",
                         "https://images-na.ssl-images-amazon.com/images/M/"
                         "MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._"
                         "V1_SY1000_SX675_AL_.jpg",
                         "https://www.youtube.com/watch?v=DBUXcNTjviI")

warcraft = media.Movie(
                        "Warcraft",
                        "When the world of the Orcs Draenor is being "
                        "destroyed by the evil fel magic that uses "
                        "life-force, the powerful warlock Gul'dan creates a "
                        "portal to the world of Azeroth and forms the Horde "
                        "with members of the Orc clans. He also captures "
                        "many prisoners to keep the portal.",
                        "https://images-na.ssl-images-amazon.com/images/M/"
                        "MV5BMjIwNTM0Mzc5MV5BMl5BanBnXkFtZTgwMDk5NDU1ODE"
                        "@._V1_SY1000_CR0,0,631,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=RhFMIRuHAL4")

ant_man = media.Movie(
                      "Ant Man",
                      "Armed with the astonishing ability to shrink in scale"
                      " but increase in strength, con-man Scott Lang must "
                      "embrace his inner-hero and help his mentor, Dr. Hank "
                      "Pym, protect the secret behind his spectacular "
                      "Ant-Man suit from a new generation of towering "
                      "threats. Against seemingly insurmountable obstacles, "
                      "Pym and Lang must plan and pull off a heist that will"
                      " save the world.",
                      "https://images-na.ssl-images-amazon.com/images/M/"
                      "MV5BMjM2NTQ5Mzc2M15BMl5BanBnXkFtZTgwNTcxMDI2NTE"
                      "@._V1_.jpg",
                      "https://www.youtube.com/watch?v=pWdKf3MneyI")

avengers3 = media.Movie(
                        "Avengers: Age of Ultron",
                        "Tony Stark creates the Ultron Program to protect "
                        "the world, but when the peacekeeping program "
                        "becomes hostile, The Avengers go into action to try"
                        " and defeat a virtually impossible enemy together."
                        " Earth's mightiest heroes must come together once "
                        "again to protect the world from global extinction.",
                        "https://images-na.ssl-images-amazon.com/images/M/"
                        "MV5BMTM4OGJmNWMtOTM4Ni00NTE3LTg3MDItZmQxYjc4N2JhNm"
                        "UxXkEyXkFqcGdeQXVyNTgzMDMzMTg@._V1_SY1000_SX675_"
                        "AL_.jpg",
                        "https://www.youtube.com/watch?v=tmeOjFno6Do")

captain_america_3 = media.Movie(
                                "Captain America: Civil War",
                                "With many people fearing the actions of "
                                "super heroes, the government decides to "
                                "push for the Hero Registration Act, a law "
                                "that limits a hero's actions. This results"
                                " in a division in The Avengers.",
                                "https://images-na.ssl-images-amazon.com/"
                                "images/M/MV5BMjQ0MTgyNjAxMV5BMl5BanBnXkFtZ"
                                "TgwNjUzMDkyODE@._V1_SY1000_CR0,0,674,1000_"
                                "AL_.jpg",
                                "https://www.youtube.com/watch?v=1L3c17AmCZw"
                                )

frozen = media.Movie(
                     "Frozen",
                     "Anna, a fearless optimist, sets off on an epic journey"
                     " - teaming up with rugged mountain man Kristoff and "
                     "his loyal reindeer Sven - to find her sister Elsa, "
                     "whose icy powers have trapped the kingdom of Arendelle"
                     " in eternal winter. Encountering Everest-like "
                     "conditions, mystical trolls and a hilarious snowman "
                     "named Olaf, Anna and Kristoff battle the elements in a"
                     " race to save the kingdom. From the outside Anna's "
                     "sister, Elsa looks poised, regal and reserved, but in "
                     "reality, she lives in fear as she wrestles with a "
                     "mighty secret-she was born with the power to create "
                     "ice and snow.",
                     "https://images-na.ssl-images-amazon.com/images/M/"
                     "MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE"
                     "@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

movies = [la_la_land, warcraft, ant_man, avengers3, captain_america_3, frozen]
fresh_tomatoes.open_movies_page(movies)