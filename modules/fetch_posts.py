import requests
from auth import authorization, ad_id, ex_id

def fetch_posts(platform, max_pages=5):
    base_url = f"https://dimesia.com/api/v1/social/{platform}/post/list"
    headers = {
        "Authorization": authorization,
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Accept-Language": "cs-CZ,cs;q=0.9",
        "Accept": "application/json",
        "Sec-Ch-Ua": "\"Chromium\";v=\"133\", \"Not(A:Brand\";v=\"99\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Sec-Ch-Ua-Mobile": "?0",
        "Origin": "https://www.dimesia.com",
        "Sec-Fetch-Site": "same-site",
    }
    
    # Open file once for all pages
    with open("tocomment.txt", "a", encoding="utf-8") as f:
        current_page = 1
        total_posts = 0
        
        while current_page <= max_pages:
            params = {
                "admin_id": ad_id,
                "exercise_id": ex_id,
                "page": current_page,
                "order_mode": "time",
            }
            
            try:
                print(f"Fetching page {current_page}...")
                response = requests.get(base_url, headers=headers, params=params)
                
                if response.status_code == 200:
                    response_data = response.json()
                    
                    if "results" in response_data and "posts" in response_data["results"]:
                        posts = response_data["results"]["posts"]
                        page_post_count = len(posts)
                        
                        if page_post_count == 0:
                            print(f"No more posts found after page {current_page-1}")
                            break
                            
                        # Extract and write required data
                        for post in posts:
                            post_id = post["id"]
                            author_id = post["author_user_id"]
                            post_text = post["text"]
                            
                            # Write in required format with newline character
                            if post_text=="":
                                print("Post text is empty, skipping...")
                            else:
                                f.write(f"{post_id};;;{author_id};;;{post_text}\n")
                                # Optional: print to console for verification
                                print("--------------------------------------")
                                print(f"post_id:     {post_id}")
                                print(f"author_id:   {author_id}")
                                print(f"post_text:   {post_text}")
                                print("--------------------------------------\n")
                        
                        total_posts += page_post_count
                        print(f"Successfully processed {page_post_count} posts from page {current_page}")
                        
                        # If there's a way to check for total pages in the API response, use that instead
                        # For example, if the API returns total_pages in the response
                        if "pagination" in response_data["results"] and "total_pages" in response_data["results"]["pagination"]:
                            total_pages = response_data["results"]["pagination"]["total_pages"]
                            if current_page >= total_pages:
                                print(f"Reached the last page ({total_pages})")
                                break
                    else:
                        print("Error: Missing 'results' or 'posts' in the response.")
                        break
                else:
                    print(f"Error: Received status code {response.status_code}")
                    print(f"Response Body: {response.text}")
                    break

                # Move to the next page
                current_page += 1
                
            except requests.RequestException as e:
                print(f"An error occurred: {e}")
                break
    
    print(f"Completed. Total posts fetched: {total_posts}")