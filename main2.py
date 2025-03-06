import threading
import time
import random
from random import randrange
import signal
import sys
from create_post import create_post

from modules.fetch_posts import fetch_posts
from run_in_batch.comment_batch import comment_batch
from run_in_batch.post_batch import post_batch
from pools import hackers, soldiers, blue_users, post_pool, soldiers_red

# Global flag to control thread execution
running = True
x = 5

def signal_handler(sig, frame):
    global running
    print("\nStopping all operations gracefully. Please wait...")
    running = False

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

def run_fetch(iterations=x):
    for i in range(iterations):
        if not running:
            break
        try:
            fetch_posts(platform="profilemag", max_pages=1)
            print(f"Fetch iteration {i+1}/{iterations} completed")
        except Exception as e:
            print(f"Error in fetch: {e}")
        if running:
            time.sleep(random.uniform(5, 15))  # Add some delay between fetches

def run_comments(iterations=x):
    for i in range(iterations):
        if not running:
            break
        try:
            comment_batch(iterations=5, frequency=10, mode="pool", PosNeg="negative", 
                         platform="profilemag", authors=hackers, theme=5)
            print(f"Comment iteration {i+1}/{iterations} completed")
        except Exception as e:
            print(f"Error in comments: {e}")
        if running:
            time.sleep(random.uniform(8, 20))  # Add some delay between comment batches

def run_posts(iterations=x):
    for i in range(iterations):
        if not running:
            break
        try:
            post_batch(iterations=5, frequency=10, platform="profilemag", 
                      authors=blue_users, theme=5)
            print(f"Post iteration {i+1}/{iterations} completed")
        except Exception as e:
            print(f"Error in posts: {e}")
        if running:
            time.sleep(random.uniform(10, 25))  # Add some delay between post batches

def run_posts_ru(iterations=x):
    for i in range(iterations):
        if not running:
            break
        try:
            post_batch(iterations=5, frequency=120, platform="profilemag", 
                      authors=soldiers_red, theme=7)
            print(f"Red post iteration {i+1}/{iterations} completed")
        except Exception as e:
            print(f"Error in red posts: {e}")
        if running:
            time.sleep(random.uniform(30, 60))  # Add some delay between post batches

# Create threads for each function
fetch_thread = threading.Thread(target=run_fetch)
comment_thread = threading.Thread(target=run_comments)
post_thread = threading.Thread(target=run_posts)
post_thread_ru = threading.Thread(target=run_posts_ru)

print("Starting all operations. Press Ctrl+C to stop gracefully.")

# Start all threads
fetch_thread.start()
comment_thread.start()
post_thread.start()
post_thread_ru.start()

# Wait for all threads to complete
try:
    fetch_thread.join()
    comment_thread.join()
    post_thread.join()
    post_thread_ru.join()
except KeyboardInterrupt:
    # This is a backup in case the signal handler doesn't catch it
    running = False
    print("\nStopping all operations gracefully. Please wait...")

print("All operations completed or stopped")