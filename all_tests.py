import unittest
from app.models import news

News = news.News

class TestNews(unittest.TestCase):
    '''tests behaviours of news class'''
    def setUp(self):
        '''runs before every test'''

        self.new_news = News("abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.",
        'https://abcnews.go.com',"general","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

    def test_init(self):
        self.assertEqual(self.new_news.id,"abc-news")
        self.assertEqual(self.new_news.name,"ABC News")
        self.assertEqual(self.new_news.description,"Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.")
        self.assertEqual(self.new_news.url,'https://abcnews.go.com')
        self.assertEqual(self.new_news.category,"general")
        self.assertEqual(self.new_news.language,"en")
        self.assertEqual(self.new_news.country,"us")

if __name__ == '__main__':
    unittest.main(verbosity=2)