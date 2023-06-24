import requests
from pprint import pprint


class NewsFeed:
    """Representing multiple news titles and links as a single string
    """
    base_url = 'https://newsapi.org/v2/everything?'
    api_key = 'key'

    def __init__(self, interest, from_date, to_date, language='en',
                 sort_by='publishedAt'):

        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language
        self.sort_by = sort_by

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ''
        for article in articles:
             email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f'{self.base_url}' \
              f'q={self.interest}&' \
              f'from={self.from_date}&' \
              f'to={self.to_date}&' \
              f'language={self.language}&' \
              f'sortBy={self.sort_by}&' \
              f'apiKey={self.api_key}'
        return url


if __name__ == "__main__":
    new_feed = NewsFeed(interest='nasa', from_date='2023-06-21', to_date='2023-06-21', language='en')
    print(new_feed.get())

