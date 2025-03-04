import requests
import json  # For handling JSON operations


def fetch_social_profiles(bearer_token, admin_id, exercise_id):
    """
    Fetch the list of social profiles from the API and print only the required fields.

    Args:
        bearer_token (str): Bearer token for authorization.
        admin_id (int): The admin ID.
        exercise_id (int): The exercise ID.
        page (int): Page number (default is 1).
        order_mode (str): Order mode, e.g., "time" (default is "time").

    Returns:
        None: This function directly prints the extracted data to the terminal.
    """
    # API endpoint
    url = "https://dimesia.com/api/v1/social/profilemag/post/list"

    # Query parameters
    params = {
        "admin_id": admin_id,
        "exercise_id": exercise_id,
        "page": 1,
        "order_mode": "time",
    }

    # HTTP headers
    headers = {
        "Authorization": f"Bearer {bearer_token}",
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
                    extracted_post = {
                        "post_id": post["id"],
                        "author_id": post["author_user_id"],
                        "text": post["text"],
                        "hashtags": post["hashtags"],
                    }
                    print
                    print(extracted_post)  # Print each post
            else:
                print("Error: Missing 'results' or 'posts' in the response.")
        else:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response Body: {response.text}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")


# Example Usage
if __name__ == "__main__":
    # Replace with your actual Bearer token
    token = "41465|DzjBCWBR2gSmumcVeWVz36FdzNN9a6WGr2Uk2xwE"

    # Call the function to fetch data
    fetch_social_profiles(
        bearer_token=token,
        admin_id=174,
        exercise_id=785
    )
