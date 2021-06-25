import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QAction, QAbstractItemView, QHeaderView, QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QIcon, QCursor, QPalette, QPixmap, QBrush, QColor, QPainter, QMovie, QFont
from PyQt5.QtCore import Qt, QTimer, QDateTime

import socket

import conersion
import home
import login


app = QApplication(sys.argv)
login = login.myLogin()
home = home.myHome()
conersion = conersion.Conversion()

login.show()


########################################## 登录事件 ##############################################
def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception as e:
        return "0.0.0.0"
    finally:
        s.close()
    return ip

def login_check():
    '''
    这里我使用的是我服务器的登录请求接口
    使用的时候换成自己封装好的登录验证接口即可

    正常来说，登录成功的话，需要将登陆成功的用户信息回传给主界面
    也就是告诉主界面，是哪个用户登录了，这个时候可以在主界面的类中定义
    一些类属性，如果登录成功，则将lineedit对象的输入内容赋值给类属性即可
    '''
    userID = login.lineEdit_1.text()
    user_PW = login.lineEdit_2.text()
    if userID == "1" and user_PW == "1":
        # login.login_state = 1
        userID = login.lineEdit_1.text()
        # print(userID)
        # home.label_3.setText(userID)
        home.label_ip.setText(str(get_host_ip()))
        login.close()
        home.show()
    elif userID == "" or user_PW == "":
        QtWidgets.QMessageBox.about(login, "提示", "请输入用户名或密码！")
    else:
        QtWidgets.QMessageBox.warning(login, "警告", "用户名或密码错误！", QtWidgets.QMessageBox.Yes)

login.pushButton_3.clicked.connect(login_check)
login.pushButton_4.clicked.connect(login.close)




########################################## 主页事件 ##############################################
def goconve_check():
    home.close()
    conersion.show()

home.pushButton_5.clicked.connect(goconve_check)



########################################## 文件转换事件 ###########################################

def goback_check():
    conersion.close()
    home.show()

conersion.pushButton_goback.clicked.connect(goback_check)



# userIDSure = ""
# flag = 0

# # def close_check():
# #     myLogin.lineEdit_1.setText("")
# #     myLogin.lineEdit_2.setText("")

sys.exit(app.exec_())