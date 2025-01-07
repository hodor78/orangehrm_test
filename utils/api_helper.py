import requests


def get_user_records_from_api(api_url):
    """Fetches user records from the API."""
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    data = response.json()
    # Assuming API returns a list of users, each with a 'username' field
    return [user["username"] for user in data["users"]]
