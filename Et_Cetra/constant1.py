# MEOWS = 3    # capitalise to do not change
  
# for _ in range(MEOWS):
#     print("meow")

class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat  = Cat()

cat.meow()