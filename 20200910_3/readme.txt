Задача_3 на автоматическое тестирование, с автогенерацией тестовых данных:

напишите программу, которая ищет наибольшее из поданных на вход целых чисел и выводит его; ввод и вывод организован аналогично описанной выше программе сортировки, с тем отличием что выводится единственное целое число.
напишите программу, которая
получает через стандартный вход целое число
генерирует набор входных данных для программы-искателя максимума (10 случайных целых чисел от 1 до 100, кроме одного из чисел, равного полученному на вход)
выдает сгенерированный набор в стандартный выход в виде списка
напишите сценарий, который:
получает на вход (параметр командной строки) целое число
запускает программу-генератор и программу-искатель максимума в конвейере через "|", при этом программе-генератору на вход подает полученное число
направляет выход программы-искателя максимума во временный файл
сравнивает выход программы-искателя максимума с эталоном (для этого генерирует временный файл, содержащий полученное на вход число)
попробуйте запустить сценарий, передавая ему:
а) число, большее чем 100
б) число, меньшее чем 100
в каком из вариантов (а, б) сценарий может "обнаружить" ошибку в программе-искателе максимума, притом что программа правильная?
