import requests
from pprint import pprint


class NewsFeed:

    def __init__(self, data):
        self.data = data

    def get(self):
        pass


url = 'https://newsapi.org/v2/everything?' \
      'qInTitle=meditation&' \
      'from=2023-05-22' \
      '&sortBy=publishedAt' \
      '&apiKey=823595b53bd84418a84f6cf0fb052807'

response = requests.get(url)
content = response.json()
pprint(content)