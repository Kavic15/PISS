import requests

def send_multipart_post():
    # API endpoint URL
    url = "https://dimesia.com/api/v1/social/profilemag/post/create"
    
    # Updated headers with new token
    headers = {
        "Host": "dimesia.com",
        "Sec-Ch-Ua-Platform": "Windows",
        "Authorization": "Bearer 40963|pbZSjY7FirxWUs0lMVOqvTfM89pYIdMFMfYtPjak",
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
    
    # Updated form data with new text message and exercise_id
    form_data = {
        "author_user_id": "20997",
        "admin_id": "174",
        "fake_counts_fb": '{"fakeLikeCount":0,"fakeShareCount":0}',
        "share_object_id": "",
        "text": "\"Bla bla\"",
        "exercise_id": "785"
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
    send_multipart_post()