import requests
import json


git_url = "https://raw.githubusercontent.com/bhargav-velisetti/apache beam examples java/master/data/sample-data.json"

response = requests.get (git_url)

dict = response.content.decode ('utf-8')

formatted_dict = [json.loads (i) for i in names dict.split ('\n') if i.strip()]

for i in formatted names dict:
  print( "Value for key: firstName: ", formatted_dict["firstName"])