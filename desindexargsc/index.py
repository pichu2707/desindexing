from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build 
from googleapiclient.http import BatchHttpRequest
import httplib2
import requests

SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# personal.json es la clave privada que creó para su cuenta de Google.
JSON_KEY_FILE = "personal.json"

#Autorizar credenciales
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)

http = credentials.authorize(httplib2.Http())

#URL_UPDATED para indexar
# print(url) cuando es únicamente una URL
requests = {'https://dominio.com/' : 'URL_DELETED',
}
 
# Creando el servicio
service = build('indexing', 'v3', credentials=credentials)
 
def insert_event(request_id, response, exception):
  """_summary_

  Args:
      request_id (any): Argumento para identificar de forma única la solicitud enviada.
      response (any): Contiene la respuesta de la solicitud esperando que sea un 200 como que está todo correcto
      exception (any): Captura y maneja las excepciones o errores que puedan ocurrir en el proceso 
  """
  if exception is not None:
    print(exception)
  else:
    print(response)
 
batch = service.new_batch_http_request(callback=insert_event)
 
for url, api_type in requests.items():
    batch.add(service.urlNotifications().publish(
        body={"url": url, "type": api_type}))
 
batch.execute()
