import requests

def posts():
    response = requests.get(
        "https://technik-backend.herokuapp.com/api/blog/posts")
    all_posts = response.json()
    return all_posts[::-1]
    
