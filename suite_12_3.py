
# Часть 1. TestSuit.
# Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с произвольным названием.
# Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
# Создайте объект класса TextTestRunner, с аргументом verbosity=2.


import unittest
import test_RunnerTest
import test_TournamentTest

runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_RunnerTest.RunnerTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_TournamentTest.TournamentTest))
text_run = unittest.TextTestRunner(verbosity=2)
text_run.run(runST)

# Часть 2. Пропуск тестов.
# Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
# Напишите соответствующий декоратор к каждому методу (кроме @classmethod),
# который при значении is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить
# сообщение 'Тесты в этом кейсе заморожены'.
# Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
# Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase.

