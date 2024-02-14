from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow
from MapsUi import Ui_MainWindow
from sys import argv, exit
from draw import draw


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.coordinates.setText("37.523453;55.741301")
        self.scale.setText("0.01;0.01")
        self.set_img()

    def set_img(self):
        coord = list(map(float, self.coordinates.text().split(";")))
        file_content = draw(coord, list(map(float, self.scale.text().split(";"))))
        pxmap = QImage.fromData(file_content.read())
        self.label.setPixmap(QPixmap.fromImage(pxmap))


if __name__ == "__main__":
    app = QApplication(argv)
    ex = MainWindow()
    ex.show()
    exit(app.exec_())