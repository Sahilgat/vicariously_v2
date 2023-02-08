import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
bearer_token = os.environ.get("BEARER_TOKEN")
headers = {
    "Authorization": "Bearer " + bearer_token,
    "User-Agent": "vicariously_v2",
}

def get_user_from_username(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200 and response.json()["data"] is not None:
        return response.json()["data"]["id"]
    else:
        print(f"Request to get_users failed with status code {response.status_code}")
        return None

def get_following(user_id):
    url = f"https://api.twitter.com/2/users/{user_id}/following?max_results=1000" # TODO Need to implement pagination for more than 100 users
    response = requests.get(url, headers=headers)

    if response.status_code == 200 and response.json()["data"] is not None:
        return response.json()["data"]
    else:
        print(f"Request to get_following failed with status code {response.status_code}")
        return None

# TODO, need to use client access token
def create_list(name, description, private=True):
    url = "https://api.twitter.com/2/lists"
    body = {
        "name": name,
        "description": description,
        "private": private
    }
    data = json.dumps(body)
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200 and response.json()["data"] is not None:
        return response.json()["data"]["id"]
    else:
        print(f"Request to create_list failed with status code {response.status_code}")
        return None
    
# TODO
# def add_users_to_list(users, list_id):

# For a given user XYZ, get all the users XYZ follows
# This result is given in 20 user pages with a maxinum of 15 requests in a 15-minute window

def main():
    username = "0xtuba"
    user_id = get_user_from_username(username)
    following = get_following(user_id)
    
    # print("Following:")
    # for user in following:
    #     print(f"- {user['name']} (@{user['username']})")

    test_list_id = create_list("test list", "I am just testing")
    print(test_list_id)

if __name__ == "__main__":
    main()