import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_nonexistent(self):
        self.assertEqual(self.stats.search("DOESNTEXIST"), None, "Search palautti pelaajan, vaikkei pitänyt.")
    def test_search(self):
        self.assertEqual(self.stats.search("Kurri").name, "Kurri", "Search palautti väärän pelaajan.")

    def test_team_nonexistent(self):
        self.assertListEqual(self.stats.team("DOESNTEXIST"), [], "Team palautti pelaajia, vaikkei pitänyt.")
    def test_team(self):
        names = [player.name for player in self.stats.team("EDM")]
        self.assertListEqual(names, ["Semenko", "Kurri", "Gretzky"], "Team palautti vääriä pelaajia.")

    def test_top_2(self):
        names = [player.name for player in self.stats.top(1)]
        def playersort(player):
            return player.points        
        oikein = PlayerReaderStub().get_players()
        oikein.sort(key=playersort, reverse=True)
        oikein = [player.name for player in oikein][:2]
        self.assertListEqual(names, oikein, "Top palautti vääriä pelaajia.")

