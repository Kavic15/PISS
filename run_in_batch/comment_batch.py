from time import sleep
import random
from random import randrange
from create_post import create_post
from AI import ask_ai
from get_random_post import get_random_post

from modules.comment_prevency import send_comment

platform = ["profilemag", "bleeper"]

def comment_batch(iterations, frequency, mode, PosNeg, platform, authors, theme):
    print("---------------\n")
    print("Posting "+str(iterations)+" comments to "+platform+"\n")
    print("---------------\n")
    from pools import comment_pool
    if mode == "ai":
        print("Using AI to generate comments\n")
    elif mode == "pool":
        print("Using comment pool to generate comments\n")

    for x in range(iterations):
        post = get_random_post()
        i=0
        while i == 0:
            userid=random.choice(authors)
            if userid==post['author_id']:
                i=0
            else:
                break

        if mode == "ai":
            message = ask_ai(type="comment", topic=1, post_text=post['post_text'], PosNeg=PosNeg, length=10, author_description="")
        elif mode == "pool":
            if PosNeg == "positive":
                message = create_post(comment_pool[1])
            elif PosNeg == "negative":
                message = create_post(comment_pool[0])

        send_comment(
            post_id=post['post_id'],
            userid=userid,
            message=message,
            platform=platform,
            remaining=iterations-x,
            OutOf=iterations)

        sleep(randrange(frequency))

    return  print("---------------\n"), print("post batch done\n"), print("---------------\n")