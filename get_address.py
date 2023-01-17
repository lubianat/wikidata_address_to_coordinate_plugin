# The key from https://positionstack.com
from API_KEY import KEY
import requests
from wdcuration import get_statement_values


qid = "Q89215891"

address = "Rua Catão, 611, Lapa, São Paulo"
url = f"http://api.positionstack.com/v1/forward?access_key={KEY}&query={address}"

r = requests.get(url)

data = r.json()

location = data["data"][0]
quickstatements_formatted = f"@{location['latitude']}/{location['longitude']}"

print(quickstatements_formatted)


get_statement_values()
