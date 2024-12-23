import sys
import os
import platform

from modules import *
from widgets import *
from utils import *
os.environ["QT_FONT_DPI"] = "96" 

from modules.ui_login import *
from modules.ui_main import *

widgets = None

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create a central widget for the QMainWindow
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Create and setup the UI
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self.central_widget)  # Setup UI on the central widget instead of self
        
        # Connect the login button
        self.ui.loginButton.clicked.connect(self.authenticate)

    def authenticate(self):
        # Пример проверки логина и пароля
        username = self.ui.emailInput.text()
        password = self.ui.passwordInput.text()

        if username == "admin" and password == "1234":
            self.main_window = MainWindow()  # Создаём экземпляр основной страницы
            self.main_window.show()  # Показываем основную страницу
            self.close()  # Закрываем окно авторизации
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль")
        

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        
        self.setWindowTitle('GedaEffect - твой кабинет.')
        #widgets.titleRightInfo.setText('Личный кабинет работника ООО ГедаЭффект был разработан для увеличения трудоэффективности работников и помощи им в повседневных задачах.')
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        UIFunctions.uiDefinitions(self)
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)

        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        useCustomTheme = True
        themeFile = "themes\py_dracula_light.qss"

        if useCustomTheme:
            UIFunctions.theme(self, themeFile, True)
            AppFunctions.setThemeHack(self)

        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    
    
    
    def buttonClick(self):    
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) 
            UIFunctions.resetStyle(self, btnName) 
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) 

        if btnName == "btn_save":
            print("Save BTN clicked!")

        
        print(f'Button "{btnName}" pressed!')


    
    
    def resizeEvent(self, event):
        UIFunctions.resize_grips(self)

    
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    login_window = LoginWindow()
    login_window.show()
    #window = MainWindow()
    sys.exit(app.exec())
