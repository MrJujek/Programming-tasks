import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtWidgets import QMessageBox
import math


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
# do tego momentu tak jak u ciebie

        self.initUI() # tutaj wywołujemy metode z linijki 12

    def initUI(self): # metoda inicjalizująca interfejs

        self.setWindowTitle('Kalkulator')
        self.setGeometry(100, 100, 300, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        # do tego momentu miałaś podobnie

        # od tego momentu robimy guziki
        self.textbox = QLineEdit()
        self.layout.addWidget(self.textbox)

        self.buttons = QGridLayout()
        self.layout.addLayout(self.buttons)

        btn1 = QPushButton('1')
        btn1.clicked.connect(self.on_click)
        self.buttons.addWidget(btn1, 2, 0)

        btn2 = QPushButton('2')
        btn2.clicked.connect(self.on_click)
        self.buttons.addWidget(btn2, 2, 1)

        btn3 = QPushButton('3')
        btn3.clicked.connect(self.on_click)
        self.buttons.addWidget(btn3, 2, 2)

        btn4 = QPushButton('4')
        btn4.clicked.connect(self.on_click)
        self.buttons.addWidget(btn4, 1, 0)

        btn5 = QPushButton('5')
        btn5.clicked.connect(self.on_click)
        self.buttons.addWidget(btn5, 1, 1)

        btn6 = QPushButton('6')
        btn6.clicked.connect(self.on_click)
        self.buttons.addWidget(btn6, 1, 2)

        btn7 = QPushButton('7')
        btn7.clicked.connect(self.on_click)
        self.buttons.addWidget(btn7, 0, 0)

        btn8 = QPushButton('8')
        btn8.clicked.connect(self.on_click)
        self.buttons.addWidget(btn8, 0, 1)

        btn9 = QPushButton('9')
        btn9.clicked.connect(self.on_click)
        self.buttons.addWidget(btn9, 0, 2)

        btnSub = QPushButton('-')
        btnSub.clicked.connect(self.on_click)
        self.buttons.addWidget(btnSub, 2, 3)

        btn0 = QPushButton('0')
        btn0.clicked.connect(self.on_click)
        self.buttons.addWidget(btn0, 3, 0)

        btnDot = QPushButton('.')
        btnDot.clicked.connect(self.on_click)
        self.buttons.addWidget(btnDot, 3, 1)

        btnEqual = QPushButton('=')
        btnEqual.clicked.connect(self.on_click)
        self.buttons.addWidget(btnEqual, 3, 2)

        btnAdd = QPushButton('+')
        btnAdd.clicked.connect(self.on_click)
        self.buttons.addWidget(btnAdd, 3, 3)

        btnMul = QPushButton('*')
        btnMul.clicked.connect(self.on_click)
        self.buttons.addWidget(btnMul, 1, 3)

        btnDiv = QPushButton('/')
        btnDiv.clicked.connect(self.on_click)
        self.buttons.addWidget(btnDiv, 0, 3)

        btnClear = QPushButton('C')
        btnClear.clicked.connect(self.clear_textbox)
        self.buttons.addWidget(btnClear, 4, 0)

        btnPow = QPushButton('^')
        btnPow.clicked.connect(self.on_click)
        self.buttons.addWidget(btnPow, 4, 1)

        btnSqrt = QPushButton('√')
        btnSqrt.clicked.connect(self.on_click)
        self.buttons.addWidget(btnSqrt, 4, 2)

    def clear_textbox(self):
        self.textbox.clear()
        # koniec robienia guzików

    def on_click(self): # metoda obsługująca kliknięcie w guzik
        sender = self.sender() # pobieramy obiekt, który wywołał zdarzenie
        text = sender.text() # pobieramy tekst z guzika
        print(text) # wyświetlamy tekst z guzika w konsoli

        if text == '=': # jeśli tekst to '=' to wykonujemy obliczenia
            try:
                poprawiony_text = self.textbox.text().replace('^', '**').replace('√', 'math.sqrt(') # zamieniamy znaki na odpowiednie operatory
                if 'math.sqrt(' in poprawiony_text:
                    poprawiony_text += ')'
                result = eval(poprawiony_text)
                # wyrażenie eval wykonuje kod pythona zapisany w postaci stringa
                # np. eval('2 + 2') zwróci 4

                print(result) # wyświetlamy wynik w konsoli

                self.textbox.setText(str(result))

            except Exception as e: # jeśli wystąpi błąd wyświetlamy komunikat 'Error'
                # np. jeśli użytkownik wpisze '2 + abc'           
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Critical)
                error_dialog.setText('Error')
                if str(e) == 'math domain error':
                    error_dialog.setInformativeText('Nie można wyciągnąć pierwiastka z liczby ujemnej')
                else: 
                    error_dialog.setInformativeText(str(e))
                error_dialog.setWindowTitle('Error')
                error_dialog.exec_()

        else: # w przeciwnym wypadku dodajemy tekst do wyświetlacza
            self.textbox.setText(self.textbox.text() + text)


# co do tego to ci zdjęcie wysłałem
app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
sys.exit(app.exec_())