import sys
from PyQt5 import QtWidgets
from monitor_selector import MonitorSelector

def main():
    app = QtWidgets.QApplication(sys.argv)
    selector = MonitorSelector()
    selector.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
