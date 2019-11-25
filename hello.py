import random
import requests

def random_int():
    print(random.randint(1, 100))

def get_response(url):
    print(requests.get(url))

if __name__ == "__main__":
    random_int()
    get_response('https://docs.pylint.org/en/1.6.0/tutorial.html')
