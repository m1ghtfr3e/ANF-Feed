'''
    Parsing Feeds from ANF News

Core Module of package.
'''

import feedparser
import re

LINK = 'https://anfenglishmobile.com/feed.rss'
HTML_TAG = re.compile(r'<[^>]+>')               # To remove HTML tags later


class ANFFeed:
    def __init__(self):
        try:
            self.feed = feedparser.parse(LINK)
        except :
            raise Error

        self.entries = self.feed.entries

    @property
    def title(self):
        titles = []
        for i in self.entries:
            titles.append(i.title)
        return titles

    @property
    def summary(self):
        summary = []
        for i in self.entries:
            summary.append(i.summary)
        return summary

    @property
    def link(self):
        link = []
        for i in self.entries:
            link.append(i.link)
        return link

    @property
    def detailed(self):
        detailed = []
        for i in self.entries:
            text = i.content[0]['value']
            text = HTML_TAG.sub('', text)       # Remove Html Tags
            detailed.append(text)
        return detailed

    @property
    def all_feeds(self):
        return list(zip(self.title, self.summary, self.link, self.detailed))

    def download_article(self, article, file='html'):
        '''
            Download Article

        Requests a chosen article
        and writes it to a file
        (default: HTML).

        :param article: The
            article to write
        :param file: The desired
            file type to write
        :type file: str, default
        '''
        if file != 'html':
            raise NotImplementedError()

        raise NotImplementedError()

if __name__ == '__main__':
    feed = ANFFeed()
    art = feed.entries[0]
    feed.download_article(art)
