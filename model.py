import pandas as pd
import numpy as np
import urllib.request
import json
import os
import ssl


def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

def apiCall(input, api_key, url):
    allowSelfSignedHttps(True) 
    data = input
    body = str.encode(json.dumps(data))
    url = url
    api_key = api_key
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        return result
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        return error

def modelCall(input):
    url = 'https://amlworkspace-focam.southeastasia.inference.ml.azure.com/score' #Model Endpoint
    with open("./token.json", 'r') as file:
        data = json.load(file)
    api_key = data.get('model_api_key')
    return apiCall(input, api_key=api_key, url=url)