import requests
import json

def fetch_posts(bearer, exid, output_file="fetch_post_response"):
    """
    Fetch the list of social profiles from the API.

    Args:
        bearer_token (str): Bearer token for authorization.
        admin_id (int): The admin ID.
        exercise_id (int): The exercise ID.
        page (int): Page number (default is 1).
        order_mode (str): Order mode, e.g., "time" (default is "time").

    Returns:
        dict: The JSON response data if the request succeeds.
        None: If the request fails or an error occurs.
    """
    # API endpoint
    url = "https://dimesia.com/api/v1/social/profilemag/post/list"

    # Query parameters
    params = {
        "admin_id": 174,
        "exercise_id": exid,
        "page": 1,
        "order_mode": "time",
    }

    # HTTP headers
    headers = {
        "Authorization": bearer,
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

            # Save JSON response to a file if output_file is specified
            if output_file:
                try:
                    with open(output_file, "w", encoding="utf-8") as file:
                        json.dump(response_data, file, indent=4, ensure_ascii=False)
                    print(f"Response successfully saved to {output_file}")
                except IOError as file_error:
                    print(f"Error writing response to file: {file_error}")

            return response_data

        else:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response Body: {response.text}")
            return None

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


# Example Usage
if __name__ == "__main__":
    # Replace with your actual Bearer token
    token = "Bearer 41465|DzjBCWBR2gSmumcVeWVz36FdzNN9a6WGr2Uk2xwE"

    # Call the function
    response_data = fetch_posts(
        bearer=token,
        exid=785,
        order_mode="time"
    )

    # Check and print the response
    if response_data:
        print("Request succeeded:")
        print(response_data)

    else:
        print("Request failed.")