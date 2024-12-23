from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt6.QtGui import QColor
from pyqttoast import Toast, ToastPreset
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

    # Shows a toast notification every time the button is clicked
    def show_toast(self):
        toast = Toast(self)
        toast.setDuration(5000)  # Hide after 5 seconds
        toast.setTitle('хуййй.')
        toast.setText('яиицооооооооооооооооооооооооо большоййййййй.')
        toast.setShowIconSeparator(False) 
        toast.setBackgroundColor(QColor('#292929'))       # Default: #E7F4F9
        toast.setTitleColor(QColor('#FFFFFF'))            # Default: #000000
        toast.setTextColor(QColor('#D0D0D0'))             # Default: #5C5C5C
        toast.setDurationBarColor(QColor('#6272A4'))      # Default: #5C5C5C
        toast.setIconColor(QColor('#6272A4'))             # Default: #5C5C5C
        toast.setIconSeparatorColor(QColor('#6272A4'))    # Default: #D9D9D9
        toast.setCloseButtonIconColor(QColor('#6272A4'))  # Default: #000000
        toast.applyPreset(ToastPreset.SUCCESS_DARK)  # Apply style preset

        toast.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window.show_toast()
    window.show_toast()
    window.show_toast()
    window.show_toast()
    window.show_toast()
    window.show_toast()
    window.show_toast()


    sys.exit(app.exec())
