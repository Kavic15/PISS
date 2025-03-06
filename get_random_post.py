import random

def get_random_post(filename="tocomment.txt"):
    try:
        # Read all lines from the file
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        
        if not lines:
            print("No posts found in the file.")
            return None
        random_line = random.choice(lines)
        
        parts = random_line.split(";;;")
        if len(parts) >= 3:
            post = {
                "post_id": parts[0],
                "author_id": parts[1],
                "post_text": parts[2]
            }
            return post
        else:
            print(f"Warning: Malformed line selected: {random_line}")
            return None
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Example usage:
# if __name__ == "__main__":
#     post = get_random_post()
    
#     if post:
#         print("Random Post:")
#         print(f"Post ID: {post['post_id']}")
#         print(f"Author ID: {post['author_id']}")
#         print(f"Text: {post['post_text']}")