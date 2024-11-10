import qt_material
import sys
import os
from PyQt5 import QtWidgets, QtCore
from screeninfo import get_monitors
from crosshair import CrosshairApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction

class MonitorSelector(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("CrosshairUp - Config")
        self.setGeometry(100, 100, 350, 250)  # Aumenté la altura para agregar el combo de juegos

        # Obtener la ruta correcta para los recursos
        if getattr(sys, 'frozen', False):
            # Si estamos en un entorno empaquetado (ejecutable)
            base_path = sys._MEIPASS
        else:
            # Si estamos en el entorno de desarrollo
            base_path = os.path.dirname(__file__)
        # Establecer el icono de la ventana
        icon_path = os.path.join(base_path, 'icon', 'icon.png')
        self.setWindowIcon(QIcon(icon_path))

        # Crear y configurar el icono de la bandeja
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(icon_path))
        
        # Eliminar el botón de maximizar (deja solo los botones de minimizar y cerrar)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        # Fijar el tamaño de la ventana para que no sea redimensionable
        self.setFixedSize(350, 250)  # Tamaño fijo (ancho, alto)

        # Aplicar el tema oscuro de qt-material
        qt_material.apply_stylesheet(QtWidgets.QApplication.instance(), theme='dark_yellow.xml')

        # Cambiar color del texto a blanco usando CSS para etiquetas y combo boxes
        self.setStyleSheet("""
            QLabel, QComboBox, QPushButton {
                color: white;
            }
            QComboBox {
                color: white;
                background-color: #333;
            }
            QComboBox QAbstractItemView {
                color: white;
                background-color: #555;
            }
        """)

        # Crear el layout
        layout = QtWidgets.QVBoxLayout()

        # Lista de monitores detectados
        self.monitors = get_monitors()
        self.combo_monitor = QtWidgets.QComboBox()
        self.combo_resolution = QtWidgets.QComboBox()
        self.combo_game = QtWidgets.QComboBox()  # Combo box para seleccionar el juego

        # Agregar los monitores al combo box
        for index, monitor in enumerate(self.monitors):
            self.combo_monitor.addItem(f"Monitor {index + 1} - {monitor.name}")

        # Agregar los juegos al combo box
        self.combo_game.addItem("Fortnite")
        self.combo_game.addItem("Left 4 Dead")

        # Seleccionar el monitor principal por defecto
        primary_monitor_index = 0
        self.combo_monitor.setCurrentIndex(primary_monitor_index)

        # Añadir los widgets al layout
        layout.addWidget(QtWidgets.QLabel("Elige el monitor:"))
        layout.addWidget(self.combo_monitor)
        layout.addWidget(QtWidgets.QLabel("Elige la resolución:"))
        layout.addWidget(self.combo_resolution)
        layout.addWidget(QtWidgets.QLabel("Elige el juego:"))
        layout.addWidget(self.combo_game)

        # Conectar la selección del monitor con la actualización de resoluciones
        self.combo_monitor.currentIndexChanged.connect(self.update_resolutions)
        self.update_resolutions()  # Cargar resoluciones del monitor por defecto

        # Botón para iniciar la mira
        self.start_button = QtWidgets.QPushButton("Iniciar Crosshair")
        self.start_button.clicked.connect(self.launch_crosshair)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def update_resolutions(self):
        # Obtener el monitor seleccionado
        selected_monitor = self.monitors[self.combo_monitor.currentIndex()]
        
        # Limpiar el combo de resoluciones
        self.combo_resolution.clear()

        # Usamos QScreen para obtener la resolución del monitor seleccionado
        screen = QtWidgets.QApplication.primaryScreen()  # Obtener el monitor activo (puedes cambiar esto según el índice seleccionado)
        
        # Usar screen.geometry() para obtener la resolución máxima soportada
        available_resolutions = [screen.geometry().size()]

        # Añadir las resoluciones al combo box
        for res in available_resolutions:
            self.combo_resolution.addItem(f"{res.width()} x {res.height()}", res)

        # Establecer la resolución actual como seleccionada por defecto
        current_resolution = QtCore.QSize(selected_monitor.width, selected_monitor.height)
        index = self.combo_resolution.findData(current_resolution)
        self.combo_resolution.setCurrentIndex(index)

    def launch_crosshair(self):
        # Obtener el monitor, resolución y juego seleccionados
        selected_monitor = self.monitors[self.combo_monitor.currentIndex()]
        selected_resolution = self.combo_resolution.currentData()
        selected_game = self.combo_game.currentText()

        # Crear y mostrar la ventana de Crosshair en la pantalla y resolución seleccionada
        self.crosshair = CrosshairApp(selected_monitor, selected_resolution, selected_game)
        self.crosshair.show()
