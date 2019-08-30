class SomeClazz:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

var1 = 'dce'
with SomeClazz() as obj:
    var2 = 'abc'
    print(var2)
    print(var1)
print(var2)




a = 3
b = 5
if b > a:
    var3 = 'aaa'

print(var3)


