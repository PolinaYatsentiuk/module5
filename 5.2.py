from typing import Callable

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def generator_numbers(text: str):
    words = text.split()

    for word in words:
        if is_float(word):
            yield float(word)
        
def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
