"""
This is just a test program to check if set up works
"""
import random
import requests

def random_int():
    """ Print random number from 1 to 100 """
    print(random.randint(1, 100))

def get_response(url):
    """ Print response from the provided url """
    print(requests.get(url))

if __name__ == "__main__":
    random_int()
    get_response('https://docs.pylint.org/en/1.6.0/tutorial.html')
