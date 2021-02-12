import pytest

class Fizzbuzz:

    def __init__(self):
        self.fizz = "Fizz"
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

# Run the tests with $ python3 -m pytest test_fizzbuzz.py

# All tests must start with test_ or end with _test for pytest to recognize it
def test_fizzbuzz_fizz_on_3s():
    fb = Fizzbuzz()

    assert fb.do_the_thing(3) == "Fizz"

def test_fizzbuzz_buzz_on_5s():
    fb = Fizzbuzz()

    for mult_of_5 in [5, 10, 20, 100]:
        assert fb.do_the_thing(5) == "Buzz"

def test_fizzbuzz_fizzbuzzes():
    fb = Fizzbuzz()

    # Ranges aren't formally taught in the new curriculum
    # but are required individual research
    for mult_of_15 in range(0, 15 * 6, 15):
        assert fb.do_the_thing(15) == "Fizzbuzz"

def test_non_multiples_are_num():
    fb = Fizzbuzz()

    assert fb.do_the_thing(1) == 1
    assert fb.do_the_thing(2) == 2
    assert fb.do_the_thing(4) == 4
    assert fb.do_the_thing(7) == 7
    assert fb.do_the_thing(8) == 8
