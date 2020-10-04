class MyError(Exception):
    def __init__(self, text_error):
        self.text_error = text_error


my_list = []

while True:
    try:
        val = int(input("Ведите число (для выхода введите 111)"))
        my_list.append(val)
        print(f"Текущий список {my_list}")
        if val == 111:
            break


    except ValueError:
        print(MemoryError("Введено не число введите число"))
