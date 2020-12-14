import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6&"

payload={}
headers = {
  'Accept': 'application/json',
  'Cookie': '__cfduid=d7ec628c2dc9a616344df39b02f85590c1606743496'
}
# First Update for GitHub
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
deck = response.json()
deck_id = deck['deck_id']
print(deck_id)
