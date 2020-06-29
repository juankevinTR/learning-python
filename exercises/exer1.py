# Highest number of three
"""
Calculate the highest number, the lowest number and the intermediate of three numbers that we will ask to the user
"""

numberOne = int(input('Introduce the first number: '))
numberTwo = int(input('Introduce the second number: '))
numberThree = int(input('Introduce the third number: '))

sortedNumbers = [numberOne, numberTwo, numberThree]
sortedNumbers.sort()

print('\n----------Results----------')
print(f'Lowest number: {sortedNumbers[0]}')
print(f'iIntermediate number: {sortedNumbers[1]}')
print(f'Highest number: {sortedNumbers[2]}')
