def test_function(x):
    def inner_function(x):
        if x % 2 == 0:
            print('Я в области функции test_function')
        else:
            print('Что то другое')

    inner_function(x)
    return a

a = 2
b = test_function(2)
# b = inner_function(2) - Выдает ошибку
print(a)
print(b)