#!/usr/bin/python

from __future__ import print_function

########### Python 2.7 #############
import httplib, urllib, base64, json
from pandas import DataFrame
import pandas as pd
from StringIO import StringIO

# Seasy
import urllib2  # HTTP requests
import re  # reeeeeeeeeeeeeeee
from PIL import Image  # gives raw binary data of a photo
import io
from google.cloud import vision
fruits_array = {}
label_list = []
colours = ['brown', 'beige', 'black', 'blue', 'cyan', 'gold', 'gray', 'grey', 'green', 'pink', 'purple', 'red', 'silver', 'turquoise', 'teal', 'white', 'yellow']
dont_want = [
'fruit',
'ingredient',
'produce',
'food',
'product',
'dessert',
'finger',
'hand',
'photo',
]

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


def createAPIConnection():

    try:
        googleVision()
        # microsoftVision(
        # key_list['example_pic_URL'],
        # key_list['subscription_key'])

    except Exception as e:
        print('Error:')
        print(e)

def googleVision():
        # -------------------- google ------------------------
        vision_client = vision.Client()
        file_name = 'test/apple.jpg'

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
            image = vision_client.image( content=content, )

        labels = image.detect_labels()

        for label in labels:
            fruits_array[label.description] = label.score

        print (fruits_array)
        print ("fuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuck")

# ------------------------ it works up to here ------------------------

        dontWant(dont_want, fruits_array)

        # remove the colours:
        for colour in colours:
            if colour in fruits_array.keys():
                print ("deleting", colour)
                del fruits_array[colour]

        print (fruits_array)

        # list of keys in the dictionary 'fruits_array'
        label_list = list(fruits_array.keys())

        print (label_list)

        # gisFruit(fruits_array)




# ----------------------- [S] remove unwanted words from dictionary ---------------------------------------------

def dontWant(csv_list, input_dictionary): #words from csv, input dictionary

    for part_of_word in csv_list:
        regex = "\'%s\'", part_of_word

        print ("THIS IS THE REGEX")
        print (regex)
        # edit more

        s = re.search('(?<=abc)def', )

    # # ghetto hardcoding
    # for word in dont_want:
    #     if word in fruits_array.keys():
    #         print ("deleting", word)
    #         del fruits_array[word]

    return input_dictionary


def microsoftVision(picURL, SUBSCRIPTION_KEY):
        # -------------------- microsoft ----------------------
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

            print (what_Fruit)

            if (what_Fruit is not None):
                fruits_array = whatFruit(output_tag_array)
                for fruit in fruits_array:
                    print (fruit)

        connection.close()

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

# A
