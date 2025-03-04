import requests

def send_multipart_post(bearer, userid, message, exid, platform, likes, shares, remaining, OutOf):
    # API endpoint URL - updated to profilemag
    url = "https://dimesia.com/api/v1/social/" + platform + "/post/create"
    
    # Updated headers
    headers = {
        "Host": "dimesia.com",
        "Sec-Ch-Ua-Platform": "Windows",
        "Authorization": bearer,
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
    
    # Updated form data for profilemag
    form_data = {
        "author_user_id": userid,
        "admin_id": "174",
        "fake_counts_fb": f'{{"fakeLikeCount":{likes},"fakeShareCount":{shares}}}',
        "share_object_id": "",
        "text": "\"" + message + "\"",
        "exercise_id": exid
    }
    
    # Send the POST request
    response = requests.post(url, headers=headers, files={}, data=form_data)
    
    # Print response details
    # print(f"Status Code: {response.status_code}")
    # print("Response Headers:")
    # for header, value in response.headers.items():
    #     print(f"  {header}: {value}")
    print("---------------------------------------------------------------------------------------------------------------------------------------------")
    print("-----   Posting    " + str(remaining) + "/" + str(OutOf) + "   -----")
    print(response.status_code)
    print("author: ", userid)
    print("text: ", message)
    print("likes: ", likes)
    print("shares: ", shares)
    print("---------------------------------------------------------------------------------------------------------------------------------------------\n")
    
    
    return response