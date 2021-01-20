'''
    Parsing Feeds from ANF News

Core Module of package.
'''

import feedparser

LINK = 'https://anfenglishmobile.com/feed.rss'


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
            detailed.append(i.summary_detail['value'])
            print(i['value'])
        return # NotImplementedYet

    @property
    def all_feeds(self):
        return list(zip(self.title, self.summary, self.link))
