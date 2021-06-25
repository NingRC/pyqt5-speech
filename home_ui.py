# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("QLineEdit{\n"
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
                                 "    background:white;\n"
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

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.label.setObjectName("label")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(0, 85, 1280, 595))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 85, 1280, 595))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, "
            "x1:0, y1:0, x2:1, y2:0, "
            "stop:1 rgba(0, 27, 161, 0.4), "
            "stop:0 rgba(0, 210, 177, 0.4));\n"
            # "background-color: linear-gradient(45deg, rgba(42, 27, 161, 0.7), rgba(29, 210, 177, 0.7) 100%);"
        )
        self.label_menu = QtWidgets.QLabel(self.centralwidget)
        self.label_menu.setGeometry(QtCore.QRect(85, 23, 120, 40))
        self.label_menu.setObjectName("label_menu")
        self.label_menu.setStyleSheet(
            "color: rgba(0, 0, 0, 0.7);"
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 35px;\n"
            "font-weight: bolder;"
            # "border: 2px solid #1E90FF !important;"
        )
        self.label_menu.setText("ProAct")

        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(210, 23, 350, 40))
        self.label_title.setObjectName("label_title")
        self.label_title.setStyleSheet(
            "color: rgba(54, 139, 180, 0.9);"
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 35px;\n"
            "font-weight: bolder;"
        )

        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(55, 685, 100, 30))
        self.label_status.setObjectName("label_status")
        self.label_status.setStyleSheet(
            "color: rgba(0, 0, 0, 0.7);"
            "font-family:\'KaiTi\';\n"
            "font-size: 22px;\n"
            # "border: 1px solid #1E90FF !important;"
        )
        self.label_status.setText("Status")

        self.label_datetime = QtWidgets.QLabel(self.centralwidget)
        self.label_datetime.setGeometry(QtCore.QRect(890, 685, 150, 30))
        self.label_datetime.setObjectName("label_datetime")
        self.label_datetime.setStyleSheet(
            "color: rgba(0, 0, 0, 0.7);"
            "font-family:\'KaiTi\';\n"
            "font-size: 18px;\n"
            # "border: 1px solid #1E90FF !important;"
        )

        self.label_ip = QtWidgets.QLabel(self.centralwidget)
        self.label_ip.setGeometry(QtCore.QRect(1120, 685, 150, 30))
        self.label_ip.setObjectName("label_ip")
        self.label_ip.setStyleSheet(
            "color: rgba(0, 0, 0, 0.7);"
            "font-family:\'KaiTi\';\n"
            "font-size: 18px;\n"
            # "border: 1px solid #1E90FF !important;"
        )


        # self.label_5 = QtWidgets.QLabel(self.centralwidget)
        # self.label_5.setGeometry(QtCore.QRect(1050, 90, 170, 70))
        # self.label_5.setObjectName("label_5")
        # self.label_5.setStyleSheet("font-family:\'Microsoft YaHei\';\n"
        #                            "font-size: 17px;\n"
        #                            "border-radius: 10px;\n"
        #                            "background: rgba(232, 232, 232, .3);\n"
        #                            )
        # self.label_5.setWordWrap(True)      # 自动换行



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

        self.pushButton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_menu.setGeometry(QtCore.QRect(25, 25, 45, 40))
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.pushButton_menu.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "border-image: url(:/icons/menu.png);\n"
            "}\n"
            "QPushButton:hover\n"
            "{\n"
                "border-radius:10px;\n"
                "background: rgba(42, 27, 161, 0.5);\n"
            "}\n")

        self.pushButton_status = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_status.setGeometry(QtCore.QRect(25, 688, 25, 25))
        self.pushButton_status.setObjectName("pushButton_status")
        self.pushButton_status.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "border-image: url(:/icons/status.png);\n"
            "}\n"
            "QPushButton:hover\n"
            "{\n"
                "border-radius:10px;\n"
                "background: rgba(29, 210, 177, 0.7);\n"
            "}\n")


        self.pushButton_datetime = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_datetime.setGeometry(QtCore.QRect(850, 688, 27, 27))
        self.pushButton_datetime.setObjectName("pushButton_datetime")
        self.pushButton_datetime.setStyleSheet(
            "QPushButton\n"
            "{\n"
            # "background: rgb(0, 0, 0);"
            "border-image: url(:/icons/datetime.png);\n"
            "}\n"
            "QPushButton:hover\n"
            "{\n"
                "border-radius:10px;\n"
                "background: rgba(29, 210, 177, 0.7);\n"
            "}\n")

        self.pushButton_ip = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ip.setGeometry(QtCore.QRect(1080, 688, 25, 25))
        self.pushButton_ip.setObjectName("pushButton_ip")
        self.pushButton_ip.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "border-image: url(:/icons/ip.png);\n"
            "}\n"
            "QPushButton:hover\n"
            "{\n"
                "border-radius:10px;\n"
                "background: rgba(29, 210, 177, 0.7);\n"
            "}\n")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 140, 300, 480))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(
            "QPushButton\n"
              "{\n"
                "background: rgba(19, 76, 102, 0.3);\n"
                # "border-image: url(:/icons/zcool.png);\n"
                "border: 2px solid #f6f5ec !important;"
                "border-radius: 40px;\n"
                "color:White;\n"
                "font-family:\'Microsoft YaHei\';\n"
                "font-size: 50px;\n"
              "}\n"
              # "QPushButton:hover\n"
              # "{\n"
              #     "background:#9D9D9D;\n"
              #     "border-image: url();\n"
              # "}\n"
        )

        # self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_5.setGeometry(QtCore.QRect(460, 140, 300, 480))
        # self.pushButton_5.setObjectName("pushButton_5")
        # self.pushButton_5.setStyleSheet(
        #     "QPushButton\n"
        #     "{\n"
        #     "background: rgba(19, 76, 102, 0.3);\n"
        #     "border: 2px solid #f6f5ec !important;"
        #     "border-radius: 40px;\n"
        #     "}\n"
        # )
        # self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_6.setGeometry(QtCore.QRect(860, 140, 330, 220))
        # self.pushButton_6.setObjectName("pushButton_6")
        # self.pushButton_6.setStyleSheet(
        #     "QPushButton\n"
        #     "{\n"
        #     "background: rgba(19, 76, 102, 0.3);\n"
        #     "border: 2px solid #f6f5ec !important;"
        #     "border-radius: 40px;\n"
        #     "}\n"
        # )
        #
        # self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_7.setGeometry(QtCore.QRect(860, 400, 330, 220))
        # self.pushButton_7.setObjectName("pushButton_7")
        # self.pushButton_7.setStyleSheet(
        #     "QPushButton\n"
        #     "{\n"
        #     "background: rgba(19, 76, 102, 0.3);\n"
        #     "border: 2px solid #f6f5ec !important;"
        #     "border-radius: 40px;\n"
        #     "}\n"
        # )
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 140, 330, 220))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background: rgba(19, 76, 102, 0.3);\n"
            "border: 2px solid #f6f5ec !important;"
            "border-radius: 40px;\n"
            "color:White;\n"
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 50px;\n"
            "}\n"
        )

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 400, 330, 220))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background: rgba(19, 76, 102, 0.3);\n"
            "border: 2px solid #f6f5ec !important;"
            "border-radius: 40px;\n"
            "color:White;\n"
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 50px;\n"
            "}\n"
        )

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(900, 140, 300, 480))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background: rgba(19, 76, 102, 0.3);\n"
            "border: 2px solid #f6f5ec !important;"
            "border-radius: 40px;\n"
            "color:White;\n"
            "font-family:\'Microsoft YaHei\';\n"
            "font-size: 50px;\n"
            "}\n"
        )

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.label.setText(_translate("MainWindow", ""))