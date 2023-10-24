from Interfaz import Interfaz
from PySide6.QtWidgets import  QApplication
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Interfaz()
    window.show()
    app.exec()
