#!/usr/bin/python

from __future__ import print_function

########### Python 2.7 #############
import httplib, urllib, base64, json
from pandas import DataFrame
import pandas as pd
from StringIO import StringIO

# Seasy
import urllib2  # HTTP requests
import re  # regex
from PIL import Image  # gives raw binary data of a photo
import io
fruits_array = []

# import global Constants
import global_constants

###############################################
#### Update or verify the following values. ###
###############################################

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'westcentralus.api.cognitive.microsoft.com'


def createAPIConnection(picURL, SUBSCRIPTION_KEY):
    headers = {
        # Request headers.
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
    }

    params = urllib.urlencode({
        # Request parameters. All of them are optional.
        'visualFeatures': 'Tags,Description',
        'language': 'en',
    })

    # The URL of a JPEG image to analyzeself.
    body = "{'url':'%s'}" % (picURL)

    try:
        # Execute the REST API call and get the response.
        connection = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        connection.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
        response = connection.getresponse()
        data = response.read()

        # Deal with response
        json_data = json.loads(data)
        print ("Response:")
        print (json.dumps(json_data, sort_keys=True, indent=2))

        # Call the method lol
        output_tag_array = getTags(json_data)

        is_Fruit = isFruit(output_tag_array)

        if (is_Fruit == True):
            what_Fruit = whatFruit(output_tag_array)

            if (what_Fruit == True):
                fruits_array = whatFruit(output_tag_array)
                for fruit in fruits_array:
                    print (fruit)

        connection.close()

    except Exception as e:
        print('Error:')
        print(e)


# ----------------------- [S] get tags ---------------------------------------------

def getTags(json_data):

    tag_array = json_data["tags"]

    # TODO change the thing later
    # for tag in tags:

    return tag_array


# ----------------------- [S] check if 'fruit' is a tag ---------------------------------------------

def isFruit(tag_array):

    fruitTag = False
    for tag in tag_array:
        if tag['name'] == "fruit" and tag['confidence'] > 0.5:
            fruitTag = True
            print ("Object is fruit with %s confidence." % (tag['confidence']))

    # If there is no fruit tag
    if fruitTag == False:
        print ("Object is not a fruit.")

    return fruitTag


# ----------------------- [S] if fruit, what/which fruit(s)?  ---------------------------------------------

def whatFruit(tag_array):

    specific_fruitTag = False
    fruits = []

    for tag in tag_array:
        if tag['confidence'] > 0.5:
            if tag.has_key("hint"):
                if tag['hint'] == "food" and not tag['name'] == "fruit":
                    specific_fruitTag = True
                    fruits.append(tag['name'])
                    # print (fruits)

    # If there is no specific fruit tag
    if specific_fruitTag == False:
        print ("Cannot specify what kind of fruit. Is just fruit. :eyes:")

    if specific_fruitTag == True:
        return fruits



# ------------------------------------------------- [A] csv stuff  ---------------------------------------------

##############  next part of the code is opening the tsv to play with it

def findByKeyword(wordlist):
    df = pd.read_csv('C:\Users\Admin\/afoodproject\/fix.csv', dtype=object)
    # POSSIBLE AND WORKING

    for x in range(0, 200):
        if type(df.iloc[x]['product_name']) != float:
            name = (df.iloc[x]['product_name'])
            for i in range(len(wordlist)):
                if name.find(wordlist[i]) == -1:
                    break
                else:
                    if i == len(wordlist) - 1:
                        print("it is a " + name + " at index : " + str(x))
