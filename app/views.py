from flask import render_template
from app import app
from .request import get_articles, get_news

#view
@app.route('/')
def index():
    '''view that returns index page'''
    general_news = get_news('general')
    sports_news = get_news('sports')
    technology_news = get_news('technology')
    science_news = get_news('science')

    
    title = 'Best News Site Worldwide'
    return render_template('index.html', title = title, general = general_news, sports= sports_news, technology=technology_news, science=science_news)