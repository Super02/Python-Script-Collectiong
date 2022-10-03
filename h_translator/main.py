from PyQt6.QtWidgets import *
import sys


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("H Translator")

        # Create layout
        vertical_layout = QVBoxLayout()

        # Define text fields
        self.input = QPlainTextEdit()
        self.output = QPlainTextEdit()
        self.output.setReadOnly(True)

        # Define buttons
        button_group = QHBoxLayout()

        self.encode = QPushButton("Encode H")
        self.encode.clicked.connect(self.slot_encode)
        self.decode = QPushButton("Decode H")
        self.decode.clicked.connect(self.slot_decode)

        button_group.addWidget(self.encode)
        button_group.addWidget(self.decode)

        # Copy button
        self.copy = QPushButton("Copy")
        self.copy.clicked.connect(self.slot_copy)

        # Add things to UI
        vertical_layout.addWidget(self.input)
        vertical_layout.addLayout(button_group)
        vertical_layout.addWidget(self.output)
        vertical_layout.addWidget(self.copy)

        # Set UI
        self.setLayout(vertical_layout)

    def slot_encode(self):
        in_ = self.input.toPlainText()

        bits = bin(int.from_bytes(in_.encode('utf-8'), 'big'))[2:]
        out = bits.zfill(8 * ((len(bits) + 7) // 8))

        out = (out
               .replace('0', 'h')
               .replace('1', 'H'))
        self.output.setPlainText(out)

    def slot_decode(self):
        in_ = self.input.toPlainText()
        in_ = (in_
               .replace('h', '0')
               .replace('H', '1'))

        try:
            n = int(in_, 2)
            out = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8')
        except ValueError:
            self.show_popup("Invalid input!")
            return

        self.output.setPlainText(out)

    def slot_copy(self):
        out = self.output.toPlainText()
        QApplication.clipboard().setText(out)

    def show_popup(self, text: str):
        self.popup = QMessageBox()
        self.popup.setIcon(QMessageBox.Icon.Critical)
        self.popup.setText("Error")
        self.popup.setWindowTitle("Error")
        self.popup.setInformativeText(text)
        self.popup.show()


if __name__ == '__main__':
    app = QApplication([])
    window = UI()
    window.show()
    sys.exit(app.exec())
