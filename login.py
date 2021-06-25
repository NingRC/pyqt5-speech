import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


from login_ui import Ui_Login
import icons_qrc


class myLogin(QtWidgets.QWidget, Ui_Login):
    # login_state = 0
    def __init__(self):
        super(myLogin,self).__init__()
        self.setupUi(self)
        # loginPalette = QPalette()
        # loginPalette.setBrush(QPalette.Background, QBrush(QPixmap("./loginbackground.jpg")))
        # loginPalette.setColor(QPalette.Background, Qt.blue)
        # self.setPalette(loginPalette)

        # 禁止关闭按钮
        # self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

        # 禁止拉伸窗口大小
        self.setFixedSize(self.width(), self.height())

        # 设置窗口标记（无边框 ）
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # 窗口居中
        winsize = self.frameGeometry()
        screen = QDesktopWidget().availableGeometry().center()
        winsize.moveCenter(screen)
        self.move(winsize.topLeft())



        # 用户字段
        self.label_2.setAlignment(Qt.AlignCenter)   # 居中
        self.label_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)   # 设置密码形式
        self.pushButton.clicked.connect(self.close)   # 按钮
        self.pushButton_2.clicked.connect(self.showMinimized)


        # 设置行为的图标
        self.visibleIcon = QIcon(":/icons/eye_on.png")
        self.hiddenIcon = QIcon(":/icons/eye_off.png")
        # 在单行文本框尾部添加该行为
        self.togglepasswordAction = self.lineEdit_2.addAction(self.visibleIcon, QtWidgets.QLineEdit.TrailingPosition)
        # 连接槽函数
        self.togglepasswordAction.triggered.connect(self.on_toggle_password_Action)
        self.password_shown = False

    # 窗口拖动
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            e.accept()
        # 鼠标点击手型光标
        self.label.setCursor(QtCore.Qt.SizeAllCursor)


    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False
        # 鼠标返回箭头光标
        self.label.setCursor(QtCore.Qt.ArrowCursor)

    def mouseMoveEvent(self, e):
        try:
            if Qt.LeftButton and self.m_drag:
                self.move(e.globalPos() - self.m_DragPosition)
                e.accept()
        except:
            pass
            # print("错误代码:000x0")

    # 定义槽函数
    def on_toggle_password_Action(self):
        if not self.password_shown:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.password_shown = True
            self.togglepasswordAction.setIcon(self.hiddenIcon)
        else:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
            self.password_shown = False
            self.togglepasswordAction.setIcon(self.visibleIcon)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myLogin = myLogin()  # 登录
    myLogin.show()
    sys.exit(app.exec_())