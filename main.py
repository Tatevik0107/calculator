from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.set_UI()

    def set_UI(self):
        self.setWindowTitle('Калькулятор')
        self.setGeometry(200, 200, 400, 400)

        self.le = QLineEdit(self)
        self.le.setGeometry(50, 20, 300, 30)

        self.btn1 = QPushButton(self)
        self.btn1.setGeometry(60, 80, 50, 50)
        self.btn1.setText('1')
        self.btn1.clicked.connect(lambda:self.set_numbers(self.btn1))
        
        self.btn2 = QPushButton(self)
        self.btn2.setGeometry(140, 80, 50, 50)
        self.btn2.setText('2')
        self.btn2.clicked.connect(lambda:self.set_numbers(self.btn2))
        
        self.btn3 = QPushButton(self)
        self.btn3.setGeometry(220, 80, 50, 50)
        self.btn3.setText('3')
        self.btn3.clicked.connect(lambda:self.set_numbers(self.btn3))
        
        self.btnCLR = QPushButton(self)
        self.btnCLR.setGeometry(300, 80, 50, 50)
        self.btnCLR.setText('CLR')
        self.btnCLR.clicked.connect(self.set_CLR)

        self.btn4 = QPushButton(self)
        self.btn4.setGeometry(60, 160, 50, 50)
        self.btn4.setText('4')
        self.btn4.clicked.connect(lambda:self.set_numbers(self.btn4))
        
        self.btn5 = QPushButton(self)
        self.btn5.setGeometry(140, 160, 50, 50)
        self.btn5.setText('5')
        self.btn5.clicked.connect(lambda:self.set_numbers(self.btn5))

        self.btn6 = QPushButton(self)
        self.btn6.setGeometry(220, 160, 50, 50)
        self.btn6.setText('6')
        self.btn6.clicked.connect(lambda:self.set_numbers(self.btn6))
        
        self.btnP = QPushButton(self)
        self.btnP.setGeometry(300, 160, 50, 50)
        self.btnP.setText('+')
        self.btnP.clicked.connect(lambda:self.set_numbers(self.btnP))

        self.btn7 = QPushButton(self)
        self.btn7.setGeometry(60, 240, 50, 50)
        self.btn7.setText('7')
        self.btn7.clicked.connect(lambda:self.set_numbers(self.btn7))
        
        self.btn8 = QPushButton(self)
        self.btn8.setGeometry(140, 240, 50, 50)
        self.btn8.setText('8')
        self.btn8.clicked.connect(lambda:self.set_numbers(self.btn8))
        
        self.btn9 = QPushButton(self)
        self.btn9.setGeometry(220, 240, 50, 50)
        self.btn9.setText('9')
        self.btn9.clicked.connect(lambda:self.set_numbers(self.btn9))

        self.btnM = QPushButton(self)
        self.btnM.setGeometry(300, 240, 50, 50)
        self.btnM.setText('-')
        self.btnM.clicked.connect(lambda:self.set_numbers(self.btnM))
        
        self.btn0 = QPushButton(self)
        self.btn0.setGeometry(60, 320, 50, 50)
        self.btn0.setText('0')
        self.btn0.clicked.connect(lambda:self.set_numbers(self.btn0))

        self.btnU = QPushButton(self)
        self.btnU.setGeometry(140, 320, 50, 50)
        self.btnU.setText('*')
        self.btnU.clicked.connect(lambda:self.set_numbers(self.btnU))

        self.btnD = QPushButton(self)
        self.btnD.setGeometry(220, 320, 50, 50)
        self.btnD.setText('/')
        self.btnD.clicked.connect(lambda:self.set_numbers(self.btnD))

        self.btnR = QPushButton(self)
        self.btnR.setGeometry(300, 320, 50, 50)
        self.btnR.setText('=')
        self.btnR.clicked.connect(self.set_Ravno)    
        
        self.show()

    def set_numbers(self, bt):
        self.le.setText(self.le.text()+bt.text())

    def set_CLR(self):
        self.le.setText("")
    def set_Ravno(self):
        char=self.le.text()
        dict=["1","2","3","4","5","6","7","8","9","0"]
        for num in range(10):
            char=char.replace(dict[num],"")
        if char:
            nums=self.le.text().split(char)
            for id in range(2):
                nums[id]=int(nums[id])
            if char=="+":
                plus=nums[0]+nums[1]
                self.le.setText(str(plus))
            if char=="-":
                minus=nums[0]-nums[1]
                self.le.setText(str(minus))
            if char=="*":
                umn=nums[0]*nums[1]
                self.le.setText(str(umn))
            if char=="/":
                if nums[1]==0:
                    self.le.setText("на ноль делить нельзя!!!")
                else:   
                    delenie=nums[0]/nums[1]
                    self.le.setText(str(delenie))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())