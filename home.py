import sys
import queue
import requests
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from PyQt5.QtCore import Qt, QTimer, QDateTime, pyqtSignal, QThread

from home_ui import Ui_MainWindow
import icons_qrc

class myHome(QtWidgets.QWidget, Ui_MainWindow):
    #构造函数
    def __init__(self):
        super(myHome,self).__init__()
        self.setupUi(self)

        # 无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置窗口背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 窗口居中
        winsize = self.frameGeometry()
        screen = QDesktopWidget().availableGeometry().center()
        winsize.moveCenter(screen)
        self.move(winsize.topLeft())

        # 用户字段
        self.pushButton_status.clicked.connect(lambda:self.buttonClick(self.label_1, self.pushButton_status))
        self.pushButton_3.clicked.connect(self.close)   # 按钮
        self.pushButton.clicked.connect(self.showMinimized)
        # 显示本地IP地址
        self.label_ip.setText("255.255.255.255")
        self.label_title.setText("DeepSpeech NING")
        self.pushButton_4.setText("实时\n语音识别")
        self.pushButton_5.setText("格式转换")
        self.pushButton_6.setText("音频切割")
        self.pushButton_7.setText("文件\n语音识别")

        # 动态显示时间在label上
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()

    # 背景图片
    def buttonClick(self, label_1, status):
        self.thread = background_image(label_1, status)
        self.thread.start()  # 启动线程
        # status.setEnabled(True)

    # 格式化时间函数
    def showtime(self):
        datetime = QDateTime.currentDateTime()
        # text = datetime.toString("hh:mm:ss yyyy/MM/dd dddd")
        text = datetime.toString("dddd hh:mm:ss")
        self.label_datetime.setText(text)
        # self.label.setFont(QFont("Roman times", 20, QFont.Bold))

    # 窗口拖动
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            e.accept()
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False
    def mouseMoveEvent(self, e):
        try:
            if Qt.LeftButton and self.m_drag:
                self.move(e.globalPos() - self.m_DragPosition)
                e.accept()
        except:
            pass
            # print("错误代码:000x0")

    # def closeEvent(self,event):    # 函数名固定不可变
    #     reply=QtWidgets.QMessageBox.question(self,u'警告',u'是否要退出！',
    #                                          QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
    #     #QtWidgets.QMessageBox.question(self,u'弹窗名',u'弹窗内容',选项1,选项2)
    #     if reply==QtWidgets.QMessageBox.Yes:
    #         event.accept()#关闭窗口
    #     else:
    #         event.ignore()#忽视点击100X事件

# 异步加载背景图片
class background_image(QThread):

    def __init__(self, label, status):
        super(background_image, self).__init__()
        self.label = label
        self.status = status

    def run(self):
        try:
            self.status.setEnabled(False)
            image_url = "https://img.xjh.me/random_img.php?type=bg&ctype=nature&return=302"
            req = requests.get(image_url)
            photo = QtGui.QPixmap()
            photo.loadFromData(req.content)
            self.label.setPixmap(photo)
            self.label.setScaledContents(True)  # 让图片自适应label大小
            self.exit(0)  # 关闭线程
        except Exception as e:
            pass
        finally:
            self.status.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myhome = myHome()      # 主页面
    myhome.show()
    sys.exit(app.exec_())