from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QCursor

class Menu:
    def __init__(self, main_window):
        self.main_window = main_window
        self.isFullScreen = False
        self.isDragging = False
        self.mousePressPos = None
        self.windowPos = None

        # Setup three buttons to minimize, maximize, and exit the app
        self.main_window.ui.button_login_exit.clicked.connect(self.main_window.close)
        self.main_window.ui.button_login_min.clicked.connect(self.main_window.showMinimized)
        self.main_window.ui.button_login_size.clicked.connect(self.toggleMaximized)
        self.main_window.ui.button_login_menu.clicked.connect(self.toggleHome)
        
        # Setup the frame_navbar for dragging
        self.main_window.ui.frame_navbar.mousePressEvent = self.mousePressEvent
        self.main_window.ui.frame_navbar.mouseMoveEvent = self.mouseMoveEvent
        self.main_window.ui.frame_navbar.mouseReleaseEvent = self.mouseReleaseEvent

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.isDragging = True
            self.mousePressPos = event.globalPos()
            self.windowPos = self.main_window.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.isDragging:
            globalPos = event.globalPos()
            moved = globalPos - self.mousePressPos
            self.main_window.move(self.windowPos + moved)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.isDragging = False
            event.accept()

    def toggleMaximized(self):
        if self.isFullScreen:
            # If the window is currently maximized, restore it
            self.main_window.showNormal()
            self.isFullScreen = False
        else:
            # If the window is not currently maximized, maximize it
            self.main_window.showMaximized()
            self.isFullScreen = True
    
    def toggleHome(self):
        self.main_window.ui.stackedWidget.setCurrentIndex(0)
