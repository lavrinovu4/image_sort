#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# Dirs choose
# Count Describe
# change arg gui
# launch program
class Form(QWidget):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)

        fbox = QFormLayout()

        self.inFe = QLineEdit()
        self.inFe.setReadOnly(True)
        inButDir = QPushButton(u"...")
        inButDir.clicked.connect(self.saveInButDir)
        inLayout = QHBoxLayout()
        inLayout.addWidget(self.inFe)
        inLayout.addWidget(inButDir)
        fbox.addRow(QLabel(u"Вкажіть назву директорії де шукати картинки"), inLayout)

        self.outFe = QLineEdit()
        self.outFe.setReadOnly(True)
        outButDir = QPushButton(u"...")
        outButDir.clicked.connect(self.saveOutButDir)
        outLayout = QHBoxLayout()
        outLayout.addWidget(self.outFe)
        outLayout.addWidget(outButDir)
        fbox.addRow(QLabel(u"Вкажіть назву директорії куди копіювати картинки"), outLayout)

        chDelete = QCheckBox(u"Видалити директорії після копіювання із диска")
        chDelete.clicked.connect(self.saveChDelete)
        fbox.addRow(chDelete)
        chRename = QCheckBox(u"Перейменовувати картинки у відповідності до дати створення")
        chRename.clicked.connect(self.saveChRename)
        fbox.addRow(chRename)
        chCount = QCheckBox(u"Дозволити обчислення скопійованих картинок")
        chCount.clicked.connect(self.saveChCount)
        fbox.addRow(chCount)

        prefix = QLineEdit()
        prefix.editingFinished.connect(lambda:self.savePrefix(prefix))
        fbox.addRow(QLabel(u"Добавити префікс до назви кожної картинки:"), prefix)

        year = QLineEdit()
        year.editingFinished.connect(lambda:self.saveYear(year))
        fbox.addRow(QLabel(u"Присвоїти всім картинкам рік створення:"), year)

        month = QLineEdit()
        month.editingFinished.connect(lambda:self.saveMonth(month))
        fbox.addRow(QLabel(u"Присвтоїти всім картинкам місяць створення:"), month)
        
        self.cp = QLineEdit()
        self.cp.setReadOnly(True)
        self.rm = QLineEdit()
        self.rm.setReadOnly(True)
        countLayout= QHBoxLayout()
        countLayout.addWidget(QLabel(u"Скопійовано картинок:"))
        countLayout.addWidget(self.cp)
        countLayout.addWidget(QLabel(u"Видалено картинок:"))
        countLayout.addWidget(self.rm)
        fbox.addRow(countLayout)

        Ok = QPushButton(u"Почати")
        Ok.clicked.connect(self.process)
        fbox.addRow(Ok)

        self.setLayout(fbox)

        self.setGeometry(100,100,1000,300)
        self.setWindowTitle(u"Сортування картинок")

        self.initVars()

    def initVars(self):
        self.inFeText = ""
        self.outFeText = ""
        self.PrefixText = ""
        self.YearText = ""
        self.MonthText = ""
        self.chDeleteIsChecked = False
        self.chRenameIsChecked = False
        self.chCountIsChecked = False

    def savePrefix(self,Prefix):
        self.PrefixText = str(Prefix.text().toUtf8())

    def saveYear(self,Year):
        self.YearText = str(Year.text().toUtf8())

    def saveMonth(self,Month):
        self.MonthText = str(Month.text().toUtf8())

    def saveChDelete(self,chDeleteIsChecked):
        self.chDeleteIsChecked = chDeleteIsChecked

    def saveChRename(self,chRenameIsChecked):
        self.chRenameIsChecked = chRenameIsChecked

    def saveChCount(self,chCountIsChecked):
        self.chCountIsChecked = chCountIsChecked

    def saveInButDir(self):
        self.inFeText = QFileDialog.getExistingDirectory(self, u'Відкрити папку звідки', 'd:\\', QFileDialog.ShowDirsOnly)
        self.inFe.setText(self.inFeText)

    def saveOutButDir(self):
        self.outFeText = QFileDialog.getExistingDirectory(self, u'Відкрити папку призначення', 'd:\\', QFileDialog.ShowDirsOnly)
        self.outFe.setText(self.outFeText)

    def process(self):
        print("Hi")
        print(self.inFeText)
        print(self.outFeText)
        print(self.PrefixText)
        print(self.YearText)
        print(self.MonthText)
        print(self.chDeleteIsChecked)
        print(self.chRenameIsChecked)
        print(self.chCountIsChecked)
        self.cp.setText(str(2))
        self.rm.setText(str(3))

def main():
    app = QApplication(sys.argv)
    win = Form()

    win.show()
    sys.exit(app.exec_())

main()

