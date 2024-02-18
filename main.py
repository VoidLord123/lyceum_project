import math
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow
from MapsUi import Ui_MainWindow
from sys import argv, exit
from draw import draw
from geocoder import *


def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000
    a_lon, a_lat = a
    b_lon, b_lat = b

    radians_latitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_latitude)

    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    distance = math.sqrt(dx * dx + dy * dy)

    return distance


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center_coord = [37.523453, 55.741301]
        self.scale = [0.01, 0.01]
        self.default_coordinates = [37.523453, 55.741301]
        self.default_scale = [0.01, 0.01]
        self.findButton.clicked.connect(self.find_object)
        self.resetButton.clicked.connect(self.reset)
        self.points = []
        self.set_img()
        self.index.clicked.connect(self.checked)

    def checked(self):
        self.find()

    def set_img(self):
        image = self.get_image(self.center_coord, self.scale)
        self.map.setPixmap(QPixmap.fromImage(image))

    def find_object(self):
        self.find()

    def find(self, move_map=True, geocode=''):
        if not geocode:
            geocode = self.object.text()
        member = get_info(geocode)
        address, post_code, coordinates = (get_object_address(member), get_object_postcode(member),
                                           get_object_coord(member))
        if coordinates:
            if move_map:
                self.center_coord = list(map(float, coordinates))
            if ','.join(coordinates) not in self.points:
                self.points.append(','.join(list(map(str, self.center_coord))))
            self.full_address.setText(address + (', ' + str(post_code) if self.index.isChecked() else ''))
            self.set_img()

    def find_organisation(self, coordinates):
        address, coords = get_organisation_properties(coordinates)
        if lonlat_distance(list(map(float, coordinates.split(','))), coords) <= 50:
            coords = ','.join(list(map(str, coords)))
            if coords not in self.points:
                self.points.append(coords)
            self.set_img()

    def reset(self):
        self.points = []
        self.center_coord = self.default_coordinates
        self.scale = self.default_scale
        self.full_address.setText('')
        self.set_img()

    def mousePressEvent(self, event):
        m_x, m_y, w, h = self.map.pos().x(), self.map.pos().y(), self.map.width(), self.map.height()
        x, y = event.localPos().x(), event.localPos().y()
        if (m_x + w) >= x >= m_x and (m_y + h) >= y >= m_y:
            x -= (m_x + w / 2)
            y -= (m_y + y / 2)
            lat_x, lat_y = self.center_coord
            t = self.scale[0]
            lat_x += (x / (w / 2)) * t
            lat_y -= (y / (h / 2)) * t
            self.find_organisation(','.join(list(map(str, [lat_x, lat_y]))))

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_PageUp:
            scale = self.scale
            n_s, n_s2 = float(scale[0] * 2), float(scale[1] * 2)
            if n_s < 180 and n_s2 < 90:
                self.scale = [n_s if n_s < 180 else 180, n_s2 if n_s2 < 90 else 90]
                self.set_img()
        elif e.key() == Qt.Key_PageDown:
            scale = self.scale
            n_s, n_s2 = float(scale[0] / 2), float(scale[1] / 2)
            if n_s > 0.00015 and n_s2 > 0.00015:
                self.scale = [n_s if n_s < 180 else 180, n_s2 if n_s2 < 90 else 90]
                self.set_img()
        elif e.key() == Qt.Key_Up:
            self.center_coord[1] += self.scale[1]
            self.set_img()
        elif e.key() == Qt.Key_Down:
            self.center_coord[1] -= self.scale[1]
            self.set_img()
        elif e.key() == Qt.Key_Right:
            self.center_coord[0] += self.scale[0]
            self.set_img()
        elif e.key() == Qt.Key_Left:
            self.center_coord[0] -= self.scale[0]
            self.set_img()

    def get_image(self, coordinates, spn):
        #В документации и материале к урокам я не нашёл значения параметра l в Static Api, тут добавьте
        modes = {"Схема": "map", "Спутник": '', "Гибрид": ""}
        size = (f"{self.map.width() if self.map.width() < 650 else 650},"
                f"{self.map.height() if self.map.height() < 450 else 450}")

        content = draw(coordinates, spn, pt='~'.join(self.points), mode='map', size=size)
        image = QImage.fromData(content.read())
        return image


def my_excepthook(type, value, tback):
    QtWidgets.QMessageBox.critical(
        app, "CRITICAL ERROR", str(value),
        QtWidgets.QMessageBox.Cancel
    )

    sys.__excepthook__(type, value, tback)


if __name__ == "__main__":
    app = QApplication(argv)
    sys.excepthook = my_excepthook
    ex = MainWindow()
    ex.show()
    exit(app.exec_())
