# This FizzBuzz

def fizz_buzz(number):

    if ((number % 3 == 0) & (number % 5 == 0)):
    	print "this is multiples of three : Fizz"
    	return "FizzBuzz"
    elif number % 5 == 0:
    	print "this is multiples of five : Buzz"
    	return "Buzz"
    elif number % 3 == 0:
        print "This is multiples of BOTH"
        return "Fizz"