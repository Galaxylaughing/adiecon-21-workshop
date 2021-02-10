class Fizzbuzz:

    def __init__(self):
        print("This is the constructor.")
        print("Every instance method (including the constructor) should have `self` as the first argument")
        print("When calling instance methods, the user does not need to provide a value for `self`")
        print("The user should supply all other arguments 'as expected'")
        print("+++++++++++++++++")

        self.fizz = "fizzzzzz"
        print("Instance methods and attributes (instance vars) are accessed through self.")
        self.buzz = "Buzz"
        self.fizzbuzz = "Fizzbuzz"

    def do_the_thing(self, num):
        if num % 3 == 0 and num % 5 == 0:
            return self.fizzbuzz
        elif num % 3 == 0:
            return self.fizz
        elif num % 5 == 0:
            return self.buzz
        else:
            return num


fb = Fizzbuzz()

print("==================")

print("3 should give Fizz:", fb.do_the_thing(3))
print("5 should give Buzz:", fb.do_the_thing(5))
print("15 should give Fizzbuzz:", fb.do_the_thing(15))
print("Everything else should give back the number:", fb.do_the_thing(98))

# Run this file with $ python3 oop_fizzbuzz.py
