# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewHidro.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#



import random
import hidrometro #importando CLIENTE UDP

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Paineldecontrole(object):
    def setupUi(self, Paineldecontrole):
        Paineldecontrole.setObjectName("Paineldecontrole")
        Paineldecontrole.resize(271, 190)
        Paineldecontrole.setFixedSize(271,190)            
        self.centralwidget = QtWidgets.QWidget(Paineldecontrole)
        self.centralwidget.setObjectName("centralwidget")
        self.botaoOk = QtWidgets.QPushButton(self.centralwidget)
        self.botaoOk.setGeometry(QtCore.QRect(90, 100, 91, 31))
        self.botaoOk.setObjectName("botaoOk")
        self.inputVazao = QtWidgets.QLineEdit(self.centralwidget)
        self.inputVazao.setGeometry(QtCore.QRect(30, 60, 211, 20))
        self.inputVazao.setReadOnly(False)
        self.inputVazao.setObjectName("inputVazao")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 191, 20))
        self.label.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 201, 20))
        self.label_2.setStyleSheet("font: italic 8pt \"Segoe UI Semilight\";")
        self.label_2.setObjectName("label_2")
        Paineldecontrole.setCentralWidget(self.centralwidget)
        self.botaoOk.clicked.connect(self.atualiza) #chama o método para atualizar o valor        

        self.retranslateUi(Paineldecontrole)
        QtCore.QMetaObject.connectSlotsByName(Paineldecontrole)

    def retranslateUi(self, Paineldecontrole):
        _translate = QtCore.QCoreApplication.translate
        Paineldecontrole.setWindowTitle(_translate("Paineldecontrole", "MainWindow"))
        self.botaoOk.setText(_translate("Paineldecontrole", "Inserir"))
        self.inputVazao.setPlaceholderText(_translate("Paineldecontrole", "Digite a vazão que deseja inserir"))
        self.label.setText(_translate("Paineldecontrole", "Painel de controle Hidrometro"))
        self.label_2.setText(_translate("Paineldecontrole", "a vazão deve ser inserida no formato \'xx\'"))

    def atualiza(self): #método para inserir valor ele inicia a thread
        vazao = int(self.inputVazao.text()) #aqui pegamos o valor da caixa de texto               
        hidrometroiD = str(random.randint(1000,9999)) #gera matricula
        hidrometro1 = hidrometro.Hidrometro(hidrometroiD) #cria objeto
        hidrometro1.threadEnvia(vazao)

        msg = QMessageBox() #abre a mensagem para notificar
        msg.setIcon(msg.Information)
        msg.setWindowTitle('Sucesso')
        msg.setText("Resultado"+str(vazao)+"ºC")
        msg.exec()
 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Paineldecontrole = QtWidgets.QMainWindow()
    ui = Ui_Paineldecontrole()
    ui.setupUi(Paineldecontrole)
    Paineldecontrole.show()
    sys.exit(app.exec_())
