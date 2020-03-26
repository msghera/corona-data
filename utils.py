import requests
import time

def requests_get(url):
    TRIES = 10
    response = None
    for i in range(TRIES):
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else :
            time.sleep(1)
    raise Exception("Response Code is found : {} while trying the url : {}."
                        .format(response.status_code, url))