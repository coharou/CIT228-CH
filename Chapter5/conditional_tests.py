print()
currentWater = 200
waterBottleCapacity = 1000
print(f'Will waterBottleCapacity == 1000?\tGuess: true.\tAnswer: {waterBottleCapacity == 1000}')
print(f'Will waterBottleCapacity > 900?\t\tGuess: true.\tAnswer: {waterBottleCapacity > 900}')
print(f'Will waterBottleCapacity >= 1110?\tGuess: false.\tAnswer: {waterBottleCapacity >= 1100}')

print()
waterBottleInterval = [4, 8, 12, 16, 20, 24, 28, 32]
desiredFillLine1 = 9
desiredFillLine2 = 28
print(f'Will desiredFillLine1 be in waterBottleInterval?\tGuess: false.\tAnswer: {desiredFillLine1 in waterBottleInterval}')
print(f'Will desiredFillLine2 be in waterBottleInterval?\tGuess: true.\tAnswer: {desiredFillLine2 in waterBottleInterval}')

print()
processorBrand = 'AMD'
print(f"Will processorBrand == 'AMD'?\t\tGuess: true.\tAnswer: {processorBrand == 'AMD'}")
print(f"Will processorBrand.lower() == 'amd'?\tGuess: true.\tAnswer: {processorBrand.lower() == 'amd'}")
print(f"Will processorBrand.lower() == 'AMD'?\tGuess: false.\tAnswer: {processorBrand.lower() == 'AMD'}")
print(f"Will processorBrand != 'Intel'?\t\tGuess: true.\tAnswer: {processorBrand != 'Intel'}")
print(f"Will processorBrand != 'AMD'?\t\tGuess: false.\tAnswer: {processorBrand != 'AMD'}")

print()
phoneCharge = 7
startCharge = 23
print(f'Will phoneCharge == 7 and startCharge == 23?\tGuess: true.\tAnswer: {phoneCharge == 7 and startCharge == 23}')
print(f'Will phoneCharge > 7 and startCharge < 23?\tGuess: false.\tAnswer: {phoneCharge > 7 and startCharge < 23}')

print()