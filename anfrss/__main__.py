import sys
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QPushButton,
                             QWidget,
                             QListWidget,
                             QHBoxLayout,
                             QMessageBox,
                             )
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication, Qt
from anffeed import ANFFeed


def show_details(feeds):
    pass


class FeedWidgets(QWidget):
    def __init__(self, *args):
        super().__init__(*args)

        self.setGeometry(10, 10, 1300, 500)
        self.setWindowTitle('Feed Overview')

        self.initUi()

    def initUi(self):
        vbox = QHBoxLayout(self)

        self.titleList = QListWidget()
        self.titleList.itemDoubleClicked.connect(self.onClicked)
        self.titleList.setGeometry(0, 0, 400, 400)
        self.news = ANFFeed()
        for item in self.news.all_feeds:
            self.titleList.addItem(item[0])
        vbox.addWidget(self.titleList)

    def onClicked(self, item):
        feeds = self.news.all_feeds
        id = 0
        for elem in range(len(feeds)):
            if feeds[elem][0] == item.text():
                id = elem

        summary = feeds[id][1] + '\n\n'
        link = feeds[id][2]

        QMessageBox.information(self, 'Details', summary + link)


class ANFApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon('anf.png'))
        self.setAutoFillBackground(True)

        self.anfInit()

        self.show()

    def anfInit(self):
        self.setWindowTitle('ANF RSS Reader')
        self.setWindowState(Qt.WindowMaximized)
        FeedWidgets(self)

        exitBtn = QPushButton(self)
        exitBtn.setGeometry(600, 600, 100, 50)
        exitBtn.setText('Exit')
        exitBtn.setStyleSheet("background-color: red")
        exitBtn.clicked.connect(self.exit)

    def exit(self):
        QCoreApplication.instance().quit()


def main():
    app = QApplication(sys.argv)
    app.setStyle('Breeze')
    window = ANFApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
