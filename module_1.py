def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()
# inner_function() - в глобальной области видимости нельзя вызвать функцию, находящуюся в локальной области видимости

