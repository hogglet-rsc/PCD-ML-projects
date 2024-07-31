import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class SimpleGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple GUI')
        self.setGeometry(100, 100, 300, 200)

        label = QLabel('Hello, World!')
        layout = QVBoxLayout()
        layout.addWidget(label)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleGUI()
    ex.show()
    sys.exit(app.exec_())