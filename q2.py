import math

def computeBill(letter, numDays, start, end):
    if letter == 'B':
        baseCharge = 40.0 * numDays
        mileCharge = 0.25 * (end - start)
    elif letter == 'D':
        if (end - start) / numDays <= 100:
            baseCharge = 60.0 * numDays
            mileCharge = 0
        else:
            baseCharge = 60.0 * numDays
            mileCharge = 0.25 * ((end - start) / numDays - 100) * numDays
    else: 
        numWeeks = math.ceil(numDays / 7)
        if numWeeks <= 1:
            baseCharge = 190
        else:
            baseCharge = 190 * numWeeks
        if (end - start) / numWeeks <= 900:
            mileCharge = 0
        elif (end - start) / numWeeks <= 1500:
            mileCharge = 100.0 * numWeeks
        else:
            mileCharge = (200.0 * numWeeks) + (0.25 * ((end - start) / numWeeks - 1500) * numWeeks)
    return baseCharge + mileCharge
    

def getValidInput(prompt, validator):
    while True:
        value = input(prompt)
        if validator(value):
            return value
        else:
            print("Invalid. Try again.")

def isValidCode(value):
    return value in ('B', 'D', 'W')

def isValidNumDays(value):
    return value.isdigit() and int(value) > 0

def isValidOdometer(value):
    return value.isdigit() and int(value) < 1000000

def main():
  
    code = getValidInput("Enter code: ", isValidCode)
    print()
    numDays = int(getValidInput("Enter number days: ", isValidNumDays))
    print()
    start = int(getValidInput("Enter starting odometer: ", isValidOdometer))
    print()
    while True:
        end = int(getValidInput("Enter ending odometer: ", isValidOdometer))
        if end >= start:
            break
        else:
            print("Invalid. Try again.")
    print()
    bill = computeBill(code, numDays, start, end)
    print(f"You owe ${bill:.2f}")
    
    
main()