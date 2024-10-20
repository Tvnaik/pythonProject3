class student:
    def walk(self):
        print("student walk")

class man:
    def walk(self):
        print("man walk")

class person:
    def walk(self):
        print("people walk")

def perform(ref):
    ref.walk()

perform(student())
perform(man())
perform(person())