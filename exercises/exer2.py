# Calculate birth day of week
"""
Without verify date
"""

weekdays = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

day = int(input('Introduce day: '))
month = int(input('Introduce month: '))
year = int(input('Introduce year: '))

# Step 1: (month + 1) multiply by 3 and all divide by 5
step1 = int(((month + 1) * 3) / 5)

# Step 2: year divide by 4
step2 = int(year / 4)

# Step 3: year divide by 100
step3 = int(year / 100)

# Step 4: year divide by 400
step4 = int(year / 400)

# Step 5: day + (month * 2) + year + step1 + step2 - step3 + step4 + 2
step5 = int(day + (month * 2) + year + step1 + step2 - step3 + step4 + 2)

# Step 6: divide step5 by 7
step6 = int(step5 / 7)

# Step 7: step5 - (step6 * 7)
result = int(step5 - (step6 * 7))

print('\n----------Result----------')
print(f"You were born on a {weekdays[result]}, {day}.{month}.{year}")
