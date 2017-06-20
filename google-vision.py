import argparse
import base64
import httplib2

from apiclient.discovery import build
from oauth2client.client import GoogleCredentials

def main(photo_file):
 '''Run a label request on a single image'''

 API_DISCOVERY_FILE = 'https://vision.googleapis.com/$discovery/rest?version=v1'
 http = httplib2.Http()

 credentials = GoogleCredentials.get_application_default().create_scoped(
     ['https://www.googleapis.com/auth/cloud-platform'])
 credentials.authorize(http)

 service = build('vision', 'v1', http, discoveryServiceUrl=API_DISCOVERY_FILE)

 with open(photo_file, 'rb') as image:
   image_content = base64.b64encode(image.read())
   service_request = service.images().annotate(
     body={
       'requests': [{
         'image': {
           'content': image_content
          },
         'features': [{
           'type': 'LABEL_DETECTION',
           'maxResults': 5,
          }]
        }]
     })
   response = service_request.execute()
   for results in response['responses']:
     if 'labelAnnotations' in results:
       for annotations in results['labelAnnotations']:
         print('Found label %s, score = %s' % (annotations['description'],annotations['score']))
   return 0

if __name__ == '__main__':
 parser = argparse.ArgumentParser()
 parser.add_argument(
   'image_file', help='The image you\'d like to label.')
 args = parser.parse_args()
 main(args.image_file)
