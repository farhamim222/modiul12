import requests


def get_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        joke_data = response.json()
        print(joke_data['value'])
    else:
        print("Failed to retrieve a joke. Please try again later.")


# Call the function to print a random joke
get_random_chuck_norris_joke()
