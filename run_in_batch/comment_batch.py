from time import sleep
import random
from random import randrange
from create_post import create_post

from modules.comment_prevency import send_comment

platform = ["profilemag", "bleeper"]

def pcomment_batch(iterations, frequency, mode, platform, authors, theme):
    print("---------------\n")
    print("Posting "+str(iterations)+" comments to "+platform+"\n")
    print("---------------\n")
    from pools import comment_pool
    if mode == "ai":
        print("Using AI to generate comments\n")
    elif mode == "pool":
        print("Using comment pool to generate comments\n")

    for x in range(iterations):
        message = create_post(comment_pool[theme])
        send_comment(
            userid=random.choice(authors),
            message=create_post(comment_pool[theme]),
            platform=platform,
            remaining=iterations-x,
            OutOf=iterations)

        sleep(randrange(frequency))

    return  print("---------------\n"), print("post batch done\n"), print("---------------\n")