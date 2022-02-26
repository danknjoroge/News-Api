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
