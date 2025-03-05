from AI import generate_pool
from AI import ask_ai
from auth import authorization, ad_id, ex_id
from pools import soldiers, hackers, blue_users, post_pool

from run_in_batch.post_batch import post_batch


post_batch(iterations=30, platform="profilemag", authors=blue_users, theme=1)
#generate_pool(output_file= "post_pool/Anti-nato_facebook.txt", count=5, topic="anti-NATO rhetoric.")
#print(ask_ai(type="post", topic="anti-NATO", post_text="", PosNeg="Negative", length="200", author_description= "dumb 20 year old kid."))