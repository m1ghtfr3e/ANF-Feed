import unittest
from anfrss import anffeed

FEED = anffeed.ANFFeed()


class TestAnfFeedSetLanguage(unittest.TestCase):

    feed = anffeed.ANFFeed()

    def test_english(self):
        self.feed.set_language('english')
        self.assertEqual(self.feed.source, 'https://anfenglishmobile.com/feed.rss')

    def test_german(self):
        # Set Language
        self.feed.set_language('german')
        self.assertEqual(self.feed.source, 'https://anfdeutsch.com/feed.rss')

    def test_krumanji(self):
        self.feed.set_language('kurmanjî')
        self.assertEqual(self.feed.source, 'https://anfkurdi.com/feed.rss')

    def test_spanish(self):
        self.feed.set_language('spanish')
        self.assertEqual(self.feed.source, 'https://anfespanol.com/feed.rss')

    def test_arab(self):
        self.feed.set_language('arab')
        self.assertEqual(self.feed.source, 'https://anfarabic.com/feed.rss')
