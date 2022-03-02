class MyClass():
    #constructor
    def __init__(self):
        self.__superprivate = "super secret"
        self._semiprivate = "semi secret"

# instatiating an object of the class type MyClass
mc = MyClass()

mc._semiprivate

print(mc._semiprivate)

# wont let you print it because it is private to the class
# print(mc.__superprivate)


# can be accessed using its mangled name though
print(mc._MyClass__superprivate)