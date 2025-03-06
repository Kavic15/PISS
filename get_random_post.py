import random

def get_random_post(filename="post_pool/tocomment.txt"):
    try:
        # Open the file to read the first line and get remaining lines
        with open(filename, "r+", encoding="utf-8") as f:
            # Read the first line
            first_line = f.readline().strip()

            # Read the remaining lines
            lines = [line.strip() for line in f if line.strip()]
        
        if not lines:
            print("No posts found in the file.")
            return None
        
        # Remove the first line from the list of lines
        lines.insert(0, first_line)

        # Choose a random line from the remaining lines
        random_line = random.choice(lines)
        
        parts = random_line.split(";;;")
        if len(parts) >= 3:
            post = {
                "post_id": parts[0],
                "author_id": parts[1],
                "post_text": parts[2]
            }

            # Reopen the file in write mode to rewrite the lines without the first line
            with open(filename, "w", encoding="utf-8") as f:
                for line in lines[1:]:
                    f.write(line + "\n")

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