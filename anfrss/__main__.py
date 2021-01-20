import os
import sys
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QPushButton,
                             QWidget,
                             QListWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QLabel,
                             QTextEdit,
                             QSplitter,
                             QMenuBar,
                             )
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, pyqtSignal

try:
    from anffeed import ANFFeed
except ImportError:
    from .anffeed import ANFFeed


# Get the current directory to set the Icon later.
DIR = os.getcwd()


class ArticleWidget(QWidget):
    def __init__(self, *args):
        super().__init__(*args)

        self.initUi()

    def initUi(self):
        self.hbox = QVBoxLayout(self)
        self.setLayout(self.hbox)

        self.label = QLabel('Your chosen Feed will be shown here:')
        self.hbox.addWidget(self.label)

        self.text = QTextEdit()
        self.hbox.addWidget(self.text)


class TitleWidget(QWidget):
    TitleClicked = pyqtSignal([list])

    def __init__(self, *args):
        super().__init__(*args)

        self.initUi()

    def initUi(self):
        self.hbox = QVBoxLayout()
        self.setLayout(self.hbox)

        self.label = QLabel('Double Click on a title:')
        self.hbox.addWidget(self.label)

        self.titleList = QListWidget()
        self.titleList.itemDoubleClicked.connect(self.onClicked)

        self.news = ANFFeed()
        for item in self.news.all_feeds:
            self.titleList.addItem(item[0])
        self.hbox.addWidget(self.titleList)

    def onClicked(self, item):
        feeds = self.news.all_feeds
        id = 0
        for elem in range(len(feeds)):
            if feeds[elem][0] == item.text():
                id = elem

        summary = feeds[id][1] + '\n\n'
        link = feeds[id][2]

        self.TitleClicked.emit([summary, link])


class ANFApp(QMainWindow):
    def __init__(self, *args):
        super().__init__(*args)

        self.setWindowState(Qt.WindowMaximized)
        self.setWindowIcon(QIcon(f'{DIR}/assets/anf.png'))
        self.setAutoFillBackground(True)

        self.anfInit()

        self.show()

    def anfInit(self):
        self.setWindowTitle('ANF RSS Reader')

        self.central_widget = QSplitter()

        self.title_widget = TitleWidget()
        self.article_widget = ArticleWidget()

        self.setCentralWidget(self.central_widget)

        self.menu_bar = QMenuBar()
        self.actionEdit = self.menu_bar.addMenu('Edit')
        self.actionDownload = self.menu_bar.addMenu('Download')
        self.actionHelp = self.menu_bar.addMenu('Help')
        self.central_widget.addWidget(self.menu_bar)

        self.central_widget.addWidget(self.title_widget)
        self.central_widget.addWidget(self.article_widget)

        self.exitBtn = QPushButton(self)
        self.exitBtn.setGeometry(50, 600, 100, 55)
        self.exitBtn.setText('Exit')
        self.exitBtn.setStyleSheet("background-color: red")
        self.exitBtn.clicked.connect(self.exit)

        # Catch Slot Signal from the TitleWidget
        self.title_widget.TitleClicked.connect(self.title_click)

        self.show()

    def title_click(self, feed):
        '''
            Signal Catcher
        Catches the Slot Signal
        of the
        :class: TitleWidget
        and sets the Text for the
        :class: ArticleWidget;

        :param feed: The Signal
            in the TitleWidget
            emits a list with
            the contents;
        type feed: list
        '''
        self.article_widget.text.setText(feed[0])
        self.article_widget.text.append(feed[1])

    def exit(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    app.setStyle('Breeze')
    window = ANFApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
