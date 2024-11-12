import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget # type: ignore
from PyQt5.QtCore import QTimer, QTime, Qt # type: ignore
from PyQt5.QtGui import QFont, QFontDatabase # type: ignore

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock By Adnan")
        self.setGeometry(600, 400, 300, 100)

        # Layout setup
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        # Styling
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("color: hsl(114, 98%, 49%);")
        self.setStyleSheet("background-color: black;")
        
        # Load custom font with error handling
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.time_label.setFont(QFont(font_family, 100))
        else:
            print("Font not found! Using default font.")
            self.time_label.setFont(QFont("Arial", 100))

        # Timer to update the time
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
