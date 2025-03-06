from time import sleep
import random
from random import randrange
from create_post import create_post

#from modules.post_prevency import send_post
from modules.fetch_posts import fetch_posts
from run_in_batch.post_batch import post_batch
from pools import hackers, soldiers, blue_users, post_pool
#from run_in_batch.comment_batch import send_comment

fetch_posts(platform="profilemag", max_pages=10)
#post_batch(iterations=100, frequency=30, platform="profilemag", authors=blue_users, theme=5)