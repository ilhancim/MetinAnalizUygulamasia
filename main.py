from PyQt5.QtWidgets import *
import panel0
import panel1
import panel2
import panel3
import panel4
import panel5

class p0(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p0 = panel0.Ui_MainWindow()
        self.p0.setupUi(self)
        self.p1 = p1()
        self.p2 = p2()
        self.p3 = p3()
        self.p4 = p4()
        self.p5 = p5()
        self.p0.pb1.clicked.connect(self.buton1)
        self.p0.pb2.clicked.connect(self.buton2)
        self.p0.pb3.clicked.connect(self.buton3)
        self.p0.pb4.clicked.connect(self.buton4)
        self.p0.pb5.clicked.connect(self.buton5)
    def buton1(self):
        self.close()
        self.p1.show()

    def buton2(self):
        self.close()
        self.p2.show()

    def buton3(self):
        self.close()
        self.p3.show()

    def buton4(self):
        self.close()
        self.p4.show()

    def buton5(self):
        self.close()
        self.p5.show()

class p1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p1 = panel1.Ui_MainWindow()
        self.p1.setupUi(self)
        self.p1.pushButton.clicked.connect(self.anaEkran)

    def anaEkran(self):
        self.close()
        self.p0 = p0()
        self.p0.show()



class p2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p2 = panel2.Ui_MainWindow()
        self.p2.setupUi(self)
        self.p2.pushButton.clicked.connect(self.anaEkran)

    def anaEkran(self):
        self.close()
        self.p0 = p0()
        self.p0.show()

class p3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p3 = panel3.Ui_MainWindow()
        self.p3.setupUi(self)
        self.p3.pushButton.clicked.connect(self.anaEkran)

    def anaEkran(self):
        self.close()
        self.p0 = p0()
        self.p0.show()

class p4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p4 = panel4.Ui_MainWindow()
        self.p4.setupUi(self)
        self.p4.pushButton.clicked.connect(self.anaEkran)

    def anaEkran(self):
        self.close()
        self.p0 = p0()
        self.p0.show()

class p5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p5 = panel5.Ui_MainWindow()
        self.p5.setupUi(self)
        self.p5.pushButton.clicked.connect(self.anaEkran)

    def anaEkran(self):
        self.close()
        self.p0 = p0()
        self.p0.show()

app = QApplication([])
pencere = p0()
pencere.show()
app.exec_()