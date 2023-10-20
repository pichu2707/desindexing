from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build 
from googleapiclient.http import BatchHttpRequest
import httplib2
import requests
import json

#url = 'httos://sanmiguelinmobiliria.com' #--> únicamente si es una url que queremos indexar o desindexar

SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# service_account_file.json is the private key that you created for your service account.
JSON_KEY_FILE = "personal.json"

#Autorizar credenciales
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)

http = credentials.authorize(httplib2.Http())


# print(url) cuando es únicamente una URL
requests = {'https://sanmiguelinmobiliaria.com/start.php?d/R62010' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/J2055049' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/R1452886' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/T3110910' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Q639920' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/P2275265' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/W3421667' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/I809561' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/M3250698' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Y2541258' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/M442023' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Z2697978' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/P1210958' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/W2120792' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/O2463946' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/J3275069' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/M11401' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/W1977698' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/G653302' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Y1094742' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/X1862343' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/M1206490' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/N1587215' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/V402263' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/C1769727' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/V3425079' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/E2288954' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/O3068413' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/L2241230' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/W2791640' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/M1478979' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/R721636' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/A191115' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/C2128213' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Q2887422' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Z1672851' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/F377011' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/P2343511' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/W2800042' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/I1972393' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/T3425315' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/J162628' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/M2795693' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/A864643' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/W1838060' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Y1207646' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/A1719242' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Q12783' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/D688446' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/O1696171' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/V1342684' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/P3098395' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/D162492' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/A2191611' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Z1528190' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/O828305' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/H477856' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/Y2277406' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/U3139698' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/T234116' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/D927152' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/F3430770' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/X482619' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/U2184867' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/A2470524' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/V1276377' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/N3275957' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/O1347641' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/E3068975' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/D783806' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/A2121172' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/I2490578' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/X3392725' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/J3379043' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/D2266290' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/H1268059' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/B2791047' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/B3086582' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/K1982179' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/U2879682' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Y2954442' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/P2586357' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Q915436' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/E1909710' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Q3412686' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/V2470233' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Q2040252' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/K503623' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/E3009081' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/M2905948' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/F1498374' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/L3285981' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/M3013020' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/C1332653' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/R1325871' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/I1407282' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/O1226796' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/K1357176' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/J2865722' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/I994038' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Q1552968' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Y2163428' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/M1352285' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/W3250084' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/A3286750' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/O621887' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/V3338797' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/U453313' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/H3443244' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/D2356181' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/A2009744' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/X3117563' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/H233701' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/N218149' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/U342871' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/P1135022' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/A2755459' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/H2119488' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/O2841180' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/M171184' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/W2144713' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/D613977' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/L3287333' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/B2465093' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/L3474333' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Z1169687' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Q910575' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/G836533' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/K3069137' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/H1181238' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/S2934284' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/S1995193' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/M2016174' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/H163124' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/H2766396' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/R2705837' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/J2968674' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Z1268712' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/K3339306' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/X1871892' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/I1974692' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/T2440979' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/G340452' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/H170503' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/C2961817' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Q2963868' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/D3391925' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/B2143678' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/F679485' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/O1898545' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/Q2576322' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/A2613209' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/F1875720' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/U2753006' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/P1343640' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/B2464625' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/L2831594' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/C956693' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/V2209917' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/N1747751' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/C2400895' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/gnsoemenu-6.html' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/L3241719' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/I819665' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/O163209' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/I1678035' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Z2767916' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/X3069254' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/S2928916' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/J2246909' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/B2752069' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/F3263772' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/L1682089' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/L645948' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/L2275391' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/K1837554' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/S2277158' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/G2643419' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/G1558197' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/U2956075' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/D3289422' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/H369656' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/K2745101' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?p/G2576522' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/Y183713' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/P1285493' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/?p=2520340.html' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/start.php?d/J2762927' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/ognlpmenu-1.html' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/riliimenu-3.html' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/dynzhmenu-29.html' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/nkedjmenu-67.html' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/emoqrmenu-188.html' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/qpdbymenu-6.html' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/cmcuvmenu-1.html' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/ztwfomenu-61.html' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/cwwttmenu-29.html' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/ricvumenu-62.html' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/guikdmenu-3.html' : 'URL_DELETED',
'https://sanmiguelinmobiliaria.com/hpxnjmenu-1.html' : 'URL_DELETED',
}
 
JSON_KEY_FILE = "personal.json"
 
SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
 
# Authorize credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
http = credentials.authorize(httplib2.Http())
 
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
