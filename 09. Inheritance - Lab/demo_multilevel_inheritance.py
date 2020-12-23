class Parent:
    @staticmethod
    def get_parent():
        return "Parent"


class Child(Parent):
    @staticmethod
    def get_child():
        return "Child"


class GrandChild(Child):
    @staticmethod
    def get_grandchild():
        return "Grand child"


parent = Parent()
child = Child()
grand_child = GrandChild()

print(parent.get_parent())

print(child.get_parent())
print(child.get_child())

print(grand_child.get_parent())
print(grand_child.get_child())
print(grand_child.get_grandchild())
