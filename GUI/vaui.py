# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'va.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SIRI(object):
    def setupUi(self, SIRI):
        SIRI.setObjectName("SIRI")
        SIRI.resize(951, 570)
        SIRI.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(SIRI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    font: 20pt \"Times New Roman\";\n"
"}\n"
"QLabel:hover{\n"
"    \n"
"    color: rgb(70, 135, 255);\n"
"}\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 471, 361))
        self.label_2.setStyleSheet("QLabel{\n"
"    border-radius:10px;\n"
"}\n"
"QLabel:hover{\n"
"    \n"
"    border-color: rgb(214, 147, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 440, 141, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 75 14pt \"Times New Roman\";\n"
"    \n"
"    background-color: rgb(0, 85, 255);\n"
"    color:white;\n"
"    border-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(124, 137, 255);\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 0, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    font: 20pt \"Times New Roman\";\n"
"}\n"
"QLabel:hover{\n"
"    \n"
"    color: rgb(70, 135, 255);\n"
"}\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(500, 60, 451, 361))
        self.textEdit.setStyleSheet("border-radius:10px;")
        self.textEdit.setObjectName("textEdit")
        SIRI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SIRI)
        self.statusbar.setObjectName("statusbar")
        SIRI.setStatusBar(self.statusbar)

        self.retranslateUi(SIRI)
        QtCore.QMetaObject.connectSlotsByName(SIRI)

    def retranslateUi(self, SIRI):
        _translate = QtCore.QCoreApplication.translate
        SIRI.setWindowTitle(_translate("SIRI", "ASSISTANT_SIRI"))
        self.label.setText(_translate("SIRI", "VIRTUAL ASSISTAN SIRI"))
        self.pushButton.setText(_translate("SIRI", "Bắt đầu"))
        self.label_3.setText(_translate("SIRI", "Thông tin phần mềm"))
        self.textEdit.setHtml(_translate("SIRI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"./imgqrc/logo_khoa.png\" /></p>\n"#####
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Đồ án ngành</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffffff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">Tên đề tài: Xây dựng hệ thống trợ lý ảo trên máy tính bằng ngôn ngữ Python.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">GVHD: </span><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Ths.Huỳnh Quang Đức.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">SVTH: Nguyễn Hoàng Khởi</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">Các chức năng chính:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:14pt; color:#ffffff;\">        </span><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:14pt; font-style:italic; color:#ffffff;\">1.Chào hỏi</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:14pt; font-style:italic; color:#ffffff;\">        2.Thông báo thời gian </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:14pt; font-style:italic; color:#ffffff;\">        3.Dự báo thời tiết </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:14pt; font-style:italic; color:#ffffff;\">        4.Mở ứng dụng office văn phòng.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:14pt; font-style:italic; color:#ffffff;\">        5.Tìm kiếm thông tin trên google, wikipedia.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:14pt; font-style:italic; color:#ffffff;\">        6.Mở nhạc,phim trên youtube </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas,Courier New,monospace\'; font-size:14pt; font-style:italic; color:#ffffff;\">        7.Thay hình nền máy tính.</span></p></body></html>"))

