from app import app
import urllib.request,json
from .models import source,article

Source = source.Source
Article = article.Article



# Getting api key
api_key = app.config['API_KEY']

# Getting the source base url

base_url = app.config["SOURCE_BASE_URL"]

article_url = app.config["ARTICLE_NEWS_URL"]
 
def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''

    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_sources(source_results_list)

    return source_results        

def process_sources(sources_list):

    '''
    Function  that processes the News result and transform them to a list of Objects
    Args:
        sources_list: A list of dictionaries that contain News source
    Returns :
        sources_results: A list of news objects
    '''

    source_results = []

    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        category = source_item.get('category')
        description = source_item.get('description')
        url = source_item.get('url')
        language = source_item.get('language')

        if id:
            sources_object = Source(id,name,category,description,url,language)
            source_results.append(sources_object)

    return source_results        


def get_articles(id):

    '''
    Function to return a list
    '''
    get_articles_url = article_url.format(id,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        articles_results = json.loads(url.read())
        articles_object = None

        if articles_results['articles']:
            articles_object = process_articles(articles_results['articles'])

    return articles_object

def process_articles(articles_list):

    '''
    Function to list all articles
    '''
    articles_object = []

    for article_item in articles_list:
        urlToImage = article_item.get('urlToImage')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        publishedAt = article_item.get('publishedAt')


        if urlToImage:
            article_result = Article(urlToImage,title,description,url,publishedAt)
            articles_object.append(article_result)

    return articles_object        


