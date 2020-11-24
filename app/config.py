class Config:

    SOURCE_BASE_URL ='https://newsapi.org/v2/sources?category={}&apiKey={}'

    ARTICLE_NEWS_URL ='https://newsapi.org/v2/everything?sources={}&apiKey={}'


class Proconfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True


    

    