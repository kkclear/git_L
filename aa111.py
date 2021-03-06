
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    pass

import numpy as np

d = {'Michael': 75, 'Bob': 75, 'Tracy': 85}
aa,bb= zip(*d.items())
aaa,bbb= np.array(list(zip(*d.items())))
print(d.items())
print(aa,bb)
print(aaa,bbb)

# nothing happen
# v2 v2
# dev 100%
a1 = aaa[0]
print(a1)