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

        # Window configuration
        self.setWindowTitle("CrosshairUp - Config")
        self.setGeometry(100, 100, 350, 250)  # Increased height to add the game combo box

        # Get the correct path for resources
        if getattr(sys, 'frozen', False):
            # If we are in a packaged environment (executable)
            base_path = sys._MEIPASS
        else:
            # If we are in the development environment
            base_path = os.path.dirname(__file__)
        # Set the window icon
        icon_path = os.path.join(base_path, 'icon', 'icon.png')
        self.setWindowIcon(QIcon(icon_path))

        # Create and configure the tray icon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(icon_path))
        
        # Remove the maximize button (leave only minimize and close buttons)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        # Set the window size to be non-resizable
        self.setFixedSize(350, 250)  # Fixed size (width, height)

        # Apply qt-material dark theme
        qt_material.apply_stylesheet(QtWidgets.QApplication.instance(), theme='dark_yellow.xml')

        # Change text color to white using CSS for labels and combo boxes
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

        # Create the layout
        layout = QtWidgets.QVBoxLayout()

        # List of detected monitors
        self.monitors = get_monitors()
        self.combo_monitor = QtWidgets.QComboBox()
        self.combo_resolution = QtWidgets.QComboBox()
        self.combo_game = QtWidgets.QComboBox()  # Combo box to select the game

        # Add monitors to the combo box
        for index, monitor in enumerate(self.monitors):
            self.combo_monitor.addItem(f"Monitor {index + 1} - {monitor.name}")

        # Add games to the combo box
        self.combo_game.addItem("Fortnite")
        self.combo_game.addItem("Left 4 Dead")

        # Select the primary monitor by default
        primary_monitor_index = 0
        self.combo_monitor.setCurrentIndex(primary_monitor_index)

        # Add widgets to the layout
        layout.addWidget(QtWidgets.QLabel("Choose the monitor:"))
        layout.addWidget(self.combo_monitor)
        layout.addWidget(QtWidgets.QLabel("Choose the resolution:"))
        layout.addWidget(self.combo_resolution)
        layout.addWidget(QtWidgets.QLabel("Choose the game:"))
        layout.addWidget(self.combo_game)

        # Connect monitor selection to resolution update
        self.combo_monitor.currentIndexChanged.connect(self.update_resolutions)
        self.update_resolutions()  # Load resolutions for the default monitor

        # Button to start the crosshair
        self.start_button = QtWidgets.QPushButton("Start Crosshair")
        self.start_button.clicked.connect(self.launch_crosshair)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def update_resolutions(self):
        # Get the selected monitor
        selected_monitor = self.monitors[self.combo_monitor.currentIndex()]
        
        # Clear the resolution combo box
        self.combo_resolution.clear()

        # Use QScreen to get the resolution of the selected monitor
        screen = QtWidgets.QApplication.primaryScreen()  # Get the active monitor (you can change this based on the selected index)
        
        # Use screen.geometry() to get the maximum supported resolution
        available_resolutions = [screen.geometry().size()]

        # Add resolutions to the combo box
        for res in available_resolutions:
            self.combo_resolution.addItem(f"{res.width()} x {res.height()}", res)

        # Set the current resolution as selected by default
        current_resolution = QtCore.QSize(selected_monitor.width, selected_monitor.height)
        index = self.combo_resolution.findData(current_resolution)
        self.combo_resolution.setCurrentIndex(index)

    def launch_crosshair(self):
        # Get the selected monitor, resolution, and game
        selected_monitor = self.monitors[self.combo_monitor.currentIndex()]
        selected_resolution = self.combo_resolution.currentData()
        selected_game = self.combo_game.currentText()

        # Create and show the Crosshair window on the selected screen and resolution
        self.crosshair = CrosshairApp(selected_monitor, selected_resolution, selected_game)
        self.crosshair.show()
