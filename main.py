from time import sleep
import random
from random import randrange
from create_post import create_post

from post_prevency import send_multipart_post

i=30
bearer="Bearer 41201|Lihagh8VOjQqXPZUa6duXOVNwp0BOfBmanaquvRT"
exid="785"
platform = ["profilemag", "bleeper"]


post_pool=["post_pool/random_posts.txt", "post_pool/Andvaria_stories.txt", "post_pool/Anti-nato_facebook.txt"]

hacker_ids=["20998", "20997", "20999"]
bluestudent_id=["20801","20802","20803","20804","20805", "20818", "20821", "20822", "20823", "20824", "20825"]

for x in range(i):
    likes = randrange(200)
    shares = randrange(200)
    send_multipart_post(
        bearer=bearer,
        userid=random.choice(hacker_ids),
        message=create_post("post_pool/nerd_posts.txt"),
        exid=exid, platform=platform[1],
        likes=likes,
        shares=shares,
        remaining=i-x,
        OutOf=i)

    sleep(randrange(30))