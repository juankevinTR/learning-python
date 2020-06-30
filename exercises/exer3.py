# Calculate salary

hoursPerWeek = 36
extraHours = 0
extraSalary = 0
eurPerExtraHour = 1.5
destinations = ['PROVINCIAL', 'NACIONAL', 'INTERNACIONAL']

weeklyHours = int(input('Introduce weekly hours: '))
eurPerHour = float(input('Introduce € per hour: '))
distance = int(input('Introduce kilometers: '))

if hoursPerWeek < weeklyHours:
	extraHours = weeklyHours - hoursPerWeek
	extraSalary = extraHours * (eurPerHour + eurPerExtraHour)

baseSalary = hoursPerWeek * eurPerHour
grossSalary = baseSalary + extraSalary
subtotal = grossSalary * 0.16
total = grossSalary - subtotal

destination = destinations[0]
if 101 <= distance < 900:
	destination = destinations[1]
elif distance > 900:
	destination = destinations[2]

taxRate = 0
if 250 < grossSalary <= 500:
	taxRate = 0.20
elif grossSalary > 500:
	taxRate = 0.50

print('\n------------------------------')
print(f'Worked hours: {weeklyHours}')
print(f'Extra hours: {extraHours}')
print(f'Eur per hour: {eurPerHour}')
print(f'Distance (Km): {distance}')
print(f'Destination: {destination}')
print(f'Tax rate: {taxRate*100}%')
print(f'Base salary: {baseSalary}')
print(f'Extra salary: {extraSalary}')
print(f'Gross salary: {grossSalary}')
print(f'VAT (16%): {subtotal}')
print('------------------------------')
print(f'TOTAL SALARY: {total}')
print('------------------------------')
print('PROGRAM ENDED!')
