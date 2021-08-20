from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow
import sys

from GUI import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # UI 파이썬 파일 생성
        self.ui = Ui_MainWindow()
        # UI 셋팅
        self.ui.setupUi(self)
        # 화면 출력
        self.show()

        image1 = QPixmap("C:/Users/wlxo0/Desktop/다운로드.jpeg")
        image2 = QPixmap("C:/Users/wlxo0/Desktop/다운로드_SR.jpeg")
        self.ui.label.setPixmap(image1.scaled(self.ui.label.width(), self.ui.label.height(), aspectRatioMode=Qt.KeepAspectRatio))
        self.ui.label_2.setPixmap(image2.scaled(self.ui.label.width(), self.ui.label.height(), aspectRatioMode=Qt.KeepAspectRatio))

    def mouseMoveEvent(self, event):
        """
        마우스가 클릭되면 실행되는 이벤트
        """
        print(f"마우스 이벤트 X : {event.x()}, Y : {event.y()}")

        if 0 <= event.x() <= self.ui.label.width() and 0 <= event.y() <= self.ui.label_2.height():
            self.ui.label_2.setGeometry(0, 0, event.x(), self.ui.label.height())
        else:
            print("범위가 아니에요")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec_()