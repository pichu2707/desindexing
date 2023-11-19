from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build 
from googleapiclient.http import BatchHttpRequest
import httplib2
import requests
import json

SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# service_account_file.json is the private key that you created for your service account.
JSON_KEY_FILE = "personal.json"

#Autorizar credenciales
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)

http = credentials.authorize(httplib2.Http())

#URL_UPDATED para indexar
# print(url) cuando es únicamente una URL
requests = {'https://dominio.com/' : 'URL_DELETED',
}
 
 
SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
 
# Build service
service = build('indexing', 'v3', credentials=credentials)
 
def insert_event(request_id, response, exception):
    if exception is not None:
      print(exception)
    else:
      print(response)
 
batch = service.new_batch_http_request(callback=insert_event)
 
for url, api_type in requests.items():
    batch.add(service.urlNotifications().publish(
        body={"url": url, "type": api_type}))
 
batch.execute()
