import PyQt5.QtWidgets as qtw

class mainWindow (qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calc')
        self.setLayout(qtw.QVBoxLayout())       
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []
        self.show()

    def keypad(self):
        container = qtw.QWidget()               # A Window to store the widgets
        container.setLayout(qtw.QGridLayout())  # Grid Layout for the Keypad 

        # Buttons
        self.result = qtw.QLineEdit()
        btn_result = qtw.QPushButton('Enter',clicked = self.func_result)
        btn_clear = qtw.QPushButton('Clear',clicked = self.clear_it) 
        btn_9 = qtw.QPushButton('9',clicked = lambda: self.num_press('9'))
        btn_8 = qtw.QPushButton('8',clicked = lambda: self.num_press('8'))
        btn_7 = qtw.QPushButton('7',clicked = lambda: self.num_press('7'))
        btn_6 = qtw.QPushButton('6',clicked = lambda: self.num_press('6'))
        btn_5 = qtw.QPushButton('5',clicked = lambda: self.num_press('5'))
        btn_4 = qtw.QPushButton('4',clicked = lambda: self.num_press('4'))
        btn_3 = qtw.QPushButton('3',clicked = lambda: self.num_press('3'))
        btn_2 = qtw.QPushButton('2',clicked = lambda: self.num_press('2'))
        btn_1 = qtw.QPushButton('1',clicked = lambda: self.num_press('1'))
        btn_0 = qtw.QPushButton('0',clicked = lambda: self.num_press('0'))
        btn_sum = qtw.QPushButton('+',clicked = lambda: self.func_press('+'))
        btn_sub = qtw.QPushButton('-',clicked = lambda: self.func_press('-'))
        btn_Mult = qtw.QPushButton('x',clicked = lambda: self.func_press('*'))
        btn_div = qtw.QPushButton('/',clicked = lambda: self.func_press('/'))


        # Adding Buttons to Container
        container.layout().addWidget(self.result,0,0,1,4)
        container.layout().addWidget(btn_result,1,0,1,2)
        container.layout().addWidget(btn_clear,1,2,1,2)
        container.layout().addWidget(btn_9,2,0)
        container.layout().addWidget(btn_8,2,1)
        container.layout().addWidget(btn_7,2,2)
        container.layout().addWidget(btn_sum,2,3)
        container.layout().addWidget(btn_6,3,0)
        container.layout().addWidget(btn_5,3,1)
        container.layout().addWidget(btn_4,3,2)
        container.layout().addWidget(btn_sub,3,3)
        container.layout().addWidget(btn_3,4,0)
        container.layout().addWidget(btn_2,4,1)
        container.layout().addWidget(btn_1,4,2)
        container.layout().addWidget(btn_Mult,4,3)
        container.layout().addWidget(btn_0,5,1)
        container.layout().addWidget(btn_div,5,3)


        # Adding Container to layout
        self.layout().addWidget(container)
        
    def num_press(self,key_num):
        self.temp_nums.append(key_num)
        temp_str = ('').join(self.temp_nums)

        if self.fin_nums:
            self.result.setText(''.join(self.fin_nums) + temp_str)
        else:
            self.result.setText(temp_str)
    
    def func_press(self,op_press):
        temp_str = ''.join(self.temp_nums)
        self.fin_nums.append(temp_str)
        self.fin_nums.append(op_press)
        self.temp_nums = []
        self.result.setText(''.join(self.fin_nums))
    
    def func_result(self):
        if self.temp_nums:
            fin_str = ''.join(self.fin_nums) + ''.join(self.temp_nums)
            result_str = eval(fin_str)
            fin_str += ' = '
            fin_str += str(result_str)
            self.result.setText(fin_str)

    def clear_it(self):
        self.result.clear()
        self.temp_nums = []
        self.fin_nums = []
        


if __name__ == "__main__":
    app = qtw.QApplication([])
    mw = mainWindow()
    app.setStyle(qtw.QStyleFactory.create('Fusion'))
    app.exec_()

