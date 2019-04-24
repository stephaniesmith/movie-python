import media

toy_story = media.Movie('Toy Story', 'A story about toys', 'https://images-na.ssl-images-amazon.com/images/I/514IG81HAhL.jpg', 'https://www.youtube.com/watch?v=KYz2wyBy3kc')

print(toy_story.storyline)

avatar = media.Movie('Avatar', 'A story about avatar', 'link', 'link')

print(avatar.storyline)

toy_story.show_trailer()