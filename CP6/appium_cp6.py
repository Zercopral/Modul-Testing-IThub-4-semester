import pytest
from AppCalculator import AppCalculator

import time

# 1.    Тест сложения
def test_plus(driver):
    calc_answer = AppCalculator(driver).calc_expression("1000", "+", "1")

    assert calc_answer == "1001"


# 2.    Тест вычитания
def test_minus(driver):
    calc_answer = AppCalculator(driver).calc_expression("10000", "-", "1600")

    assert calc_answer == "8400"


# 3.    Тест умножения
def test_multiply(driver):
    calc_answer = AppCalculator(driver).calc_expression("10101", "*", "9")

    assert calc_answer == "90909"


# 4.    Тест деления
def test_devide(driver):
    calc_answer = AppCalculator(driver).calc_expression("10000", "/", "1000")

    assert calc_answer == "10"


# 5.    Тест экзамен
def test_exam(driver):
    calc_answer = AppCalculator(driver).calc_expression("10", "-", "9", "*", "75", "/", "5", "+", "150")

    assert calc_answer == "25"