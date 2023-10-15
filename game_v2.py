"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def createGuessFunction(number: int):
    """ Returns guess function

    Args:
        number (int): desired number

    Returns:
        function: guess function
    """
    def guess(assumption: int) -> -1 | 0 | 1:
        """ Responds to attempts to guess the number
        
        Args:
            assumption (int): desired number
            
        Returns:
            -1 | 0 | 1: Direction of further guessing
        """
        if (number == assumption):
            return 0
        if (number < assumption):
            return -1
        return 2
    return guess

def random_predict(guessFunction) -> int:
    """Рандомно угадываем число

    Args:
        guessFunction (function): Responds to attempts to guess the number

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if guessFunction(predict_number) == 0:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        guessFunction = createGuessFunction(number)
        count_ls.append(random_predict(guessFunction))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
