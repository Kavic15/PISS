import requests

def send_comment(commented_post, comment_author, text):
    url = "https://dimesia.com/api/v1/social/profilemag/create-comment"
    headers = {
        "Authorization": "Bearer 41644|eQe0G8gNozyfqmQQWQcaibenuWE6rRjhhD5DiTP4",
        "Accept-Language": "cs-CZ,cs;q=0.9",
        "Sec-Ch-Ua": '"Chromium";v="133", "Not(A:Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Origin": "https://www.dimesia.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.dimesia.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i",
        "Connection": "keep-alive"
    }
    
    data = {
        "author_user_id": comment_author,
        "admin_id": "174",
        "parent_object_id": commented_post,
        "parent_object_type": "post",
        "content": text,
        "fake_like_count": "0",
        "status": "active",
        "exercise_id": "785"
    }
    
    response = requests.post(url, headers=headers, files=data)
    return response.json()

# Example usage
if __name__ == "__main__":
    result = send_comment()
    print(result)
