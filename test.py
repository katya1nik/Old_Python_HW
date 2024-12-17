def say_hello(name: str, age: int):
    """
    Функция приветствия.
    :param name: Имя пользователя
    :param age: Возраст пользователя
    """
    print(f"Привет, {name}! Тебе {age} лет.")

say_hello("Иван", 30)
say_hello(25, "Петр")

message: None = say_hello("Иван", 30)
