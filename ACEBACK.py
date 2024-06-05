import sys
import os
import shutil
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor, QPainterPath, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget, QDesktopWidget

class BackupApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.m_flag = False  # flag to check if the window is being dragged
    
    def initUI(self):
        self.setWindowTitle('AceBack - Backup Tool')

        # Define a cor de fundo
        color1 = "#354257"

        # Remove a moldura padrão da janela


        self.label = QLabel('Escolha a pasta para backup:', self)
        self.backup_button = QPushButton('Selecionar Pasta e Fazer Backup', self)
        self.backup_button.clicked.connect(self.backup)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.backup_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Obter a geometria do desktop
        desktop = QDesktopWidget().availableGeometry()

        self.setWindowIcon(QIcon('icon.ico'))

        # Definir a geometria da janela no centro do desktop
        WindowSize = ["800", "600"]
        self.setGeometry((desktop.width() - int(WindowSize[0])) // 2, (desktop.height() - int(WindowSize[1])) // 2, int(WindowSize[0]), int(WindowSize[1]))
        

        self.show()

    def paintEvent(self, event):
        # Cria um objeto QPainter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Define a cor de fundo
        color1 = QColor("#354257")

        # Define uma path com bordas arredondadas
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 20, 20)

        # Desenha a cor de fundo na janela
        painter.fillPath(path, QBrush(color1))

    def backup(self):
        source_dir = QFileDialog.getExistingDirectory(self, 'Selecione a pasta Acessus')
        if source_dir:
            backup_dir = os.path.join(os.path.expanduser('~'), 'Backups')
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            backup_name = f"ACESSUS-{self.current_day()}-{self.current_date()}"
            backup_path = os.path.join(backup_dir, backup_name)
            shutil.copytree(source_dir, backup_path)
            self.label.setText(f'Backup concluído: {backup_path}')

    def current_day(self):
        return ['SEGUNDA', 'TERÇA', 'QUARTA', 'QUINTA', 'SEXTA', 'SÁBADO', 'DOMINGO'][datetime.datetime.now().weekday()]

    def current_date(self):
        return datetime.datetime.now().strftime('%d-%m-%Y')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BackupApp()
    sys.exit(app.exec_())
