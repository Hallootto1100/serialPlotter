import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView
from PySide6.QtQuickControls2 import QQuickStyle
from pathlib import Path


def main():
    app = QApplication()
    QQuickStyle.setStyle('Material')
    engine = QQmlApplicationEngine()
    
    qml_file = Path('serialPlotter/ui/view.qml')
    engine.load(qml_file)
    
    if not engine.rootObjects():
        sys.exit(-1)
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
