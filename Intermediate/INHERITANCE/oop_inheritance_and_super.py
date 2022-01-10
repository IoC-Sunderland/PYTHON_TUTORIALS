class Parent:
    def __init__(self):
        self.foo = "foo"
        self.bar = "bar"
    
    def test(self):
        return "Hi from Parent's test() method!"

class Child(Parent):
    def __init__(self):
        ''' Calling the super classes super().__init__()
            method initialises the instance of Child with
            Parent's attribute "self.foo" and "self.baz"
        '''
        super().__init__()
        self.baz = "baz"
    
    def test(self):
        print(super().test()) # Hi from Parent's test method!"
        return "Hi from Child's test() method!"

class Infant(Child):
    def test(self):
        print("\nInfant:")
        print(Parent().test())
        print(super().test()) # "Hi from Child's test method!"
        return "Hi from Infant's test() method!"


p1 = Parent()
c1 = Child()

# Attributes
print(p1.foo) # "bar"
print(c1.foo) # "baz"

print(p1.bar) # "biz"
print(c1.bar) # "biz"

print(c1.bar) # "baz"

# Methods
print(p1.test())
print(c1.test())

# And for Infant instance?
i1 = Infant()

# Attributes
print(i1.foo)
print(i1.bar)
print(i1.baz)

# Methods
print(i1.test())

#TODO: Using super()