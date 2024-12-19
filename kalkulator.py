import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QLineEdit, QWidget
from PyQt5.QtCore import Qt

class CalculatorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setFixedSize(300, 400)
        # Центральный виджет
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        # Основной макет
        layout = QGridLayout()
        central_widget.setLayout(layout)
        # Красное поле для вывода
        self.output_field = QLineEdit()
        self.output_field.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.output_field.setReadOnly(True)
        self.output_field.setFixedHeight(50)
        self.output_field.setStyleSheet("border: 2px solid red;")
        layout.addWidget(self.output_field, 0, 0, 1, 4)
        # Синее поле для кнопок
        button_container = QWidget()
        button_container.setStyleSheet("border: 2px solid blue;")
        button_layout = QGridLayout()
        button_container.setLayout(button_layout)
        layout.addWidget(button_container, 1, 0, 1, 4)
        # Кнопки калькулятора
        buttons = [
            ('', 0, 0), ('', 0, 1), ('', 0, 2), ('', 0, 3),
            ('', 1, 0), ('', 1, 1), ('', 1, 2), ('', 1, 3),
            ('', 2, 0), ('', 2, 1), ('', 2, 2), ('', 2, 3),
            ('', 3, 0), ('', 3, 1),
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFixedSize(50, 50)
            button.setStyleSheet("border: 2px solid green;")
            button_layout.addWidget(button, row, col)
        equal_plus_button = QPushButton('')
        equal_plus_button.setFixedSize(125, 50)
        equal_plus_button.setStyleSheet("border: 2px solid green;")
        button_layout.addWidget(equal_plus_button, 3, 2, 1, 2)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorUI()
    window.show()
    sys.exit(app.exec())