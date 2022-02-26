from app import app
import urllib.request, json
from .models import news, articles

News = news.News

Article = articles.Article

# Getting api key
apiKey = app.config['NEWS_API_KEY']


#get base url for news api
base_url =app.config["NEWS_API_BASE_URL"]

article_base_url = app.config["ARTICLE_API_BASE_URL"]

def get_news(category):
    '''function that gets json response to url format'''
    get_news_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results
