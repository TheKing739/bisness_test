#현재 개발 주 로직

from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QColorDialog, QComboBox, QLineEdit, QFileDialog,
    QTextEdit
)
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
import sys

TEMPLATE_COLORS = {
    "모던&미니멀":    ("#2C3E50", "#C8BFE7", "#000000"),       # 남색 계열
    "감성&따뜻한":    ("#6E2C00", "#F8BBD0", "#FCE4EC"),       # 밝은 청록 계열
    "강조&다이내믹":    ("#2E4053", "#FF5733", "#F0F3F4"),       # 모던한 검회+포인트 블루
    "내추럴&클린":  ("#E8F8F5", "#28B463", "#145A32"),       # 강렬한 빨주노
    "프리미엄&럭셔리":  ("#2C3E50", "#F1C40F", "#ECF0F1"),       # 자연계 그린 계열
}

class Step1Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("상세페이지 자동 생성기")
        self.setFixedSize(600, 400)

        # 색상 저장 변수
        self.color_primary = None
        self.color_secondary = None
        self.color_accent = None

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(6)  # 🔧 기본 간격 조정 (기본은 10~12쯤)
        main_layout.setContentsMargins(10, 10, 10, 10)  # 🔧 좌우 여백도 조절 가능

        # 색상 선택 버튼
        color_layout = QHBoxLayout()

        self.primary_color_button = QPushButton("🎨 주 색상 선택")
        self.primary_color_button.clicked.connect(lambda: self.select_color('primary'))
        self.primary_color_button.setFixedHeight(50)
        color_layout.addWidget(self.primary_color_button)

        self.secondary_color_button = QPushButton("🎨 보조 색상 선택")
        self.secondary_color_button.clicked.connect(lambda: self.select_color('secondary'))
        self.secondary_color_button.setFixedHeight(50)
        color_layout.addWidget(self.secondary_color_button)

        self.accent_color_button = QPushButton("🎨 보조 색상2 선택")
        self.accent_color_button.clicked.connect(lambda: self.select_color('accent'))
        self.accent_color_button.setFixedHeight(50)
        color_layout.addWidget(self.accent_color_button)
        
        main_layout.addLayout(color_layout)

        # 템플릿 선택
        self.template_label = QLabel("템플릿 선택")
        self.template_dropdown = QComboBox()
        self.template_dropdown.addItems(["모던&미니멀", "감성&따뜻한", "강조&다이내믹", "내추럴&클린", "프리미엄&럭셔리"])
        self.template_dropdown.setFixedHeight(50)
        self.template_dropdown.currentTextChanged.connect(self.on_template_changed)  # ✅ 호출 연결
        main_layout.addWidget(self.template_label)
        main_layout.addWidget(self.template_dropdown)

        # 필수 문구
        self.required_text = QTextEdit()
        self.required_text.setPlaceholderText("주제어를 입력해주세요")
        main_layout.addWidget(self.required_text)

        # 버튼 두 개
        button_layout = QHBoxLayout()
        self.generate_btn = QPushButton("템플릿 기준 생성")
        self.generate_btn.setFixedHeight(50)
        self.random_btn = QPushButton("랜덤 디자인 생성")
        self.random_btn.setFixedHeight(50)

        button_layout.addWidget(self.generate_btn)
        button_layout.addWidget(self.random_btn)
        main_layout.addLayout(button_layout)

        self.on_template_changed(self.template_dropdown.currentText())  # 초기 템플릿 적용

    def select_color(self, key):
        color = QColorDialog.getColor()
        if color.isValid():
            if key == 'primary':
                self.color_primary = color.name()
                self.primary_color_button.setStyleSheet(f"background-color: {self.color_primary}; color: white")
            elif key == 'secondary':
                self.color_secondary = color.name()
                self.secondary_color_button.setStyleSheet(f"background-color: {self.color_secondary}; color: white")
            elif key == 'accent':
                self.color_accent = color.name()
                self.accent_color_button.setStyleSheet(f"background-color: {self.color_accent}; color: white")

    def on_template_changed(self, template_name):
        if template_name in TEMPLATE_COLORS:
            main, sub1, sub2 = TEMPLATE_COLORS[template_name]
            self.color_primary = main
            self.color_secondary = sub1
            self.color_accent = sub2

            # 버튼 색상 변경
            self.primary_color_button.setStyleSheet(f"background-color: {main}; color: white;")
            self.secondary_color_button.setStyleSheet(f"background-color: {sub1}; color: white;")
            self.accent_color_button.setStyleSheet(f"background-color: {sub2}; color: white;")
    
    def on_template_changed(self, template_name):
        if template_name in TEMPLATE_COLORS:
            main, sub1, sub2 = TEMPLATE_COLORS[template_name]
            self.color_primary = main
            self.color_secondary = sub1
            self.color_accent = sub2

            # 버튼 색상 변경
            self.primary_color_button.setStyleSheet(f"background-color: {main}; color: white;")
            self.secondary_color_button.setStyleSheet(f"background-color: {sub1}; color: white;")
            self.accent_color_button.setStyleSheet(f"background-color: {sub2}; color: white;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Step1Window()
    window.show()
    sys.exit(app.exec())
