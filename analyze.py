#!/usr/bin/python

from __future__ import print_function
from nltk.corpus.reader.wordnet import NOUN
from nltk.corpus import wordnet
from nltk.compat import python_2_unicode_compatible

# from nltk import lemmatize
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
########### Python 2.7 #############
import httplib
import json
import urllib

import pandas as pd
# from pattern.en import singularize

# Seasy
fruits_array = []

# import global Constants

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

            if (what_Fruit is not None):
                fruits_array = whatFruit(output_tag_array)
                for fruit in fruits_array:
                    print (fruit)

                return fruits_array
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
    df = pd.read_excel('C:\Users\Admin\/afoodproject\datasetbest.xlsx', dtype=object)
    # POSSIBLE AND WORKING

    for x in range(0, 1000):
        if type(df.iloc[x][0]) != float:
            name = (df.iloc[x][0])
            for i in range(len(wordlist)):
                if name.find(wordlist[i]) == -1:
                    break
                else:
                    if i == len(wordlist) - 1:
                        print("The word was found in " + name + " at index : " + str(x+2))


def remove_duplicates(l):
    return list(set(l))

def makelistofingredients():
    df = pd.read_excel('C:\Users\Admin\/afoodproject\datasetbest.xlsx', dtype=object)
    # POSSIBLE AND WORKING
    # from pattern.text.en import singularize
    #
    # plurals = ['caresses', 'flies', 'dies', 'mules', 'geese', 'mice', 'bars', 'foos',
    #            'families', 'dogs', 'child', 'wolves']
    #
    # singles = [singularize(plural) for plural in plurals]
    # print
    # singles
    totallist=[]

    for x in range(0, 1000):
        if type(df.iloc[x][0]) != float:
            ingredient = (df.iloc[x][0])
            ingredient = ingredient.lower()
            if ingredient.find('cooked') != -1:
                continue;
            if ingredient.find('bread') != -1:
                continue;
            ingredient = ingredient.replace('(', ',')
            ingredient = ingredient.replace(')', ',')
            ingredient = ingredient.replace('[', ',')
            ingredient = ingredient.replace(']', ',')
            ingredient = ingredient.replace("and/or", ',')
            ingredient = ingredient.replace('.', '')
            ingredient = ingredient.replace(',', '')
            ingredient = ingredient.replace("natural", '')
            ingredient = ingredient.replace("org ", '')
            ingredient = ingredient.replace("refined", '')
            ingredient = ingredient.replace("raw ", '')
            ingredient = ingredient.replace("unrefined", '')
            ingredient = ingredient.replace("golden ", '')
            ingredient = ingredient.replace("&", ',')
            ingredient = ingredient.replace("with", ',')
            ingredient = ingredient.replace("expeller ", '')
            ingredient = ingredient.replace("pressed ", '')
            ingredient = ingredient.replace("and ", ',')
            ingredient = ingredient.replace("california", '')
            ingredient = ingredient.replace("wild ", '')
            ingredient = ingredient.replace("basmati ", '')
            ingredient = ingredient.replace("white ", '')
            ingredient = ingredient.replace("brown ", '')
            ingredient = ingredient.replace(" red ", '')
            ingredient = ingredient.replace("un ", '')
            ingredient = ingredient.replace("flavor ", '')
            ingredient = ingredient.replace("diam ", '')
            ingredient = ingredient.replace("2% ", '')
            ingredient = ingredient.replace("extra ", '')
            ingredient = ingredient.replace("virgin ", '')
            ingredient = ingredient.replace("dried ", '')
            ingredient = ingredient.replace(" dry", '')
            ingredient = ingredient.replace("roasted ", '')
            ingredient = ingredient.replace("light ", '')
            ingredient = ingredient.replace("italian ", '')
            ingredient = ingredient.replace("french ", '')
            ingredient = ingredient.replace("frozen ", '')
            ingredient = ingredient.replace("fresh ", '')
            ingredient = ingredient.replace("boiled ", '')
            ingredient = ingredient.replace("drained ", '')
            ingredient = ingredient.replace("canned " , '')
            ingredient = ingredient.replace("covered " , '')
            ingredient = ingredient.replace("belgium ", '')
            ingredient = ingredient.replace("pastry ", '')
            ingredient = ingredient.replace("fruit ", '')
            # ready - to - drink





            ingredientwords = [x.strip() for x in ingredient.split(',')]
            ingredientwords = [wnl.lemmatize(word) for word in ingredientwords]
            for word in ingredientwords :
                if '' == word:
                    ingredientwords.remove(word)
            ingredientwords = [item.encode('utf-8') for item in ingredientwords]
            noduplicateslist = remove_duplicates(ingredientwords)
            totallist.append(noduplicateslist)

    return totallist
