import requests

url = "https://react-amazon-bestsellers-books-dy.netlify.app/"

resp = requests.get(url)

print(resp.content)