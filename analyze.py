#!/usr/bin/python

########### Python 2.7 #############
import httplib, urllib, base64, json
from pandas import DataFrame
import pandas as pd
from StringIO import StringIO

# Seasy
import urllib2 #HTTP requests
import re #regex
from PIL import Image #gives raw binary data of a photo
import io


###############################################
#### Update or verify the following values. ###
###############################################
#
# # Replace the subscription_key string value with your valid subscription key.
# subscription_key = 'af3d9522bfd948238041619e61a8f27c'
#
# # Replace or verify the region.
# #
# # You must use the same region in your REST API call as you used to obtain your subscription keys.
# # For example, if you obtained your subscription keys from the westus region, replace
# # "westcentralus" in the URI below with "westus".
# #
# # NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# # a free trial subscription key, you should not need to change this region.
# uri_base = 'westcentralus.api.cognitive.microsoft.com'
#
# headers = {
#     # Request headers.
#     'Content-Type': 'application/json',
#     'Ocp-Apim-Subscription-Key': subscription_key,
# }
#
# params = urllib.urlencode({
#     # Request parameters. All of them are optional.
#     'visualFeatures': 'Categories,Description,Color',
#     'language': 'en',
# })
#
# # The URL of a JPEG image to analyze.
# body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Muffin_NIH.jpg/220px-Muffin_NIH.jpg'}"
# try:
#     # Execute the REST API call and get the response.
#     conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
#     conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
#     response = conn.getresponse()
#     data = response.read()
#     #
#         parsed = json.loads(data)
#         # print ("Response:")
#         # print (json.dumps(parsed, sort_keys=True, indent=2))
#
#         # gets tagged words
#         tags = parsed["description"]["tags"]
#         print tags
#
# #     conn.close()
#
# except Exception as e:
#     print('Error:')
#     print(e)
##############next part of the code is opening the tsv to play with it

    # # gets tagged words
    # tags = parsed["description"]["tags"]
    # for x,y in tags.items():
    #     tags[x] = str(y)
    # print tags
# dtype = str,
df = pd.read_csv('C:\Users\Admin\/afoodproject\database.csv', dtype = str )

# print(df.loc[10][7])
# print("in the column" + df[df['7'].str.contains("apple") == True])
s = "Organic"
# if "Acai" in df.loc[77][7]:
#     print "here!!"
# print(df.loc[77][7])
# #

# POSSIBLE AND WORKING
for x in range(0,500):
    if s in df.loc[x][7]:
        print(df.loc[x][7])
    # x=x+1
# #


            # print "We're on time %d" % (x)

# for row in df.rows:
    # if (row[7] == "apple"):
        # print row[7]
# print(df[df[7].str.contains("apple")])
# # Using `loc[]`
# print(df.loc[0]['A'])
#
# # Using `at[]`
# print(df.at[0,'A'])
#
# # Using `iat[]`
# # print(df.iat[0,0])
#
# # Using `get_value(index, column)`