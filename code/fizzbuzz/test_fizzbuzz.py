import pytest


# All tests must start with test_ or end with _test for pytest to recognize it
def test_fizzbuzz_fizz_on_3s():
    fb = Fizzbuzz()

    assert fb.do_the_thing(3) == "Fizz"


def test_fizzbuzz_buzz_on_5s():
    fb = Fizzbuzz()

    # Just wanted to give y'all a lil glimpse of a Python loop ;)
    for mult_of_5 in [5, 10, 20, 100]:
        assert fb.do_the_thing(mult_of_5) == "Buzz"


def test_fizzbuzz_fizzbuzzes():
    fb = Fizzbuzz()

    for mult_of_15 in range(0, 15 * 6, 15):
        assert fb.do_the_thing(mult_of_15) == "Fizzbuzz"

def tes
t_non_multiples_are_num():
    fb = Fizzbuzz()

    assert fb.do_the_thing(1) == 1
    assert fb.do_the_thing(2) == 2
    assert fb.do_the_thing(4) == 4
    assert fb.do_the_thing(7) == 7
    assert fb.do_the_thing(8) == 8

# Run the tests with $ python3 -m pytest test_fizzbuzz.py
