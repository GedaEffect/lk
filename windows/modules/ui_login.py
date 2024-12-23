# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(1280, 720)
        LoginForm.setMinimumSize(QSize(1280, 560))
        self.mainLayout = QVBoxLayout(LoginForm)
        self.mainLayout.setObjectName(u"mainLayout")
        self.centerWidget = QWidget(LoginForm)
        self.centerWidget.setObjectName(u"centerWidget")
        self.centerLayout = QVBoxLayout(self.centerWidget)
        self.centerLayout.setObjectName(u"centerLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.centerLayout.addItem(self.verticalSpacer)

        self.logoLabel = QLabel(self.centerWidget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMinimumSize(QSize(250, 150))
        self.logoLabel.setMaximumSize(QSize(150, 150))
        self.logoLabel.setPixmap(QPixmap(u"images/images/logo.svg"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setAlignment(Qt.AlignCenter)

        self.centerLayout.addWidget(self.logoLabel, 0, Qt.AlignHCenter)

        self.authLabel = QLabel(self.centerWidget)
        self.authLabel.setObjectName(u"authLabel")
        self.authLabel.setAlignment(Qt.AlignCenter)

        self.centerLayout.addWidget(self.authLabel)

        self.emailInput = QLineEdit(self.centerWidget)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setMinimumSize(QSize(250, 40))
        self.emailInput.setMaximumSize(QSize(250, 40))

        self.centerLayout.addWidget(self.emailInput, 0, Qt.AlignHCenter)

        self.passwordInput = QLineEdit(self.centerWidget)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setMinimumSize(QSize(250, 40))
        self.passwordInput.setMaximumSize(QSize(250, 40))
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.centerLayout.addWidget(self.passwordInput, 0, Qt.AlignHCenter)

        self.loginButton = QPushButton(self.centerWidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(250, 40))
        self.loginButton.setMaximumSize(QSize(250, 40))

        self.centerLayout.addWidget(self.loginButton, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.centerLayout.addItem(self.verticalSpacer_2)


        self.mainLayout.addWidget(self.centerWidget)


        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.authLabel.setStyleSheet(QCoreApplication.translate("LoginForm", u"\n"
"          font-size: 24px;\n"
"          font-weight: bold;\n"
"          color: #2E2E2E;\n"
"         ", None))
        self.authLabel.setText(QCoreApplication.translate("LoginForm", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.emailInput.setStyleSheet(QCoreApplication.translate("LoginForm", u"\n"
"          border: 2px solid #CCCCCC;\n"
"          border-radius: 10px;\n"
"          padding: 8px;\n"
"          font-size: 14px;\n"
"         ", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("LoginForm", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.passwordInput.setStyleSheet(QCoreApplication.translate("LoginForm", u"\n"
"          border: 2px solid #CCCCCC;\n"
"          border-radius: 10px;\n"
"          padding: 8px;\n"
"          font-size: 14px;\n"
"         ", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("LoginForm", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.loginButton.setStyleSheet(QCoreApplication.translate("LoginForm", u"\n"
"          background-color: #4800D4;\n"
"          color: #FFFFFF;\n"
"          font-size: 16px;\n"
"          border-radius: 10px;\n"
"          padding: 10px;\n"
"         ", None))
        self.loginButton.setText(QCoreApplication.translate("LoginForm", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

