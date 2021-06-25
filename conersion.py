from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QAbstractItemView, QTableWidgetItem, QFileDialog
from PyQt5.QtCore import Qt, QBasicTimer

import sys
import os
import uuid
import math
from pydub import AudioSegment

from conersion_ui import Ui_Conversion
import icons_qrc


class Conversion(QtWidgets.QWidget, Ui_Conversion):
    def __init__(self):
        super(Conversion,self).__init__()
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
        self.label_2.setText("音频格式转换")
        self.label_2.setAlignment(Qt.AlignCenter)  # 左右居中
        self.label_12.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # 上下居中靠右
        # self.combobox.addItem("目标格式")
        self.combobox.addItems(['目标格式', 'WAV', 'MP3', 'MP4', 'OGG', 'FLAC'])
        index = self.combobox.model().index(0, 0)   # index(i, 0),i代表的是第几个选项
        self.combobox.model().setData(index, 0, QtCore.Qt.UserRole - 1)
        # 将表格变为禁止编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格为整行选择
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 表格表头和垂直表头隐藏
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        # 不显示表格单元格的分割线
        self.tableWidget.setShowGrid(False)
        # 调整列宽
        self.tableWidget.setColumnCount(4)
        # self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnWidth(0, 130)
        self.tableWidget.setColumnWidth(1, 220)
        self.tableWidget.setColumnWidth(2, 365)
        self.tableWidget.setColumnWidth(3, 365)
        # 设置tableWidget所有列的默认行高为20。
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        #鼠标移入手型光标
        self.pushButton_4.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_5.setCursor(QtCore.Qt.PointingHandCursor)
        self.combobox.setCursor(QtCore .Qt.PointingHandCursor)

        # self.tableWidget.setItem(0, 0, QTableWidgetItem("1"))
        # newItem = QTableWidgetItem("ghfhfg")
        # self.tableWidget.setItem(0, 1, newItem)
        # self.tableWidget.setItem(1, 2, QTableWidgetItem("160kb"))
        # self.tableWidget.setItem(2, 3, QTableWidgetItem("sdfsfsfsdfs"))

        # self.pushButton_4.clicked.connect(self.showDialog1)
        self.pushButton.clicked.connect(self.showMinimized)
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_4.clicked.connect(self.on_button_4_check)
        self.pushButton_5.clicked.connect(self.on_button_5_check)
        self.combobox.currentTextChanged.connect(self.on_combobox_check)

        self.timer = QBasicTimer()
        self.timer_time = 10
        self.step = 0
        self.id = 0
    def on_combobox_check(self):
        # 启用按钮
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setText("开始转换")
        self.pushButton_5.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "background: rgba(242, 89, 97, .9);\n"
                                        "color: Snow;\n"
                                        "font-family:\'Microsoft YaHei\';\n"
                                        "font-size: 17px;\n"
                                        "border: 1px solid 	#E6E6FA !important;"
                                        "border-radius: 5px;\n"
                                        "}\n")

    # 定义打开文件夹目录的函数
    def on_button_4_check(self):

        filename, filetype = QFileDialog.getOpenFileName(self, '选择音频文件',
                                                         os.getcwd(),
                                                         "Sound Files (*.mp3 *.ogg *.wav *.m4a)", "",
                                                         QFileDialog.DontUseNativeDialog)
        # "Vertex file(*.wav *.WAV *.mp3 *.m4a)", "",
        # print(filename, filetype)
        self.label_12.setText(filename)
        # self.label_12.setText(filename.split('/')[-1])
        path = self.label_12.text()
        if path == "":
            self.pushButton_4.setText("加载文件")
        else:
            self.pushButton_4.setText("加载完成")
            # 启用按钮
            self.pushButton_5.setEnabled(True)
            self.pushButton_5.setStyleSheet("QPushButton\n"
                                            "{\n"
                                            "background: rgba(242, 89, 97, .9);\n"
                                            "color: Snow;\n"
                                            "font-family:\'Microsoft YaHei\';\n"
                                            "font-size: 17px;\n"
                                            "border: 1px solid 	#E6E6FA !important;"
                                            "border-radius: 5px;\n"
                                            "}\n")

    # 定时器处理函数
    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            # 修改文本标签显示内容
            self.pushButton_5.setText("转换完成")
            self.pushButton_5.setStyleSheet("QPushButton\n"
                                            "{\n"
                                            "background: #FFC0CB;\n"
                                            "color: Snow;\n"
                                            "font-family:\'Microsoft YaHei\';\n"
                                            "font-size: 17px;\n"
                                            "border: 1px solid 	#E6E6FA !important;"
                                            "border-radius: 5px;\n"
                                            "}\n")
            return

        self.step = self.step + 1
        self.progressBar.setValue(self.step)

        # 把进度条卡在80，等处理好了再到100
        if self.step == 80:
            self.timer.stop()
            if self.conersion() == True:
                self.timer.start(self.timer_time, self)
    # 进度条启动函数
    def onStart(self):
        self.timer.start(self.timer_time, self)
        self.pushButton_5.setText('转换中.....')
        #禁用按钮
        self.pushButton_5.setEnabled(False)

        # 已经走到头了,重新启动起来
        if self.progressBar.value() >= 100:
            self.step = 0
            self.progressBar.setValue(0)
            self.timer.start(self.timer_time, self)
            # self.pushButton_5.setText('再次转换中...')

    # 处理具体的业务逻辑,文件转换函数
    def conersion(self):
        filepath = self.label_12.text()
        target = self.combobox.currentText()
        format_type = filepath.split('/')[-1].split('.')[-1]
        # 默认娶一个通道,采样率为16KHz
        song = AudioSegment.from_file(filepath, format=format_type.lower()).set_frame_rate(16000).set_channels(1)
        # 导出
        out_path = filepath.split('.')[0] + "-" + str(uuid.uuid4())[0:6]
        out_audio = f"{out_path}.{target.lower()}"
        song.export(out_audio, format=target.lower())

        # if format_type.lower() == "wav":
        # if format == "WAV":/
        #     sound = AudioSegment.from_file(filepath, format="wav")
        # elif format == "MP3":
        #     sound = AudioSegment.from_file(filepath, format="mp3")
        # elif format == "M4A":
        #     sound = AudioSegment.from_file(filepath, format="mp4")

        # 获取文件地址
        outsize = os.path.getsize(out_audio)
        self.id +=1
        self.tableshow(str(self.id), filepath, self.pybyte(outsize), out_audio)
        return True

    # 进度条处理函数
    def on_button_5_check(self):
        path = self.label_12.text()
        format = self.combobox.currentText()
        if path == "":
            QtWidgets.QMessageBox.about(self, "提示", "文件未加载！")
        elif format == "目标格式":
            QtWidgets.QMessageBox.about(self, "提示", "格式未选择！")
        else:
            self.onStart()

    def pybyte(self, size, dot=1):
        size = float(size)
        # 位 比特 bit
        if 0 <= size < 1:
            human_size = str(round(size / 0.125, dot)) + 'b'
        # 字节 字节 Byte
        elif 1 <= size < 1024:
            human_size = str(round(size, dot)) + 'B'
        # 千字节 千字节 Kilo Byte
        elif math.pow(1024, 1) <= size < math.pow(1024, 2):
            human_size = str(round(size / math.pow(1024, 1), dot)) + 'KB'
        # 兆字节 兆 Mega Byte
        elif math.pow(1024, 2) <= size < math.pow(1024, 3):
            human_size = str(round(size / math.pow(1024, 2), dot)) + 'MB'
        # 吉字节 吉 Giga Byte
        elif math.pow(1024, 3) <= size < math.pow(1024, 4):
            human_size = str(round(size / math.pow(1024, 3), dot)) + 'GB'
        # 太字节 太 Tera Byte
        elif math.pow(1024, 4) <= size < math.pow(1024, 5):
            human_size = str(round(size / math.pow(1024, 4), dot)) + 'TB'
        # 拍字节 拍 Peta Byte
        elif math.pow(1024, 5) <= size < math.pow(1024, 6):
            human_size = str(round(size / math.pow(1024, 5), dot)) + 'PB'
        # 艾字节 艾 Exa Byte
        elif math.pow(1024, 6) <= size < math.pow(1024, 7):
            human_size = str(round(size / math.pow(1024, 6), dot)) + 'EB'
        # 泽它字节 泽 Zetta Byte
        elif math.pow(1024, 7) <= size < math.pow(1024, 8):
            human_size = str(round(size / math.pow(1024, 7), dot)) + 'ZB'
        # 尧它字节 尧 Yotta Byte
        elif math.pow(1024, 8) <= size < math.pow(1024, 9):
            human_size = str(round(size / math.pow(1024, 8), dot)) + 'YB'
        # 千亿亿亿字节 Bront Byte
        elif math.pow(1024, 9) <= size < math.pow(1024, 10):
            human_size = str(round(size / math.pow(1024, 9), dot)) + 'BB'
        # 百万亿亿亿字节 Dogga Byte
        elif math.pow(1024, 10) <= size < math.pow(1024, 11):
            human_size = str(round(size / math.pow(1024, 10), dot)) + 'NB'
        # 十亿亿亿亿字节 Dogga Byte
        elif math.pow(1024, 11) <= size < math.pow(1024, 12):
            human_size = str(round(size / math.pow(1024, 11), dot)) + 'DB'
        # 万亿亿亿亿字节 Corydon Byte
        elif math.pow(1024, 12) <= size:
            human_size = str(round(size / math.pow(1024, 12), dot)) + 'CB'
        # 负数
        else:
            raise ValueError("Not")
            # raise ValueError('{}() takes number than or equal to 0, but less than 0 given.'.format(pybyte.__name__))
        return human_size

    # 显示
    def tableshow(self, id, inpath, outsize, outpath):
        inpath = inpath.split("/")[-1]
        outpath = outpath.split("/")[-1]
        itemdata = [[id, outsize, inpath, outpath]]
        # 添加数据
        for i in range(len(itemdata)):
            item = itemdata[i]
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for j in range(len(item)):
                # print(self.data[i][j])
                # print(type(self.data[i][j]))
                item = QTableWidgetItem(str(itemdata[i][j]))
                self.tableWidget.setItem(row, j, item)
        # 设置单元格对齐方式
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                try:
                    item = self.tableWidget.item(row, col).text()
                    newItem = QTableWidgetItem(str(item))
                    self.tableWidget.setItem(row, col, newItem)
                    newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                except Exception as e:
                    continue
                # print(item)


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
    conversion = Conversion()      # 主页面
    conversion.show()
    sys.exit(app.exec_())