from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPen

class CrosshairApp(QtWidgets.QWidget):
    def __init__(self, monitor, resolution, game):
        super().__init__()

        self.monitor = monitor
        self.resolution = resolution
        self.game = game

        # Crosshair window configuration
        self.setWindowTitle(f"Crosshair for {self.game}")
        self.setGeometry(monitor.x, monitor.y, resolution.width(), resolution.height())
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint | 
            QtCore.Qt.WindowStaysOnTopHint | 
            QtCore.Qt.SubWindow |
            QtCore.Qt.WindowTransparentForInput  # Ignore input events completely
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Crosshair settings
        self.crosshair_size = 20  # Reduced crosshair size for better accuracy
        self.crosshair_thickness = 2  # Thickness of the crosshair lines
        self.crosshair_color = QColor("green")  # Crosshair color

        self.setFixedSize(self.crosshair_size * 2, self.crosshair_size * 2)

        # Center the crosshair on the screen
        self.center_crosshair()

        self.show()

    def center_crosshair(self):
        """Centers the crosshair on the monitor based on resolution and monitor position."""
        monitor_center_x = self.monitor.x + self.monitor.width // 2
        monitor_center_y = self.monitor.y + self.monitor.height // 2

        # Calculate the position for the crosshair to be centered
        crosshair_center_x = monitor_center_x - self.crosshair_size
        crosshair_center_y = monitor_center_y - self.crosshair_size

        self.move(crosshair_center_x, crosshair_center_y)

    def paintEvent(self, event):
        """Draws the crosshair at the center of the window."""
        painter = QPainter(self)
        pen = QPen(self.crosshair_color)
        pen.setWidth(self.crosshair_thickness)
        painter.setPen(pen)

        # Draw crosshair lines
        half_size = self.crosshair_size
        painter.drawLine(half_size, half_size - 10, half_size, half_size + 10)  # Vertical line
        painter.drawLine(half_size - 10, half_size, half_size + 10, half_size)  # Horizontal line

    def keyPressEvent(self, event):
        """Close the crosshair when the Esc key is pressed."""
        if event.key() == Qt.Key_Escape:
            self.close()
