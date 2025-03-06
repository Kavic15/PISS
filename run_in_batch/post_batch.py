from time import sleep
import random
from random import randrange
from create_post import create_post
import os

from modules.post_prevency import send_post

platform = ["profilemag", "bleeper"]

def post_batch(iterations, frequency, platform, authors, theme):
    print("---------------\n")
    print("Posting "+str(iterations)+" posts to "+platform+"\n")
    print("---------------\n")
    #from pools import soldiers, hackers, blue_users, post_pool
    from pools import post_pool
    
    for x in range(iterations):
        if os.stat(post_pool[theme]).st_size == 0:
            print("The \"" + post_pool[theme] + " file is empty.")
            return 1

        send_post(
            userid=random.choice(authors),
            message=create_post(post_pool[theme]),
            platform=platform,
            remaining=iterations-x,
            OutOf=iterations)

        sleep(randrange(frequency))

    return  print("---------------\n"), print("post batch done\n"), print("---------------\n")