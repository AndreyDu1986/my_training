def test_function(x):
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function(2)

try:
    inner_function()
except Exception as e:
    print(f"Произошла ошибка: {e}")