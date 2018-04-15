# -*- coding: utf-8 -*-
import sys
import core
from language import language
from PyQt4 import QtGui,QtCore

class Form(QtGui.QWidget):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)

        fbox = QtGui.QFormLayout()

        uab = QtGui.QPushButton(QtGui.QIcon("ua.jpeg"),"")
        uab.setMinimumSize(QtCore.QSize(16777215, 50))
        uab.clicked.connect(self.changeLangUA)
        usb = QtGui.QPushButton(QtGui.QIcon("us.png"),"")
        usb.setMinimumSize(QtCore.QSize(16777215, 50))
        usb.clicked.connect(self.changeLangUS)
        itb = QtGui.QPushButton(QtGui.QIcon("it.png"),"")
        itb.setMinimumSize(QtCore.QSize(16777215, 50))
        itb.clicked.connect(self.changeLangIT)
        lang_layout = QtGui.QHBoxLayout()
        lang_layout.addWidget(uab)
        lang_layout.addWidget(usb)
        lang_layout.addWidget(itb)
        fbox.addRow(lang_layout)

        self.inFe = QtGui.QLineEdit()
        self.inFe.setReadOnly(True)
        inButDir = QtGui.QPushButton(u"...")
        inButDir.clicked.connect(self.saveInButDir)
        inLayout = QtGui.QHBoxLayout()
        inLayout.addWidget(self.inFe)
        inLayout.addWidget(inButDir)
        self.src_folder_label = QtGui.QLabel()
        fbox.addRow(self.src_folder_label, inLayout)

        self.outFe = QtGui.QLineEdit()
        self.outFe.setReadOnly(True)
        outButDir = QtGui.QPushButton(u"...")
        outButDir.clicked.connect(self.saveOutButDir)
        outLayout = QtGui.QHBoxLayout()
        outLayout.addWidget(self.outFe)
        outLayout.addWidget(outButDir)
        self.dst_folder_label = QtGui.QLabel()
        fbox.addRow(self.dst_folder_label, outLayout)

        self.chDelete = QtGui.QCheckBox()
        self.chDelete.clicked.connect(self.saveChDelete)
        fbox.addRow(self.chDelete)
        self.chRename = QtGui.QCheckBox()
        self.chRename.clicked.connect(self.saveChRename)
        fbox.addRow(self.chRename)

        prefix = QtGui.QLineEdit()
        prefix.editingFinished.connect(lambda:self.savePrefix(prefix))
        self.add_prefix_label = QtGui.QLabel()
        fbox.addRow(self.add_prefix_label, prefix)

        year = QtGui.QLineEdit()
        year.editingFinished.connect(lambda:self.saveYear(year))
        self.change_year_label = QtGui.QLabel()
        fbox.addRow(self.change_year_label, year)

        month = QtGui.QLineEdit()
        month.editingFinished.connect(lambda:self.saveMonth(month))
        self.change_month_label = QtGui.QLabel()
        fbox.addRow(self.change_month_label, month)
        
        self.cp = QtGui.QLineEdit()
        self.cp.setReadOnly(True)
        self.rm = QtGui.QLineEdit()
        self.rm.setReadOnly(True)
        countLayout= QtGui.QHBoxLayout()
        self.copied_img_label = QtGui.QLabel()
        countLayout.addWidget(self.copied_img_label)
        countLayout.addWidget(self.cp)
        self.deleted_img_label = QtGui.QLabel()
        countLayout.addWidget(self.deleted_img_label)
        countLayout.addWidget(self.rm)
        fbox.addRow(countLayout)

        self.Ok = QtGui.QPushButton()
        self.Ok.clicked.connect(self.process)
        fbox.addRow(self.Ok)

        self.setLayout(fbox)

        self.setGeometry(100,100,1000,300)

        self.initVars()
        self.changeLang("us")

    def initVars(self):
        self.inFeText = ""
        self.outFeText = ""
        self.PrefixText = ""
        self.YearText = ""
        self.MonthText = ""
        self.chDeleteIsChecked = False
        self.chRenameIsChecked = False

    def changeLang(self, lang):
        list_names = language[lang]
        self.src_folder_label.setText(list_names["src_folder"])
        self.dst_folder_label.setText(list_names["dst_folder"])
        self.chDelete.setText(list_names["del_img"])
        self.chRename.setText(list_names["rename_img"])
        self.add_prefix_label.setText(list_names["add_prefix"])
        self.change_year_label.setText(list_names["change_year"])
        self.change_month_label.setText(list_names["change_month"])
        self.copied_img_label.setText(list_names["copied_img"])
        self.deleted_img_label.setText(list_names["deleted_img"])
        self.Ok.setText(list_names["start"])
        self.setWindowTitle(list_names["sort_image_title"])
        self.open_src_lbl = list_names["open_src"]
        self.open_dst_lbl = list_names["open_dst"]

    def changeLangUS(self):
        self.changeLang("us")

    def changeLangUA(self):
        self.changeLang("ua")

    def changeLangIT(self):
        self.changeLang("it")

    def savePrefix(self, Prefix):
        self.PrefixText = Prefix.text()

    def saveYear(self,Year):
        self.YearText = Year.text()

    def saveMonth(self,Month):
        self.MonthText = Month.text()

    def saveChDelete(self,chDeleteIsChecked):
        self.chDeleteIsChecked = chDeleteIsChecked

    def saveChRename(self,chRenameIsChecked):
        self.chRenameIsChecked = chRenameIsChecked

    def saveInButDir(self):
        self.inFeText = QtGui.QFileDialog.getExistingDirectory(self, self.open_src_lbl, 'd:\\', QtGui.QFileDialog.ShowDirsOnly)
        self.inFe.setText(self.inFeText)

    def saveOutButDir(self):
        self.outFeText = QtGui.QFileDialog.getExistingDirectory(self, self.open_dst_lbl, 'd:\\', QtGui.QFileDialog.ShowDirsOnly)
        self.outFe.setText(self.outFeText)

    def process(self):
        parameters = {'delete': self.chDeleteIsChecked,
                      'rename': self.chRenameIsChecked,
                      'prefix': str(self.PrefixText),
                      'year': str(self.YearText),
                      'month': str(self.MonthText),
                      'day': ""
                      }

        (numberCp, numberRm) = core.sortImgs(str(self.inFeText), str(self.outFeText), parameters)

        self.cp.setText(str(numberCp))
        self.rm.setText(str(numberRm))

def interface():
    app = QtGui.QApplication(sys.argv)
    win = Form()

    win.show()
    sys.exit(app.exec_())

