from time import sleep
import random
from random import randrange
from create_post import create_post
from run_in_batch.comment_batch import comment_batch

#from modules.post_prevency import send_post
from modules.fetch_posts import fetch_posts
from run_in_batch.post_batch import post_batch
from pools import hackers, soldiers, blue_users, post_pool
#from run_in_batch.comment_batch import send_comment

fetch_posts(platform="profilemag", max_pages=5)
#post_batch(iterations=100, frequency=30, platform="profilemag", authors=blue_users, theme=5)

#PosNeg= "positive" or "negative"
#Platform = "profilemag" or "bleeper"

comment_batch(iterations=10, frequency=10, mode="pool", PosNeg="negative", platform="profilemag", authors=hackers, theme=5)