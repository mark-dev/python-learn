class JavaBurnOut:
    clazz_var = 'aaaaaa'

    def __init__(self,var1,var2):
        self.var1 = var1
        self.var2 = var2
        JavaBurnOut.clazz_var = var1


print(JavaBurnOut.clazz_var)
b1 = JavaBurnOut('first','second')
print(b1.clazz_var)
b2 = JavaBurnOut('third','four')



print(b2.clazz_var)
