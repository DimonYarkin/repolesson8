class MyError(Exception):
    def __init__(self, text_error):
        self.text_error = text_error

while True:
    try:
        my_list = []
        val = int(input("Ведите число (для выхода введите 111)"))
        my_list.append(val)
        print(f"Текущий список {my_list}")


    except ValueError:
        print(MemoryError("Введено не число введите число"))
