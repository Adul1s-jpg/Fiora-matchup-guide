import unittest
from main import ChampionFactory

class TestChampionFactory(unittest.TestCase):
    def setUp(self):
        self.factory = ChampionFactory.getInstance()

    def test_very_easy_champion_creation(self):
        champion_data = {
            "name": "Sample Champion",
            "icon_path": "/path/to/icon.png",
            "difficulty": "Very Easy",
            "tips": "Some tips for the champion",
            "runes_path": "/path/to/runes.png",
            "summoner_spells": ["/path/to/spell1.png", "/path/to/spell2.png"],
            "starter_items": ["/path/to/item1.png"],
            "boots": ["/path/to/boots.png"],
            "core_items": ["/path/to/core_item1.png", "/path/to/core_item2.png"],
            "other_items": ["/path/to/other_item1.png"]
        }
        champion = self.factory.create_champion(champion_data)
        self.assertEqual(champion.difficulty, "Very Easy")

    def test_easy_champion_creation(self):
        champion_data = {
            "name": "Sample Champion",
            "icon_path": "/path/to/icon.png",
            "difficulty": "Easy",
            "tips": "Some tips for the champion",
            "runes_path": "/path/to/runes.png",
            "summoner_spells": ["/path/to/spell1.png", "/path/to/spell2.png"],
            "starter_items": ["/path/to/item1.png"],
            "boots": ["/path/to/boots.png"],
            "core_items": ["/path/to/core_item1.png", "/path/to/core_item2.png"],
            "other_items": ["/path/to/other_item1.png"]
        }
        champion = self.factory.create_champion(champion_data)
        self.assertEqual(champion.difficulty, "Easy")

    def test_medium_champion_creation(self):
        champion_data = {
            "name": "Sample Champion",
            "icon_path": "/path/to/icon.png",
            "difficulty": "Even",  # Change "Medium" to "Even"
            "tips": "Some tips for the champion",
            "runes_path": "/path/to/runes.png",
            "summoner_spells": ["/path/to/spell1.png", "/path/to/spell2.png"],
            "starter_items": ["/path/to/item1.png"],
            "boots": ["/path/to/boots.png"],
            "core_items": ["/path/to/core_item1.png", "/path/to/core_item2.png"],
            "other_items": ["/path/to/other_item1.png"]
        }
        champion = self.factory.create_champion(champion_data)
        self.assertEqual(champion.difficulty, "Even")

    def test_hard_champion_creation(self):
        champion_data = {
            "name": "Sample Champion",
            "icon_path": "/path/to/icon.png",
            "difficulty": "Hard",
            "tips": "Some tips for the champion",
            "runes_path": "/path/to/runes.png",
            "summoner_spells": ["/path/to/spell1.png", "/path/to/spell2.png"],
            "starter_items": ["/path/to/item1.png"],
            "boots": ["/path/to/boots.png"],
            "core_items": ["/path/to/core_item1.png", "/path/to/core_item2.png"],
            "other_items": ["/path/to/other_item1.png"]
        }
        champion = self.factory.create_champion(champion_data)
        self.assertEqual(champion.difficulty, "Hard")

    def test_very_hard_champion_creation(self):
        champion_data = {
            "name": "Sample Champion",
            "icon_path": "/path/to/icon.png",
            "difficulty": "Very Hard",
            "tips": "Some tips for the champion",
            "runes_path": "/path/to/runes.png",
            "summoner_spells": ["/path/to/spell1.png", "/path/to/spell2.png"],
            "starter_items": ["/path/to/item1.png"],
            "boots": ["/path/to/boots.png"],
            "core_items": ["/path/to/core_item1.png", "/path/to/core_item2.png"],
            "other_items": ["/path/to/other_item1.png"]
        }
        champion = self.factory.create_champion(champion_data)
        self.assertEqual(champion.difficulty, "Very Hard")

    def test_invalid_difficulty(self):
        champion_data = {
            "name": "Sample Champion",
            "icon_path": "/path/to/icon.png",
            "difficulty": "Impossible",
            "tips": "Some tips for the champion",
            "runes_path": "/path/to/runes.png",
            "summoner_spells": ["/path/to/spell1.png", "/path/to/spell2.png"],
            "starter_items": ["/path/to/item1.png"],
            "boots": ["/path/to/boots.png"],
            "core_items": ["/path/to/core_item1.png", "/path/to/core_item2.png"],
            "other_items": ["/path/to/other_item1.png"]
        }
        with self.assertRaises(ValueError):
            champion = self.factory.create_champion(champion_data)

if __name__ == "__main__":
    unittest.main()