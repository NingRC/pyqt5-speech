from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QTextEdit,QFontDialog, QLineEdit,QStyle,QFormLayout, QInputDialog,QVBoxLayout,QWidget,QApplication ,QHBoxLayout,QDialog,QPushButton,QMainWindow,QGridLayout,QLabel

class Ui_Incise(object):
    def setupUi(self, Incise):
        Incise.setObjectName("Incise")
        Incise.resize(1280, 720)
        Incise.setStyleSheet("QLineEdit{\n"
                                 "    border:0px;    \n"
                                 "    margin:10px;\n"
                                 "    margin-left:10px; \n"
                                 "    margin-right:10px;\n"
                                 "    border-bottom: 2px solid #B3B3B3;\n"
                                 "    font-family:\'Microsoft YaHei\';\n"
                                 "    font-size:20px;\n"
                                 "    font-weight:bold;\n"
                                 "    }\n"
                                 "\n"
                                 "QLineEdit:hover{\n"
                                 "    border-bottom: 3px solid #66A3FF;\n"
                                 "    }\n"
                                 "\n"
                                 "QLineEdit:focus{\n"
                                 "    border-bottom: 3px solid #E680BD;\n"
                                 "    }\n"
                                 "\n"
                                 "QWidget#centralwidget{\n"
                                 "    background: white;\n"
                                 "    border-radius:10px;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel{\n"
                                 "    text-align:right;\n"
                                 "    font-family:\'Microsoft YaHei\';\n"
                                 "    font-size:20px;\n"
                                 "    font-weight:bold;\n"
                                 "    }\n"
                                 "\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(Incise)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 20, 500, 80))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet(
                                    "font-family:\'Microsoft YaHei\';\n"
                                    "font-size: 20px;\n"
                                    "border-radius: 5px ;\n"
                                    "border: 1px solid 	#1E90FF !important;"
                                   )

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 1140, 140))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet(
                                    "border-radius: 10px ;\n"
                                    "border: 1px solid #9370DB !important;"
                                   )
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 280, 1160, 400))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet(
                                    "border-radius: 10px ;\n"
                                    # "border: 1.5px solid #9370DB !important;"
                                    "border-image: url(:/icons/background.png);\n"
                                   )

        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(62, 358, 1155, 2))
        self.line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.line_1.setStyleSheet("border: 1px solid LightGrey;")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1100, 30, 80, 26))
        self.pushButton.setMinimumSize(QtCore.QSize(22, 22))
        self.pushButton.setMaximumSize(QtCore.QSize(22, 22))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton\n"
                                      "{\n"
                                          "color:White;\n"
                                          "background: #9D9D9D;\n"
                                          "border-radius:10px;\n"
                                      "}\n"
                                      "QPushButton:hover\n"
                                      "{\n"
                                          "background: #6C6C6C;\n"
                                      "}\n"
                                      "QPushButton:pressed\n"
                                      "{\n"
                                          "border: 1px solid #3C3C3C!important;"
                                          "background: #281f1d;"
                                      "}\n"
                                      "\n")
        self.pushButton.setText("一")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1150, 30, 80, 26))
        self.pushButton_2.setMinimumSize(QtCore.QSize(22, 22))
        self.pushButton_2.setMaximumSize(QtCore.QSize(22, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton\n"
                                        "{\n"
                                            "color:White;\n"
                                            "background: #FFE4B5;\n"
                                            "border-radius:10px;\n"
                                        "}\n"
                                        "QPushButton:hover\n"
                                        "{\n"
                                            "background: #FFA500;\n"
                                        "}\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                            "border: 1px solid #3C3C3C!important;"
                                        "}\n"
                                        "\n"
                                        "")
        self.pushButton_2.setText("口")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1200, 30, 80, 26))
        self.pushButton_3.setMinimumSize(QtCore.QSize(22, 22))
        self.pushButton_3.setMaximumSize(QtCore.QSize(22, 22))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("QPushButton\n"
                                        "{\n"
                                            "color:White;\n"
                                            "background: #F08080;\n"
                                            "border-radius:10px;\n"
                                        "}\n"
                                        "QPushButton:hover\n"
                                        "{\n"
                                            "background: #FF2D2D;\n"
                                        "}\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                            "border: 1px solid #3C3C3C!important;"
                                        "}\n"
                                        "\n"
                                        "")
        self.pushButton_3.setText("X")

        self.pushButton_goback = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_goback.setGeometry(QtCore.QRect(40, 30, 50, 30))
        self.pushButton_goback.setObjectName("pushButton_goback")
        self.pushButton_goback.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "border-radius: 15px;\n"
            "border: 1px solid rgba(100, 100, 100, .9) !important;"
            "}\n"
            "QPushButton:hover\n"
            "{\n"
            "background: Gainsboro;\n"
            "}\n"
        )
        self.pushButton_goback.setText("⇦")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 300, 40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "color: Snow;\n"
            "background: #9370DB;\n"
            "font-family:\'Microsoft YaHei\';\n"
            # "font-size: 17px;\n"
            "border: 1px solid 	#E6E6FA !important;"
            "border-radius: 15px;\n"
            "}\n"
            "QPushButton:hover\n"
            "{\n"
            "background: #E6E6FA;\n"
            "}\n"
        )
        self.pushButton_4.setText("加载\n文件")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 300, 40, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "color: Snow;\n"
            "background: #9370DB;\n"
            "font-family:\'Microsoft YaHei\';\n"
            # "font-size: 17px;\n"
            "border: 1px solid 	#E6E6FA !important;"
            "border-radius: 15px;\n"
            "}\n"
            "QPushButton:hover\n"
            "{\n"
            "background: #E6E6FA;\n"
            "}\n"
        )
        self.pushButton_5.setText("开始\n切割")


        self.retranslateUi(Incise)
        QtCore.QMetaObject.connectSlotsByName(Incise)

    def retranslateUi(self, Conversion):
        _translate = QtCore.QCoreApplication.translate
        Conversion.setWindowTitle(_translate("Conversion", "MainWindow"))