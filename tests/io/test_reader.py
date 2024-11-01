import unittest

import src.io.reader as reader


class TestReader(unittest.TestCase):
    def test_read_file(self):
        test_file = r"game_files\game1.txt"
        riddle, solution = reader.read_file(test_file)
        self.assertEqual(riddle, [["fenster", "putzer", "fisch"],
                                  ["wasser", "spiegel", "bild"],
                                  ["kaffe", "klatsch", "presse"]])
        self.assertEqual(solution, "eis")

    def test_get_available_games(self):
        games = reader.get_available_games()
        self.assertIn("test_game.txt", games)



if __name__ == '__main__':
    unittest.main()