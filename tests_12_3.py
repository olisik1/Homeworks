
import unittest


def freeze_tests(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @freeze_tests
    def test_challenge(self):
        self.assertTrue(True)

    @freeze_tests
    def test_run(self):
        self.assertTrue(True)

    @freeze_tests
    def test_walk(self):
        self.assertTrue(True)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @freeze_tests
    def test_first_tournament(self):

        self.assertTrue(True)

    @freeze_tests
    def test_second_tournament(self):

        self.assertTrue(True)

    @freeze_tests
    def test_third_tournament(self):

        self.assertTrue(True)

if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))


    runner = unittest.TextTestRunner(verbosity=2)


    runner.run(suite)