import fresh_tomatoes
import media

toy_story = media.Movie('Toy Story', 'A story about toys', 'https://images-na.ssl-images-amazon.com/images/I/514IG81HAhL.jpg', 'https://www.youtube.com/watch?v=KYz2wyBy3kc')
avatar = media.Movie('Avatar', 'A story about avatar', 'link', 'link')
school_of_rock = media.Movie('School of Rock', 'A story about music', 'link', 'link')
ratatouille = media.Movie('Ratatouille', 'A story about a rat chef', 'link', 'link')
hunger_games = media.Movie('Hunger Games', 'A story about reality show', 'link', 'link')

movies = [toy_story, avatar, school_of_rock, ratatouille, hunger_games]
fresh_tomatoes.open_movies_page(movies)
# print(toy_story.storyline)


# print(avatar.storyline)

# toy_story.show_trailer()