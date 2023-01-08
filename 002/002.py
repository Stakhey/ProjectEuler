fibonacciSequence = [1, 1]
evenFibonacci = []
number = 1
while number < 4000000:
    number += fibonacciSequence[-2]
    if number%2 == 0:
        evenFibonacci.append(number)
    fibonacciSequence.append(number)
print(sum(evenFibonacci))