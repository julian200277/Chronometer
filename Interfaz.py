from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QMainWindow
from Styles import Estilos_1
import sys
from datetime import datetime
import os
import platform


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(991, 268)
        MainWindow.setWindowIcon(QtGui.QIcon('img/logo.png'))
        self.estilos = Estilos_1()
        MainWindow.setStyleSheet(self.estilos.estiloPrincipal)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.splitter = QSplitter(self.frame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spinBox = QSpinBox(self.layoutWidget)
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_2.addWidget(self.spinBox)

        self.spinBox_2 = QSpinBox(self.layoutWidget)
        self.spinBox_2.setAlignment(Qt.AlignCenter)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.horizontalLayout_2.addWidget(self.spinBox_2)

        self.spinBox_3 = QSpinBox(self.layoutWidget)
        self.spinBox_3.setAlignment(Qt.AlignCenter)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.horizontalLayout_2.addWidget(self.spinBox_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.lcdNumber_2 = QLCDNumber(self.layoutWidget1)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setFrameShape(QFrame.Panel)
        self.lcdNumber_2.setLineWidth(2)
        self.lcdNumber_2.setDigitCount(12)

        self.gridLayout.addWidget(self.lcdNumber_2, 1, 1, 1, 1)

        self.lcdNumber = QLCDNumber(self.layoutWidget1)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setFrameShape(QFrame.Panel)
        self.lcdNumber.setLineWidth(2)
        self.lcdNumber.setDigitCount(12)

        self.gridLayout.addWidget(self.lcdNumber, 1, 0, 1, 1)

        self.splitter.addWidget(self.layoutWidget1)

        self.horizontalLayout_3.addWidget(self.splitter)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 991, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Temporizador", u"Temporizador", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Programar Apagado", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Horas", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Minutos", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Segundos", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"HORA ACTUAL", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SE APAGA EN...", None))
    # retranslateUi

class Interfaz(QMainWindow):
    def __init__(self):
        super(Interfaz, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QTimer() #Temporizador

        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.tiempo_total = 0

        #SEÑALES
        self.ui.spinBox.valueChanged.connect(self.valores_tiempo)
        self.ui.spinBox_2.valueChanged.connect(self.valores_tiempo)
        self.ui.spinBox_3.valueChanged.connect(self.valores_tiempo)
        self.ui.pushButton.clicked.connect(self.iniciar)
        self.ui.pushButton_2.clicked.connect(self.cancelar)
        self.ui.pushButton_3.clicked.connect(self.salir)
        self.timer.timeout.connect(self.lcd_display)

    def valores_tiempo(self):
        self.horas = self.ui.spinBox.value() #horas en segundos
        self.minutos = self.ui.spinBox_2.value() #minutos en segundos
        self.segundos = self.ui.spinBox_3.value() # directo
        self.tiempo_total = (self.horas * 3600) + (self.minutos * 60) + self.segundos

    def lcd_display(self):
        sistema = platform.system()
        #print("Estamos en {}".format(sistema))
        #Este código es como un bucle en el tiempo que se detiene hasta que sea llamada la funcion stop
        tiempo = datetime.now()
        self.timer.start(1000)
        tiempo_formateado = tiempo.strftime("%I:%M:%S:%p")
        self.ui.lcdNumber.display(tiempo_formateado) # LCD 1
        self.ui.lcdNumber_2.display(self.formatear_tiempo(self.tiempo_total)) #LCD 2

        if(self.tiempo_total == 0):
            self.timer.stop()
            if(sistema == "Linux"):
                os.system('shutdown now')
            elif(sistema == "Windows"):
                os.system('shutdown /P')
        self.tiempo_total -= 1

    def formatear_tiempo(self, segundos):
        horas = int(segundos / 60 / 60)
        segundos -= horas * 60 * 60
        minutos = int(segundos / 60)
        segundos -= minutos * 60
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    def iniciar(self):
        self.lcd_display()

    def cancelar(self):
        self.timer.stop()


    def salir(self):
        self.timer.stop()
        sys.exit()


