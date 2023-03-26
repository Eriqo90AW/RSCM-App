from app import *

class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.sidebar.width()
            maxExtend = maxWidth
            standard = 50

            # SET MAX WIDTH
            if width == 50:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.sidebar, b"maximumWidth")
            self.animation.setDuration(150)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()


