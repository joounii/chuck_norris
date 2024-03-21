import requests

# Icon doesn't work because it no longer exist on the API
def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()
    print(response_json)
    return response_json