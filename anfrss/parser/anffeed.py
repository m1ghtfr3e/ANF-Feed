'''
Parsing Feeds from ANF News
##########################

Core Module of package.
Supports several languages:
    - English
    - German
    - Kurmanji
    - Spanish
( More languages available soon. )

:class: ANFFeed

See docs of containing class/es
to learn more about.
'''

import re
import feedparser


# Define available Languages:
# The specific link is assigned to.
ENGLISH = 'https://anfenglishmobile.com/feed.rss'
GERMAN = 'https://anfdeutsch.com/feed.rss'
KURMANJI = 'https://anfkurdi.com/feed.rss'
SPANISH = 'https://anfespanol.com/feed.rss'
ARAB = 'https://anfarabic.com/feed.rss'

# RegEx Tag
HTML_TAG = re.compile(r'<[^>]+>')               # To remove HTML tags later


class ANFFeed:
    ''' ANF Feed Parser

    This class fetches the news posts from
    one of the links defined at the more up
    (depending on the chosen language,
    default="english").

    Parameters
    ----------
    source : str
        Link to set;
        Depending on chosen
        Language.
    '''

    source = ENGLISH

    def __init__(self) -> None:
        try:
            self.feed = feedparser.parse(self.source)
        except NameError:
            raise NameError

        self.entries = self.feed.entries

    @classmethod
    def set_language(cls, language: str) -> None:
        '''
        Set language of link
        ====================

        :param language: Language to set
        :type language: str
        '''
        if language == 'english':
            cls.source = ENGLISH
        elif language == 'german':
            cls.source = GERMAN
        elif language == 'kurmanjî':
            cls.source = KURMANJI
        elif language == 'spanish':
            cls.source = SPANISH
        elif language == 'arab':
            cls.source = ARAB
        else:
            # We should not reach this
            # as the GUI just shows
            # available options
            raise NotImplementedError()

    @property
    def title(self) -> None:
        '''
        Titles Attribute
        ================
        '''
        titles = []
        for i in self.entries:
            titles.append(i.title)
        return titles

    @property
    def summary(self) -> None:
        '''
        Summary Attribute
        =================
        '''
        summary = []
        for i in self.entries:
            summary.append(i.summary)
        return summary

    @property
    def detailed(self) -> None:
        '''
        Detailed Attribute
        ==================
        '''
        detailed = []
        for i in self.entries:
            text = i.content[0]['value']
            text = HTML_TAG.sub('', text)       # Remove Html Tags
            detailed.append(text)
        return detailed

    @property
    def link(self) -> None:
        '''
        Links Attribute
        ===============
        '''
        links = []
        for i in self.entries:
            links.append(i.link)
        return links

    @property
    def all_feeds(self) -> None:
        '''
        All Feeds Attribute
        ===================
        '''
        return list(zip(self.title, self.summary, self.link, self.detailed))

    def download_article(self, ident, target):
        '''
        Download Article
        ===============

        Requests a chosen article
        and writes it to a file

        :param ident: Identifier;
            Can be link or title
            which will identify
            the article to down-
            load
        :type ident: str
        :param target: Directory
            to write to
        :type target: str
        '''
        query = self.entries[ident]
        result = query.content[0]['value']
        result = HTML_TAG.sub('', result)
        link = self.link[ident]
        title = self.title[ident]
        
        file_name = target + title + '.txt'
        with open(file_name, 'a') as f:
            f.write(title)
            f.write('\n\n')
            f.write(link)
            f.write('\n\n')
            f.write(result)
        return f'\n{title} written succesfully to {target}.\n'
    

    def __repr__(self) -> str:
        return (f'Spider: {self.__class__.__name__}\n'
                f'URL: {self.source!r}\n'
                f'Available articles: {len(self.entries)}\n'
                )


if __name__ == '__main__':
    anf = ANFFeed()
    article = anf.download_article(1, '/home/n0name/')
