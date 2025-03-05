import requests
from auth import authorization, ad_id, ex_id
from random import randrange

def send_comment(userid, post_id, message, platform, remaining, OutOf):
    url = "https://dimesia.com/api/v1/social/" + platform + "/create-comment"
    
    # Headers with updated token
    headers = {
        "Host": "dimesia.com",
        "Sec-Ch-Ua-Platform": "Windows",
        "Authorization": authorization,
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
    
    form_data = {
        "author_user_id": userid,
        "admin_id": ad_id,
        "parent_object_id": post_id,
        "parent_object_type": "post",
        "content": "\"" + message + "\"",
        "fake_like_count": randrange(100),
        "status": "active",
        "exercise_id": ex_id
    }
    
    # Send the POST request
    response = requests.post(url, headers=headers, files={}, data=form_data)
    
    # # Print response details
    # print(f"Status Code: {response.status_code}")
    # print("Response Headers:")
    # for header, value in response.headers.items():
    #     print(f"  {header}: {value}")
    print("---------------------------------------------------------------------------------------------------------------------------------------------")
    print("-----   Posting    " + str(remaining) + "/" + str(OutOf) + "   -----")
    print(response.status_code)
    print("author: ", userid)
    print("text: ", message)
    print("---------------------------------------------------------------------------------------------------------------------------------------------\n")
    
    return response