class Article:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,urlToImage,title,description,url,publishedAt):
        
        self.urlToImage = urlToImage
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt = publishedAt