class DivError(Exception):
    def __init__(self, text_error):
        self.text_error = text_error


try:
    divider = float(input("Вветите делимое число "))
    denominator = float(input("Введите число делитель "))
    if denominator == 0:
        raise DivError("Делить на 0 нельзя")


except (ValueError, DivError) as err:
    print(err)
else:
    print(f"Результат деления = {round(divider / denominator)}")
