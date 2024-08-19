
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызовем inner_function внутри test_function
    inner_function()

# Вызовем test_function
test_function()

# Попробуем вызвать inner_function вне функции test_function
try:
    inner_function()
except NameError as e:
    print(f"Ошибка: {e}")
