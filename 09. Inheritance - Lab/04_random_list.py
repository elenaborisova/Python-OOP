from random import choice


class RandomList(list):
    def get_random_element(self):
        random_element = choice(self)
        self.remove(random_element)
        return random_element


ll = RandomList()
ll.append(6)
ll.append(1.3)
ll.append(10)
ll.pop()
ll.reverse()
print(ll.get_random_element())
print(ll)
