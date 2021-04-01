#reading in json file to data var
import json
f = open('keys.json',)
data = json.load(f)

flask_secret_key = data["flask_secret_key"]
image_upload_folder = ".../revue/server/images"