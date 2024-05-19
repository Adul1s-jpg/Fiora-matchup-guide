# Fiora Matchup Guide

## Introduction

### What is your application?
The Fiora Matchup Guide is a desktop application designed to assist players of the game "League of Legends" in preparing for matches against specific enemy champions. This application provides detailed information on how to counter various champions when playing as Fiora, including difficulty ratings, gameplay tips, recommended runes, summoner spells, and item builds.

### How to run the program?
1. Download the `Fiora-matchup-guide-main` from the repository.
2. Extract the zip file in the place of your choice.
3. Double-click the `main.exe` file to run the application.

### How to use the program?
1. Open the application by running the executable file.
2. Select an enemy champion from the list to view detailed matchup information.
3. Use the provided tips, runes, summoner spells, and item recommendations to improve your gameplay.

## Body/Analysis

### Functional Requirements Implementation

- **Champion Data Representation:** Each champion's data is encapsulated in the `Champion` class and its subclasses (`VeryEasyChampion`, `EasyChampion`, `MediumChampion`, `HardChampion`, `VeryHardChampion`). This design allows for easy extension and management of different champion difficulties.

```python
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
```

- **Singleton Pattern:** The `ChampionFactory` class uses the Singleton pattern to ensure only one instance of the factory exists, allowing centralized creation of `Champion` objects.

```python
class ChampionFactory(Singleton):
    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
```

- **User Interface:** The UI is created using PyQt5, with a main window that displays the list of champions and their respective matchup information when selected.

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fiora Matchup Guide")
        self.setup_ui()
        ...
```

- **Data Loading:** Matchup data is loaded from a JSON file (`matchup_data.json`), which contains all necessary information for each champion.

```python
def load_matchup_data(self):
    with open('matchup_data.json') as f:
        data = json.load(f)
        for champion, champion_data in data.items():
            champion_data["icon_path"] = os.path.join(os.path.dirname(__file__), champion_data.get("champion_icon", ""))
            champion_data["runes_path"] = os.path.join(os.path.dirname(__file__), champion_data.get("runes", ""))
            ...
        return data
```

## Results and Summary

### Results
- Successfully implemented a desktop application to guide Fiora matchups.
- Covered all functional requirements, including data representation, UI, and singleton pattern usage.
- Faced challenges with PyQt5 layout management and JSON data handling, which were resolved with iterative testing and debugging.

### Conclusions
- This project achieved the goal of providing a comprehensive Fiora matchup guide with a user-friendly interface.
- The resulting application allows users to quickly access and utilize game information to enhance their gameplay.
- Future extensions could include adding more champions, improving the UI design, and integrating live data updates.

### Future Prospects
- Adding more champions and matchup data.
- Enhancing the UI for better user experience.
- Integrating live updates for real-time matchup information.

## Optional: Resources and References
- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [Python Official Documentation](https://docs.python.org/3/)
- [Singleton Pattern in Python](https://refactoring.guru/design-patterns/singleton)