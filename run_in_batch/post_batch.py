from time import sleep
import random
from random import randrange
from create_post import create_post

from modules.post_prevency import send_post

platform = ["profilemag", "bleeper"]

def post_batch(iterations, frequency, platform, authors, theme):
    print("---------------\n")
    print("Posting "+str(iterations)+" posts to "+platform+"\n")
    print("---------------\n")
    #from pools import soldiers, hackers, blue_users, post_pool
    from pools import post_pool
    
    for x in range(iterations):
        send_post(
            userid=random.choice(authors),
            message=create_post(post_pool[theme]),
            platform=platform,
            remaining=iterations-x,
            OutOf=iterations)

        sleep(randrange(frequency))

    return  print("---------------\n"), print("post batch done\n"), print("---------------\n")