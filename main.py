import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://linktr.ee/ChAbdulWahab"))
        self.urlbar = QLineEdit()
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.status = QStatusBar()
        self.setCentralWidget(self.browser)
        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction("Forward", self)
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.urlbar.returnPressed.connect(self.navigate_to_url)

        navtb.addWidget(self.urlbar)

        stop_btn = QAction("Stop", self)
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        self.setWindowIcon(QIcon("aura-mindfulness-stress-anxiety-daily-relief-2017-08-29.png"))

        if QPalette().color(QPalette.Base).lightness() < 128:
            # Dark theme
            background_color = "#2d2d2d"
        else:
            # Light theme
            background_color = "#f6f6f6"

        self.setStyleSheet(f"""
                QMainWindow {{
                    background-color: {background_color};
                    font-family: Poppins, sans-serif;
                }}

                QToolBar {{
                    background-color: {background_color};
                }}

                QLineEdit {{
                    background-color: #fff;
                    border: 1px solid #dcdcdc;
                    border-radius: 3px;
                    padding: 5px;
                    font-size: 14px;
                }}

                QLineEdit:focus {{
                    border-color: #3578e5;
                }}

                QToolButton {{
                    background-color: transparent;
                    border: none;
                    font-size: 14px;
                }}

                QToolButton:hover {{
                    background-color: #ebebeb;
                }}
            """)

        self.show()

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://linktr.ee/ChAbdulWahab"))

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle(f"{title} - My Browser")


app = QApplication(sys.argv)
app.setApplicationName("My Browser")
window = MainWindow()
app.exec_()
