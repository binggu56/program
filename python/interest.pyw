#!/usr/bin/env python3
# Copyright (c) 2008-10 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):

    def __init__(self, parent=None):

        super(Form, self).__init__(parent)

        amountLabel = QLabel('Amount')
        principalLabel = QLabel('Principal')
        rateLabel = QLabel('Rate')
        yearLabel = QLabel('Years')

        self.principalSpinBox = QDoubleSpinBox()
        self.principalSpinBox.setRange(0.01, 10000000.00)
        self.principalSpinBox.setValue(2000.00)
        self.principalSpinBox.setPrefix('$')

        self.rateSpinBox = QDoubleSpinBox()
        self.rateSpinBox.setRange(0.01, 10000000.00)
        self.rateSpinBox.setValue(5.25)
        self.rateSpinBox.setSuffix('%')

        self.years=[]
        for i in range(2,30):
            year = str(i)+' years'
            self.years.append(year)

        self.yearComboBox = QComboBox()
        self.yearComboBox.addItems(self.years)

        self.toamountLabel = QLabel("$ 2215.51")

        grid = QGridLayout()
        grid.addWidget(principalLabel,0, 0)
        grid.addWidget(self.principalSpinBox,0,1)
        grid.addWidget(rateLabel, 1, 0)
        grid.addWidget(self.rateSpinBox, 1, 1)
        grid.addWidget(yearLabel,2,0)
        grid.addWidget(self.yearComboBox,2,1)
        grid.addWidget(amountLabel, 3, 0)
        grid.addWidget(self.toamountLabel,3,1)
        self.setLayout(grid)        

        self.connect(self.yearComboBox,SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.rateSpinBox,SIGNAL("valueChanged(double)"), self.updateUi)
        self.connect(self.principalSpinBox,SIGNAL("valueChanged(double)"), self.updateUi)
        self.setWindowTitle("Interest")


    def updateUi(self):
        """amount = principal * ((1 + (rate / 100.0)) ** years"""

        from_ = self.yearComboBox.currentText()
        amount =self.principalSpinBox.value()*((1+self.rateSpinBox.value()/100)**(self.years.index(from_)))
        self.toamountLabel.setText("$ {0:.2f}".format(amount))



app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

