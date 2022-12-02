import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.num1 = 0
        self.test = ""

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_all = QGridLayout()
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_equation = QLabel("Equation: ")
        self.equation = QLineEdit("")
        self.solution = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addRow(label_equation, self.equation)

        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")
        button_remain = QPushButton("%")
        button_reciprocal = QPushButton("1/x")
        button_square = QPushButton("x^2")
        button_root = QPushButton("x^(1/2)")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))
        button_remain.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))
        button_reciprocal.clicked.connect(lambda state, operation = "1/x": self.button_operation1_clicked(operation)) 
        button_square.clicked.connect(lambda state, operation = "x^2": self.button_operation1_clicked(operation))
        button_root.clicked.connect(lambda state, operation = "x^(1/2)": self.button_operation1_clicked(operation))
        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_all.addWidget(button_plus, 4, 3)
        layout_all.addWidget(button_minus, 3, 3)
        layout_all.addWidget(button_product, 2, 3)
        layout_all.addWidget(button_division, 1, 3)
        
        layout_all.addWidget(button_remain, 0, 0)
        layout_all.addWidget(button_reciprocal, 1, 0)
        layout_all.addWidget(button_square, 1, 1)
        layout_all.addWidget(button_root, 1, 2)


        ### =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("C")
        button_ce = QPushButton("CE")
        button_backspace = QPushButton("Backspace")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_ce.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_all.addWidget(button_clear, 0, 2)
        layout_all.addWidget(button_ce, 0, 1)
        layout_all.addWidget(button_backspace, 0, 3)
        layout_all.addWidget(button_equal, 5, 3)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                x += 2
                layout_all.addWidget(number_button_dict[number], x, y)
            elif number==0:
                layout_all.addWidget(number_button_dict[number], 5, 1)

        ### 소숫점 버튼과 +/- 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.button_dot(num))
        layout_all.addWidget(button_dot, 5, 2)

        button_negative = QPushButton("+/-")
        button_negative.clicked.connect(self.button_negative)
        layout_all.addWidget(button_negative, 5, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_all)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        if self.equation.text() == '+':
            self.equation.setText("")
            equation = self.equation.text()
            equation += str(num)
        if self.equation.text() == '-':
            self.equation.setText("")
            equation = self.equation.text()
            equation += str(num)
        if self.equation.text() == '*':
            self.equation.setText("")
            equation = self.equation.text()
            equation += str(num)
        if self.equation.text() == '/':
            self.equation.setText("")
            equation = self.equation.text()
            equation += str(num)
        if self.equation.text() == '%':
            self.equation.setText("")
            equation = self.equation.text()
            equation += str(num)
            self.equation.setText(equation)
        else:
            equation = self.equation.text()
            equation += str(num)
            self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        self.num1 = self.equation.text()
        self.test = operation
        self.equation.setText(self.test)

    def button_operation1_clicked(self, operation):
        equation = self.equation.text()
        if operation == "1/x":
            number = float(equation)
            number = 1/number
            self.equation.setText(str(number))

        if operation == "x^2":
            number = float(equation)
            number = number * number
            self.equation.setText(str(number))

        if operation == "x^(1/2)":
            number = float(equation)
            number = number ** (1/2)
            self.equation.setText(str(number))

    def button_negative(self):
        num2 = self.equation.text()
        num2 = -1 * float(num2)
        self.equation.setText(str(num2))

    def button_dot(self, num):
        num2 = self.equation.text()         ## 이미 소숫점이 존재할 떄 더이상 점을 못찍게 하는 함수
        if (num2.find('.') == -1):
            equation = self.equation.text()
            equation += str(num)
            self.equation.setText(equation)
        else :
            return

    
    def button_equal_clicked(self):
        if self.test == '+':
            num2 = self.equation.text()
            sum = float(self.num1) + float(num2)
            self.equation.setText(str(sum))
        if self.test == '-':
            num2 = self.equation.text()
            sum = float(self.num1) - float(num2)
            self.equation.setText(str(sum))
        if self.test == '*':
            num2 = self.equation.text()
            sum = float(self.num1) * float(num2)
            self.equation.setText(str(sum))
        if self.test == '/':
            num2 = self.equation.text()
            sum = float(self.num1) / float(num2)
            self.equation.setText(str(sum))
        if self.test == '%':
            num2 = self.equation.text()
            sum = float(self.num1) % int(num2)
            self.equation.setText(str(sum))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.test = ""

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())