import json
import requests


#response=requests.get('https://open.spotify.com/artist/1McMsnEElThX1knmY4oliG')
response=requests.get('https://itunes.apple.com/lookup?id=909253')
print(response.status_code)
o=json.dumps(response.json(),indent=2) #only for formatting
resp=response.json()
l=resp['results']

for i in l:
    print(i['artistName'])
    print(i['artistId'])
    


