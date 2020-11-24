from flask import render_template
from app import app
from .request import get_sources,get_articles
from .models import source


#views

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    science = get_sources('science')
    sports = get_sources('sports')
    entertainment = get_sources('entertainment')
    technology = get_sources('technology')
    general = get_sources('general')
    business = get_sources('business')
    health = get_sources('health')

    title = 'News website'
   
    return render_template('index.html',title = title, science = science, sports = sports, entertainment = entertainment, technology = technology, general = general, business = business, health = health)

@app.route('/source/<id>')

def articles(id):
    '''
    View article page function that returns the news details page and its data
    '''
    articles = get_articles(id)
    title = f'{id}'
    return render_template('article.html',title = title, articles = articles)

