class sample:
    def __init__(self,num):
        self.num=num

    def __add__(self, obj):
        return self.num+obj.num

    def __mul__(self, obj):
        return self.num * obj.num

    def __sub__(self, obj):
        return self.num - obj.num

s1=sample(21)
s2=sample(34)
s3=sample(12)
s4=sample(1)
print(s1-s2+s3*s4)
print(s1+s2)
print(s1-s2)
print(s1*s2)

