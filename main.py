import os
import sys
import json
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QScrollArea, QFrame, QTextEdit
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPalette, QBrush

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


class Champion:
    def __init__(self, name, icon_path, difficulty, tips, runes_path, summoner_spells, starter_items, boots, core_items, other_items):
        self.name = name
        self.icon_path = icon_path
        self.difficulty = difficulty
        self.tips = tips
        self.runes_path = runes_path
        self.summoner_spells = summoner_spells
        self.starter_items = starter_items
        self.boots = boots
        self.core_items = core_items
        self.other_items = other_items

    def display_info(self):
        print(f"Champion: {self.name}")
        print(f"Difficulty: {self.difficulty}")
        print(f"Tips: {self.tips}")

class VeryEasyChampion(Champion):
    def __init__(self, name, icon_path, tips, runes_path, summoner_spells, starter_items, boots, core_items, other_items):
        super().__init__(name, icon_path, "Very Easy", tips, runes_path, summoner_spells, starter_items, boots, core_items, other_items)

class EasyChampion(Champion):
    def __init__(self, name, icon_path, tips, runes_path, summoner_spells, starter_items, boots, core_items, other_items):
        super().__init__(name, icon_path, "Easy", tips, runes_path, summoner_spells, starter_items, boots, core_items, other_items)

class MediumChampion(Champion):
    def __init__(self, name, icon_path, tips, runes_path, summoner_spells, starter_items, boots, core_items, other_items):
        super().__init__(name, icon_path, "Even", tips, runes_path, summoner_spells, starter_items, boots, core_items, other_items)

class HardChampion(Champion):
    def __init__(self, name, icon_path, tips, runes_path, summoner_spells, starter_items, boots, core_items, other_items):
        super().__init__(name, icon_path, "Hard", tips, runes_path, summoner_spells, starter_items, boots, core_items, other_items)

class VeryHardChampion(Champion):
    def __init__(self, name, icon_path, tips, runes_path, summoner_spells, starter_items, boots, core_items, other_items):
        super().__init__(name, icon_path, "Very Hard", tips, runes_path, summoner_spells, starter_items, boots, core_items, other_items)

class StarterItem:
    def __init__(self, name, icon_path):
        self.name = name
        self.icon_path = icon_path

class Boots:
    def __init__(self, name, icon_path):
        self.name = name
        self.icon_path = icon_path

class CoreItem:
    def __init__(self, name, icon_path):
        self.name = name
        self.icon_path = icon_path

class OtherItem:
    def __init__(self, name, icon_path):
        self.name = name
        self.icon_path = icon_path

