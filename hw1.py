
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


import unittest


class RunnerTest(unittest.TestCase):
    # класс RunnerTest, наследуемый от TestCase из модуля unittest.

    def test_wolk(self):
        # test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
        run1 = Runner('VANYA')
        # вызовите метод walk у этого объекта 10 раз.
        t = 0
        for i in range(0, 10):
            t += 1
            run1.walk()
        dist1 = run1.distance
        # методом assertEqual сравните distance этого объекта со значением 50.
        self.assertEqual(dist1, 50)

    def test_run(self):
        # """"test_run - метод, в котором создаётся объект класса Runner с произвольным именем."""
        run2 = Runner('SANYA')
        # Далее вызовите метод run у этого объекта 10 раз.
        t = 0
        for _ in range(0, 10):
            t += 1
            run2.run()
        self.assertEqual(run2.distance, 100)
        # После чего методом assertEqual сравните distance этого объекта со значением 100.


    def test_challenge(self):
        # """test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами""".
        run3 = Runner('TANYA')
        run4 = Runner('ANYA')
        t = 0
        for _ in range(0, 10):
            t += 1
            run3.run()
            run4.walk()
        self.assertNotEqual(run3.distance, run4.distance,)
# Далее 10 раз у объектов вызываются методы run и walk соответственно.
# Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.

if __name__ == '__main__':
    unittest.main


