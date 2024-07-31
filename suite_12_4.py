# _____ДАНО_________
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только числом, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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

# ___________________________________________________________________
import unittest
import logging

class RunnerTest(unittest.TestCase):# класс RunnerTest, наследуемый от TestCase из модуля unittest.

    # Оберните основной код конструкцией try-except.
    # При создании объекта Runner передавайте отрицательное значение в speed.
    # В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
    # В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING
    # с сообщением "Неверная скорость для Runner".

    def test_walk(self):# метод, в котором создаётся объект класса Runner с произвольным именем и отриц.скоростью
        try:
            logging.info('"test_walk" выполнен успешно')
            run1 = Runner('Вося', -10)
            t = 0
            for i in range(0, 10): # вызовите метод walk у этого объекта 10 раз.
                t += 1
                run1.walk()
            dist1 = run1.distance
            self.assertEqual(dist1, 50)# сравните distance этого объекта со значением 50.
        except ValueError:
            logging.error("Неверная скорость для Runner", exc_info=True)


    # test_run:
    # Оберните основной код конструкцией try-except.
    # При создании объекта Runner передавайте что-то кроме строки в name.
    # В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
    # В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING
    # с сообщением "Неверный тип данных для объекта Runner".


    def test_run(self): # метод, в котором создаётся объект класса Runner с произвольным именем
        try:
            logging.info('"test_run" выполнен успешно')
            run2 = Runner(45, 10)
            t = 0
            for _ in range(0, 10):# Далее вызовите метод run у этого объекта 10 раз.
                t += 1
                run2.run()
            self.assertEqual(run2.distance, 100)# сравните distance этого объекта со значением 100.
        except TypeError:
            logging.error('"Неверный тип данных для объекта Runner"', exc_info=True)


    def test_challenge(self):# метод в котором создаются 2 объекта класса Runner с произвольными именами
        run3 = Runner('TANYA')
        run4 = Runner('ANYA')
        t = 0
        for _ in range(0, 10):# Далее 10 раз у объектов вызываются методы run и walk соответственно.
            t += 1
            run3.run()
            run4.walk()
        self.assertNotEqual(run3.distance, run4.distance,)# дистанции должны быть разными

if __name__ == '__main__':
    unittest.main

    # basicConfig на следующие параметры:
    # Уровень - INFO # Режим - чтение # Название файла - runner_tests.log # Кодировка - UTF-8
    # Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.
    logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_tests.log", encoding='utf-8',
                        format='%(levelname)s, | %(message)s | %(asctime)s')


    first = Runner('Вося', -10)
    second = Runner('Илья', 5)
    third = Runner(45, 10)
    t = Tournament(101, first, second, third)
    print(t.start())