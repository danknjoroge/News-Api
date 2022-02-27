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


@app.route('/articles/<source_id>')
def news(source_id):
    '''view on news page'''
    article_source = get_articles('trending')
    title = f'{source_id} |Articles'

    return render_template('news.html',title = title, name = source_id, articles = article_source )

    # return render_template('news.html', title = title, article = article)
