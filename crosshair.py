from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPen

class CrosshairApp(QtWidgets.QWidget):
    def __init__(self, monitor, resolution, game):
        super().__init__()

        self.monitor = monitor
        self.resolution = resolution
        self.game = game

        # Configuración de la ventana de la mira
        self.setWindowTitle(f"Crosshair for {self.game}")
        self.setGeometry(monitor.x, monitor.y, resolution.width(), resolution.height())
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint | 
            QtCore.Qt.WindowStaysOnTopHint | 
            QtCore.Qt.SubWindow |
            QtCore.Qt.WindowTransparentForInput  # Ignorar eventos de entrada completamente
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Configuración de la mira (crosshair)
        self.crosshair_size = 20  # Tamaño reducido de la mira para mayor precisión
        self.crosshair_thickness = 2  # Grosor de las líneas de la mira
        self.crosshair_color = QColor("green")  # Color de la mira

        self.setFixedSize(self.crosshair_size * 2, self.crosshair_size * 2)

        # Centrar la mira en la pantalla
        self.center_crosshair()

        self.show()

    def center_crosshair(self):
        """Centra la mira en el monitor según la resolución y la posición del monitor."""
        monitor_center_x = self.monitor.x + self.monitor.width // 2
        monitor_center_y = self.monitor.y + self.monitor.height // 2

        # Calcular la posición de la mira para que esté centrada
        crosshair_center_x = monitor_center_x - self.crosshair_size
        crosshair_center_y = monitor_center_y - self.crosshair_size

        self.move(crosshair_center_x, crosshair_center_y)

    def paintEvent(self, event):
        """Dibuja la mira en el centro de la ventana."""
        painter = QPainter(self)
        pen = QPen(self.crosshair_color)
        pen.setWidth(self.crosshair_thickness)
        painter.setPen(pen)

        # Dibujar líneas de la mira
        half_size = self.crosshair_size
        painter.drawLine(half_size, half_size - 10, half_size, half_size + 10)  # Línea vertical
        painter.drawLine(half_size - 10, half_size, half_size + 10, half_size)  # Línea horizontal

    def keyPressEvent(self, event):
        """Cerrar la mira cuando presionamos la tecla Esc."""
        if event.key() == Qt.Key_Escape:
            self.close()
