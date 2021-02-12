def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Fizzbuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


print("3 should give Fizz:", fizzbuzz(3))
print("5 should give Buzz:", fizzbuzz(5))
print("15 should give Fizzbuzz:", fizzbuzz(15))
print("Everything else should give back the number:", fizzbuzz(98))

# Run this with $ python3 fizzbuzz.py

want_to_see_more_non_ruby_syntax = False

if want_to_see_more_non_ruby_syntax:
    print("Python supports comma-separated print args", "and it's pretty useful!")

    print(
        f"To interpolate, Python 3 introduced the f-string syntax. The f before the string lets us print expressions: {fizzbuzz(1)}")
