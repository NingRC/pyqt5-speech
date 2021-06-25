# designer                          打开UI编辑器
# pyuic5 -o name.py name.ui         生成UI界面
# pyrcc5 icons.qrc -o icons_qrc.py   生成图片路径

# pyinstaller -F -c -i img.ico main.py		打包单个
# pyinstaller -D -c -i img.ico main.py		打包项目
# pyinstaller -F -w main.py -n seepch.exe
# -n [自定义名称] 如果不使用-n,则默认是脚本脚本文件的名称
# 注意在Ubuntu下打包生成执行文件， exe得在win10下面打包
# pyinstaller window.spec   生成可执行文件或exe

# PyQt5==5.15.4
# PyQt5-sip==12.9.0
# PyQt5-tools==5.15.4.3.2
