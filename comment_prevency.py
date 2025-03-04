import requests

def send_comment_post(post_id, comment_author, comment_text, exid):
    # API endpoint URL for creating a comment
    url = "https://dimesia.com/api/v1/social/profilemag/create-comment"
    
    # Headers with updated token
    headers = {
        "Host": "dimesia.com",
        "Sec-Ch-Ua-Platform": "Windows",
        "Authorization": "Bearer 41030|RBAiQPKERfUZD3Rzqj1AzeBExmFr1zWH6s4nbii5",
        "Accept-Language": "cs-CZ,cs;q=0.9",
        "Sec-Ch-Ua": "\"Chromium\";v=\"133\", \"Not(A:Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Origin": "https://www.dimesia.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.dimesia.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    
    # Comment form data
    form_data = {
        "author_user_id": comment_author,
        "admin_id": "174",
        "parent_object_id": post_id,
        "parent_object_type": "post",
        "content": "\"" + comment_text + "\"",
        "fake_like_count": "0",
        "status": "active",
        "exercise_id": exid
    }
    
    # Send the POST request
    response = requests.post(url, headers=headers, files={}, data=form_data)
    
    # Print response details
    print(f"Status Code: {response.status_code}")
    print("Response Headers:")
    for header, value in response.headers.items():
        print(f"  {header}: {value}")
    print("\nResponse Body:")
    print(response.text)
    
    return response

if __name__ == "__main__":
    send_comment_post()