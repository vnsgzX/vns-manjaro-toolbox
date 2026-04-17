#!/usr/bin/env python3
import sys
import subprocess
import platform
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QPushButton, QTextEdit, QLabel, QGridLayout, QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class VNSManjaroToolbox(QWidget):
    def __init__(self):
        super().__init__()
        self.version = "1.0.1"
        self.initUI()

    def initUI(self):
        # Postavljene kompaktne dimenzije (širina 500, visina 550)
        self.setWindowTitle(f'VNS-Manjaro-Toolbox {self.version}')
        self.setGeometry(300, 150, 500, 550) 
        self.setStyleSheet("background-color: #2e3440; color: #d8dee9;")

        layout = QVBoxLayout()
        layout.setSpacing(8) 
        layout.setContentsMargins(12, 12, 12, 12)

        # --- SYSTEM INFO SECTION ---
        # Uklonjen hostname radi privatnosti, fokus na kernelu i verziji alata
        info_frame = QFrame()
        info_frame.setStyleSheet("background-color: #3b4252; border-radius: 8px;")
        info_layout = QVBoxLayout()
        info_layout.setContentsMargins(8, 8, 8, 8)
        
        kernel = platform.release()
        system_type = platform.system()
        
        info_label = QLabel(f"<b>System:</b> {system_type} | <b>Kernel:</b> {kernel} | <b>Version:</b> {self.version}")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info_label.setStyleSheet("font-size: 11px; color: #88c0d0;")
        info_layout.addWidget(info_label)
        
        info_frame.setLayout(info_layout)
        layout.addWidget(info_frame)

        # --- BUTTON GRID ---
        grid = QGridLayout()
        grid.setSpacing(6)

        # Optimizovane komande za maksimalnu pouzdanost
        buttons = [
            ('Update System', 'yay -Syu --noconfirm', '#5e81ac'),
            ('Deep Clean', 'yay -Sc --noconfirm && yay -Yc --noconfirm', '#bf616a'),
            ('Refresh Mirrors', 'sudo pacman-mirrors --fasttrack && sudo pacman -Syy', '#ebcb8b'),
            ('SSD Trim', 'sudo fstrim -av', '#a3be8c'),
            ('View Error Logs', 'journalctl -p 3 -xb', '#b48ead'),
            ('FIX DB LOCKS', 'sudo rm -f /var/lib/pacman/db.lck && yay -Syy', '#d08770')
        ]

        row, col = 0, 0
        for text, cmd, color in buttons:
            btn = QPushButton(text)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color}; 
                    color: white; 
                    padding: 12px; 
                    border-radius: 5px; 
                    font-weight: bold;
                    font-size: 11px;
                }}
                QPushButton:hover {{
                    background-color: #4c566a;
                }}
            """)
            btn.clicked.connect(lambda ch, c=cmd: self.run_command(c))
            grid.addWidget(btn, row, col)
            col += 1
            if col > 1:
                col = 0
                row += 1

        layout.addLayout(grid)

        # --- LOG AREA ---
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        self.log_area.setPlaceholderText("Activity log will appear here...")
        self.log_area.setStyleSheet("""
            background-color: #1b1e23; 
            color: #a3be8c; 
            font-family: 'Monospace'; 
            font-size: 10px; 
            border: 1px solid #4c566a;
            border-radius: 4px;
        """)
        layout.addWidget(self.log_area)

        # --- FOOTER ---
        footer_layout = QVBoxLayout()
        clear_btn = QPushButton("Clear Output")
        clear_btn.setStyleSheet("""
            background-color: #4c566a; 
            color: white; 
            padding: 4px; 
            font-size: 10px;
            border-radius: 3px;
        """)
        clear_btn.clicked.connect(lambda: self.log_area.clear())
        footer_layout.addWidget(clear_btn)

        layout.addLayout(footer_layout)
        self.setLayout(layout)

    def run_command(self, command):
        """Pokreće komandu u xfce4-terminalu za interaktivnost."""
        self.log_area.append(f"<span style='color: #88c0d0;'><b>> Running:</b> {command}</span>")
        
        # Terminal ostaje otvoren dok korisnik ne pritisne Enter nakon završetka
        terminal_cmd = f"xfce4-terminal --title='VNS Task' -e 'bash -c \"{command}; echo; echo ------------------------; echo Task finished. Press Enter to close; read\"'"
        
        try:
            subprocess.Popen(terminal_cmd, shell=True)
            self.log_area.append("<span style='color: #a3be8c;'>[OK] Terminal session started.</span>")
        except Exception as e:
            self.log_area.append(f"<span style='color: #bf616a;'><b>Error:</b> {str(e)}</span>")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VNSManjaroToolbox()
    ex.show()
    sys.exit(app.exec())
