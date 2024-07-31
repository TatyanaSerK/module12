class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

# ---------Домашнее задание по теме "Методы Юнит-тестирования"----------------

import unittest

# Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):# setUpClass - метод, где создаётся атрибут класса all_results.

        cls.all_results = {} # Это словарь в который будут сохраняться результаты всех тестов.

    def setUp(self):# setUp - метод, где создаются 3 объекта:
        self.runner1 = Runner('Усейн', 10)# Бегун по имени Усэйн, со скоростью 10.
        self.runner2 = Runner('Андрей', 9)# Бегун по имени Андрей, со скоростью 9.
        self.runner3 = Runner('Ник', 3)# Бегун по имени Ник, со скоростью 3.

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

    def test_run1(self):# Усэйн и Ник
        t1 = Tournament(90, self.runner1, self.runner3 )
        result1 = t1.start()
        self.all_results[1] = result1
        self.assertTrue(result1[2] == 'Ник')

    def test_run2(self): # Андрей и Ник
        t2 = Tournament(90, self.runner2, self.runner3 )
        result2 = t2.start()
        self.all_results[2] = result2
        self.assertTrue(result2[2] == 'Ник')


    def test_run3(self): # Усэйн, Андрей и Ник.
        t3 = Tournament(90, self.runner1, self.runner2, self.runner3 )
        result3 = t3.start()
        self.all_results[3] = result3
        self.assertTrue(result3[3] == 'Ник')



