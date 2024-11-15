import unittest

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усэйн", speed=10)
        self.runner_andrey = Runner("Андрей", speed=9)
        self.runner_nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_race_usain_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        results = tournament.start()
        self.__class__.all_results["UsainNick"] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        self.__class__.all_results["AndreyNick"] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        self.__class__.all_results["UsainAndreyNick"] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

if __name__ == '__main__':
    unittest.main()