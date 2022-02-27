import unittest
from app.models import news,articles

News = news.News
Article = articles.Article

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



class TestArticle(unittest.TestCase):
    '''tests behaviours for articles class'''
    def setUp(self):
        '''runs before every test'''
        self.new_articles = Article("Fob Meyer", "In whose hsnd are we safe", "Its all about politics",'https://abcnews.go.com','https://img.go.com', 12/21/21, 'amazing')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles, Article))

    def test_init(self):
        self.assertEqual(self.new_articles.author, "Fob Meyer")
        self.assertEqual(self.new_articles.title, "In whose hsnd are we safe")
        self.assertEqual(self.new_articles.description, "Its all about politics")
        self.assertEqual(self.new_articles.url, "https://abcnews.go.com")
        self.assertEqual(self.new_articles.urlToImage, 'https://img.go.com')
        self.assertEqual(self.new_articles.publishedAt,12/21/21)
        self.assertEqual(self.new_articles.content, 'amazing')

if __name__ == '__main__':
    unittest.main(verbosity=2)