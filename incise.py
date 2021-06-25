from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QAbstractItemView, QTableWidgetItem, QFileDialog
from PyQt5.QtCore import Qt, QBasicTimer

import sys
import os
import uuid
import math
from pydub import AudioSegment

from incise_ui import Ui_Incise
import icons_qrc


class Incise(QtWidgets.QWidget, Ui_Incise):
    def __init__(self):
        super(Incise,self).__init__()
        self.setupUi(self)

        # 设置窗口标记（无边框）
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 设置窗口背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 窗口居中
        winsize = self.frameGeometry()
        screen = QDesktopWidget().availableGeometry().center()
        winsize.moveCenter(screen)
        self.move(winsize.topLeft())

        # 用户字段
        self.label_2.setText("音频文件剪辑")
        self.label_2.setAlignment(Qt.AlignCenter)  # 左右居中
        self.pushButton.clicked.connect(self.showMinimized)
        self.pushButton_3.clicked.connect(self.close)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    incise = Incise()      # 主页面
    incise.show()
    sys.exit(app.exec_())