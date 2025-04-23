# # # import sys
# # # from PyQt5 import QtWidgets
# # # from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
# # # from PyQt5.QtGui import QIcon

# # # def window():
# # #     app = QApplication(sys.argv)
# # #     win = QMainWindow()

# # #     win.setWindowTitle('First Application')
# # #     win.setGeometry(200,200,700,700)
# # #     win.setWindowIcon(QIcon('icon.png'))
# # #     win.setToolTip('my tooltip')

# # #     win.show()
# # #     sys.exit(app.exec_())

# # # window()

# # import sys
# # from PyQt5 import QtWidgets
# # from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
# # from PyQt5.QtGui import QIcon

# # def window():
# #     app = QApplication(sys.argv)
# #     win = QMainWindow()   

# #     win.setWindowTitle('First Application')
# #     win.setGeometry(200,200,700,700)
# #     win.setWindowIcon(QIcon('icon.png'))
# #     win.setToolTip('my tooltip')

# #     lbl_name = QtWidgets.QLabel(win)
# #     lbl_name.setText('Adınız: ')
# #     lbl_name.move(50,30)

# #     lbl_surname = QtWidgets.QLabel(win)
# #     lbl_surname.setText('Soyadınız: ')
# #     lbl_surname.move(50,70)

# #     txt_name = QtWidgets.QLineEdit(win)
# #     txt_name.move(150, 30)

# #     txt_surname = QtWidgets.QLineEdit(win)
# #     txt_surname.move(150, 70)

# #     def clicked(self):
# #         print('butona tıklandı name: '+ txt_name.text()+ ' surname: '+ txt_surname.text())

# #     btn_save = QtWidgets.QPushButton(win)
# #     btn_save.setText('Kaydet')
# #     btn_save.move(150,110)
# #     btn_save.clicked.connect(clicked)

# #     win.show()
# #     sys.exit(app.exec_())

# # window()

# import sys
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
# from PyQt5.QtGui import QIcon

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()

#         self.setWindowTitle('First Application')
#         self.setGeometry(200,200,700,700)
#         self.setWindowIcon(QIcon('icon.png'))
#         self.setToolTip('my tooltip')
#         self.initUI()

#     def initUI(self):
#         self.lbl_name = QtWidgets.QLabel(self)
#         self.lbl_name.setText('Adınız: ')
#         self.lbl_name.move(50,30)

#         self.lbl_surname = QtWidgets.QLabel(self)
#         self.lbl_surname.setText('Soyadınız: ')
#         self.lbl_surname.move(50,70)

#         self.lbl_resut = QtWidgets.QLabel(self)
#         self.lbl_resut.resize(300,50)
#         self.lbl_resut.move(150,300)

#         self.txt_name = QtWidgets.QLineEdit(self)
#         self.txt_name.move(150, 30)
#         self.txt_name.resize(200,32)

#         self.txt_surname = QtWidgets.QLineEdit(self)
#         self.txt_surname.move(150, 70)
#         self.txt_surname.resize(200,32)

#         self.btn_save = QtWidgets.QPushButton(self)
#         self.btn_save.setText('Kaydet')
#         self.btn_save.move(150,110)
#         self.btn_save.clicked.connect(self.clicked)

#     def clicked(self):
#         self.lbl_resut.setText('ad: '+ self.txt_name.text()+ ' soyad: '+ self.txt_surname.text())        

# def window():
#     app = QApplication(sys.argv)
#     win = MyWindow()  
#     win.show()
#     sys.exit(app.exec_())

# window()


import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('Sayı 1: ')
        self.lbl_sayi1.move(50,30)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText('Sayı 2: ')
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText('Toplama')
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.hesapma)

        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText('Çıkarma')
        self.btn_cikar.move(150,170)
        self.btn_cikar.clicked.connect(self.hesapma)

        self.btn_carpma = QtWidgets.QPushButton(self)
        self.btn_carpma.setText('Çarpma')
        self.btn_carpma.move(150,210)
        self.btn_carpma.clicked.connect(self.hesapma)

        self.btn_bolme = QtWidgets.QPushButton(self)
        self.btn_bolme.setText('Bölme')
        self.btn_bolme.move(150,250)
        self.btn_bolme.clicked.connect(self.hesapma)

        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText('sonuç: ')
        self.lbl_sonuc.move(150,290)

    def hesapma(self):
        sender = self.sender().text()
        result = 0

        if sender == 'Toplama':
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        elif sender == 'Çıkarma':
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        elif sender == 'Çarpma':
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        elif sender == 'Bölme':
            result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())

        self.lbl_sonuc.setText('sonuç: '+ str(result))

def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()