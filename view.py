import model
import sys, random
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia

class MainWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)


        #
        # If you are going to use a timer, create one. Oh, and look up timers.
        #
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

        #
        # I'm not actually sure why I thought this was a good idea.
        # Someone should really look into this.
        #
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        #
        # You can set a background if you'd like:
        #
        self.background = QtGui.QPixmap()
        root = QtCore.QFileInfo(__file__).absolutePath()
        self.background.load(root + '/graphics/riverChoose.jpg')

        #
        # You can have a painter draw directly onto this widget, but you have more
        # options when you draw on an image. We will do that a little later.
        #
        #self.image = QtGui.QImage(self.width(), self.height(), QtGui.QImage.Format_RGB32)
        #self.image.fill(0)





    def paintEvent(self, event):
        """
        By magic, this event occasionally gets called. Maybe on self.update()? Certainly on
        a window resize.
        """
        painter = QtGui.QPainter(self)
        rectangle = self.contentsRect()

        #
        # Set Background
        #
        painter.drawPixmap(rectangle, self.background, rectangle)
        #
        # If we were drawing on an image, we would need to do some resizing
        # stuff like this. We will do this eventually.
        #
        #newSize = self.size()
        #self.image = self.image.scaled(newSize)
        #painter.drawImage(0, 0, self.image)

        #
        # Do any drawing that you need to do next.
        #

    def keyPressEvent(self, event):
        """
        You could, of course, do more interesting things than print here.
        :param event:
        :return:
        """
        if event.key() in [QtCore.Qt.Key_Right, QtCore.Qt.Key_Up]:
            print('up')
        elif event.key() in [QtCore.Qt.Key_Left, QtCore.Qt.Key_Down]:
            print('down')
        elif event.key() in [QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return, QtCore.Qt.Key_Space]:
            print('select')
            self.update()

    def wheelEvent(self, event):
        """should work a lot like keypress..."""
        if event.angleDelta().y() > 0:
            print('up')
        else:
            print('down')



    def mousePressEvent(self, event):
        print("click (display)")

    def mouseReleaseEvent(self, event):
        print("release (display)")
