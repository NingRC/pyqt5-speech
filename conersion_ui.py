# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conversion.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QTextEdit,QFontDialog, QLineEdit,QStyle,QFormLayout, QInputDialog,QVBoxLayout,QWidget,QApplication ,QHBoxLayout,QDialog,QPushButton,QMainWindow,QGridLayout,QLabel

class Ui_Conversion(object):
    def setupUi(self, Conversion):
        Conversion.setObjectName("Conversion")
        Conversion.resize(1280, 720)
        Conversion.setStyleSheet("QLineEdit{\n"
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
        self.centralwidget = QtWidgets.QWidget(Conversion)
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
        self.label_3.setGeometry(QtCore.QRect(70, 120, 1140, 100))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet(
                                    "border-radius: 10px ;\n"
                                    # "border-image: url(:/icons/background.png);\n"
                                    "border: 1px solid #9370DB !important;"
                                   )

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 240, 1160, 440))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet(
                                    "border-radius: 10px ;\n"
                                    # "border: 1.5px solid #9370DB !important;"
                                    "border-image: url(:/icons/background.png);\n"
                                   )

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 120, 180, 95))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet(
            "color: DimGray;\n"
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 13px;\n"
            "border-radius: 5px;\n"
        )
        self.label_5.setWordWrap(True)
        self.label_5.setText("1：选择本地文件。 2：选择目标格式并设置转换选项（可选）。 3：单击“开始转换”按钮，然后等待转换完成。")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(95, 310, 100, 50))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet(
            "color: DimGray;\n"
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 19px;\n"
        )
        self.label_6.setText("输出文件")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 380, 100, 50))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet(
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 17px;\n"
        )
        self.label_7.setText("#")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(300, 380, 100, 50))
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet(
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 17px;\n"
        )
        self.label_8.setText("文件大小")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(590, 380, 100, 50))
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet(
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 17px;\n"
        )
        self.label_9.setText("输入文件")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(950, 380, 100, 50))
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet(
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 17px;\n"
        )
        self.label_10.setText("输出文件")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(95, 245, 150, 50))
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet(
            "color: DimGray;\n"
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 19px;\n"
            # "border: 1px solid #3C3C3C!important;"
        )
        self.label_11.setText("输入文件")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(250, 245, 900, 50))
        self.label_12.setObjectName("label_12")
        self.label_12.setStyleSheet(
            "color: DimGray;\n"
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 16px;\n"
            # "border: 1px solid #3C3C3C!important;"
        )

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(320, 130, 20, 80))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(620, 130, 16, 80))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(920, 130, 16, 80))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(62, 300, 1155, 1))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_4.setStyleSheet("border: 1px solid LightGrey;")

        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(62, 358, 1155, 2))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_5.setStyleSheet("border: 1px solid LightGrey;")

        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(90, 448, 1100, 2))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_6.setStyleSheet("border: 1px solid LightGrey;")



        # Conversion.setCentralWidget(self.centralwidget)
        # self.statusbar = QtWidgets.QStatusBar(Conversion)
        # self.statusbar.setObjectName("statusbar")
        # Conversion.setStatusBar(self.statusbar)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1100, 30, 80, 26))
        self.pushButton.setMinimumSize(QtCore.QSize(22, 22))
        self.pushButton.setMaximumSize(QtCore.QSize(22, 22))
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
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1150, 30, 80, 26))
        self.pushButton_2.setMinimumSize(QtCore.QSize(22, 22))
        self.pushButton_2.setMaximumSize(QtCore.QSize(22, 22))
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
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1200, 30, 80, 26))
        self.pushButton_3.setMinimumSize(QtCore.QSize(22, 22))
        self.pushButton_3.setMaximumSize(QtCore.QSize(22, 22))
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
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 140, 185, 60))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "color: Snow;\n"
            "background: #9370DB;\n"
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 17px;\n"
            "border: 1px solid 	#E6E6FA !important;"
            "border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover\n"
            "{\n"
            "background: #E6E6FA;\n"
            "}\n"
        )
        self.pushButton_4.setText("加载文件")
        self.pushButton_3.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(980, 140, 185, 60))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "color: Snow;\n"
            "background: rgba(242, 89, 97, .9);\n"
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 17px;\n"
            "border: 1px solid 	#E6E6FA !important;"
            "border-radius: 5px;\n"
            "}\n"
            "QPushButton:hover\n"
            "{\n"
            "background: #FFC0CB;\n"
            "}\n"
        )
        self.pushButton_5.setText("开始转换")
        self.pushButton_5.setObjectName("pushButton_5")

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

        self.combobox = QtWidgets.QComboBox(self.centralwidget)
        self.combobox.setGeometry(QtCore.QRect(680, 140, 185, 60))
        self.combobox.setObjectName("combobox")
        self.combobox.setStyleSheet(
            "QComboBox\n"
            "{\n"
            "color: Snow;\n"
            "combobox-popup: 0;\n"  # 滚动条设置必需
            "padding-left: 60px;  "   # 字体距离左边的距离
            "background: #9370DB;\n"
            "border: 1px solid 	#E6E6FA !important;"
            "border-radius: 5px;\n"
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 17px;\n"
            "}\n"

            "QComboBox:hover\n"
            "{\n"
            "background: #E6E6FA;\n"
            "}\n"

            "QComboBox:drop-down {"  # 选择箭头样式
            "border: none;  "
            "subcontrol-position: right center; "  # 位置
            "subcontrol-origin: padding;}\n"  # 对齐方式

            "QComboBox QAbstractItemView {"  # 下拉选项样式
            "border: 1px solid 	#E6E6FA !important;"
            "border-radius: 5px;\n"
            # "color:black; "
            # "background: transparent; "
            "selection-color:rgba(93,169,255,1);"
            "selection-background-color: rgba(255,255,255,1);"
            "}\n"
        )

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(90, 450, 1100, 225))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet(
            "QTableWidget { "
                "background: White;\n"
                "border: 1px solid 	White !important;"
                # "border-radius: 5px;\n"
                "font-family:\'Microsoft YaHei\';\n"
                "font-size: 17px;\n"
            "}\n"
            "QTableWidget::item:selected { "
                "background-color: #9C9C9C;\n"
            "}"
        )

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.progressBar.setGeometry(30, 40, 200, 25)
        self.progressBar.setGeometry(QtCore.QRect(900, 320, 250, 28))
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setStyleSheet(
            "QProgressBar {"
            "color: Snow;\n"
            "border: 2px solid white;"
            "border-radius: 5px;"
            # "background-color: #FFFFFF;"
            "text-align: center;"
            "}"
            "QProgressBar::chunk {"
            "background-color: #007FFF;"
            "border-radius: 5px;"
            # "width: 10px; "
            # "margin: 0.5px;"
            "}"
        )

        self.retranslateUi(Conversion)
        QtCore.QMetaObject.connectSlotsByName(Conversion)


    def retranslateUi(self, Conversion):
        _translate = QtCore.QCoreApplication.translate
        Conversion.setWindowTitle(_translate("Conversion", "MainWindow"))
        # self.label.setText(_translate("Conversion", "TextLabel"))
        # self.label_3.setText(_translate("Conversion", "TextLabel"))
        # self.label_4.setText(_translate("Conversion", "TextLabel"))
        # self.label_2.setText(_translate("Conversion", "TextLabel"))
