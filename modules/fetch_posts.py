import requests
from auth import authorization, ad_id, ex_id
import json

def fetch_posts(platform):
    url = "https://dimesia.com/api/v1/social/" + platform + "/post/list"
    params = {
        "admin_id": ad_id,
        "exercise_id": ex_id,
        "page": 1,
        "order_mode": "time",
    }
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

    try:
        # Send the GET request
        response = requests.get(url, headers=headers, params=params)

        # Check for a successful HTTP status code
        if response.status_code == 200:
            response_data = response.json()  # Parse JSON response

            # Verify if 'results' and 'posts' keys exist in the data
            if "results" in response_data and "posts" in response_data["results"]:
                posts = response_data["results"]["posts"]

                # Extract and print required data
                for post in posts:
                    post_id = post["id"]
                    author_id = post["author_user_id"]
                    post_text = post["text"]
                    hashtags =  post["hashtags"]
                    f = open("tocomment.txt", "a")
                    f.write(str(post_id)+";;;"+str(author_id)+";;;"+str(post_text)+";;;"+str(hashtags))
                    f.close()
                    print("--------------------------------------")
                    print("post_id:     "+ str(post_id))
                    print("author_id:   "+ str(author_id))
                    print("post_text:   "+ str(post_text))
                    print("hashtags:    "+ str(hashtags))
                    print("--------------------------------------\n")

                    # extracted_post = {
                    #     "post_id": post["id"],
                    #     "author_id": post["author_user_id"],
                    #     "text": post["text"],
                    #     "hashtags": post["hashtags"],
                    # }
                    # print(extracted_post)  # Print each post
            else:
                print("Error: Missing 'results' or 'posts' in the response.")
        else:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response Body: {response.text}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")