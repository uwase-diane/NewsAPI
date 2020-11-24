import unittest
from models import  article
Article = article.Article

class ArticleTest(unittest.TestCase):

    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):

        '''
        Set up method that will run before every Test
        '''

        self.new_article = Article("https://ichef.bbci.co.uk/live-experience/cps/624/cpsprodpb/B874/production/_115602274_p08z8g2n.jpg",'business','marketing','http://www.abc.net.au/news',"2020-11-22T18:49:22Z")

    

    def test_instance(self):

        self.assertTrue(isinstance(self.new_article,Article))       
            
        
        

if __name__ == '__main__':
    unittest.main()

   

    
            