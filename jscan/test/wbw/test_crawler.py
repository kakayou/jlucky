import wbw.crawler as crawler
import unittest


class TestCrawler(unittest.TestCase):

    def test_latest_term(self):
        term = crawler.latest_term()
        self.assertGreaterEqual(20013)

    def test_crawler_data(self):
        data = crawler.crawler_data("20000", "20013")
        self.assertCountEqual(data.count(), 1)


if __name__ == '__main__':
    unittest.main()
