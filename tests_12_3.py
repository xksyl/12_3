import unittest


def freeze_test(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @freeze_test
    def test_run(self):
        self.assertEqual(1 + 1, 2)

    @freeze_test
    def test_walk(self):
        self.assertEqual(2 * 2, 4)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @freeze_test
    def test_first_tournament(self):
        self.assertEqual('E', 'E')

    @freeze_test
    def test_second_tournament(self):
        self.assertEqual(4 / 2, 2)









