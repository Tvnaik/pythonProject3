from duck_typing import person


class animal:
    def roar(self):
        pass

class cat(animal):
    def roar(self):
        print("meowww")

class dog(animal):
    def roar(self):
        print("bbbb")
class tiger(animal):
    def roar(self):
        print("aaaaaaaaaa")
    def hunting(self):
        print("tiger hunting")

def perform(ref):
    if isinstance(ref,tiger):
        print(">>>>>>>>>>>")
        ref.roar()
        ref.hunting()
    else:

        ref.roar()

perform(cat())
perform(dog())
perform(tiger())