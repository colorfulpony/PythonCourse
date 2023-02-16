import requests
import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtWidgets import QFileDialog, QLineEdit, QLabel
from PyQt6.QtCore import Qt

def get_word_definition():
    full_text = ""
    word = input.text()
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    print(word)
    response = requests.get(url)
    result = json.loads(response.text)
    for result in result[0]['meanings']:
        for r in result["definitions"]:
            full_text += r["definition"] + "\n"
    output_label.setText(full_text)



app = QApplication([])
window = QWidget()
window.setWindowTitle('Word Definition')
layout = QVBoxLayout()

description = QLabel('Enter the word you want to get definition of.')
layout.addWidget(description)

layout1 = QHBoxLayout()
layout.addLayout(layout1)

input = QLineEdit()
layout1.addWidget(input)

btn = QPushButton('Convert')
btn.setToolTip("Open File")
btn.setFixedWidth(100)
layout1.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
btn.clicked.connect(get_word_definition)

output_label = QLabel("")
layout.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()
