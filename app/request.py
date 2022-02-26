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


def process_results(news_list):
    '''Function  that processes the movie result and transform them to a list of Objects'''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        
        news_object = News(id, name,  description, url, category, language, country)
        news_results.append(news_object)
    return news_results


def get_articles(title):
    article_url = article_base_url.format(title ,apiKey)
    with urllib.request.urlopen(article_url) as url:
        article_details = url.read()
        article_response = json.loads(article_details)

        article_results= None

        if article_response['articles']:
            article_results_list = article_response['articles']
            article_results = process_result(article_results_list)

    return article_results



def process_result(article_list):
    '''function to process article results'''
    article_results = []
    for articles in article_list:
        author = articles.get('author')
        title = articles.get('title')
        description = articles.get('description')
        url = articles.get('url')
        urlToImage = articles.get('urlToImage')
        publishedAt = articles.get('publishedAt')
        content = articles.get('content')





        #  article_object = []
        # if article_response:
        #     author = article_response('author')
        #     title = article_response('title')
        #     description = article_response('description')
        #     url = article_response('url')
        #     urlToImage = article_response('urlToImage')
        #     publishedAt = article_response('publishedAt')
        #     content = article_response('content')
        #     # 
        # article_object = []
        
        article_object = Article(author,title,  description, url, urlToImage, publishedAt, content)
        article_results.append(article_object)
    return article_results

    