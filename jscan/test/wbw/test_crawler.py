import wbw.crawler as crawler
import unittest


class TestCrawler(unittest.TestCase):

    def test_latest_term(self):
        term = crawler.latest_term()
        print(term)
        self.assertGreaterEqual(int(term), 20044)

    def test_crawler_data(self):
        data = crawler.crawler_data("20000", "20044")
        print(data)


if __name__ == '__main__':
    unittest.main()
