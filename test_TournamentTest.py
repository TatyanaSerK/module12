import unittest
import runner

r= runner
class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):# setUpClass - метод, где создаётся атрибут класса all_results.

        cls.all_results = {} # Это словарь в который будут сохраняться результаты всех тестов.

    def setUp(self):# setUp - метод, где создаются 3 объекта:
        self.runner1 = r.Runner('Усейн', 10)# Бегун по имени Усэйн, со скоростью 10.
        self.runner2 = r.Runner('Андрей', 9)# Бегун по имени Андрей, со скоростью 9.
        self.runner3 = r.Runner('Ник', 3)# Бегун по имени Ник, со скоростью 3.

    @classmethod
    def tearDownClass(cls):
# tearDownClass - метод, где выводятся all_results по очереди в столбец.

        for n, run in cls.all_results.items():
            # print(n, run)
            print('забег N', n)
            for key, value in run.items():
                print(key, value)

# методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
# У объекта класса Tournament запускается метод start, который возвращает словарь в переменную results.
# В конце вызывается метод assertTrue, в котором сравниваются последний объект из result и имя последнего бегуна
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run1(self):# Усэйн и Ник
        t1 = r.Tournament(90, self.runner1, self.runner3 )
        result1 = t1.start()
        self.all_results[1] = result1
        self.assertTrue(result1[2] == 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run2(self): # Андрей и Ник
        t2 = r.Tournament(90, self.runner2, self.runner3 )
        result2 = t2.start()
        self.all_results[2] = result2
        self.assertTrue(result2[2] == 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run3(self): # Усэйн, Андрей и Ник.
        t3 = r.Tournament(90, self.runner1, self.runner2, self.runner3 )
        result3 = t3.start()
        self.all_results[3] = result3
        self.assertTrue(result3[3] == 'Ник')