class ChampionFactory(Singleton):
    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        super().__init__()
        self._champion_map = {}

    def create_champion(self, data):
        difficulty = data.get("difficulty", "").lower()
        if difficulty == "very easy":
            return VeryEasyChampion(
                data.get("name", ""),
                data.get("icon_path", ""),
                data.get("tips", ""),
                data.get("runes_path", ""),
                data.get("summoner_spells", []),
                data.get("starter_items", []),
                data.get("boots", []),
                data.get("core_items", []),
                data.get("other_items", [])
            )
        elif difficulty == "easy":
            return EasyChampion(
                data.get("name", ""),
                data.get("icon_path", ""),
                data.get("tips", ""),
                data.get("runes_path", ""),
                data.get("summoner_spells", []),
                data.get("starter_items", []),
                data.get("boots", []),
                data.get("core_items", []),
                data.get("other_items", [])
            )
        elif difficulty == "even":
            return MediumChampion(
                data.get("name", ""),
                data.get("icon_path", ""),
                data.get("tips", ""),
                data.get("runes_path", ""),
                data.get("summoner_spells", []),
                data.get("starter_items", []),
                data.get("boots", []),
                data.get("core_items", []),
                data.get("other_items", [])
            )
        elif difficulty == "hard":
            return HardChampion(
                data.get("name", ""),
                data.get("icon_path", ""),
                data.get("tips", ""),
                data.get("runes_path", ""),
                data.get("summoner_spells", []),
                data.get("starter_items", []),
                data.get("boots", []),
                data.get("core_items", []),
                data.get("other_items", [])
            )
        elif difficulty == "very hard":
            return VeryHardChampion(
                data.get("name", ""),
                data.get("icon_path", ""),
                data.get("tips", ""),
                data.get("runes_path", ""),
                data.get("summoner_spells", []),
                data.get("starter_items", []),
                data.get("boots", []),
                data.get("core_items", []),
                data.get("other_items", [])
            )
        else:
            raise ValueError("Invalid difficulty level")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fiora Matchup Guide")
        self.set_window_icon()
        self.set_window_geometry()

        self.matchup_data = self.load_matchup_data()
        self.champion_factory = ChampionFactory()

        self.setup_ui()

    def set_window_icon(self):
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "icon.png")
        self.setWindowIcon(QIcon(icon_path))

    def set_window_geometry(self):
        window_width = 1366
        window_height = 768
        screen_resolution = QApplication.desktop().screenGeometry()
        x = (screen_resolution.width() - window_width) // 2
        y = (screen_resolution.height() - window_height) // 2
        self.setGeometry(x, y, window_width, window_height)

    def load_matchup_data(self):
        with open('matchup_data.json') as f:
            data = json.load(f)
            for champion, champion_data in data.items():
                champion_data["icon_path"] = os.path.join(os.path.dirname(__file__), champion_data.get("champion_icon", ""))
                champion_data["runes_path"] = os.path.join(os.path.dirname(__file__), champion_data.get("runes", ""))
                difficulty_mapping = {
                    "very easy": "Very Easy",
                    "easy": "Easy",
                    "even": "Even",
                    "hard": "Hard",
                    "very hard": "Very Hard"
                }
                champion_data["difficulty"] = difficulty_mapping.get(champion_data.get("difficulty", "").lower(), "")
            return data

    def setup_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setSpacing(0)

        background_image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "fiora_splash.jpg")
        self.set_background_image(background_image_path)

        exit_button_icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "exit.png")
        exit_button_icon = QIcon(exit_button_icon_path)
        exit_button_icon_scaled = exit_button_icon.pixmap(QtCore.QSize(600, 251)).scaled(QtCore.QSize(200, 84), QtCore.Qt.KeepAspectRatio)

        self.exit_button = QPushButton(self)
        self.exit_button.setIcon(QIcon(exit_button_icon_scaled))
        self.exit_button.setIconSize(QtCore.QSize(200, 84))
        self.exit_button.clicked.connect(self.on_exit_clicked)
        self.exit_button.setGeometry(self.width() - 240, 20, 200, 84)
        self.exit_button.show()


        self.select_champion_label = QLabel("Select Enemy Champion", self)
        self.select_champion_label.setStyleSheet("background-color: white; padding: 10px; font-size: 20px; font-weight: bold;")
        self.select_champion_label.setFixedWidth(int(self.width() * 0.375))
        self.select_champion_label.setFixedHeight(50)
        layout.addWidget(self.select_champion_label)

        self.matchups_widget = QWidget(self)
        matchups_layout = QVBoxLayout(self.matchups_widget)
        matchups_layout.setSpacing(0)

        self.last_champion_button = QPushButton("Open Last Champion", self)
        self.last_champion_button.setStyleSheet("font-size: 16px;")
        self.last_champion_button.setFixedWidth(int(self.width() * 0.375 - 45))
        self.last_champion_button.clicked.connect(self.open_last_champion)
        matchups_layout.addWidget(self.last_champion_button)

        for champion_name in self.matchup_data.keys():
            button = QPushButton(champion_name, self)
            button.setStyleSheet("font-size: 16px;")
            button.setFixedWidth(int(self.width() * 0.375 - 45))
            button.clicked.connect(lambda _, name=champion_name: self.on_champion_clicked(name))
            matchups_layout.addWidget(button)

        button_height = button.sizeHint().height()
        scroll_area_height = button_height * 9 + 15

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.matchups_widget)
        self.scroll_area.setFixedWidth(int(self.width() * 0.375))
        self.scroll_area.setFixedHeight(scroll_area_height)
        self.scroll_area.setStyleSheet("background-color: white;")
        layout.addWidget(self.scroll_area)
        layout.addStretch(1)

        self.back_button = QPushButton(self)
        self.back_button.setIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "back_button.png")))
        self.back_button.setIconSize(QtCore.QSize(50, 50))
        self.back_button.clicked.connect(self.on_back_clicked)
        self.back_button.setGeometry(self.width() - 70, 20, 50, 50)
        self.back_button.hide()

        self.champion_info_frame = QFrame(self)
        self.champion_info_frame.setStyleSheet("background-color: white; border: 2px solid black;")
        self.champion_info_frame.hide()

        self.champion_icon_label = QLabel(self.champion_info_frame)
        self.champion_icon_label.setGeometry(10, 10, 100, 100)

        self.champion_name_label = QLabel(self.champion_info_frame)
        self.champion_name_label.setGeometry(120, 10, 200, 30)
        self.champion_name_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.champion_name_label.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.difficulty_label = QLabel(self.champion_info_frame)
        self.difficulty_label.setGeometry(120, 50, 200, 30)
        self.difficulty_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.difficulty_label.setStyleSheet("font-size: 16px;")

        self.matchup_tips_frame = QFrame(self)
        self.matchup_tips_frame.setStyleSheet("background-color: white; border: 2px solid black;")
        self.matchup_tips_frame.hide()

        self.matchup_tips_textbox = QTextEdit(self.matchup_tips_frame)
        self.matchup_tips_textbox.setGeometry(10, 10, 400, 200)
        self.matchup_tips_textbox.setStyleSheet("font-size: 18px;")
        self.matchup_tips_textbox.setReadOnly(True)

        self.runes_label = QLabel(self)
        self.runes_label.setGeometry(10, self.height() - 365, 100, 100)

        self.runes_text_label = QLabel("Runes: ", self)
        self.runes_text_label.setGeometry(10, self.height() - 405, 120, 40)
        self.runes_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.runes_text_label.setStyleSheet("font-size: 35px; background-color: white; color: black;")
        self.runes_text_label.hide()

        self.summs_label = QLabel(self)
        self.summs_label.setGeometry(10, self.height() - 525, 120, 120)

        self.summs_text_label = QLabel("Summs: ", self)
        self.summs_text_label.setGeometry(10, self.height() - 565, 140, 40)
        self.summs_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.summs_text_label.setStyleSheet("font-size: 35px; background-color: white; color: black;")
        self.summs_text_label.hide()

        self.starter_items_label = QLabel("Starter Items: ", self)
        self.starter_items_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.starter_items_label.hide()

        self.boots_label = QLabel("Boots: ", self)
        self.boots_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.boots_label.hide()

        self.core_items_label = QLabel("Core Items: ", self)
        self.core_items_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.core_items_label.hide()

        self.other_items_label = QLabel("Other Items: ", self)
        self.other_items_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.other_items_label.hide()

    def set_background_image(self, image_path):
        background_image = QImage(image_path)
        background_image = background_image.scaled(self.size(), QtCore.Qt.IgnoreAspectRatio)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(background_image))
        self.setPalette(palette)

    def on_exit_clicked(self):
        QApplication.quit()

    def on_champion_clicked(self, champion_name):
        with open('last_champion.txt', 'w') as f:
            f.write(champion_name)

        self.select_champion_label.hide()
        self.scroll_area.hide()
        self.exit_button.hide()
        self.back_button.show()
        self.runes_label.show()
        self.runes_text_label.show()
        self.champion_info_frame.show()
        self.matchup_tips_frame.show()
        self.summs_label.show()
        self.summs_text_label.show()
        self.starter_items_label.show()
        self.boots_label.show()
        self.core_items_label.show()
        self.other_items_label.show()

        runes_label_width = 595
        runes_label_height = 360
        self.runes_label.setFixedSize(runes_label_width, runes_label_height)

        summs_label_width = 360
        summs_label_height = 120
        self.summs_label.setFixedSize(summs_label_width, summs_label_height)

        self.champion_name_label.setText(champion_name)
        champion_data = self.matchup_data.get(champion_name, {})
        champion = self.champion_factory.create_champion(champion_data)  # Pass champion data here
        self.champion_icon_label.setPixmap(QPixmap(champion.icon_path))
        self.difficulty_label.setText(f"Difficulty: {champion.difficulty}")
        self.matchup_tips_textbox.setText(f"{champion.tips}")
        self.runes_label.setPixmap(QPixmap(champion.runes_path))


        for child in self.summs_label.children():
            if isinstance(child, QLabel):
                child.deleteLater()

        summoner_spells = champion.summoner_spells
        for index, spell_path in enumerate(summoner_spells):
            spell_label = QLabel(self.summs_label)
            spell_label.setPixmap(QPixmap(spell_path).scaled(64, 64))
            spell_label.setGeometry(index * 74, 0, 64, 64)
            spell_label.show()

        summs_label_width = len(summoner_spells) * 74
        summs_label_height = 64
        self.summs_label.setFixedSize(summs_label_width, summs_label_height)

        frame_width = 350
        frame_height = 120
        self.champion_info_frame.setGeometry(10, 10, frame_width, frame_height)

        frame_width = 420
        frame_height = 220
        self.matchup_tips_frame.setGeometry(self.width() - frame_width - 10, 80, frame_width, frame_height)

        self.load_item_icons(champion)

        items_label_height = 64
        items_label_x = self.width() - 10

        total_items_height = 4 * items_label_height
        items_label_y = self.height() - total_items_height - 10

        self.starter_items_label.adjustSize()
        self.starter_items_label.move(items_label_x - self.starter_items_label.width(), items_label_y)
        self.starter_items_label.show()

        self.boots_label.adjustSize()
        self.boots_label.move(items_label_x - self.boots_label.width(), items_label_y + items_label_height)
        self.boots_label.show()

        self.core_items_label.adjustSize()
        self.core_items_label.move(items_label_x - self.core_items_label.width(), items_label_y + 2 * items_label_height)
        self.core_items_label.show()

        self.other_items_label.adjustSize()
        self.other_items_label.move(items_label_x - self.other_items_label.width(), items_label_y + 3 * items_label_height)
        self.other_items_label.show()

    def open_last_champion(self):
        with open('last_champion.txt', 'r') as f:
            last_champion = f.read()
        self.on_champion_clicked(last_champion)

    def on_back_clicked(self):
        self.select_champion_label.show()
        self.scroll_area.show()
        self.exit_button.show()
        self.back_button.hide()
        self.champion_info_frame.hide()
        self.matchup_tips_frame.hide()
        self.runes_label.hide()
        self.runes_text_label.hide()
        self.summs_label.hide()
        self.summs_text_label.hide()
        self.starter_items_label.hide()
        self.boots_label.hide()
        self.core_items_label.hide()
        self.other_items_label.hide()

    def load_item_icons(self, champion):
        starter_items = [StarterItem(os.path.basename(path), path) for path in champion.starter_items]
        self.load_item_icons_for_category(starter_items, self.starter_items_label, "Starter Items")

        boots = [Boots(os.path.basename(path), path) for path in champion.boots]
        self.load_item_icons_for_category(boots, self.boots_label, "Boots")

        core_items = [CoreItem(os.path.basename(path), path) for path in champion.core_items]
        self.load_item_icons_for_category(core_items, self.core_items_label, "Core Items")

        other_items = [OtherItem(os.path.basename(path), path) for path in champion.other_items]
        self.load_item_icons_for_category(other_items, self.other_items_label, "Other Items")


    def load_item_icons_for_category(self, items, label, section_name):
        for child in label.children():
            if isinstance(child, QLabel):
                child.deleteLater()

        section_name += ":"
        section_label = QLabel(section_name, label)
        section_label.setStyleSheet("background-color: white; font-size: 20px;")
        section_label.setGeometry(0, 0, 150, 64)
        section_label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        section_label.show()

        items_label_width = 0
        for index, item in enumerate(items):
            item_label = QLabel(label)
            item_pixmap = QPixmap(item.icon_path)
            if not item_pixmap.isNull():
                item_label.setPixmap(item_pixmap.scaled(64, 64))
                item_label.setGeometry(150 + index * 74, 0, 64, 64)
                item_label.show()
            else:
                print("Invalid item icon path:", item.icon_path)

        label_width = 150 + len(items) * 74
        label_height = 64
        label.setFixedSize(label_width, label_height)

        label_y = self.height() - label_height - 10
        label.move(label.x(), label_y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())